"""Diagnose hybrid ranking for T03 and T14 without changing ChromaDB.

Run: .venv/Scripts/python.exe diagnose_retrieval.py
Makes two OpenAI query embedding calls (one per question).
"""
from __future__ import annotations

import csv
from pathlib import Path

import config
from retrieval import Retriever, friendly_error

TEST_IDS = {'T03', 'T14'}
POOL = 30


def section(result):
    return str(result.node.metadata.get('section_id', result.node.node_id))


def main():
    csv_path = Path(config.PROJECT_ROOT) / 'evaluation_questions.csv'
    with csv_path.open(encoding='utf-8-sig', newline='') as stream:
        tests = [row for row in csv.DictReader(stream) if row['id'] in TEST_IDS]
    retriever = Retriever(top_k=5, mode='hybrid')
    pool = min(POOL, retriever.chunk_count)
    for row in tests:
        question = row['question']
        expected = set(row['expected_sections'].split(';'))
        vector = retriever._index.as_retriever(similarity_top_k=pool).retrieve(question)
        lexical = retriever._bm25.retrieve(question, pool)
        ranks = {}
        for label, results in [('vector', vector), ('bm25', lexical)]:
            for rank, result in enumerate(results, 1):
                ranks.setdefault(result.node.node_id, {'section': section(result)})[label] = rank
        print(f'\n{row["id"]}: {question}\nExpected: {", ".join(expected)}')
        for label, results in [('Vector', vector), ('BM25', lexical)]:
            print(f'\n{label} top 15:')
            for rank, result in enumerate(results[:15], 1):
                marker = ' <-- EXPECTED' if section(result) in expected else ''
                print(f' {rank:2}. {section(result)} ({result.score:.4f}){marker}')
            for target in sorted(expected):
                found = next((i for i, item in enumerate(results, 1) if section(item) == target), None)
                print(f' {target} rank: {found if found is not None else "not in top 30"}')
        for weight in [1.0, 1.5, 2.0]:
            ordered = sorted(ranks.values(), key=lambda item: -(
                (1 / (60 + item['vector']) if 'vector' in item else 0)
                + (weight / (60 + item['bm25']) if 'bm25' in item else 0)
            ))
            ids = [item['section'] for item in ordered[:5]]
            print(f'\nRRF vector:BM25 = 1:{weight:g}: {ids}; all expected: {expected.issubset(ids)}')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        print('Error:', friendly_error(exc))
        raise SystemExit(1)
