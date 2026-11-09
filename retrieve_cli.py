"""Interactive retrieval tester (no answer generation).

Type a Hebrew question and see the Top-K retrieved chunks with their source
file, section, cosine similarity and text. Reuses the existing ChromaDB - no
re-embedding of the knowledge base. Each question costs one tiny embedding call.

Run from the project folder:
    .\\.venv\\Scripts\\python.exe retrieve_cli.py

Commands:  :k N   change Top-K      :full   toggle full chunk text
           :q     quit (also: exit, empty line, Ctrl+C)

Every query is also appended to reports/retrieval_log.md, which displays
Hebrew right-to-left correctly when opened in VS Code's Markdown preview.
"""
from __future__ import annotations

import sys
from datetime import datetime

import config
from retrieval import Retriever, friendly_error

LOG_FILE = config.PROJECT_ROOT / "reports" / "retrieval_log.md"
SNIPPET_CHARS = 220


def chunk_body(text: str) -> str:
    """Chunk text without its heading line (the heading is shown separately)."""
    lines = text.strip().splitlines()
    if lines and lines[0].startswith("#"):
        lines = lines[1:]
    return "\n".join(lines).strip()


def print_results(question: str, results, full: bool, mode: str) -> None:
    print(f"\nTop-{len(results)} for: {question}")
    print("-" * 70)
    for rank, r in enumerate(results, 1):
        m = r.node.metadata
        print(f"#{rank}  {"similarity" if mode == "vector" else "rrf"}={r.score:.4f}  {m['source_file']}  [{m['section_id']}]  {m['section_title']}")
        body = chunk_body(r.node.text)
        if not full:
            body = " ".join(body.split())
            body = body[:SNIPPET_CHARS] + ("..." if len(body) > SNIPPET_CHARS else "")
        print("    " + body.replace("\n", "\n    "))
        print()


def log_results(question: str, results, top_k: int, mode: str) -> None:
    LOG_FILE.parent.mkdir(exist_ok=True)
    new = not LOG_FILE.exists()
    with LOG_FILE.open("a", encoding="utf-8") as f:
        if new:
            f.write("# Retrieval tester log\n\nAppended automatically by retrieve_cli.py.\n")
        f.write(f"\n## {question}\n\n_{datetime.now():%Y-%m-%d %H:%M:%S} · Top-{top_k} · "
                f"{config.EMBEDDING_MODEL} · mode {mode} · chunk {config.CHUNK_SIZE}/{config.CHUNK_OVERLAP}_\n\n")
        f.write(f"| # | {'Similarity' if mode == 'vector' else 'RRF'} | Source | Section | Title |\n|---:|---:|---|---|---|\n")
        for rank, r in enumerate(results, 1):
            m = r.node.metadata
            f.write(f"| {rank} | {r.score:.3f} | {m['source_file']} | {m['section_id']} | {m['section_title']} |\n")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    print("Liora Fashion — retrieval tester (no LLM answers, retrieval only)")
    try:
        retriever = Retriever(top_k=config.TOP_K, mode="hybrid")
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {friendly_error(exc)}")
        return 1

    meta = retriever.collection_metadata
    print(f"Loaded {retriever.chunk_count} chunks from ChromaDB "
          f"(built {meta.get('built_at', '?')}, {meta.get('embedding_model', '?')}, "
          f"distance={meta.get('hnsw:space', '?')}).")
    for w in retriever.config_warnings:
        print(f"WARNING: database differs from config.py: {w}. Re-run ingest.py.")
    print("Scores: RRF in hybrid mode; cosine similarity in vector mode.")
    print("Commands: :mode vector|hybrid · :k N · :full · :q\n")

    full = False
    while True:
        try:
            question = input(f"שאלה [Top-{retriever.top_k}]> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if question.lower() in ("", ":q", "exit", "quit"):
            break
        if question.startswith(":mode"):
            parts = question.split()
            if len(parts) != 2 or parts[1] not in ("vector", "hybrid"):
                print("Usage: :mode vector|hybrid")
            else:
                try:
                    retriever = Retriever(top_k=retriever.top_k, mode=parts[1])
                    print(f"Mode set to {retriever.mode}")
                except Exception as exc:
                    print(f"ERROR: {friendly_error(exc)}")
            continue
        if question == ":full":
            full = not full
            print(f"Full text: {'on' if full else 'off'}")
            continue
        if question.startswith(":k"):
            try:
                k = int(question.split()[1])
                if not 1 <= k <= retriever.chunk_count:
                    raise ValueError
                retriever.top_k = k
                print(f"Top-K set to {k}")
            except (IndexError, ValueError):
                print(f"Usage: :k N   (N between 1 and {retriever.chunk_count})")
            continue

        try:
            results = retriever.retrieve(question)
        except Exception as exc:  # noqa: BLE001 - keep the session alive
            print(f"ERROR: {friendly_error(exc)}\n")
            continue
        print_results(question, results, full, retriever.mode)
        log_results(question, results, retriever.top_k, retriever.mode)

    print("Bye.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
