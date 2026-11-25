# Exam Builder (منشئ الاختبارات) — AI documentation index

You are an AI assistant helping a teacher build a printable exam with the
"منشئ الاختبارات" web tool. The documentation is split into small files so you
only load what the current task needs. **Do not fetch everything by default.**

## Fetch-on-demand map

| File | When to fetch it |
|---|---|
| `quiz-creator-ai.md` | **Always start here.** The core guide: how to write the exam JSON (structure, 8 question types, marks, images, quality checklist). This is the only file you need for writing an exam. |
| `example-quiz.json` | When you want a complete worked example of a valid exam JSON. |
| `templates.md` | **Only** when the teacher asks about the exam's look/design/template, or asks you to pick a template. It lists the template ids you may suggest in `exam.template`. Skip it otherwise — template styling never changes how you write questions. |

Base URL of this folder (GitHub Pages):
`https://mohammedxmoussa.github.io/quiz-builder-syria/ai/`

The tool itself: `https://mohammedxmoussa.github.io/quiz-builder-syria/`
