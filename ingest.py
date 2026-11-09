"""Build the vector database: chunk -> embed -> store in ChromaDB.

Run once (and again only when the knowledge base or chunking settings change):
    .\\.venv\\Scripts\\python.exe ingest.py

The collection is rebuilt from scratch each time, so results are reproducible
and no stale chunks remain. Only knowledge_base/*.md is ingested.
"""
from __future__ import annotations

import sys
from datetime import datetime

from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore

import config
from chunking import build_nodes
from retrieval import friendly_error, get_chroma_client, get_embed_model


def main() -> int:
    try:
        nodes = build_nodes()
        print(f"Chunked knowledge base: {len(nodes)} chunks from {config.KNOWLEDGE_BASE_DIR.name}/")
        embed_model = get_embed_model()

        client = get_chroma_client()
        if config.CHROMA_COLLECTION in [c.name for c in client.list_collections()]:
            client.delete_collection(config.CHROMA_COLLECTION)
            print(f"Deleted old collection '{config.CHROMA_COLLECTION}' (full rebuild).")

        collection = client.create_collection(
            config.CHROMA_COLLECTION,
            metadata={
                "hnsw:space": config.CHROMA_DISTANCE,
                # Build settings, checked later by the retriever for mismatches.
                "embedding_model": config.EMBEDDING_MODEL,
                "chunk_size": config.CHUNK_SIZE,
                "chunk_overlap": config.CHUNK_OVERLAP,
                "built_at": datetime.now().isoformat(timespec="seconds"),
            },
        )
        storage = StorageContext.from_defaults(vector_store=ChromaVectorStore(chroma_collection=collection))
        print(f"Embedding {len(nodes)} chunks with {config.EMBEDDING_MODEL} ...")
        VectorStoreIndex(nodes, storage_context=storage, embed_model=embed_model, show_progress=False)

        stored = collection.count()
        print(f"Stored {stored} vectors in {config.CHROMA_DIR} (distance: {config.CHROMA_DISTANCE}).")
        if stored != len(nodes):
            print(f"WARNING: expected {len(nodes)} vectors but found {stored}.")
            return 1
        return 0
    except Exception as exc:  # noqa: BLE001 - show a clean message, never a key
        print(f"ERROR: {friendly_error(exc)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
