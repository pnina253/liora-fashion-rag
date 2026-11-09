"""Central configuration for the Liora Fashion RAG bot.

Every tunable parameter lives here so experiments only change this file.
The API key is NOT stored here - it is loaded from .env.
"""
from pathlib import Path

# --- Paths -----------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent
KNOWLEDGE_BASE_DIR = PROJECT_ROOT / "knowledge_base"   # the only folder that is ingested
CHROMA_DIR = PROJECT_ROOT / "chroma_db"                # generated, excluded from Git
EVAL_QUESTIONS_FILE = PROJECT_ROOT / "evaluation_questions.csv"  # never ingested

# --- Vector DB (ChromaDB) --------------------------------------------------
CHROMA_COLLECTION = "liora_fashion"
# Chroma's default distance is L2; we explicitly request cosine (decision 9).
CHROMA_DISTANCE = "cosine"

# --- Models (OpenAI) -------------------------------------------------------
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"
LLM_TEMPERATURE = 0.0  # deterministic answers - easier to compare before/after

# --- Chunking --------------------------------------------------------------
# Structure-aware: split by Markdown headings first; only sections larger than
# CHUNK_SIZE are split further with SentenceSplitter using CHUNK_OVERLAP.
CHUNK_SIZE = 512      # max tokens per chunk
CHUNK_OVERLAP = 50    # tokens, applied only when an oversized section is split
# Tokens are counted with the embedding model's tokenizer (text-embedding-3-small).
TOKENIZER_ENCODING = "cl100k_base"

# Which chunk metadata is visible to the embedding model / the answering LLM.
# LlamaIndex includes ALL metadata in both by default, which would pollute the
# vectors with technical fields (token counts, part numbers). Everything not
# listed here is still stored in Chroma and available to the UI for citations.
EMBED_METADATA_KEYS = ["document_title"]
LLM_METADATA_KEYS = ["source_file", "document_title", "section_id", "section_title"]

# --- Retrieval -------------------------------------------------------------
TOP_K = 5
# Minimum cosine similarity for a chunk to be used. None = no cutoff.
# Deliberately left unset: it will be calibrated from evaluation results.
SIMILARITY_CUTOFF = None
