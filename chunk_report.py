"""Generate a detailed chunking report (no embeddings, no API calls).

Usage:
    python chunk_report.py                      # uses config values
    python chunk_report.py --chunk-size 128     # experiment without editing config

Writes reports/chunk_report.md (or chunk_report_<size>_<overlap>.md for overrides)
and prints a short summary.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict

from llama_index.core.schema import MetadataMode

import config
from chunking import build_nodes, count_tokens, load_documents

REPORTS_DIR = config.PROJECT_ROOT / "reports"


def coverage_problems(nodes) -> list[str]:
    """Every non-empty source line must appear in at least one chunk of its file."""
    problems = []
    text_by_file = defaultdict(str)
    for n in nodes:
        text_by_file[n.metadata["source_file"]] += "\n" + n.text
    for doc in load_documents():
        name = doc.metadata["source_file"]
        for line in doc.text.splitlines():
            if line.strip() and line.strip() not in text_by_file[name]:
                problems.append(f"{name}: missing line: {line.strip()[:80]}")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-size", type=int, default=config.CHUNK_SIZE)
    parser.add_argument("--chunk-overlap", type=int, default=config.CHUNK_OVERLAP)
    args = parser.parse_args()
    size, overlap = args.chunk_size, args.chunk_overlap

    nodes = build_nodes(chunk_size=size, chunk_overlap=overlap)

    per_doc = Counter(n.metadata["source_file"] for n in nodes)
    tokens = [n.metadata["token_count"] for n in nodes]
    split_sections = sorted({(n.metadata["source_file"], n.metadata["section_id"], n.metadata["total_parts"])
                             for n in nodes if n.metadata["was_split"]})
    oversized = [n for n in nodes if n.metadata["token_count"] > size]
    no_id = [n for n in nodes if not n.metadata["section_id"]]
    dup_ids = [i for i, c in Counter(n.node_id for n in nodes).items() if c > 1]
    missing = coverage_problems(nodes)

    L = []
    L.append("# Chunk report — Liora Fashion\n")
    L.append(f"- Chunk size limit: **{size}** tokens · overlap (only for split sections): **{overlap}** tokens")
    L.append(f"- Tokenizer: `{config.TOKENIZER_ENCODING}` (same as `{config.EMBEDDING_MODEL}`)")
    L.append(f"- Metadata visible to embedding: `{config.EMBED_METADATA_KEYS}` · to LLM: `{config.LLM_METADATA_KEYS}`")
    L.append("- No embeddings or API calls were made to produce this report.\n")

    L.append("## Summary\n")
    L.append(f"| Metric | Value |\n|---|---|")
    L.append(f"| Total chunks | **{len(nodes)}** |")
    L.append(f"| Tokens per chunk (min / avg / max) | {min(tokens)} / {sum(tokens) / len(tokens):.0f} / {max(tokens)} |")
    L.append(f"| Total tokens (chunk text) | {sum(tokens)} |")
    L.append(f"| Sections split into parts | {len(split_sections)} |")
    L.append(f"| Chunks over {size} tokens | {len(oversized)} |")
    L.append(f"| Chunks without a section ID | {len(no_id)} |")
    L.append(f"| Duplicate chunk IDs | {len(dup_ids)} |")
    L.append(f"| Source lines missing from chunks | {len(missing)} |\n")

    L.append("## Chunks per document\n")
    L.append("| Document | Chunks | Tokens |\n|---|---:|---:|")
    for name in sorted(per_doc):
        doc_tokens = sum(n.metadata["token_count"] for n in nodes if n.metadata["source_file"] == name)
        L.append(f"| {name} | {per_doc[name]} | {doc_tokens} |")
    L.append("")

    L.append("## Split sections\n")
    if split_sections:
        L.append("| Document | Section | Parts |\n|---|---|---:|")
        L += [f"| {f} | {s} | {p} |" for f, s, p in split_sections]
    else:
        L.append(f"None — every section fits within {size} tokens, so SentenceSplitter "
                 f"and the {overlap}-token overlap were not applied to any section.")
    L.append("")

    L.append(f"## Chunks over {size} tokens\n")
    L.append("None." if not oversized else "\n".join(f"- `{n.node_id}`: {n.metadata['token_count']}" for n in oversized))
    L.append("")
    if no_id or dup_ids or missing:
        L.append("## Warnings\n")
        L += [f"- No section ID: `{n.node_id}`" for n in no_id]
        L += [f"- Duplicate ID: `{i}`" for i in dup_ids]
        L += [f"- {m}" for m in missing]
        L.append("")

    L.append("## All chunks\n")
    L.append("Text tokens = the chunk text. Embed tokens = what is actually sent to the "
             "embedding model (text + visible metadata).\n")
    L.append("| # | Document | Section ID | Section title | Type | Part | Text tokens | Embed tokens |")
    L.append("|---:|---|---|---|---|---|---:|---:|")
    for i, n in enumerate(nodes, 1):
        m = n.metadata
        embed_tokens = count_tokens(n.get_content(metadata_mode=MetadataMode.EMBED))
        L.append(f"| {i} | {m['source_file']} | {m['section_id']} | {m['section_title']} | {m['chunk_type']} "
                 f"| {m['part']}/{m['total_parts']} | {m['token_count']} | {embed_tokens} |")
    L.append("")

    L.append("## Chunk texts (exactly as they will be embedded)\n")
    for i, n in enumerate(nodes, 1):
        L.append(f"### {i}. `{n.node_id}`\n")
        L.append("```text\n" + n.get_content(metadata_mode=MetadataMode.EMBED) + "\n```\n")

    REPORTS_DIR.mkdir(exist_ok=True)
    default = (size, overlap) == (config.CHUNK_SIZE, config.CHUNK_OVERLAP)
    out = REPORTS_DIR / ("chunk_report.md" if default else f"chunk_report_{size}_{overlap}.md")
    out.write_text("\n".join(L), encoding="utf-8")

    print(f"Chunks: {len(nodes)} | per document: {dict(sorted(per_doc.items()))}")
    print(f"Tokens min/avg/max: {min(tokens)}/{sum(tokens) / len(tokens):.0f}/{max(tokens)}")
    print(f"Split sections: {len(split_sections)} | over {size}: {len(oversized)} | "
          f"no ID: {len(no_id)} | duplicate IDs: {len(dup_ids)} | missing lines: {len(missing)}")
    print(f"Report written to: {out}")


if __name__ == "__main__":
    main()
