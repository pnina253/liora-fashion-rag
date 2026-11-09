"""Structure-aware chunking of the Liora Fashion knowledge base.

Pipeline:
1. Read every *.md file in knowledge_base/ (and nothing else).
2. Split each document on Markdown headings with LlamaIndex MarkdownNodeParser,
   so every product, policy section and FAQ question-answer pair is one unit.
3. Only a section larger than CHUNK_SIZE tokens is split further with
   SentenceSplitter (CHUNK_OVERLAP applies only there). Every part repeats the
   section heading so it stays self-describing.
4. Attach document + section metadata to every chunk, with stable chunk IDs.

No embeddings or API calls happen in this module.
"""
from __future__ import annotations

import re
from pathlib import Path

import tiktoken
from llama_index.core import Document
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter
from llama_index.core.schema import TextNode

import config

# "## PR-DR-101 | שמלת מיה"  /  "## FAQ-03 האם אפשר..."  ->  (id, title)
SECTION_HEADING_RE = re.compile(r"^#{2,}\s+([A-Z]+(?:-[A-Z]+)*-\d+)\s*\|?\s*(.*)$")
DOCUMENT_TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
DOCUMENT_ID_RE = re.compile(r"מזהה:\s*([A-Z]+)")

ALL_METADATA_KEYS = [
    "source_file", "document_id", "document_title", "section_id", "section_title",
    "chunk_type", "part", "total_parts", "was_split", "token_count",
]

_encoding = tiktoken.get_encoding(config.TOKENIZER_ENCODING)


def count_tokens(text: str) -> int:
    return len(_encoding.encode(text))


def load_documents(kb_dir: Path = config.KNOWLEDGE_BASE_DIR) -> list[Document]:
    """Load only the Markdown files of the knowledge base."""
    eval_file = config.EVAL_QUESTIONS_FILE.resolve()
    documents = []
    for path in sorted(kb_dir.glob("*.md")):
        # Guard: evaluation data must never be ingested.
        if path.resolve() == eval_file or "evaluation" in path.name.lower():
            raise ValueError(f"Refusing to ingest evaluation file: {path}")
        text = path.read_text(encoding="utf-8")
        title_match = DOCUMENT_TITLE_RE.search(text)
        id_match = DOCUMENT_ID_RE.search(text)
        documents.append(Document(
            text=text,
            metadata={
                "source_file": path.name,
                "document_title": title_match.group(1).strip() if title_match else path.stem,
                "document_id": id_match.group(1) if id_match else path.stem.upper(),
            },
        ))
    if not documents:
        raise FileNotFoundError(f"No .md files found in {kb_dir}")
    return documents


def _section_info(heading_line: str, doc_meta: dict) -> tuple[str, str, str]:
    """Return (chunk_type, section_id, section_title) for a section's first line."""
    if heading_line.startswith("# "):  # H1 = document title + intro note
        return "preamble", f"{doc_meta['document_id']}-INTRO", doc_meta["document_title"]
    match = SECTION_HEADING_RE.match(heading_line)
    if match:
        return "section", match.group(1), match.group(2).strip()
    # Heading without an ID: keep it, the report flags these.
    return "section", "", heading_line.lstrip("#").strip()


def _make_node(text: str, doc_meta: dict, chunk_type: str, section_id: str,
               section_title: str, part: int, total_parts: int) -> TextNode:
    metadata = {
        "source_file": doc_meta["source_file"],
        "document_id": doc_meta["document_id"],
        "document_title": doc_meta["document_title"],
        "section_id": section_id,
        "section_title": section_title,
        "chunk_type": chunk_type,
        "part": part,
        "total_parts": total_parts,
        "was_split": total_parts > 1,
        "token_count": count_tokens(text),
    }
    node_id = f"{doc_meta['source_file']}::{section_id or section_title}::p{part}"
    return TextNode(
        id_=node_id,
        text=text,
        metadata=metadata,
        excluded_embed_metadata_keys=[k for k in ALL_METADATA_KEYS if k not in config.EMBED_METADATA_KEYS],
        excluded_llm_metadata_keys=[k for k in ALL_METADATA_KEYS if k not in config.LLM_METADATA_KEYS],
    )


def build_nodes(chunk_size: int = config.CHUNK_SIZE,
                chunk_overlap: int = config.CHUNK_OVERLAP,
                kb_dir: Path = config.KNOWLEDGE_BASE_DIR) -> list[TextNode]:
    """Chunk the whole knowledge base. Parameters default to config values."""
    documents = load_documents(kb_dir)
    md_parser = MarkdownNodeParser(include_metadata=False, include_prev_next_rel=False)

    nodes: list[TextNode] = []
    for doc in documents:
        for section in md_parser.get_nodes_from_documents([doc]):
            text = section.get_content().strip()
            heading_line, _, body = text.partition("\n")
            chunk_type, section_id, section_title = _section_info(heading_line, doc.metadata)

            if count_tokens(text) <= chunk_size:
                nodes.append(_make_node(text, doc.metadata, chunk_type, section_id,
                                        section_title, part=1, total_parts=1))
                continue

            # Oversized section: split the body, repeat the heading on every part.
            heading_budget = count_tokens(heading_line + "\n")
            splitter = SentenceSplitter(
                chunk_size=chunk_size - heading_budget,
                chunk_overlap=chunk_overlap,
                tokenizer=_encoding.encode,
            )
            parts = splitter.split_text(body.strip())
            for i, part_text in enumerate(parts, start=1):
                nodes.append(_make_node(f"{heading_line}\n{part_text}", doc.metadata,
                                        chunk_type, section_id, section_title,
                                        part=i, total_parts=len(parts)))
    return nodes
