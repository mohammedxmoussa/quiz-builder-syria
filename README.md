# منشئ الاختبارات — Exam Builder for Syrian Teachers

A client-only, Arabic (RTL) printable exam generator built for teachers who are **not** technical.

A teacher asks their own AI chatbot to write an exam as JSON, pastes that JSON into this page, uploads any images, picks a template, and prints a clean A4 exam from the browser — or downloads an editable Word file. **No backend, no accounts, no sign-up, and no data ever leaves the teacher's browser.**

🌐 **Live site:** https://mohammedxmoussa.github.io/quiz-builder-syria/

---

## لماذا؟ (Why this exists)

Most exam tools assume technical teachers. This one assumes the opposite: the teacher's only job is to describe the exam to a chatbot in plain Arabic. The chatbot writes the JSON using the published AI guide; this tool validates it (with Arabic error messages the teacher can copy back to the chatbot), lays it out in an official-looking template, and prints it — usually on **one sheet of paper, front and back**, because that is what 95% of real exams are.

## Features

- **6 print templates** — كلاسيكي، بسيط، الإنكليزي الوزاري، العلوم نموذج شامل، الوزاري المؤتمت (the ministry's automated MCQ format), وزاري — each with a compact «مضغوط» variant
- **8 question types** — multiple choice, true/false, fill-in-the-blank, short answer, essay, matching, tables, and reading passages, with sub-parts
- **Shuffled versions** أ / ب / ج / د with deterministic seeding, plus an answer-key mode
- **Arabic validation errors** with a one-click "copy the errors back to your AI" button
- **Built-in question editor** for teachers who prefer forms over JSON
- **Editable Word (.docx) export** alongside browser printing
- **Digit toggle** — Western (123) or Arabic-Indic (١٢٣) numerals
- **PWA** — installable, works offline once loaded
- **Textbook library** — the official Syrian textbooks for grades 9 and 12 (32 books), split into 50-page Markdown chunks with their figures and page images, published under [`ai/books/`](ai/books/INDEX.md) so a teacher's AI can build an exam "from pages 1–100" of the real book

## How it works

```
Teacher ⇄ their AI chatbot ──(exam JSON, written using ai/quiz-creator-ai.md)──► this page
                                                                                    │
                                              validate → pick template → print / Word
```

The AI-facing documentation lives in [`ai/`](ai/index.md) and is deliberately split for fetch-on-demand:

| File | Purpose |
|---|---|
| `ai/quiz-creator-ai.md` | The core guide every chatbot reads: the JSON format, question types, rules |
| `ai/templates.md` | Template/design details — fetched only when the teacher asks about looks |
| `ai/example-quiz.json` | A complete working example |
| `ai/books/INDEX.md` | The textbook library index — fetched only for book-based exams |

## Project structure

```
index.html                  The whole app (single static page)
manifest.json, sw.js        PWA manifest + service worker (never caches /ai/)
icons/                      App icons
ai/                         AI guides, example JSON, and the textbook library
docs/design-guidelines.md   The standing print-design rules (read before template work)
```

## Running locally

There is no build step and nothing to install:

```bash
git clone https://github.com/mohammedxmoussa/quiz-builder-syria.git
cd quiz-builder-syria
python3 -m http.server 8000   # then open http://localhost:8000
```

Opening `index.html` directly also works for most features; a local server is closer to production.

## Contributing

Contributions are welcome — bug reports, new templates from real Syrian exam papers, translations of the guides, and fixes. Please:

1. **Read [`docs/design-guidelines.md`](docs/design-guidelines.md) first.** The printed paper has strict rules: black & white only, one compact header, modest titles, government Word-typist aesthetic, and a typical exam must fit on one sheet (2 pages). PRs that add color or decoration to the *paper* will be declined (the app UI is a different matter).
2. **Verify print changes with a real print-to-PDF** of a real exam, ideally with an uploaded image — layout bugs hide until paper is involved.
3. Keep it **client-only**: no backend, no analytics, no external requests at runtime, no teacher data leaving the browser.
4. Keep the AI guides in sync: if you change the JSON format or templates, update `ai/quiz-creator-ai.md` / `ai/templates.md` in the same PR.
5. Open an issue before large changes so we can agree on the approach.

## Deployment

GitHub Pages, branch-based: every push to `main` auto-deploys the repository root. There is no build step and no CI workflow.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Not yet chosen — all rights reserved until the maintainer selects one. (If you want to reuse this project, please open an issue.)
