---
name: วย 271 บทที่ 5 Pipe Flow Revision
description: A formal Thai worked-solution document (navy title, gold kicker, numbered equations) with a light and a dark mode.
---

# Design

Written like a printed physics solution, not an app: one centred column (max 800px), Sarabun for Thai text, KaTeX for every formula. The reference is a formal Thai LaTeX-style solution: gold kicker, navy title, "แนวคิดในการแก้ปัญหา", ขั้นที่ 1–3, numbered equations `(1)`, `(2)`, a closing line "คำตอบที่ถูกต้องคือ".

## Colour (CSS variables in `assets/style.css`)

| token | light | dark | meaning |
|---|---|---|---|
| `--bg` | #ffffff | #10131a | page |
| `--ink` | #16181d | #e7eaf0 | body text, rules |
| `--navy` | #14295b | #a9c1ff | titles, headings |
| `--gold` | #a8651a | #e3a556 | kicker, notes |
| `--blue` | #1c2fa8 | #86a0ff | given data |
| `--red` | #b3201f | #ff8178 | answers, "No" |
| `--green` | #17702a | #63d487 | "OK", checks |

Theme is `data-theme` on `<html>`, set before first paint from `localStorage.theme` or `prefers-color-scheme`. The nav button toggles it. Figures use the same variables so they follow the theme.

## Structure

- One `<section>` per page, only the one named by the URL hash is shown; KaTeX renders a page the first time it is opened.
- Each problem page: statement, figure, **เฉลยวิธีทำ** (`.exam` box: one `.row` per step, label left, equations right), then **เฉลยละเอียด** (`.detail`: plan, ขั้นที่ 1–3, equations, ตรวจสอบ, คำตอบ).
- Practice mode (`body.practice`) hides every `.exam .row` after the first and `.detail`; tapping a row reveals it.
- Cheat sheet (`#sum`): formulas, per-type steps (`.ty` cards), reference tables, exam-room rules.

## Rules

- No Unicode `·` inside `\text{}` (KaTeX shows red `\cdotp`); use `\!\cdot\!`.
- Colour in equations comes from `\htmlClass{no|ok}{…}` so it follows the theme.
- Long equations are split into `aligned` lines by `scripts/site/common.py` (`wrap_exam`, `wrap_math`) so they fit a phone without sideways scrolling.
- Tap targets ≥ 44px, body text 18px, line-height 1.85 for Thai.
