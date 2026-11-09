# Retrieval evaluation — Vector vs Hybrid

Run: 2026-11-09 20:39:27 · Top-5 · 15 questions

## Aggregate metrics

| Mode | Hit@1 | Hit@5 | All-required@5 | MRR@5 |
|---|---:|---:|---:|---:|
| vector | 64.3% | 85.7% | 71.4% | 0.738 |
| hybrid | 71.4% | 100.0% | 92.9% | 0.824 |

For multi-source questions, Hit@K means *at least one* expected section was found; All-required@5 requires *every* expected section.
Unanswerable questions (expected_sections=none) are excluded from aggregate metrics; retrieval alone cannot evaluate refusal/abstention.

## Per-question results

| ID | Type | Expected sections | Vector Top-5 | Hybrid Top-5 | Vector all? | Hybrid all? |
|---|---|---|---|---|---|---|
| T01 | direct | SH-02 | SH-02, FAQ-06, SH-03, SH-05, SH-01 | SH-03, SH-02, FAQ-06, SH-01, SH-05 | YES | YES |
| T02 | direct | SH-02 | SH-02, SH-05, FAQ-06, SH-03, RT-03 | SH-02, SH-03, FAQ-06, SH-01, SH-05 | YES | YES |
| T03 | multi_source | PR-DR-102, SH-03 | SH-03, FAQ-06, SH-01, SH-02, SH-05 | SH-03, FAQ-06, SH-01, PR-DR-102, OP-05 | NO | YES |
| T04 | conditional | RT-01 | RT-01, FAQ-03, RT-02, RT-04, RT-05 | RT-01, RT-02, RT-04, FAQ-03, FAQ-07 | YES | YES |
| T05 | process | RT-05 | FAQ-09, RT-05, RT-03, PR-00, RT-01 | RT-05, FAQ-07, RT-03, RT-02, FAQ-09 | YES | YES |
| T06 | semantic | PR-DR-101 | FAQ-08, PR-DR-101, FAQ-04, PR-SK-204, PR-BL-303 | PR-BL-303, PR-SK-204, PR-DR-101, PR-KN-403, FAQ-08 | YES | YES |
| T07 | numeric | PR-SK-201, PR-SK-204 | PR-SK-201, PR-SK-204, PR-SK-203, SH-02, SH-03 | PR-SK-201, SH-03, PR-SK-203, PR-SK-204, PR-SK-202 | YES | YES |
| T08 | comparison | PR-DR-101, PR-DR-102 | SZ-03, SZ-05, SZ-02, OP-04, OP-05 | SZ-03, PR-DR-101, PR-DR-102, SZ-05, SZ-02 | NO | YES |
| T09 | table | SZ-01, SZ-03 | SZ-01, SZ-03, SZ-05, FAQ-05, FAQ-02 | SZ-01, SZ-03, SZ-02, SZ-05, FAQ-05 | YES | YES |
| T10 | multi_source_math | PR-DR-101, SH-03 | SH-03, SH-02, FAQ-06, SH-01, SH-05 | SH-03, SH-02, FAQ-06, FAQ-08, SH-01 | NO | NO |
| T11 | conditional | OP-03 | OP-03, SH-05, OP-04, FAQ-06, OP-02 | OP-03, SH-05, OP-04, FAQ-01, SH-01 | YES | YES |
| T12 | explicit_negative | SH-01 | FAQ-04, FAQ-08, OP-05, OP-04, OP-01 | SH-01, FAQ-04, FAQ-08, OP-05, OP-04 | NO | YES |
| T13 | unanswerable | none | SH-04, OP-05, OP-04, FAQ-04, FAQ-03 | SH-04, OP-05, OP-04, FAQ-04, FAQ-03 | N/A | N/A |
| T14 | capability_boundary | OP-06 | OP-04, OP-02, OP-06, SH-02, SH-05 | OP-04, OP-03, OP-02, FAQ-04, OP-06 | YES | YES |
| T15 | catalog_filter | PR-SK-202 | PR-SK-202, SZ-01, SZ-03, SZ-04, SIZES-INTRO | PR-SK-202, PR-SK-201, SZ-03, SZ-01, FAQ-08 | YES | YES |

## Changes by question

- **T01** — UNCHANGED: כמה עולה משלוח רגיל?
- **T02** — UNCHANGED: תוך כמה זמן מגיע משלוח רגיל?
- **T03** — IMPROVED: האם שמלת נועה ב־329 ₪ זכאית למשלוח חינם?
- **T04** — UNCHANGED: אפשר לבקש החזרה אחרי 10 ימים?
- **T05** — UNCHANGED: מה עושים אם קיבלתי מוצר פגום?
- **T06** — UNCHANGED: איזו שמלה מכילה כותנה?
- **T07** — UNCHANGED: איזה חצאיות עולות פחות מ־200 ₪?
- **T08** — IMPROVED: מה ההבדל בין שמלת מיה לשמלת נועה?
- **T09** — UNCHANGED: היקף החזה שלי 92, המותן 74 והירכיים 100. איזו מידה בטבלה?
- **T10** — UNCHANGED: כמה אשלם על שמלת מיה עם משלוח רגיל ללא הנחה?
- **T11** — UNCHANGED: אפשר לשנות כתובת אחרי שההזמנה נמסרה לחברת המשלוחים?
- **T12** — IMPROVED: האם אתם שולחים לקנדה?
- **T13** — Not scored (unanswerable): האם ייפתח סניף בחיפה בשנה הבאה?
- **T14** — UNCHANGED: מה מצב ההזמנה האישית שלי מספר 12345?
- **T15** — UNCHANGED: האם חצאית ג׳ינס מקסי קיימת במידה XL?
