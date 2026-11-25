# Exam Builder: Templates Guide (for AI assistants)

This file is an **optional add-on** to the core guide at `quiz-creator-ai.md`.
Fetch and read it **only** when the teacher asks about the exam's look, design,
layout or template — or asks you to choose/suggest a template. For writing exam
questions you do NOT need this file; the core guide is enough.

You cannot change layout or styling through JSON. The only thing you can do is
**suggest** one template by setting `exam.template` to one of the ids below.
The teacher makes the final choice inside the tool and can change it any time
without re-generating the JSON.

## Available templates

| id (use in `exam.template`) | Arabic name in the tool | What it looks like | Suggest it when |
|---|---|---|---|
| `classic` | كلاسيكي | Traditional framed paper: double border around the page, formal header with school/teacher fields, two columns. | The teacher wants a familiar, formal school exam look. This is the safe default for Arabic subjects. |
| `minimal` | بسيط | Clean, light layout: thin rules, no heavy frame, lots of white space, two columns. | The teacher wants a modern, simple, ink-saving print. |
| `ministerial` | وزاري | Official Syrian ministerial WRITTEN style: header with «الجمهورية العربية السورية — وزارة التربية والتعليم» and the certificate title line («امتحان شهادة الدراسة الثانوية العامة», or «امتحان شهادة التعليم الأساسي والإعدادية الشرعية» for 9th grade), sections headed أولاً / ثانياً / ثالثاً with the section total in brackets [٦٠]. | Written (non-automated) ministry papers: **Arabic, religion (التربية الإسلامية/المسيحية), French/Russian**, and **9th-grade** basic-certificate exams. |
| `automated` | الوزاري المؤتمت | The ministry's official AUTOMATED exam: one bordered 3-column header (الجمهورية العربية السورية / وزارة التربية / المادة \| «نموذج للاختبار المؤتمت لطلاب الشهادة الثانوية العامة» — التعليم الأساسي for 9th grade \| الاسم / المدة / الدرجة), the fixed instruction «اختر الإجابة الصحيحة ثم ظلل على ورقة إجابتك دائرة الحرف الموافق للإجابة الصحيحة (لكل سؤال إجابة صحيحة واحدة فقط)», single column, continuous numbering (1)(2)(3)…, every MCQ's options in one bordered row with LATIN letter boxes **A B C D**. | The subject is an **automated final**: رياضيات، فيزياء، كيمياء، علم الأحياء، تاريخ، جغرافية، فلسفة، التربية الوطنية، اللغة الإنكليزية (المؤتمتة). Write the exam as MCQ questions (4 options each). |
| `english` | الإنكليزي الوزاري | Syrian baccalaureate **English** exam style: Arabic RTL header frame (subject, teacher, name/number, duration, total grade /300), a star medallion showing the model number, then an **LTR English** body in a serif font inside a bordered two-column grid. Sections are numbered with Roman numerals (I, II, III…), each section heading is underlined and shows the section's total as `(N marks)`, question numbering is continuous across sections, and the paper ends with "END OF EXAM / انتهت الأسئلة". | The subject is **English** (اللغة الإنكليزية), especially Syrian secondary/baccalaureate English exams. For English exams prefer this template. |
| `science` | العلوم (نموذج شامل) | Syrian comprehensive science-model style (نماذج امتحانية شاملة): **single column**, the shared compact header (with the model number), section headings «السؤال الأول: …» with numbering restarting per section, MCQ options laid out as a bordered 4-cell row (a/b/c/d), and smart placement for diagrams (wide figures full width, tall figures beside the text). | The subject is a science (العلوم، الأحياء، الفيزياء، الكيمياء…), especially Syrian baccalaureate-style comprehensive models with diagrams and grid-style MCQ. |

## Compact variants (مضغوط) — one shared header

Every template above also has a **compact variant**. All templates share ONE
compact header component: a modest exam title line, the info fields arranged
in tidy columns (subject / grade | duration / date / total marks | school and
teacher **only when provided**), and a student line (الاسم / الرقم) with
blanks to write in. Nothing is stacked above or below it. The printed paper
is black & white only in every template.

- **Good-luck line is optional.** A teacher may add a closing wish that
  prints after «انتهت الأسئلة», e.g. «مع تمنياتي لكم بالتوفيق والنجاح» — put
  it in `exam.goodLuck`, or the teacher can type it in the tool's UI, or skip
  it (nothing prints).

- **Teacher name is optional.** If the teacher never gave a name, the paper
  prints cleanly without any teacher line. The teacher can give their name in
  the chat with you (put it in `exam.teacher`), type it later in the tool's
  web UI, or skip it entirely. Never invent a name.
- Compact density tightens spacing and image sizes so a typical exam fits
  **one sheet of paper — 2 pages, front and back** (the case for ~95% of
  exams). To suggest it, keep `exam.template` as the base template id and add
  **`"compact": true`** inside `exam`. Suggest compact whenever the teacher
  wants the exam to fit on a single sheet; the teacher can also switch
  density in the tool (عادي/مضغوط toggle) without regenerating the JSON.

## Notes for English exams (`english` template)

- Write all question text, passages and options in English as usual; the tool
  lays them out left-to-right automatically when this template is selected.
- Section titles you write in `sections[].title` are shown after the Roman
  numeral, so write them as the instruction itself, e.g.
  `"Read the following text then do the tasks below:"` — do not add your own
  numbering (no "I –", no "1.") inside the title.
- The `(N marks)` shown in each section heading is the sum of that section's
  question marks, computed by the tool — just make sure every question carries
  its correct `marks`, and that they add up to `exam.totalMarks` (300 in the
  official English baccalaureate model).
- Typical English baccalaureate structure (for reference only — follow the
  teacher's own plan): two reading texts with comprehension tasks, gap-fill
  paragraph, word-list fill, dialogue completion, rewrite-as-required,
  clause completion, choose-the-correct-word, verb correction, translation
  (into Arabic and into English), and a composition (~50 marks).
