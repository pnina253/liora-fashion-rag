"""Vector and Hebrew-aware hybrid retrieval over the existing Chroma collection."""
from __future__ import annotations

import math
import os
import re
from collections import Counter

import chromadb
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex
from llama_index.core.schema import NodeWithScore, TextNode
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

import config


class SetupError(RuntimeError):
    """A fixable configuration error."""


def load_api_key() -> None:
    load_dotenv(config.PROJECT_ROOT / '.env', override=False)
    if not os.environ.get('OPENAI_API_KEY'):
        raise SetupError('OPENAI_API_KEY was not found. Check .env in the project folder.')


def get_embed_model() -> OpenAIEmbedding:
    load_api_key()
    return OpenAIEmbedding(model=config.EMBEDDING_MODEL, max_retries=2, timeout=30)


_KEY_PATTERN = re.compile(r'sk-[A-Za-z0-9_\-*]{4,}')


def redact(text: str) -> str:
    return _KEY_PATTERN.sub('sk-***REDACTED***', text)


def friendly_error(exc: BaseException) -> str:
    last = getattr(exc, 'last_attempt', None)
    if last is not None and hasattr(last, 'exception') and last.exception():
        exc = last.exception()
    if isinstance(exc, SetupError):
        return str(exc)
    import openai
    if isinstance(exc, openai.AuthenticationError):
        return 'OpenAI rejected the API key (401). Check the key in .env.'
    if isinstance(exc, openai.PermissionDeniedError):
        return 'The API key has no permission for this model/project (403).'
    if isinstance(exc, openai.RateLimitError):
        if 'insufficient_quota' in str(exc):
            return 'Your OpenAI account has no available credit (insufficient_quota).'
        return 'OpenAI rate limit reached (429). Wait and retry.'
    if isinstance(exc, openai.NotFoundError):
        return f'Model not found (404): {config.EMBEDDING_MODEL}.'
    if isinstance(exc, (openai.APIConnectionError, openai.APITimeoutError)):
        return 'Could not reach OpenAI (network/timeout).'
    if isinstance(exc, openai.APIError):
        return f'OpenAI API error: {redact(str(exc))[:300]}'
    return f'{type(exc).__name__}: {redact(str(exc))[:300]}'


def get_chroma_client() -> chromadb.ClientAPI:
    return chromadb.PersistentClient(path=str(config.CHROMA_DIR))


def open_collection():
    if not config.CHROMA_DIR.exists():
        raise SetupError('Vector database not found. Run ingest.py first.')
    client = get_chroma_client()
    try:
        collection = client.get_collection(config.CHROMA_COLLECTION)
    except Exception as exc:
        raise SetupError(f"Collection '{config.CHROMA_COLLECTION}' not found.") from exc
    if collection.count() == 0:
        raise SetupError('The vector database is empty.')
    return collection


def check_collection_matches_config(collection) -> list[str]:
    meta = collection.metadata or {}
    warnings = []
    if meta.get('hnsw:space') != config.CHROMA_DISTANCE:
        warnings.append(f"distance is '{meta.get('hnsw:space')}', config says '{config.CHROMA_DISTANCE}'")
    for key in ('embedding_model', 'chunk_size', 'chunk_overlap'):
        expected = getattr(config, key.upper())
        if meta.get(key) != expected:
            warnings.append(f"{key} is '{meta.get(key)}', config says '{expected}'")
    return warnings


def to_cosine_similarity(score: float) -> float:
    return 1.0 + math.log(score) if score > 0 else -1.0


# Hebrew-specific lexical matching. Normalize Unicode quotes and common prefixes;
# do not use an English stemmer on Hebrew. This is deliberately conservative:
# stripping prefixes is an additional matching option, never a replacement.
_WORD = re.compile(r'[\u0590-\u05ff]+|[a-z0-9]+', re.IGNORECASE)
_STOP = {'את', 'אתם', 'אתן', 'אני', 'אנחנו', 'האם', 'יש', 'של', 'על', 'עם',
         'או', 'גם', 'זה', 'זו', 'מה', 'איך', 'כמה', 'אפשר', 'ניתן', 'לי', 'לנו',
         'הוא', 'היא', 'הם', 'הן', 'אם', 'כל', 'לא', 'כן', 'רק', 'עוד', 'כדי'}


def tokenize_hebrew(text: str) -> list[str]:
    words = _WORD.findall(text.lower())
    tokens = []
    for word in words:
        if word in _STOP:
            continue
        tokens.append(word)
        # Common attached Hebrew prepositions/articles, e.g. לקנדה -> קנדה.
        # Keep original token too, so exact matches retain their signal.
        if len(word) >= 5 and word[0] in 'בלכמשהו' and '\u0590' <= word[1] <= '\u05ff':
            stem = word[1:]
            if stem not in _STOP:
                tokens.append(stem)
    return tokens


class HebrewBM25:
    """Small, local BM25 index; scores computed from the same persisted chunks."""

    def __init__(self, nodes: list[TextNode], k1: float = 1.5, b: float = 0.75):
        self.nodes = nodes
        self.k1, self.b = k1, b
        self.tfs = [Counter(tokenize_hebrew(node.text)) for node in nodes]
        self.lengths = [sum(tf.values()) for tf in self.tfs]
        self.avgdl = sum(self.lengths) / max(len(nodes), 1)
        self.df = Counter(token for tf in self.tfs for token in tf)

    def retrieve(self, query: str, top_k: int) -> list[NodeWithScore]:
        terms = set(tokenize_hebrew(query))
        n = len(self.nodes)
        matches = []
        for i, tf in enumerate(self.tfs):
            score = 0.0
            for term in terms:
                freq = tf.get(term, 0)
                if not freq:
                    continue
                df = self.df[term]
                idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
                norm = self.k1 * (1 - self.b + self.b * self.lengths[i] / max(self.avgdl, 1))
                score += idf * freq * (self.k1 + 1) / (freq + norm)
            if score > 0:
                matches.append((score, i))
        matches.sort(key=lambda item: (-item[0], item[1]))
        return [NodeWithScore(node=self.nodes[i], score=score) for score, i in matches[:top_k]]


class Retriever:
    """Compatible vector/hybrid interface, with RRF over larger candidate pools."""

    def __init__(self, top_k: int = config.TOP_K, mode: str = 'hybrid'):
        if mode not in ('vector', 'hybrid'):
            raise ValueError("mode must be 'vector' or 'hybrid'")
        collection = open_collection()
        self.collection_metadata = collection.metadata or {}
        self.chunk_count = collection.count()
        self.config_warnings = check_collection_matches_config(collection)
        vector_store = ChromaVectorStore(chroma_collection=collection)
        self._index = VectorStoreIndex.from_vector_store(vector_store, embed_model=get_embed_model())
        self.top_k = top_k
        self.mode = mode
        self._bm25 = None
        if mode == 'hybrid':
            data = collection.get(include=['documents', 'metadatas'])
            nodes = [TextNode(id_=node_id, text=doc, metadata=meta or {})
                     for node_id, doc, meta in zip(data['ids'], data['documents'], data['metadatas'])]
            self._bm25 = HebrewBM25(nodes)

    def retrieve(self, question: str) -> list[NodeWithScore]:
        k = min(self.top_k, self.chunk_count)
        if self.mode == 'vector':
            results = self._index.as_retriever(similarity_top_k=k).retrieve(question)
            for result in results:
                result.score = to_cosine_similarity(result.score)
            return results

        # Retrieve more candidates than the final Top-K. BM25 scores are never
        # mixed numerically with vector scores: only positions enter RRF.
        candidate_k = min(self.chunk_count, max(20, k * 4))
        vector = self._index.as_retriever(similarity_top_k=candidate_k).retrieve(question)
        lexical = self._bm25.retrieve(question, candidate_k)
        scores: dict[str, float] = {}
        nodes = {}
        # Slightly favor lexical evidence for exact names/places/identifiers.
        # Both sources still contribute; missing entries contribute zero.
        for ranking, weight in ((vector, 1.0), (lexical, 2.0)):
            for rank, result in enumerate(ranking, 1):
                node_id = result.node.node_id
                nodes[node_id] = result.node
                scores[node_id] = scores.get(node_id, 0.0) + weight / (60 + rank)
        ordered = sorted(scores, key=lambda node_id: scores[node_id], reverse=True)

        # Protect the highest-ranked evidence from *both* retrievers before
        # filling the remaining slots by RRF. Ordinary RRF can suppress a
        # highly relevant result when it ranks poorly in the other source.
        # For Top-5, consider the first three results of each source; the
        # union is often <= 5 because the sources share strong candidates.
        protected_depth = min(3, k)
        protected = {r.node.node_id for r in vector[:protected_depth]}
        protected.update(r.node.node_id for r in lexical[:protected_depth])
        chosen = [node_id for node_id in ordered if node_id in protected][:k]
        chosen_set = set(chosen)
        chosen.extend(node_id for node_id in ordered
                      if node_id not in chosen_set and len(chosen) < k)
        return [NodeWithScore(node=nodes[node_id], score=scores[node_id])
                for node_id in chosen]
