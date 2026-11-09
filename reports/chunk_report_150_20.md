# Chunk report — Liora Fashion

- Chunk size limit: **150** tokens · overlap (only for split sections): **20** tokens
- Tokenizer: `cl100k_base` (same as `text-embedding-3-small`)
- Metadata visible to embedding: `['document_title']` · to LLM: `['source_file', 'document_title', 'section_id', 'section_title']`
- No embeddings or API calls were made to produce this report.

## Summary

| Metric | Value |
|---|---|
| Total chunks | **108** |
| Tokens per chunk (min / avg / max) | 33 / 111 / 150 |
| Total tokens (chunk text) | 11963 |
| Sections split into parts | 41 |
| Chunks over 150 tokens | 0 |
| Chunks without a section ID | 0 |
| Duplicate chunk IDs | 0 |
| Source lines missing from chunks | 37 |

## Chunks per document

| Document | Chunks | Tokens |
|---|---:|---:|
| faq.md | 12 | 1308 |
| orders_payments.md | 11 | 1171 |
| products.md | 48 | 5602 |
| returns_policy.md | 14 | 1468 |
| shipping_policy.md | 11 | 1139 |
| size_guide.md | 12 | 1275 |

## Split sections

| Document | Section | Parts |
|---|---|---:|
| faq.md | FAQ-01 | 2 |
| faq.md | FAQ-09 | 2 |
| orders_payments.md | OP-03 | 2 |
| orders_payments.md | OP-04 | 2 |
| orders_payments.md | OP-05 | 2 |
| orders_payments.md | OP-06 | 2 |
| products.md | PR-00 | 2 |
| products.md | PR-BL-301 | 2 |
| products.md | PR-BL-302 | 2 |
| products.md | PR-BL-303 | 2 |
| products.md | PR-BL-304 | 3 |
| products.md | PR-DR-101 | 2 |
| products.md | PR-DR-102 | 3 |
| products.md | PR-DR-103 | 3 |
| products.md | PR-DR-104 | 2 |
| products.md | PR-KN-401 | 2 |
| products.md | PR-KN-402 | 2 |
| products.md | PR-KN-403 | 2 |
| products.md | PR-KN-404 | 2 |
| products.md | PR-OT-501 | 2 |
| products.md | PR-OT-502 | 2 |
| products.md | PR-OT-503 | 2 |
| products.md | PR-OT-504 | 3 |
| products.md | PR-SK-201 | 2 |
| products.md | PR-SK-202 | 3 |
| products.md | PR-SK-203 | 2 |
| products.md | PR-SK-204 | 2 |
| returns_policy.md | RT-01 | 3 |
| returns_policy.md | RT-02 | 2 |
| returns_policy.md | RT-03 | 3 |
| returns_policy.md | RT-04 | 2 |
| returns_policy.md | RT-05 | 2 |
| shipping_policy.md | SH-02 | 2 |
| shipping_policy.md | SH-03 | 3 |
| shipping_policy.md | SH-04 | 2 |
| shipping_policy.md | SH-05 | 2 |
| size_guide.md | SZ-01 | 3 |
| size_guide.md | SZ-02 | 2 |
| size_guide.md | SZ-03 | 2 |
| size_guide.md | SZ-04 | 2 |
| size_guide.md | SZ-05 | 2 |

## Chunks over 150 tokens

None.

## Warnings

- faq.md: missing line: אפשר לפנות בדוא״ל support@liora.example. שעות המענה הדמיוניות: ימים ראשון עד חמי
- faq.md: missing line: ניתן להציע מוצרים לפי מחיר, הרכב בד, צבע, גזרה ומידות המופיעים בקטלוג. אין להמצי
- orders_payments.md: missing line: ניתן לבקש שינוי כתובת משלוח דרך שירות הלקוחות כל עוד ההזמנה טרם נמסרה לחברת המשל
- orders_payments.md: missing line: כדי לבקש ביטול הזמנה פונים לשירות הלקוחות עם מספר ההזמנה. אם ההזמנה טרם נשלחה, ה
- orders_payments.md: missing line: ניתן להזין קוד קופון אחד לכל הזמנה. קופון תקף רק למוצרים ולתקופה שמצוינים בתנאיו
- orders_payments.md: missing line: העוזרת מספקת מידע כללי בלבד: היא אינה בודקת חיובים, מספרי כרטיסים, סטטוס הזמנה, 
- products.md: missing line: כל מחיר נקוב בשקלים חדשים (₪) למוצר יחיד, לפני דמי משלוח והנחות. רשימת המידות הי
- products.md: missing line: - הרכב בד: 95% כותנה, 5% אלסטן
- products.md: missing line: - תיאור: בד קליל, אינו מכיל כותנה.
- products.md: missing line: - גזרה ומאפיינים: גזרה רחבה; אורך מידי; שרוול שלושה רבעים
- products.md: missing line: - הרכב בד: 70% ויסקוזה, 30% פוליאסטר
- products.md: missing line: - הרכב בד: 98% כותנה, 2% אלסטן
- products.md: missing line: - גזרה ומאפיינים: גזרה ישרה; אורך מקסי
- products.md: missing line: - מידות מוצעות: XS, S, M, L, XL
- products.md: missing line: - הרכב בד: 95% כותנה, 5% אלסטן
- products.md: missing line: - מידות מוצעות: S, M, L, XL, XXL
- products.md: missing line: - גזרה ומאפיינים: גזרה רחבה; שרוול ארוך; דורשת שכבת בסיס
- products.md: missing line: - הרכב בד: 60% כותנה, 40% אקריליק
- products.md: missing line: - הרכב בד: 50% ויסקוזה, 50% אקריליק
- products.md: missing line: - הרכב בד: 70% אקריליק, 30% צמר
- products.md: missing line: - הרכב בד: 65% פוליאסטר, 35% ויסקוזה
- products.md: missing line: - הרכב בד: 70% פוליאסטר, 30% ויסקוזה
- products.md: missing line: - מידות מוצעות: XS, S, M, L, XL
- returns_policy.md: missing line: לפי מדיניות ההדגמה של החנות ניתן לבקש החזרה בתוך 14 ימים ממועד קבלת המוצר. כדי ש
- returns_policy.md: missing line: פונים לשירות הלקוחות בדוא״ל support@liora.example עם מספר הזמנה, קוד מוצר וסיבת 
- returns_policy.md: missing line: לאחר קבלת המוצר ובדיקתו, החזר כספי מאושר יבוצע לאמצעי התשלום המקורי בתוך עד 7 ימ
- returns_policy.md: missing line: ניתן לבקש החלפת מידה בתוך 14 ימים מקבלת המוצר, אם המוצר עומד בתנאי RT-01. ההחלפה
- returns_policy.md: missing line: אם התקבל מוצר פגום או מוצר שונה מהמוזמן, יש לפנות ל־support@liora.example עם מספ
- shipping_policy.md: missing line: עלות משלוח רגיל היא 25 ₪ להזמנה. זמן האספקה המשוער הוא 3–5 ימי עסקים ממועד אישור
- shipping_policy.md: missing line: בהזמנה שסכום המוצרים שלה הוא 299 ₪ ומעלה, המשלוח הרגיל חינם. הזכאות נקבעת לפי סכ
- shipping_policy.md: missing line: איסוף עצמי הוא ללא תשלום. ההזמנה תהיה מוכנה לאיסוף בדרך כלל בתוך 1–2 ימי עסקים מ
- shipping_policy.md: missing line: לאחר מסירת הזמנה לחברת המשלוחים נשלחת הודעת מעקב לכתובת הדוא״ל שנמסרה בהזמנה. במ
- size_guide.md: missing line: | מידה | היקף חזה (ס״מ) | היקף מותן (ס״מ) | היקף ירכיים (ס״מ) |
- size_guide.md: missing line: חזה: מודדים סביב החלק הרחב ביותר, בלי להדק את סרט המדידה. מותן: מודדים סביב החלק
- size_guide.md: missing line: כאשר המדידות נמצאות בין שתי מידות, יש לבחון את הגזרה ואת סוג הבד. בגזרה ישרה או 
- size_guide.md: missing line: גזרה רחבה: נופלת באופן משוחרר. גזרה ישרה: קו אחיד יחסית. גזרה מחויטת: בנויה קרוב
- size_guide.md: missing line: הטבלה מסבירה מה משמעות המידות; היא אינה מעידה שכל מוצר נמכר בכל המידות. זמינות מ

## All chunks

Text tokens = the chunk text. Embed tokens = what is actually sent to the embedding model (text + visible metadata).

| # | Document | Section ID | Section title | Type | Part | Text tokens | Embed tokens |
|---:|---|---|---|---|---|---:|---:|
| 1 | faq.md | FAQ-INTRO | Liora Fashion — שאלות נפוצות | preamble | 1/1 | 54 | 76 |
| 2 | faq.md | FAQ-01 | איך פונים לשירות הלקוחות? | section | 1/2 | 101 | 123 |
| 3 | faq.md | FAQ-01 | איך פונים לשירות הלקוחות? | section | 2/2 | 78 | 100 |
| 4 | faq.md | FAQ-02 | איך יודעים אם מידה זמינה? | section | 1/1 | 130 | 152 |
| 5 | faq.md | FAQ-03 | האם אפשר לקבל התראה כשמידה חוזרת למלאי? | section | 1/1 | 143 | 165 |
| 6 | faq.md | FAQ-04 | האם קיימת אריזת מתנה? | section | 1/1 | 123 | 145 |
| 7 | faq.md | FAQ-05 | איך בוחרים מידה? | section | 1/1 | 106 | 128 |
| 8 | faq.md | FAQ-06 | מהן אפשרויות המשלוח? | section | 1/1 | 127 | 149 |
| 9 | faq.md | FAQ-07 | איך מחזירים מוצר? | section | 1/1 | 116 | 138 |
| 10 | faq.md | FAQ-08 | האם יש הנחה קבועה לסטודנטיות? | section | 1/1 | 126 | 148 |
| 11 | faq.md | FAQ-09 | האם אפשר לקבל המלצה על מוצר? | section | 1/2 | 101 | 123 |
| 12 | faq.md | FAQ-09 | האם אפשר לקבל המלצה על מוצר? | section | 2/2 | 103 | 125 |
| 13 | orders_payments.md | ORDERS-INTRO | Liora Fashion — הזמנות ותשלומים | preamble | 1/1 | 62 | 87 |
| 14 | orders_payments.md | OP-01 | אמצעי תשלום | section | 1/1 | 124 | 149 |
| 15 | orders_payments.md | OP-02 | אישור הזמנה | section | 1/1 | 131 | 156 |
| 16 | orders_payments.md | OP-03 | שינוי כתובת | section | 1/2 | 100 | 125 |
| 17 | orders_payments.md | OP-03 | שינוי כתובת | section | 2/2 | 111 | 136 |
| 18 | orders_payments.md | OP-04 | בקשת ביטול | section | 1/2 | 131 | 156 |
| 19 | orders_payments.md | OP-04 | בקשת ביטול | section | 2/2 | 125 | 150 |
| 20 | orders_payments.md | OP-05 | קופונים והנחות | section | 1/2 | 103 | 128 |
| 21 | orders_payments.md | OP-05 | קופונים והנחות | section | 2/2 | 118 | 143 |
| 22 | orders_payments.md | OP-06 | מידע אישי | section | 1/2 | 123 | 148 |
| 23 | orders_payments.md | OP-06 | מידע אישי | section | 2/2 | 43 | 68 |
| 24 | products.md | PRODUCTS-INTRO | Liora Fashion — קטלוג מוצרים | preamble | 1/1 | 119 | 141 |
| 25 | products.md | PR-00 | כללי קטלוג | section | 1/2 | 143 | 165 |
| 26 | products.md | PR-00 | כללי קטלוג | section | 2/2 | 74 | 96 |
| 27 | products.md | PR-DR-101 | שמלת מיה | section | 1/2 | 124 | 146 |
| 28 | products.md | PR-DR-101 | שמלת מיה | section | 2/2 | 148 | 170 |
| 29 | products.md | PR-DR-102 | שמלת נועה | section | 1/3 | 101 | 123 |
| 30 | products.md | PR-DR-102 | שמלת נועה | section | 2/3 | 141 | 163 |
| 31 | products.md | PR-DR-102 | שמלת נועה | section | 3/3 | 33 | 55 |
| 32 | products.md | PR-DR-103 | שמלת אלה | section | 1/3 | 98 | 120 |
| 33 | products.md | PR-DR-103 | שמלת אלה | section | 2/3 | 84 | 106 |
| 34 | products.md | PR-DR-103 | שמלת אלה | section | 3/3 | 93 | 115 |
| 35 | products.md | PR-DR-104 | שמלת רוני | section | 1/2 | 121 | 143 |
| 36 | products.md | PR-DR-104 | שמלת רוני | section | 2/2 | 141 | 163 |
| 37 | products.md | PR-SK-201 | חצאית פליסה | section | 1/2 | 105 | 127 |
| 38 | products.md | PR-SK-201 | חצאית פליסה | section | 2/2 | 144 | 166 |
| 39 | products.md | PR-SK-202 | חצאית ג׳ינס מקסי | section | 1/3 | 139 | 161 |
| 40 | products.md | PR-SK-202 | חצאית ג׳ינס מקסי | section | 2/3 | 71 | 93 |
| 41 | products.md | PR-SK-202 | חצאית ג׳ינס מקסי | section | 3/3 | 108 | 130 |
| 42 | products.md | PR-SK-203 | חצאית סאטן | section | 1/2 | 107 | 129 |
| 43 | products.md | PR-SK-203 | חצאית סאטן | section | 2/2 | 143 | 165 |
| 44 | products.md | PR-SK-204 | חצאית כותנה | section | 1/2 | 118 | 140 |
| 45 | products.md | PR-SK-204 | חצאית כותנה | section | 2/2 | 140 | 162 |
| 46 | products.md | PR-BL-301 | חולצת ליבי | section | 1/2 | 129 | 151 |
| 47 | products.md | PR-BL-301 | חולצת ליבי | section | 2/2 | 125 | 147 |
| 48 | products.md | PR-BL-302 | חולצת כפתורים | section | 1/2 | 110 | 132 |
| 49 | products.md | PR-BL-302 | חולצת כפתורים | section | 2/2 | 142 | 164 |
| 50 | products.md | PR-BL-303 | חולצת כותנה | section | 1/2 | 107 | 129 |
| 51 | products.md | PR-BL-303 | חולצת כותנה | section | 2/2 | 134 | 156 |
| 52 | products.md | PR-BL-304 | חולצת שיפון | section | 1/3 | 103 | 125 |
| 53 | products.md | PR-BL-304 | חולצת שיפון | section | 2/3 | 89 | 111 |
| 54 | products.md | PR-BL-304 | חולצת שיפון | section | 3/3 | 96 | 118 |
| 55 | products.md | PR-KN-401 | סריג רך | section | 1/2 | 123 | 145 |
| 56 | products.md | PR-KN-401 | סריג רך | section | 2/2 | 130 | 152 |
| 57 | products.md | PR-KN-402 | קרדיגן ארוך | section | 1/2 | 125 | 147 |
| 58 | products.md | PR-KN-402 | קרדיגן ארוך | section | 2/2 | 132 | 154 |
| 59 | products.md | PR-KN-403 | סריג פסים | section | 1/2 | 115 | 137 |
| 60 | products.md | PR-KN-403 | סריג פסים | section | 2/2 | 141 | 163 |
| 61 | products.md | PR-KN-404 | סריג צווארון | section | 1/2 | 130 | 152 |
| 62 | products.md | PR-KN-404 | סריג צווארון | section | 2/2 | 121 | 143 |
| 63 | products.md | PR-OT-501 | ז׳קט מחויט | section | 1/2 | 131 | 153 |
| 64 | products.md | PR-OT-501 | ז׳קט מחויט | section | 2/2 | 122 | 144 |
| 65 | products.md | PR-OT-502 | וסט ארוך | section | 1/2 | 104 | 126 |
| 66 | products.md | PR-OT-502 | וסט ארוך | section | 2/2 | 139 | 161 |
| 67 | products.md | PR-OT-503 | בלייזר קלאסי | section | 1/2 | 135 | 157 |
| 68 | products.md | PR-OT-503 | בלייזר קלאסי | section | 2/2 | 131 | 153 |
| 69 | products.md | PR-OT-504 | עליונית קלילה | section | 1/3 | 114 | 136 |
| 70 | products.md | PR-OT-504 | עליונית קלילה | section | 2/3 | 83 | 105 |
| 71 | products.md | PR-OT-504 | עליונית קלילה | section | 3/3 | 96 | 118 |
| 72 | returns_policy.md | RETURNS-INTRO | Liora Fashion — החזרות והחלפות | preamble | 1/1 | 106 | 131 |
| 73 | returns_policy.md | RT-01 | בקשת החזרה | section | 1/3 | 85 | 110 |
| 74 | returns_policy.md | RT-01 | בקשת החזרה | section | 2/3 | 134 | 159 |
| 75 | returns_policy.md | RT-01 | בקשת החזרה | section | 3/3 | 109 | 134 |
| 76 | returns_policy.md | RT-02 | איך מבקשים החזרה | section | 1/2 | 129 | 154 |
| 77 | returns_policy.md | RT-02 | איך מבקשים החזרה | section | 2/2 | 50 | 75 |
| 78 | returns_policy.md | RT-03 | החזר כספי | section | 1/3 | 116 | 141 |
| 79 | returns_policy.md | RT-03 | החזר כספי | section | 2/3 | 131 | 156 |
| 80 | returns_policy.md | RT-03 | החזר כספי | section | 3/3 | 50 | 75 |
| 81 | returns_policy.md | RT-04 | החלפת מידה | section | 1/2 | 130 | 155 |
| 82 | returns_policy.md | RT-04 | החלפת מידה | section | 2/2 | 59 | 84 |
| 83 | returns_policy.md | RT-05 | מוצר פגום או שגוי | section | 1/2 | 130 | 155 |
| 84 | returns_policy.md | RT-05 | מוצר פגום או שגוי | section | 2/2 | 148 | 173 |
| 85 | returns_policy.md | RT-06 | סייג חשוב | section | 1/1 | 91 | 116 |
| 86 | shipping_policy.md | SHIPPING-INTRO | Liora Fashion — מדיניות משלוחים | preamble | 1/1 | 82 | 105 |
| 87 | shipping_policy.md | SH-01 | אזורי משלוח | section | 1/1 | 129 | 152 |
| 88 | shipping_policy.md | SH-02 | משלוח רגיל | section | 1/2 | 104 | 127 |
| 89 | shipping_policy.md | SH-02 | משלוח רגיל | section | 2/2 | 102 | 125 |
| 90 | shipping_policy.md | SH-03 | משלוח חינם | section | 1/3 | 132 | 155 |
| 91 | shipping_policy.md | SH-03 | משלוח חינם | section | 2/3 | 79 | 102 |
| 92 | shipping_policy.md | SH-03 | משלוח חינם | section | 3/3 | 105 | 128 |
| 93 | shipping_policy.md | SH-04 | איסוף עצמי | section | 1/2 | 144 | 167 |
| 94 | shipping_policy.md | SH-04 | איסוף עצמי | section | 2/2 | 46 | 69 |
| 95 | shipping_policy.md | SH-05 | מעקב ועיכובים | section | 1/2 | 93 | 116 |
| 96 | shipping_policy.md | SH-05 | מעקב ועיכובים | section | 2/2 | 123 | 146 |
| 97 | size_guide.md | SIZES-INTRO | Liora Fashion — מדריך מידות | preamble | 1/1 | 72 | 91 |
| 98 | size_guide.md | SZ-01 | טבלת מידות גוף בסנטימטרים | section | 1/3 | 146 | 165 |
| 99 | size_guide.md | SZ-01 | טבלת מידות גוף בסנטימטרים | section | 2/3 | 150 | 169 |
| 100 | size_guide.md | SZ-01 | טבלת מידות גוף בסנטימטרים | section | 3/3 | 93 | 112 |
| 101 | size_guide.md | SZ-02 | אופן מדידה | section | 1/2 | 143 | 162 |
| 102 | size_guide.md | SZ-02 | אופן מדידה | section | 2/2 | 65 | 84 |
| 103 | size_guide.md | SZ-03 | בחירת מידה | section | 1/2 | 75 | 94 |
| 104 | size_guide.md | SZ-03 | בחירת מידה | section | 2/2 | 139 | 158 |
| 105 | size_guide.md | SZ-04 | הבדלי גזרות | section | 1/2 | 115 | 134 |
| 106 | size_guide.md | SZ-04 | הבדלי גזרות | section | 2/2 | 100 | 119 |
| 107 | size_guide.md | SZ-05 | זמינות מידות | section | 1/2 | 82 | 101 |
| 108 | size_guide.md | SZ-05 | זמינות מידות | section | 2/2 | 95 | 114 |

## Chunk texts (exactly as they will be embedded)

### 1. `faq.md::FAQ-INTRO::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

# Liora Fashion — שאלות נפוצות
> מסמך הדגמה. מזהה: FAQ. גרסה: 1.0.
```

### 2. `faq.md::FAQ-01::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-01 איך פונים לשירות הלקוחות?
אפשר לפנות בדוא״ל support@liora.example. שעות המענה הדמיוניות: ימים ראשון עד חמישי, 09:00–17:00.
```

### 3. `faq.md::FAQ-01::p2`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-01 איך פונים לשירות הלקוחות?
כתובת הדוא״ל משתמשת בדומיין example ואינה תיבת שירות אמיתית.
```

### 4. `faq.md::FAQ-02::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-02 איך יודעים אם מידה זמינה?
רשימת המידות המוצעות מופיעה ב־products.md תחת כל מוצר. המידע אינו מלאי בזמן אמת. לבירור מלאי עדכני יש לפנות לנציג שירות.
```

### 5. `faq.md::FAQ-03::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-03 האם אפשר לקבל התראה כשמידה חוזרת למלאי?
אפשר לבקש מנציג שירות לקבל עדכון, אך אין במערכת הדמיונית שירות התראות אוטומטי או התחייבות לזמן חידוש מלאי.
```

### 6. `faq.md::FAQ-04::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-04 האם קיימת אריזת מתנה?
ניתן לבקש אריזת מתנה ללא תוספת תשלום בעת ההזמנה, בכפוף לזמינות חומרי אריזה. אין שירות הוספת הקדשה אישית.
```

### 7. `faq.md::FAQ-05::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-05 איך בוחרים מידה?
יש לעיין בטבלת המידות שב־size_guide.md ולהצליב עם גזרת המוצר המפורטת ב־products.md. אין התחייבות להתאמה אישית.
```

### 8. `faq.md::FAQ-06::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-06 מהן אפשרויות המשלוח?
פרטי עלויות, זמני אספקה, סף משלוח חינם ואיסוף עצמי מפורטים ב־shipping_policy.md. מסמך זה אינו משנה את תנאי המשלוח.
```

### 9. `faq.md::FAQ-07::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-07 איך מחזירים מוצר?
תנאי ההחזרה, החלפת המידה וטיפול במוצר פגום מפורטים ב־returns_policy.md. יש לפנות לשירות הלקוחות לפי ההוראות שם.
```

### 10. `faq.md::FAQ-08::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-08 האם יש הנחה קבועה לסטודנטיות?
אין במאגר מדיניות הנחה קבועה לסטודנטיות. אין להסיק מכך בוודאות שהנחה כזו קיימת או שאינה קיימת.
```

### 11. `faq.md::FAQ-09::p1`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-09 האם אפשר לקבל המלצה על מוצר?
ניתן להציע מוצרים לפי מחיר, הרכב בד, צבע, גזרה ומידות המופיעים בקטלוג.
```

### 12. `faq.md::FAQ-09::p2`

```text
document_title: Liora Fashion — שאלות נפוצות

## FAQ-09 האם אפשר לקבל המלצה על מוצר?
אין להמציא התאמה למבנה גוף, זמינות בזמן אמת או תכונות שלא מופיעות במסמכים.
```

### 13. `orders_payments.md::ORDERS-INTRO::p1`

```text
document_title: Liora Fashion — הזמנות ותשלומים

# Liora Fashion — הזמנות ותשלומים
> נתוני הדגמה בלבד. מזהה: ORDERS. גרסה: 1.0.
```

### 14. `orders_payments.md::OP-01::p1`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-01 אמצעי תשלום
באתר הדמיוני ניתן לשלם בכרטיס אשראי. אין תמיכה במזומן בעת המסירה, בהעברה בנקאית או בתשלום באמצעות ארנק דיגיטלי.
```

### 15. `orders_payments.md::OP-02::p1`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-02 אישור הזמנה
לאחר אישור התשלום נשלח אישור הזמנה לדוא״ל, הכולל מספר הזמנה ורשימת פריטים. אישור הזמנה אינו מהווה התחייבות למלאי בזמן אמת.
```

### 16. `orders_payments.md::OP-03::p1`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-03 שינוי כתובת
ניתן לבקש שינוי כתובת משלוח דרך שירות הלקוחות כל עוד ההזמנה טרם נמסרה לחברת המשלוחים.
```

### 17. `orders_payments.md::OP-03::p2`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-03 שינוי כתובת
לאחר מסירתה לחברת המשלוחים, לא ניתן לשנות את הכתובת דרך החנות. אין לעוזרת ה־AI גישה למצב ההזמנה האישית.
```

### 18. `orders_payments.md::OP-04::p1`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-04 בקשת ביטול
כדי לבקש ביטול הזמנה פונים לשירות הלקוחות עם מספר ההזמנה. אם ההזמנה טרם נשלחה, הצוות יבדוק אפשרות לביטול לפני משלוח.
```

### 19. `orders_payments.md::OP-04::p2`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-04 בקשת ביטול
אם כבר נשלחה, יש לפעול בהתאם להוראות השירות ולמדיניות ההחזרות, בכפוף לדין. אין לעוזרת ה־AI אפשרות לבצע ביטול בפועל.
```

### 20. `orders_payments.md::OP-05::p1`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-05 קופונים והנחות
ניתן להזין קוד קופון אחד לכל הזמנה. קופון תקף רק למוצרים ולתקופה שמצוינים בתנאיו.
```

### 21. `orders_payments.md::OP-05::p2`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-05 קופונים והנחות
חישוב סף המשלוח החינם מתבצע על סכום המוצרים לאחר הנחות. אין במאגר קוד קופון פעיל או הבטחה למבצע מסוים.
```

### 22. `orders_payments.md::OP-06::p1`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-06 מידע אישי
העוזרת מספקת מידע כללי בלבד: היא אינה בודקת חיובים, מספרי כרטיסים, סטטוס הזמנה, החזרים אישיים או נתוני לקוחות.
```

### 23. `orders_payments.md::OP-06::p2`

```text
document_title: Liora Fashion — הזמנות ותשלומים

## OP-06 מידע אישי
אין למסור לה פרטי כרטיס אשראי.
```

### 24. `products.md::PRODUCTS-INTRO::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

# Liora Fashion — קטלוג מוצרים
> נתוני הדגמה בלבד. מזהה: PRODUCTS. גרסה: 1.0. מצב המידות והצבעים הוא צילום מצב לימודי, לא נתוני מלאי בזמן אמת.
```

### 25. `products.md::PR-00::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-00 כללי קטלוג
כל מחיר נקוב בשקלים חדשים (₪) למוצר יחיד, לפני דמי משלוח והנחות. רשימת המידות היא רשימת מידות המוצעות בקטלוג, ואינה מבטיחה מלאי חי.
```

### 26. `products.md::PR-00::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-00 כללי קטלוג
לכל מוצר קוד קבוע. ההגדרות של מידות הגוף נמצאות במסמך size_guide.md.
```

### 27. `products.md::PR-DR-101::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-101 | שמלת מיה
- קוד מוצר: DR-101
- קטגוריה: שמלות
- מחיר: 249 ₪
- צבעים: שחור, בז׳, כחול
- מידות מוצעות: S, M, L, XL
- הרכב בד: 95% כותנה,
```

### 28. `products.md::PR-DR-101::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-101 | שמלת מיה
5% אלסטן
- גזרה ומאפיינים: גזרה ישרה; אורך מידי; שרוול ארוך
- הוראות טיפול: כביסה עד 30°C
- תיאור: בד כותנה נעים ונושם עם גמישות קלה.
```

### 29. `products.md::PR-DR-102::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-102 | שמלת נועה
- קוד מוצר: DR-102
- קטגוריה: שמלות
- מחיר: 329 ₪
- צבעים: שחור, ירוק זית
- מידות מוצעות: M, L,
```

### 30. `products.md::PR-DR-102::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-102 | שמלת נועה
L, XL
- הרכב בד: 100% פוליאסטר
- גזרה ומאפיינים: גזרה רחבה; אורך מקסי; שרוול ארוך
- הוראות טיפול: כביסה עד 30°C
- תיאור: בד קליל,
```

### 31. `products.md::PR-DR-102::p3`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-102 | שמלת נועה
אינו מכיל כותנה.
```

### 32. `products.md::PR-DR-103::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-103 | שמלת אלה
- קוד מוצר: DR-103
- קטגוריה: שמלות
- מחיר: 279 ₪
- צבעים: שמנת, תכלת
- מידות מוצעות: XS, S, M,
```

### 33. `products.md::PR-DR-103::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-103 | שמלת אלה
S, M, L
- הרכב בד: 100% ויסקוזה
- גזרה ומאפיינים: גזרה רחבה; אורך מידי;
```

### 34. `products.md::PR-DR-103::p3`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-103 | שמלת אלה
אורך מידי; שרוול שלושה רבעים
- הוראות טיפול: כביסה עד 30°C
- תיאור: בד ויסקוזה רך.
```

### 35. `products.md::PR-DR-104::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-104 | שמלת רוני
- קוד מוצר: DR-104
- קטגוריה: שמלות
- מחיר: 359 ₪
- צבעים: בורדו, שחור
- מידות מוצעות: S, M, L
- הרכב בד: 70% ויסקוזה,
```

### 36. `products.md::PR-DR-104::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-DR-104 | שמלת רוני
30% פוליאסטר
- גזרה ומאפיינים: גזרה מחויטת; אורך מקסי; שרוול ארוך
- הוראות טיפול: ניקוי עדין
- תיאור: שמלה אלגנטית לאירועים.
```

### 37. `products.md::PR-SK-201::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-201 | חצאית פליסה
- קוד מוצר: SK-201
- קטגוריה: חצאיות
- מחיר: 189 ₪
- צבעים: שחור, חום
- מידות מוצעות: S, M, L,
```

### 38. `products.md::PR-SK-201::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-201 | חצאית פליסה
M, L, XL
- הרכב בד: 100% פוליאסטר
- גזרה ומאפיינים: גזרה רחבה; אורך מקסי
- הוראות טיפול: כביסה עד 30°C
- תיאור: קפלים קבועים.
```

### 39. `products.md::PR-SK-202::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-202 | חצאית ג׳ינס מקסי
- קוד מוצר: SK-202
- קטגוריה: חצאיות
- מחיר: 219 ₪
- צבעים: כחול כהה, שחור
- מידות מוצעות: XS, S, M, L
- הרכב בד: 98% כותנה,
```

### 40. `products.md::PR-SK-202::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-202 | חצאית ג׳ינס מקסי
2% אלסטן
- גזרה ומאפיינים: גזרה ישרה;
```

### 41. `products.md::PR-SK-202::p3`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-202 | חצאית ג׳ינס מקסי
אורך מקסי
- הוראות טיפול: כביסה הפוכה עד 30°C
- תיאור: בד ג׳ינס עם גמישות קלה.
```

### 42. `products.md::PR-SK-203::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-203 | חצאית סאטן
- קוד מוצר: SK-203
- קטגוריה: חצאיות
- מחיר: 229 ₪
- צבעים: שמפניה, שחור
- מידות מוצעות: S, M,
```

### 43. `products.md::PR-SK-203::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-203 | חצאית סאטן
M, L
- הרכב בד: 100% פוליאסטר
- גזרה ומאפיינים: גזרה רחבה; אורך מקסי
- הוראות טיפול: כביסה עדינה ביד
- תיאור: גימור מבריק.
```

### 44. `products.md::PR-SK-204::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-204 | חצאית כותנה
- קוד מוצר: SK-204
- קטגוריה: חצאיות
- מחיר: 169 ₪
- צבעים: לבן, בז׳, ירוק זית
- מידות מוצעות: XS, S, M, L,
```

### 45. `products.md::PR-SK-204::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-SK-204 | חצאית כותנה
S, M, L, XL
- הרכב בד: 100% כותנה
- גזרה ומאפיינים: גזרה רחבה; אורך מידי
- הוראות טיפול: כביסה עד 30°C
- תיאור: בד נושם ליומיום.
```

### 46. `products.md::PR-BL-301::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-301 | חולצת ליבי
- קוד מוצר: BL-301
- קטגוריה: חולצות
- מחיר: 139 ₪
- צבעים: לבן, ורוד בהיר
- מידות מוצעות: S, M, L, XL
- הרכב בד: 95% כותנה,
```

### 47. `products.md::PR-BL-301::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-301 | חולצת ליבי
5% אלסטן
- גזרה ומאפיינים: גזרה ישרה; שרוול ארוך
- הוראות טיפול: כביסה עד 30°C
- תיאור: חולצה רכה ונוחה.
```

### 48. `products.md::PR-BL-302::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-302 | חולצת כפתורים
- קוד מוצר: BL-302
- קטגוריה: חולצות
- מחיר: 179 ₪
- צבעים: לבן, תכלת
- מידות מוצעות: XS, S, M,
```

### 49. `products.md::PR-BL-302::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-302 | חולצת כפתורים
S, M, L
- הרכב בד: 100% כותנה
- גזרה ומאפיינים: גזרה מחויטת; שרוול ארוך
- הוראות טיפול: כביסה עד 30°C
- תיאור: חולצה מכופתרת.
```

### 50. `products.md::PR-BL-303::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-303 | חולצת כותנה
- קוד מוצר: BL-303
- קטגוריה: חולצות
- מחיר: 119 ₪
- צבעים: שחור, שמנת
- מידות מוצעות: S, M, L, XL,
```

### 51. `products.md::PR-BL-303::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-303 | חולצת כותנה
M, L, XL, XXL
- הרכב בד: 100% כותנה
- גזרה ומאפיינים: גזרה רחבה; שרוול ארוך
- הוראות טיפול: כביסה עד 30°C
- תיאור: בד נושם.
```

### 52. `products.md::PR-BL-304::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-304 | חולצת שיפון
- קוד מוצר: BL-304
- קטגוריה: חולצות
- מחיר: 159 ₪
- צבעים: שמנת, כחול
- מידות מוצעות: S, M,
```

### 53. `products.md::PR-BL-304::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-304 | חולצת שיפון
M, L
- הרכב בד: 100% פוליאסטר
- גזרה ומאפיינים: גזרה רחבה; שרוול ארוך;
```

### 54. `products.md::PR-BL-304::p3`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-BL-304 | חולצת שיפון
שרוול ארוך; דורשת שכבת בסיס
- הוראות טיפול: כביסה עדינה ביד
- תיאור: בד שיפון קל.
```

### 55. `products.md::PR-KN-401::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-401 | סריג רך
- קוד מוצר: KN-401
- קטגוריה: סריגים
- מחיר: 199 ₪
- צבעים: אפור, בז׳
- מידות מוצעות: S, M, L, XL
- הרכב בד: 60% כותנה,
```

### 56. `products.md::PR-KN-401::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-401 | סריג רך
40% אקריליק
- גזרה ומאפיינים: גזרה רחבה; שרוול ארוך
- הוראות טיפול: כביסה עדינה עד 30°C
- תיאור: סריג רך לעונות מעבר.
```

### 57. `products.md::PR-KN-402::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-402 | קרדיגן ארוך
- קוד מוצר: KN-402
- קטגוריה: סריגים
- מחיר: 239 ₪
- צבעים: שחור, חום
- מידות מוצעות: S, M, L
- הרכב בד: 50% ויסקוזה,
```

### 58. `products.md::PR-KN-402::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-402 | קרדיגן ארוך
50% אקריליק
- גזרה ומאפיינים: גזרה רחבה; אורך ארוך
- הוראות טיפול: כביסה עדינה עד 30°C
- תיאור: שכבה עליונה פתוחה.
```

### 59. `products.md::PR-KN-403::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-403 | סריג פסים
- קוד מוצר: KN-403
- קטגוריה: סריגים
- מחיר: 189 ₪
- צבעים: שחור־לבן, כחול־לבן
- מידות מוצעות: XS, S, M,
```

### 60. `products.md::PR-KN-403::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-403 | סריג פסים
S, M, L
- הרכב בד: 100% כותנה
- גזרה ומאפיינים: גזרה ישרה; שרוול ארוך
- הוראות טיפול: כביסה עד 30°C
- תיאור: סריג כותנה מפוספס.
```

### 61. `products.md::PR-KN-404::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-404 | סריג צווארון
- קוד מוצר: KN-404
- קטגוריה: סריגים
- מחיר: 209 ₪
- צבעים: שמנת, ירוק כהה
- מידות מוצעות: M, L, XL
- הרכב בד: 70% אקריליק,
```

### 62. `products.md::PR-KN-404::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-KN-404 | סריג צווארון
30% צמר
- גזרה ומאפיינים: גזרה ישרה; שרוול ארוך
- הוראות טיפול: כביסה ביד במים קרים
- תיאור: סריג חמים.
```

### 63. `products.md::PR-OT-501::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-501 | ז׳קט מחויט
- קוד מוצר: OT-501
- קטגוריה: עליוניות
- מחיר: 349 ₪
- צבעים: שחור, אפור
- מידות מוצעות: S, M, L
- הרכב בד: 65% פוליאסטר,
```

### 64. `products.md::PR-OT-501::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-501 | ז׳קט מחויט
35% ויסקוזה
- גזרה ומאפיינים: גזרה מחויטת; שרוול ארוך
- הוראות טיפול: ניקוי יבש
- תיאור: ז׳קט מובנה.
```

### 65. `products.md::PR-OT-502::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-502 | וסט ארוך
- קוד מוצר: OT-502
- קטגוריה: עליוניות
- מחיר: 229 ₪
- צבעים: בז׳, שחור
- מידות מוצעות: S, M, L,
```

### 66. `products.md::PR-OT-502::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-502 | וסט ארוך
M, L, XL
- הרכב בד: 100% פוליאסטר
- גזרה ומאפיינים: גזרה ישרה; ללא שרוולים
- הוראות טיפול: כביסה עד 30°C
- תיאור: וסט לשכבות.
```

### 67. `products.md::PR-OT-503::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-503 | בלייזר קלאסי
- קוד מוצר: OT-503
- קטגוריה: עליוניות
- מחיר: 389 ₪
- צבעים: שחור, כחול כהה
- מידות מוצעות: S, M, L
- הרכב בד: 70% פוליאסטר,
```

### 68. `products.md::PR-OT-503::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-503 | בלייזר קלאסי
30% ויסקוזה
- גזרה ומאפיינים: גזרה מחויטת; שרוול ארוך
- הוראות טיפול: ניקוי יבש
- תיאור: בלייזר לאירועים ולעבודה.
```

### 69. `products.md::PR-OT-504::p1`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-504 | עליונית קלילה
- קוד מוצר: OT-504
- קטגוריה: עליוניות
- מחיר: 199 ₪
- צבעים: שמנת, ירוק זית
- מידות מוצעות: XS, S, M, L,
```

### 70. `products.md::PR-OT-504::p2`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-504 | עליונית קלילה
S, M, L, XL
- הרכב בד: 100% ויסקוזה
- גזרה ומאפיינים: גזרה רחבה;
```

### 71. `products.md::PR-OT-504::p3`

```text
document_title: Liora Fashion — קטלוג מוצרים

## PR-OT-504 | עליונית קלילה
שרוול ארוך
- הוראות טיפול: כביסה עדינה עד 30°C
- תיאור: עליונית קלה לעונות מעבר.
```

### 72. `returns_policy.md::RETURNS-INTRO::p1`

```text
document_title: Liora Fashion — החזרות והחלפות

# Liora Fashion — החזרות והחלפות
> מדיניות דמיונית לצורכי הדגמה בלבד, שאינה מחליפה זכויות לפי דין. מזהה: RETURNS. גרסה: 1.0.
```

### 73. `returns_policy.md::RT-01::p1`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-01 בקשת החזרה
לפי מדיניות ההדגמה של החנות ניתן לבקש החזרה בתוך 14 ימים ממועד קבלת המוצר.
```

### 74. `returns_policy.md::RT-01::p2`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-01 בקשת החזרה
כדי שהחזרה תאושר, המוצר צריך להיות ללא שימוש, נקי, עם התוויות המקוריות ובמצב תקין. יש להציג מספר הזמנה או אישור רכישה.
```

### 75. `returns_policy.md::RT-01::p3`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-01 בקשת החזרה
בקשה לאחר 14 ימים אינה זכאית להחזרה לפי מדיניות ההדגמה הרגילה; זכויות הקבועות בדין אינן נשללות.
```

### 76. `returns_policy.md::RT-02::p1`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-02 איך מבקשים החזרה
פונים לשירות הלקוחות בדוא״ל support@liora.example עם מספר הזמנה, קוד מוצר וסיבת ההחזרה. נציג יחזור עם הוראות למסירת המוצר.
```

### 77. `returns_policy.md::RT-02::p2`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-02 איך מבקשים החזרה
אין לשלוח מוצר לפני קבלת הנחיות.
```

### 78. `returns_policy.md::RT-03::p1`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-03 החזר כספי
לאחר קבלת המוצר ובדיקתו, החזר כספי מאושר יבוצע לאמצעי התשלום המקורי בתוך עד 7 ימי עסקים ממועד האישור.
```

### 79. `returns_policy.md::RT-03::p2`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-03 החזר כספי
דמי המשלוח המקוריים אינם מוחזרים במסגרת מדיניות ההדגמה הרגילה, למעט מקרים שבהם נדרש אחרת על פי דין או בשל טעות של החנות.
```

### 80. `returns_policy.md::RT-03::p3`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-03 החזר כספי
אין התחייבות להחזר לפני בדיקת המוצר.
```

### 81. `returns_policy.md::RT-04::p1`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-04 החלפת מידה
ניתן לבקש החלפת מידה בתוך 14 ימים מקבלת המוצר, אם המוצר עומד בתנאי RT-01. ההחלפה כפופה לזמינות המידה המבוקשת במלאי בעת הטיפול.
```

### 82. `returns_policy.md::RT-04::p2`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-04 החלפת מידה
לא ניתן להבטיח מראש שמידה מסוימת עדיין זמינה.
```

### 83. `returns_policy.md::RT-05::p1`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-05 מוצר פגום או שגוי
אם התקבל מוצר פגום או מוצר שונה מהמוזמן, יש לפנות ל־support@liora.example עם מספר הזמנה, קוד מוצר, תיאור הבעיה ותמונה אם אפשר.
```

### 84. `returns_policy.md::RT-05::p2`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-05 מוצר פגום או שגוי
צוות השירות יבדוק את הפנייה וימסור הוראות להחלפה או להחזר. אין צורך להניח שמדיניות ההחזרה הרגילה ממצה את זכויות הלקוחה במקרה כזה.
```

### 85. `returns_policy.md::RT-06::p1`

```text
document_title: Liora Fashion — החזרות והחלפות

## RT-06 סייג חשוב
המדיניות נוצרה לצורכי תרגול RAG ואינה ייעוץ משפטי או נוסח תקנון לחנות פעילה.
```

### 86. `shipping_policy.md::SHIPPING-INTRO::p1`

```text
document_title: Liora Fashion — מדיניות משלוחים

# Liora Fashion — מדיניות משלוחים
> מסמך דמיוני לצורכי פרויקט לימודי בלבד. מזהה: SHIPPING. גרסה: 1.0.
```

### 87. `shipping_policy.md::SH-01::p1`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-01 אזורי משלוח
החנות מבצעת משלוחים לכתובות בתוך ישראל בלבד. אין משלוחים לחו״ל, לרבות קנדה. השירות אינו מאפשר משלוח לנקודות איסוף חיצוניות.
```

### 88. `shipping_policy.md::SH-02::p1`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-02 משלוח רגיל
עלות משלוח רגיל היא 25 ₪ להזמנה. זמן האספקה המשוער הוא 3–5 ימי עסקים ממועד אישור ההזמנה.
```

### 89. `shipping_policy.md::SH-02::p2`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-02 משלוח רגיל
ימי עסקים הם ראשון עד חמישי, לא כולל חגים. מדובר בטווח משוער, ולא בהתחייבות לתאריך מדויק.
```

### 90. `shipping_policy.md::SH-03::p1`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-03 משלוח חינם
בהזמנה שסכום המוצרים שלה הוא 299 ₪ ומעלה, המשלוח הרגיל חינם. הזכאות נקבעת לפי סכום המוצרים לאחר הנחות ולפני דמי משלוח.
```

### 91. `shipping_policy.md::SH-03::p2`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-03 משלוח חינם
בהזמנה שסכום המוצרים שלה נמוך מ־299 ₪, עלות המשלוח הרגיל היא 25 ₪.
```

### 92. `shipping_policy.md::SH-03::p3`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-03 משלוח חינם
לדוגמה: מוצר ב־249 ₪ ללא הנחה יעלה 274 ₪ כולל משלוח; מוצר ב־329 ₪ ללא הנחה זכאי למשלוח רגיל חינם.
```

### 93. `shipping_policy.md::SH-04::p1`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-04 איסוף עצמי
איסוף עצמי הוא ללא תשלום. ההזמנה תהיה מוכנה לאיסוף בדרך כלל בתוך 1–2 ימי עסקים מאישורה. נקודת האיסוף הדמיונית: רחוב הדוגמה 12, תל אביב.
```

### 94. `shipping_policy.md::SH-04::p2`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-04 איסוף עצמי
יש להמתין להודעת אישור לפני הגעה.
```

### 95. `shipping_policy.md::SH-05::p1`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-05 מעקב ועיכובים
לאחר מסירת הזמנה לחברת המשלוחים נשלחת הודעת מעקב לכתובת הדוא״ל שנמסרה בהזמנה.
```

### 96. `shipping_policy.md::SH-05::p2`

```text
document_title: Liora Fashion — מדיניות משלוחים

## SH-05 מעקב ועיכובים
במקרה של עיכוב ניתן לפנות לשירות הלקוחות עם מספר ההזמנה. לעוזרת ה־AI אין גישה לסטטוס משלוח אישי בזמן אמת.
```

### 97. `size_guide.md::SIZES-INTRO::p1`

```text
document_title: Liora Fashion — מדריך מידות

# Liora Fashion — מדריך מידות
> טבלת מידות דמיונית לצורכי הדגמה. מזהה: SIZES. גרסה: 1.0.
```

### 98. `size_guide.md::SZ-01::p1`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-01 טבלת מידות גוף בסנטימטרים
הטבלה מתייחסת להיקפי גוף ולא למידות הבגד עצמו. המספרים הם טווחי הדגמה.

| מידה | היקף חזה (ס״מ) | היקף מותן (ס״מ) |
```

### 99. `size_guide.md::SZ-01::p2`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-01 טבלת מידות גוף בסנטימטרים
| היקף מותן (ס״מ) | היקף ירכיים (ס״מ) |
|---|---:|---:|---:|
| XS | 78–82 | 60–64 | 86–90 |
| S | 83–88 | 65–70 | 91–96 |
| M | 89–94 | 71–76 | 97–102 |
| L | 95–101 | 77–83
```

### 100. `size_guide.md::SZ-01::p3`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-01 טבלת מידות גוף בסנטימטרים
| 97–102 |
| L | 95–101 | 77–83 | 103–109 |
| XL | 102–109 | 84–91 | 110–117 |
| XXL | 110–118 | 92–100 | 118–126 |
```

### 101. `size_guide.md::SZ-02::p1`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-02 אופן מדידה
חזה: מודדים סביב החלק הרחב ביותר, בלי להדק את סרט המדידה. מותן: מודדים סביב החלק הצר של המותן. ירכיים: מודדים סביב החלק הרחב של הירכיים.
```

### 102. `size_guide.md::SZ-02::p2`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-02 אופן מדידה
מומלץ למדוד בעמידה ישרה ולוודא שהסרט מקביל לרצפה.
```

### 103. `size_guide.md::SZ-03::p1`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-03 בחירת מידה
כאשר המדידות נמצאות בין שתי מידות, יש לבחון את הגזרה ואת סוג הבד.
```

### 104. `size_guide.md::SZ-03::p2`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-03 בחירת מידה
בגזרה ישרה או מחויטת ייתכן שתועדף המידה הגדולה יותר; בגזרה רחבה יש יותר חופש תנועה. התאמה אישית אינה מובטחת על סמך הטבלה בלבד.
```

### 105. `size_guide.md::SZ-04::p1`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-04 הבדלי גזרות
גזרה רחבה: נופלת באופן משוחרר. גזרה ישרה: קו אחיד יחסית. גזרה מחויטת: בנויה קרוב יותר לקווי הגוף.
```

### 106. `size_guide.md::SZ-04::p2`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-04 הבדלי גזרות
בד עם אלסטן עשוי להיות גמיש יותר מבד ללא אלסטן. יש לעיין גם בתיאור המוצר הספציפי.
```

### 107. `size_guide.md::SZ-05::p1`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-05 זמינות מידות
הטבלה מסבירה מה משמעות המידות; היא אינה מעידה שכל מוצר נמכר בכל המידות.
```

### 108. `size_guide.md::SZ-05::p2`

```text
document_title: Liora Fashion — מדריך מידות

## SZ-05 זמינות מידות
זמינות מידות לפי מוצר מוגדרת אך ורק במסמך products.md, והיא תמונת מצב לימודית ולא מלאי חי.
```
