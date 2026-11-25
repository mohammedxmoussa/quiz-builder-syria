# Exam Builder — Template Design Guidelines (STANDING RULES)

These rules come from the user's feedback on real printed exams (2026-11-25).
They apply to EVERY template, current and future. Do not re-litigate them.
If memory is lost, this file + `~/MEMORY.md` are the source of truth. A copy
also lives in the GitHub repo (docs/design-guidelines.md).

## Look & feel
1. **No colors anywhere in the printed templates.** Black and white only —
   black text, black/grey borders. Teachers print and photocopy; color is
   cost and noise. (UI of the app itself may use color; the PAPER may not.)
2. **Government Word-typist aesthetic:** the paper should look like an
   official exam typed in Microsoft Word by a ministry clerk — formal,
   plain, symmetrical, standard fonts, black border frames, no decoration
   for decoration's sake. If it looks "designed", it's wrong.
3. **Title size is modest.** The exam title is a normal bold line, never a
   big display headline. Nothing on the paper shouts.

## Header (shared component, all templates)
4. ONE compact header block per paper — never stacked bands/rows above or
   below it.
5. Header fields are arranged **in columns** (a tidy grid: e.g. المادة |
   الصف | المدة | الدرجة …), not one long wrapping line.
6. The header contains a student line: الاسم: ______ الرقم: ______ with
   blanks to write in.
7. **Teacher name is OPTIONAL.** Empty teacher (or school) = print nothing
   for it — no label, no blank, no placeholder. Teachers can give their
   name in the AI chat (exam.teacher), type it in the web UI, or skip it.
8. Screen-only, non-blocking print warning when no teacher name was
   provided («لم تُدخل اسم المعلم/ة…»). Warnings never print.

## Footer & endings
9. **No page-number ornament in the footer** — no boxed { 1 }, no medallion
   numbers at the bottom. (Removed 2026-11-25 per user: "remove the 1 sign
   at the footer, I don't know why it is there".)
10. «انتهت الأسئلة» is plain — **no underline**, no decorative rules.
11. Teachers can add a good-luck closing line (e.g. «مع تمنياتي لكم
    بالتوفيق والنجاح») after «انتهت الأسئلة» — editable in the UI and via
    JSON, optional, empty = nothing prints.

## Space & print
12. **95% of exams are ONE sheet: 2 pages, front and back.** Design and
    verify against that. Conserve space everywhere: tight question gaps,
    tight option-cell padding, compact density variant (exam.compact)
    available for every template.
13. Images: medium means medium (≤ ~38% width / 70mm height below text);
    only large/full-span goes full width; tall images float beside text
    with a height cap; never upscale.
14. Print output must be provable: verify with real print-to-PDF using a
    real exam + uploaded image before claiming a template works.
15. No watermarks, no app branding, no URL on the paper. @page margin 0;
    step-4 instructions tell teachers to uncheck browser headers/footers,
    margins None, background graphics on, A4.

## Product constraints (from the original spec — unchanged)
16. Client-only, no backend, localStorage only, bundled fonts only,
    no PDF libraries (print = browser dialog), Arabic RTL UI.
17. Docs split for AI bots on GitHub Pages /ai/: core guide always,
    templates.md only on demand.
