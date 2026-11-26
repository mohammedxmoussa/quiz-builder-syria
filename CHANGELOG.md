# Changelog

All notable changes to منشئ الاختبارات (Exam Builder) are recorded here.
The format follows [Keep a Changelog](https://keepachangelog.com/), and the
project is deployed continuously from `main` to GitHub Pages, so entries are
grouped by date rather than version numbers.

## [Unreleased]

### Fixed
- **Word export: exam columns now read in the right order.** The downloaded `.docx` never marked its sections as right-to-left, so Word (and LibreOffice) laid the two columns out left-to-right — the first question landed in the left column and the exam read backwards across columns. The bundled docx.js library has no section-level bidi option, so it is now patched (like the earlier Node-polyfill patches) to emit `<w:bidi/>` in each section's properties for Arabic templates; the English template stays LTR. Verified by rendering the generated file: question 1 now starts top-right.

## 2026-11-26 — Textbook figures, OCR, and repo docs

### Added
- **Textbook figures and page renders are live**: 3,247 extracted figures plus
  1,051 full-page renders (JPEG) for the grade 9 & 12 books, under
  `ai/books/<book>/images/` and `ai/books/<book>/pages-img/`.
- The book index now documents the image folders and per-book image counts
  («الصور والأشكال» section), so a teacher's AI can find and cite figures.
- This changelog, and a full README with contributing guidelines.

### Changed
- **OCR pass completed and published** for the 16 scanned textbooks: 2,381
  pages OCR'd (Tesseract, 300 DPI). Every scanned book now carries a quality
  grade in the index (B ×8, C ×4, D ×4) with per-book caveats — e.g. grade-12
  Physics formulas and the calligraphic Islamic-studies books must be checked
  against the page image before quoting numbers or formulas.

## 2026-11-25 — Textbook library

### Added
- **The official Syrian textbooks for grades 9 and 12**: 32 books, 5,214
  pages, published as 108 Markdown chunks of 50 pages each under `ai/books/`,
  with an Arabic index (`ai/books/INDEX.md`) that lets an AI fetch only the
  chunk(s) covering a requested page range.
- The AI fetch map (`ai/index.md`) gained a books entry, fetched only when a
  teacher asks for a book-based exam.

### Changed
- Service worker: `/ai/` paths are never cached, so the PWA stays small and
  book files are only ever fetched on demand.

## 2026-11-25 — Ministry templates and Word export

### Added
- **الوزاري المؤتمت template** — the ministry's automated MCQ format: bordered
  3-column header, «ظلل على ورقة إجابتك» instruction, continuous (1)(2)(3)
  numbering, options in a bordered row with Latin A–D letter boxes.
- **وزاري template** — ministry letterhead, certificate title line, and
  أولاً/ثانياً sections with bracketed section totals.
- **Editable Word (.docx) export**, built on the real docx.js library.

### Fixed
- Word export: the exam header no longer sits alone on page 1 (a section-break
  bug in how the document was assembled), and Word's default blue theme styles
  and headers/footers no longer leak into the export — output is black,
  Traditional Arabic, header and questions together in two columns.

## 2026-11-25 — Design release: one sheet, black & white

### Added
- **Shared compact header** for all templates: one block, fields in columns,
  student name/number line included; every template gained a «مضغوط» compact
  variant (also settable via `"compact": true` in the JSON).
- Two new templates from real exam papers: **الإنكليزي الوزاري** (baccalaureate
  English model) and **العلوم نموذج شامل** (biology models), with smart image
  placement by aspect ratio in all templates.
- Optional teacher good-luck line (`exam.goodLuck`), a first-visit landing
  page, a sticky validity summary, a floating preview helper, and PWA support
  (installable, offline app shell).

### Changed
- **Printed paper is black & white only** in every template; titles are modest;
  the footer page-number ornament was removed; «انتهت الأسئلة» is plain.
- Teacher name is optional: omitted from the paper entirely when not provided,
  with a screen-only reminder before printing.

### Fixed
- **Printing produced 8 empty pages** (and stamped the page URL) when an exam
  contained an uploaded photo: the print stylesheet hid the panel in a way
  that still paginated it, and the paper was positioned outside the print
  flow. Printing now produces the real pages only.

## 2026-11-25 — Initial release

### Added
- The Exam Builder app: paste exam JSON written by the teacher's own AI
  chatbot, upload images, pick a template, print a two-column A4 exam.
- All 8 question types (MCQ, true/false, fill-in-the-blank, short answer,
  essay, matching, table, passage) with sub-parts; rich-text marks
  (`**bold**`, `__underline__`, `{{blank}}`).
- Tolerant JSON parsing with Arabic validation errors and a "copy errors back
  to your AI" button.
- Built-in form editor for every question type, synced live with the JSON.
- Deterministic shuffled versions (أ/ب/ج/د) and answer-key mode; Western /
  Arabic-Indic digit toggle.
- AI documentation under `ai/` (core guide, template guide, example JSON)
  with one-tap "copy the prompt" buttons in the app.
- First templates: كلاسيكي and بسيط.
