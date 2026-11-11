# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS served from GitHub Pages (existing repo; no build step). Math via KaTeX. Content in Thai with scientific terms kept in English.

## Users

Thammasat civil-engineering students taking วย 271 (Fluid Mechanics for Civil Engineers), revising the night before and the morning of the Chapter 5 pipe-flow quiz. Read mostly on a phone, secondarily on a laptop. They already attended lectures; they need to recall the method fast and rehearse writing it in the professor's order.

## Product Purpose

A revision site for the Chapter 5 (Flow in Pipe) quiz. Success: a student can (1) recall the method for each problem type in one page and (2) work Q1–Q8 and the two exam-style problems on their own, then check against line-by-line worked solutions written in the order the professor expects.

## Positioning

Every worked solution is traceable to the professor's own handouts (ch5 example sheet, her board photos, the 15-point exam-style problem) and every number is verified against a Colebrook solver; nothing is presented as "real exam" unless it is in the professor's files.

## Operating Context

- Quiz scope per the class: examples Q1–Q8 of the ch5 sheet, plus exam-style problems of the series-inclined and parallel-network kind (15 points).
- Q9–Q13 are supplementary practice, not the main quiz scope.
- Exam materials: Glasgow pipe friction chart (Moody-type), sudden expansion/contraction K charts, ν = 10⁻⁶ m²/s for water.
- Professor: สุนิสา สมิทธการ. Source files: ch5.pdf, ฟลูอิด บท5.pdf, allprobsfluid 2.pdf, syllabus.

## Capabilities and Constraints

- Static site, works offline-ish after first load; KaTeX and fonts load from CDN/Google Fonts.
- Content language: Thai, scientific words in English.
- Existing parts to keep: Python solver (scripts/solver_engine.py) with unit tests, the trial-and-error calculator idea.
- Removed on purpose: exam problems 2 (L = 1500 m) and 3 (two huge tanks) because they are not in the professor's files available to the team.

## Brand Commitments

Original author: Thanaporn Nopparat (repo owner). The revamp credits the original author and a contributor; no "AI Squad" branding and no fake QC badge.

## Evidence on Hand

Professor's handwritten and board-photo solutions for Q1–Q3, Q6–Q9 in `final/pipe/ฟลูอิด บท5.pdf`; partial solutions for the two exam-style problems. Q10–Q13 have no professor solution; they are solved by the team and verified numerically, and must be labelled as such.

## Product Principles

1. Method before arithmetic: each problem type has one visible procedure.
2. Written in the professor's order, because the quiz is graded on the working.
3. Never present an unverified number as fact; label what is professor-sourced and what is team-solved.
4. Phone-first reading: formulas must be legible and scroll rather than break.

## Accessibility & Inclusion

Thai text must render in a proper Thai face with generous line height; WCAG AA contrast; respect prefers-reduced-motion; tap targets ≥ 44px.
