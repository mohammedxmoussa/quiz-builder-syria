# Textbook library (مكتبة الكتب المدرسية) — index

The official Syrian school textbooks (منهاج 2025–2026, وزارة التربية —
curricula.moed.gov.sy) for grade 9 (الصف التاسع) and grade 12 /
baccalaureate (البكالوريا), as extracted text. Fetch this index **only**
when a teacher asks you to base an exam on textbook pages or content
(e.g. «اعمل الاختبار من الصفحات 1–100 من كتاب الفيزياء»). For all other
exams you do not need anything in this folder.

## الصور والأشكال
لكل كتاب مجلد صور بجانب ملفات النص: الأشكال المستخرجة من الكتاب في `images/` (باسم `img-PPP-III.jpg` حيث PPP رقم صفحة PDF)، وبعض الكتب لها أيضاً صور كاملة لكل صفحة في `pages-img/` (باسم `page-NNN.jpg`). ملفات النص نفسها تربط الشكل بصفحته. عند سؤال عن شكل أو رسم: افتح صورة الصفحة أو الشكل من نفس مجلد الكتاب.
- `12-English-Sci-wb/`: 138 شكل
- `12-English-lit-Sb/`: 255 شكل
- `12-French-SB/`: 179 شكل
- `12-French-lit/`: 96 شكل
- `12-Lit-Philosophy-1/`: 20 شكل
- `12-Lit-Philosophy-2/`: 23 شكل
- `12-christianity/`: 18 شكل
- `12-geography-Lit/`: 264 شكل
- `12-islamic/`: 2 شكل
- `12-lit-Russian/`: 1 شكل
- `12-physics-Sci/`: 0 شكل + 268 صورة صفحة كاملة
- `12-sci-Russian/`: 1 شكل
- `12-sci-math-1/`: 2 شكل
- `12-sci-math-2/`: 6 شكل
- `12-science/`: 599 شكل + 287 صورة صفحة كاملة
- `9-Algebra/`: 2 شكل
- `9-English-AB/`: 53 شكل
- `9-English-SB/`: 206 شكل
- `9-Geometry/`: 14 شكل + 84 صورة صفحة كاملة
- `9-Physics-Chemistry/`: 0 شكل + 180 صورة صفحة كاملة
- `9-Russian/`: 2 شكل
- `9-arabic/`: 175 شكل
- `9-christianity/`: 128 شكل
- `9-history/`: 123 شكل
- `9-islamic/`: 1 شكل
- `9-music/`: 58 شكل
- `9-science/`: 523 شكل + 232 صورة صفحة كاملة
- `9-technology/`: 358 شكل

## How to use this library

1. Find the teacher's book below by grade and subject.
2. Each book is split into chunk files of **50 pages**. Work out which
   chunk file(s) cover the page range the teacher asked for, and fetch
   **only those chunks** — a normal request (e.g. pages 1–100) needs just
   one or two files. Never fetch a whole book, and there are no
   single-page files to fetch one by one.
3. Inside a chunk, every page starts with a marker line `## صفحة N`.
   **N is the book's page number** (the PDF page). When the teacher says
   «الصفحة 40» they mean the text under `## صفحة 40`.
4. Write questions strictly from the content of the pages you fetched,
   in the teacher's requested range. Do not invent book content for
   pages you did not read.

## ⚠️ OCR books — quality grades, read this before promising anything

All formerly scanned books have now been OCR'd, and each one carries a
quality grade in its status line: «نص OCR — الدرجة X (ثقة NN%)», where
the percentage is the OCR engine's mean word confidence. Use the grades
like this:

- **Grades A and B** — trustworthy. Write questions from the text as
  you would from a digital book.
- **Grade C** — usable, but carefully: prose is generally sound, yet
  individual words, numbers and formulas may be misread. Prefer
  questions whose answers do not hinge on one exact number or symbol.
- **Grade D** — treat the exact wording with suspicion. The gist and
  topics are real, but words, numbers and formulas are often wrong.
  Prefer concept questions; do **not** quote numbers or formulas from
  a grade-D book without checking the page image first, and tell the
  teacher the text is low-quality OCR.

Books marked «نص رقمي نظيف» are born-digital, fully extracted and
safe to use. Whatever the grade, never write questions from memory
and pretend they came from the book.

Base URL of this folder (GitHub Pages):
`https://mohammedxmoussa.github.io/quiz-builder-syria/ai/books/`

## الصف التاسع (Grade 9)

### اللغة العربية — الصف التاسع

- Total pages: 200 · Status: نص رقمي نظيف
- [الصفحات 1–50](9-arabic/pages-001-050.md)
- [الصفحات 51–100](9-arabic/pages-051-100.md)
- [الصفحات 101–150](9-arabic/pages-101-150.md)
- [الصفحات 151–200](9-arabic/pages-151-200.md)

### الجبر — الصف التاسع

- Total pages: 116 · Status: نص OCR — الدرجة B (ثقة 81%)
- [الصفحات 1–50](9-Algebra/pages-001-050.md)
- [الصفحات 51–100](9-Algebra/pages-051-100.md)
- [الصفحات 101–116](9-Algebra/pages-101-116.md)

### الهندسة — الصف التاسع

- Total pages: 84 · Status: نص OCR — الدرجة B (ثقة 81%)
- [الصفحات 1–50](9-Geometry/pages-001-050.md)
- [الصفحات 51–84](9-Geometry/pages-051-084.md)

### الفيزياء والكيمياء — الصف التاسع

- Total pages: 180 · Status: نص OCR — الدرجة C (ثقة 75%) — الصيغ والمعادلات تحتاج حذراً
- [الصفحات 1–50](9-Physics-Chemistry/pages-001-050.md)
- [الصفحات 51–100](9-Physics-Chemistry/pages-051-100.md)
- [الصفحات 101–150](9-Physics-Chemistry/pages-101-150.md)
- [الصفحات 151–180](9-Physics-Chemistry/pages-151-180.md)

### العلوم (علم الأحياء والأرض) — الصف التاسع

- Total pages: 232 · Status: نص رقمي نظيف
- [الصفحات 1–50](9-science/pages-001-050.md)
- [الصفحات 51–100](9-science/pages-051-100.md)
- [الصفحات 101–150](9-science/pages-101-150.md)
- [الصفحات 151–200](9-science/pages-151-200.md)
- [الصفحات 201–232](9-science/pages-201-232.md)

### الجغرافية — الصف التاسع

- Total pages: 176 · Status: نص OCR — الدرجة C (ثقة 76%)
- [الصفحات 1–50](9-geography/pages-001-050.md)
- [الصفحات 51–100](9-geography/pages-051-100.md)
- [الصفحات 101–150](9-geography/pages-101-150.md)
- [الصفحات 151–176](9-geography/pages-151-176.md)

### التاريخ — الصف التاسع

- Total pages: 123 · Status: نص OCR — الدرجة B (ثقة 80%)
- [الصفحات 1–50](9-history/pages-001-050.md)
- [الصفحات 51–100](9-history/pages-051-100.md)
- [الصفحات 101–123](9-history/pages-101-123.md)

### التربية الدينية الإسلامية — الصف التاسع

- Total pages: 140 · Status: نص OCR — الدرجة D (ثقة 60%) — عرضة للأخطاء بسبب الخطوط المزخرفة
- [الصفحات 1–50](9-islamic/pages-001-050.md)
- [الصفحات 51–100](9-islamic/pages-051-100.md)
- [الصفحات 101–140](9-islamic/pages-101-140.md)

### التربية الدينية المسيحية — الصف التاسع

- Total pages: 148 · Status: نص رقمي نظيف
- [الصفحات 1–50](9-christianity/pages-001-050.md)
- [الصفحات 51–100](9-christianity/pages-051-100.md)
- [الصفحات 101–148](9-christianity/pages-101-148.md)

### اللغة الإنكليزية (كتاب الطالب) — الصف التاسع

- Total pages: 80 · Status: نص رقمي نظيف
- [الصفحات 1–50](9-English-SB/pages-001-050.md)
- [الصفحات 51–80](9-English-SB/pages-051-080.md)

### اللغة الإنكليزية (كتاب الأنشطة) — الصف التاسع

- Total pages: 64 · Status: نص رقمي نظيف
- [الصفحات 1–50](9-English-AB/pages-001-050.md)
- [الصفحات 51–64](9-English-AB/pages-051-064.md)

### اللغة الفرنسية (كتاب الأنشطة) — الصف التاسع

- Total pages: 56 · Status: نص OCR — الدرجة B (ثقة 87%)
- [الصفحات 1–50](9-French-AB/pages-001-050.md)
- [الصفحات 51–56](9-French-AB/pages-051-056.md)

### اللغة الروسية — الصف التاسع

- Total pages: 96 · Status: نص OCR — الدرجة B (ثقة 86%)
- [الصفحات 1–50](9-Russian/pages-001-050.md)
- [الصفحات 51–96](9-Russian/pages-051-096.md)

### تكنولوجيا المعلومات والاتصالات — الصف التاسع

- Total pages: 189 · Status: نص رقمي نظيف
- [الصفحات 1–50](9-technology/pages-001-050.md)
- [الصفحات 51–100](9-technology/pages-051-100.md)
- [الصفحات 101–150](9-technology/pages-101-150.md)
- [الصفحات 151–189](9-technology/pages-151-189.md)

### التربية الموسيقية — الصف التاسع

- Total pages: 64 · Status: نص OCR — الدرجة D (ثقة 58%) — صفحات التدوين الموسيقي غير مقروءة كنص
- [الصفحات 1–50](9-music/pages-001-050.md)
- [الصفحات 51–64](9-music/pages-051-064.md)

## البكالوريا — الصف الثاني عشر (Grade 12)

### اللغة العربية — البكالوريا العلمي

- Total pages: 110 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-Arabic-Sci/pages-001-050.md)
- [الصفحات 51–100](12-Arabic-Sci/pages-051-100.md)
- [الصفحات 101–110](12-Arabic-Sci/pages-101-110.md)

### اللغة العربية — البكالوريا الأدبي

- Total pages: 148 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-Arabic-Lit/pages-001-050.md)
- [الصفحات 51–100](12-Arabic-Lit/pages-051-100.md)
- [الصفحات 101–148](12-Arabic-Lit/pages-101-148.md)

### الرياضيات ١ — البكالوريا العلمي

- Total pages: 232 · Status: نص OCR — الدرجة C (ثقة 74%) — الصيغ والمعادلات تحتاج حذراً
- [الصفحات 1–50](12-sci-math-1/pages-001-050.md)
- [الصفحات 51–100](12-sci-math-1/pages-051-100.md)
- [الصفحات 101–150](12-sci-math-1/pages-101-150.md)
- [الصفحات 151–200](12-sci-math-1/pages-151-200.md)
- [الصفحات 201–232](12-sci-math-1/pages-201-232.md)

### الرياضيات ٢ — البكالوريا العلمي

- Total pages: 196 · Status: نص OCR — الدرجة C (ثقة 77%) — الصيغ والمعادلات تحتاج حذراً
- [الصفحات 1–50](12-sci-math-2/pages-001-050.md)
- [الصفحات 51–100](12-sci-math-2/pages-051-100.md)
- [الصفحات 101–150](12-sci-math-2/pages-101-150.md)
- [الصفحات 151–196](12-sci-math-2/pages-151-196.md)

### الفيزياء — البكالوريا العلمي

- Total pages: 268 · Status: نص OCR — الدرجة D (ثقة 67%) — النثر مقروء لكن الصيغ والرموز غير موثوقة
- [الصفحات 1–50](12-physics-Sci/pages-001-050.md)
- [الصفحات 51–100](12-physics-Sci/pages-051-100.md)
- [الصفحات 101–150](12-physics-Sci/pages-101-150.md)
- [الصفحات 151–200](12-physics-Sci/pages-151-200.md)
- [الصفحات 201–250](12-physics-Sci/pages-201-250.md)
- [الصفحات 251–268](12-physics-Sci/pages-251-268.md)

### علم الأحياء — البكالوريا العلمي

- Total pages: 287 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-science/pages-001-050.md)
- [الصفحات 51–100](12-science/pages-051-100.md)
- [الصفحات 101–150](12-science/pages-101-150.md)
- [الصفحات 151–200](12-science/pages-151-200.md)
- [الصفحات 201–250](12-science/pages-201-250.md)
- [الصفحات 251–287](12-science/pages-251-287.md)

### الجغرافية — البكالوريا الأدبي

- Total pages: 280 · Status: نص OCR — الدرجة B (ثقة 80%)
- [الصفحات 1–50](12-geography-Lit/pages-001-050.md)
- [الصفحات 51–100](12-geography-Lit/pages-051-100.md)
- [الصفحات 101–150](12-geography-Lit/pages-101-150.md)
- [الصفحات 151–200](12-geography-Lit/pages-151-200.md)
- [الصفحات 201–250](12-geography-Lit/pages-201-250.md)
- [الصفحات 251–280](12-geography-Lit/pages-251-280.md)

### الفلسفة ١ — البكالوريا الأدبي

- Total pages: 144 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-Lit-Philosophy-1/pages-001-050.md)
- [الصفحات 51–100](12-Lit-Philosophy-1/pages-051-100.md)
- [الصفحات 101–144](12-Lit-Philosophy-1/pages-101-144.md)

### الفلسفة ٢ — البكالوريا الأدبي

- Total pages: 156 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-Lit-Philosophy-2/pages-001-050.md)
- [الصفحات 51–100](12-Lit-Philosophy-2/pages-051-100.md)
- [الصفحات 101–150](12-Lit-Philosophy-2/pages-101-150.md)
- [الصفحات 151–156](12-Lit-Philosophy-2/pages-151-156.md)

### التربية الدينية الإسلامية — البكالوريا

- Total pages: 164 · Status: نص OCR — الدرجة D (ثقة 60%) — عرضة للأخطاء بسبب الخطوط المزخرفة
- [الصفحات 1–50](12-islamic/pages-001-050.md)
- [الصفحات 51–100](12-islamic/pages-051-100.md)
- [الصفحات 101–150](12-islamic/pages-101-150.md)
- [الصفحات 151–164](12-islamic/pages-151-164.md)

### التربية الدينية المسيحية — البكالوريا

- Total pages: 135 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-christianity/pages-001-050.md)
- [الصفحات 51–100](12-christianity/pages-051-100.md)
- [الصفحات 101–135](12-christianity/pages-101-135.md)

### اللغة الإنكليزية (كتاب الأنشطة) — البكالوريا العلمي

- Total pages: 112 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-English-Sci-wb/pages-001-050.md)
- [الصفحات 51–100](12-English-Sci-wb/pages-051-100.md)
- [الصفحات 101–112](12-English-Sci-wb/pages-101-112.md)

### اللغة الإنكليزية (كتاب الطالب) — البكالوريا الأدبي

- Total pages: 128 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-English-lit-Sb/pages-001-050.md)
- [الصفحات 51–100](12-English-lit-Sb/pages-051-100.md)
- [الصفحات 101–128](12-English-lit-Sb/pages-101-128.md)

### اللغة الفرنسية (كتاب الطالب) — البكالوريا

- Total pages: 120 · Status: نص رقمي نظيف
- [الصفحات 1–50](12-French-SB/pages-001-050.md)
- [الصفحات 51–100](12-French-SB/pages-051-100.md)
- [الصفحات 101–120](12-French-SB/pages-101-120.md)

### اللغة الفرنسية — البكالوريا الأدبي

- Total pages: 40 · Status: نص رقمي نظيف
- [الصفحات 1–40](12-French-lit/pages-001-040.md)

### اللغة الروسية — البكالوريا العلمي

- Total pages: 128 · Status: نص OCR — الدرجة B (ثقة 85%)
- [الصفحات 1–50](12-sci-Russian/pages-001-050.md)
- [الصفحات 51–100](12-sci-Russian/pages-051-100.md)
- [الصفحات 101–128](12-sci-Russian/pages-101-128.md)

### اللغة الروسية — البكالوريا الأدبي

- Total pages: 140 · Status: نص OCR — الدرجة B (ثقة 85%)
- [الصفحات 1–50](12-lit-Russian/pages-001-050.md)
- [الصفحات 51–100](12-lit-Russian/pages-051-100.md)
- [الصفحات 101–140](12-lit-Russian/pages-101-140.md)

---

Not yet available: التربية الفنية — الصف التاسع (art). The ministry's
file for it is corrupted, so it is not in the library yet. If a teacher
asks for it, say it is not available yet instead of inventing content.
