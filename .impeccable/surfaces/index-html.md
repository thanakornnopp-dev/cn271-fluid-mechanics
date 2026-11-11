---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Surface brief: index.html (วย 271 บท 5 pipe-flow revision site)

## Scope and mode
Read (a revision document read mostly on a phone, secondarily on a laptop). Code-led. Static HTML/CSS/JS, Thai content with English technical terms, KaTeX for math.

## Audience, job, content
TU civil-engineering students the night before the Chapter 5 quiz. Jobs: (1) skim a one-page method sheet, (2) read line-by-line worked solutions in the professor's order for Q1-Q8 and the two 15-point exam-style problems. Supplementary: Q9-Q13, a trial-and-error calculator, K and f reference tables. Every number verified by scripts/pipeflow.py.

## Chosen direction
Engineering drawing sheet. Assigned by the roll; confirmed by the user. Pen-colour grammar from the professor's own handwriting (blue = given/substitution, red = key result and trap, violet = check). Memorable moment: each problem opens with a real title block and ends with a revision table listing the traps.

## Direction contract
THESIS: A set of drawing sheets where each problem is one sheet with a title block, not a blog of cards. Refuses the generic docs-site arrangement (left tree, centered article, accent-colour links).
OWN-WORLD: Cool white sheet (no cream), graphite ink, hairline and 1.5px linework, thin double border, dimension-line ticks. Three pen inks only for meaning: blue given, red result/trap, violet check. Chakra Petch for title-block and labels, Sarabun for reading. Tabular numerals everywhere.
STORY: The reader knows what the sheet is, which problem type it is, can find the procedure in seconds, and reads the working exactly as it should be written in the exam.
FIRST VIEWPORT (phone 390x844): thin top bar with course + sheet counter and an index button; title block table (title, type, status, sheet n/N); the one-page method sheet starts immediately: the three problem types as a decision table, then the master equations. Bottom bar holds previous/next sheet. Laptop: persistent sheet index rail on the left, sheet centred at about 70ch with margin notes for traps.
FORM: engineering drawing sheet with title block and revision table, position 3 on the ordered list, seed:f84f0f69edbda5db
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Unresolved
Exam problem figures are redrawn as simple SVG schematics (not the professor's images). Q11 roughness missing in the source; shown as incomplete.
