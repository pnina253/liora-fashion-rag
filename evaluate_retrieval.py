"""Compare Vector and Hybrid retrieval against evaluation_questions.csv.

Run from project root: .\.venv\Scripts\python.exe evaluate_retrieval.py
Requires OpenAI query embeddings (2 per question), but does NOT ingest or modify ChromaDB.
"""
from __future__ import annotations

import csv
import sys
from datetime import datetime
from pathlib import Path

from retrieval import Retriever, friendly_error
import config

TOP_K = 5
CSV_PATH = config.PROJECT_ROOT / 'evaluation_questions.csv'
REPORT_PATH = config.PROJECT_ROOT / 'reports' / 'retrieval_evaluation.md'


def expected_ids(raw: str) -> set[str]:
    return {item.strip() for item in raw.split(';') if item.strip() and item.strip().lower() != 'none'}


def evaluate_one(retriever, question: str, expected: set[str]):
    results = retriever.retrieve(question)
    ids = [str(r.node.metadata.get('section_id', '')) for r in results]
    if not expected:
        # A retrieval-only evaluation cannot establish whether an LLM will abstain.
        return {'ids': ids, 'hit1': None, 'hit5': None, 'all5': None, 'rr': None}
    ranks = [ids.index(s) + 1 for s in expected if s in ids]
    best = min(ranks) if ranks else None
    return {
        'ids': ids,
        'hit1': int(best == 1),
        'hit5': int(best is not None),
        'all5': int(expected.issubset(set(ids))),
        'rr': 1 / best if best is not None else 0.0,
    }


def stats(rows, mode):
    valid = [row[mode] for row in rows if row[mode]['hit1'] is not None]
    n = len(valid)
    return {k: sum(item[k] for item in valid) / n if n else 0
            for k in ('hit1', 'hit5', 'all5', 'rr')}


def main():
    if not CSV_PATH.is_file():
        print(f'Missing {CSV_PATH}. Rename the uploaded CSV to evaluation_questions.csv and put it in the project root.')
        return 1
    with CSV_PATH.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        required = {'id', 'question', 'expected_sections', 'test_type'}
        if not required.issubset(reader.fieldnames or []):
            print('CSV missing columns:', ', '.join(sorted(required - set(reader.fieldnames or []))))
            return 1
        tests = list(reader)
    try:
        retrievers = {mode: Retriever(top_k=TOP_K, mode=mode) for mode in ('vector', 'hybrid')}
    except Exception as exc:
        print('Setup error:', friendly_error(exc))
        return 1

    print(f'Running {len(tests)} questions in both modes; up to {2 * len(tests)} paid query-embedding calls.')
    rows = []
    for i, test in enumerate(tests, 1):
        expected = expected_ids(test['expected_sections'])
        row = {'id': test['id'], 'question': test['question'], 'expected': expected,
               'type': test['test_type']}
        for mode, retriever in retrievers.items():
            try:
                row[mode] = evaluate_one(retriever, test['question'], expected)
            except Exception as exc:
                print(f"ERROR {test['id']} ({mode}): {friendly_error(exc)}")
                return 1
        rows.append(row)
        v, h = row['vector'], row['hybrid']
        print(f"{i:02}/{len(tests)} {test['id']}: Vector {v['ids'][:3]} | Hybrid {h['ids'][:3]}")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        '# Retrieval evaluation — Vector vs Hybrid', '',
        f'Run: {datetime.now():%Y-%m-%d %H:%M:%S} · Top-{TOP_K} · {len(rows)} questions', '',
        '## Aggregate metrics', '',
        '| Mode | Hit@1 | Hit@5 | All-required@5 | MRR@5 |',
        '|---|---:|---:|---:|---:|',
    ]
    for mode in ('vector', 'hybrid'):
        s = stats(rows, mode)
        lines.append(f"| {mode} | {s['hit1']:.1%} | {s['hit5']:.1%} | {s['all5']:.1%} | {s['rr']:.3f} |")
    lines += ['', 'For multi-source questions, Hit@K means *at least one* expected section was found; All-required@5 requires *every* expected section.',
              'Unanswerable questions (expected_sections=none) are excluded from aggregate metrics; retrieval alone cannot evaluate refusal/abstention.', '',
              '## Per-question results', '',
              '| ID | Type | Expected sections | Vector Top-5 | Hybrid Top-5 | Vector all? | Hybrid all? |',
              '|---|---|---|---|---|---|---|']
    for row in rows:
        def yes(mode):
            flag = row[mode]['all5']
            return 'N/A' if flag is None else ('YES' if flag else 'NO')
        lines.append('| ' + ' | '.join([
            row['id'], row['type'], ', '.join(sorted(row['expected'])) or 'none',
            ', '.join(row['vector']['ids']), ', '.join(row['hybrid']['ids']),
            yes('vector'), yes('hybrid')]) + ' |')
    lines += ['', '## Changes by question', '']
    for row in rows:
        v, h = row['vector']['all5'], row['hybrid']['all5']
        if v is None:
            label = 'Not scored (unanswerable)'
        elif h > v:
            label = 'IMPROVED'
        elif h < v:
            label = 'REGRESSED'
        else:
            label = 'UNCHANGED'
        lines.append(f"- **{row['id']}** — {label}: {row['question']}")
    REPORT_PATH.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n' + '\n'.join(lines[4:8]))
    print(f'\nReport saved: {REPORT_PATH}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
