---
name: วย 271 บทที่ 5 Pipe Flow Revision
description: Engineering drawing sheets in graphite ink on cool white, with three pen inks that carry meaning.
colors:
  sheet: "#fbfcfc"
  desk: "#e4e7ea"
  graphite-ink: "#1b1f24"
  graphite-soft: "#444c56"
  pen-blue: "#1a46c8"
  pen-red: "#bf2a21"
  pen-violet: "#6535b0"
  wash-blue: "#eaf0ff"
  wash-red: "#fdeceb"
  wash-violet: "#f1ebfb"
  night-sheet: "#14181c"
  night-desk: "#0b0d0f"
  night-ink: "#e9ecef"
  night-ink-soft: "#aab2bb"
  night-blue: "#8fb2ff"
  night-red: "#ff8f86"
  night-violet: "#c9a9ff"
typography:
  title:
    fontFamily: "Chakra Petch, Sarabun, system-ui, sans-serif"
    fontSize: "clamp(22px, 5.4vw, 30px)"
    fontWeight: 700
    lineHeight: 1.3
  headline:
    fontFamily: "Chakra Petch, Sarabun, system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1.5
  section:
    fontFamily: "Chakra Petch, Sarabun, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: 1.4
  step:
    fontFamily: "Chakra Petch, Sarabun, system-ui, sans-serif"
    fontSize: "16.5px"
    fontWeight: 700
    lineHeight: 1.55
  body:
    fontFamily: "Sarabun, Noto Sans Thai, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.8
  label:
    fontFamily: "Chakra Petch, Sarabun, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "0em"
rounded:
  none: "0px"
  round: "50%"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "28px"
components:
  sheet:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.none}"
    padding: "0 16px"
  note-trap:
    backgroundColor: "{colors.wash-red}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.none}"
    padding: "10px 14px"
  note-check:
    backgroundColor: "{colors.wash-violet}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.none}"
    padding: "10px 14px"
  note-hint:
    backgroundColor: "{colors.wash-blue}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.none}"
    padding: "10px 14px"
  answer-box:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.pen-red}"
    rounded: "{rounded.none}"
    padding: "12px 16px 14px"
  button-run:
    backgroundColor: "{colors.graphite-ink}"
    textColor: "{colors.sheet}"
    rounded: "{rounded.none}"
    height: "50px"
  button-run-hover:
    backgroundColor: "{colors.pen-blue}"
  step-number:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.round}"
    size: "34px"
  table-head:
    backgroundColor: "{colors.wash-blue}"
    textColor: "{colors.graphite-ink}"
    padding: "8px 12px"
---

# Design System: วย 271 บทที่ 5 Pipe Flow Revision

## Overview

**Creative North Star: "The Drawing Sheet"**

Every problem is one engineering drawing sheet, not a card in a feed. A sheet has a double border, a title block (title, type, status, sheet n/N), numbered working steps, a boxed answer and a revision table that lists the traps. The page reads like paper the professor handed over: graphite ink on cool white (no cream), hairline and 1.5-2px linework, square corners, and nothing decorative that a draughtsman would not draw.

Meaning comes only from three pen inks lifted from the professor's handwriting: blue for given values and substitution, red for the key result and traps, violet for checks. Each ink has a pale wash used only behind notes and table heads. Density is high but airy in the line (17px Sarabun at 1.8) because the reader is a student revising on a phone the night before a quiz.

**Key Characteristics:**
- Cool white sheet on a grey desk; thin double border on wide screens (2px border plus 1px outline offset 5px).
- Square corners everywhere; the only round shape is the numbered step circle.
- Flat: no shadows, depth by linework and the desk/sheet tonal step.
- Tabular numerals globally; Chakra Petch for the title block, labels and step headings, Sarabun for reading.
- Dark mode is the same sheet inverted, with lighter pen inks for contrast.

## Colors

Graphite on cool white with three pen inks that never act as decoration.

### Primary
- **Pen Blue** (#1a46c8): given values, substitution, links, focus ring, selected index row, hover on the run button. Dark: #8fb2ff.

### Secondary
- **Pen Red** (#bf2a21): key results, traps, the answer box border and the revision-table numbers. Dark: #ff8f86.

### Tertiary
- **Pen Violet** (#6535b0): checks and completion marks. Dark: #c9a9ff.

### Neutral
- **Cool Sheet** (#fbfcfc): the paper. Dark: #14181c.
- **Desk Grey** (#e4e7ea): the page behind the sheet. Dark: #0b0d0f.
- **Graphite Ink** (#1b1f24): text and strong linework. Dark: #e9ecef.
- **Soft Graphite** (#444c56): secondary labels and captions. Dark: #aab2bb.
- **Hairline** (rgba(27,31,36,.22)): row dividers and inner table rules.
- **Washes** (#eaf0ff blue, #fdeceb red, #f1ebfb violet): note backgrounds and table heads only. Dark: #1a2538, #36201f, #271f38.

### Named Rules
**The Three Pens Rule.** Blue, red and violet each mean one thing (given, result/trap, check). A color is never used for emphasis that does not match its meaning.
**The No-Cream Rule.** The sheet is cool white; warm paper tones are not part of this world.

## Typography

**Display Font:** Chakra Petch (with Sarabun, system-ui)
**Body Font:** Sarabun (with Noto Sans Thai, system-ui)

**Character:** Chakra Petch is the squared, technical lettering of a title block; Sarabun is a calm Thai reading face. Thai text is never letter-spaced.

### Hierarchy
- **Title** (700, clamp(22px, 5.4vw, 30px), 1.3): the sheet title inside the title block.
- **Headline** (700, 19px, 1.5): h3 sub-headings inside a sheet.
- **Section** (700, 18px, 1.4): h2 section headings, set under a 2px rule.
- **Step** (700, 16.5px, 1.55): step headings, tinted by tone (blue, red, violet).
- **Body** (400, 17px, 1.8; 17.5px at 1040px+): reading text, capped at 72ch.
- **Label** (600, 13px, 1.5, no tracking): title-block captions, table heads, notes' lead word, tags. Never uppercase-tracked.

### Named Rules
**The Tabular Rule.** Numerals are tabular in all text and tables so columns of working align.
**The Thai Untracked Rule.** No letter-spacing on Thai labels. The only tracking in the build is 0.02em on the Latin course name in the top bar.

## Layout

Phone first. A sticky 52px top bar (course, sheet counter, index button) and a fixed 60px bottom bar (previous/next, plus safe-area inset) frame a full-width sheet with 16px side margins; figures, tables and the title block run edge to edge. At 1040px and up the index becomes a persistent 300px left rail, the sheet centres at max 880px with 28px margins inside a double border, and the bottom bar shifts right of the rail. Title block is 2 columns on phone, 1fr 1.6fr 1fr on wide. Spacing rhythm is 4, 8, 12, 16, 28px; sections open with 34px top margin. Given values use an auto-fill grid of 150px minimum cells. Motion: sheet change fades and rises 6px over .28s, only when reduced motion is not requested.

## Elevation & Depth

Flat. No box-shadows. Depth is the grey desk behind a white sheet, plus line weight: 1px hairlines for rows, 1px strong for tables and notes, 2px for bars, section rules and the answer box. The one inset ring is a 1.5px blue line marking the current index row.

### Named Rules
**The Linework Rule.** Hierarchy comes from line weight (hairline, 1px, 2px), not from shadow or fill.

## Shapes

Square. Every border radius is 0 (inputs set it explicitly). The single exception is the 34px circular step number with a 1.6px graphite ring. Icons are inline SVG with square caps and miter joins, 2 to 2.2px stroke, drawn in currentColor. Answers use a double underline in red.

## Components

### Title Block
Two-column (three on wide) grid of cells with 1px strong borders and a 2px bottom rule. Small 13px soft label over 15px semi-bold value; the title cell uses the Title style. Includes a checkbox (24px, violet accent) for done, and source tags: 1px outlined 13px tags in blue (professor), violet (team) or red (gap).

### Steps
Numbered list with circle numerals, 1px hairline between steps, heading in Step style tinted by tone. In practice mode only the open step shows its body and closed headings show a "tap to reveal" hint.

### Notes
1px strong-bordered box, 10px 14px padding, bold 14px lead word. Variants: trap (red border, red wash), check (violet), hint (blue).

### Answer Box
2px red border on the sheet color, red 14px label, result at clamp(22px, 6vw, 30px) bold red with a 1.5px double underline.

### Tables
Collapsed borders, 1px hairline rows inside a 1px strong frame, 15.5px text, wash-blue head in 13px Label, right-aligned numeric columns. The revision table's first column is bold red.

### Calculator Fields and Button
Square 46px-high inputs with 1px strong border and blue semi-bold values; run button is 50px, graphite fill with sheet text, turning blue on hover. Focus: 2px blue outline offset 2px on everything focusable.

### Navigation
Top bar and bottom bar are sheet-colored with 2px strong rules; cells are separated by 1px strong dividers; hover is the blue wash. Index rows are a 3-column grid (number, title with 13.5px caption, check) separated by hairlines.

## Do's and Don'ts

### Do:
- **Do** use blue for given/substitution, red for results and traps, violet for checks, and nothing else for emphasis.
- **Do** build hierarchy with line weight (hairline, 1px, 2px) on square corners.
- **Do** keep Thai labels untracked at 13px or larger and use Chakra Petch for title-block text and headings.
- **Do** keep interactive targets at least 40px high and give every control the 2px blue focus outline.
- **Do** swap to the paired dark values through the custom properties, never hard-coded colors.

### Don't:
- **Don't** use shadows, rounded cards or cream paper tones.
- **Don't** use the three inks as decoration or on large fills; only washes sit behind notes and table heads.
- **Don't** fall back to the generic docs-site arrangement (left tree, centered article, accent-colored links) on phone; the sheet and title block lead.
- **Don't** add icon glyphs or emoji; icons are inline SVG with square caps.
