---
name: chandamama-extract
description: Transcribe one Sanskrit Chandamama story range from scan images into a single print-faithful story file. Use for Phase A (images open) of a story range assigned by the coordinator.
---

# Chandamama extract (Phase A, images open)

Transcribes what the print shows, nothing more. Output is one story file for the assigned range. The same agent continues into chandamama-proofread (Phase B) on the same file. The phase boundary is one-way: when Phase A ends the images close and never reopen; anything uncertain travels forward as blocks, never back for another look.

## Input and output

- Assignment from the coordinator: story start page `<START>`, end page (exclusive), and the output path `.processing/samskrta_chandamama/<ISSUE>/p<START>.md`.
- Page images: `.processing/samskrta_chandamama/<ISSUE>/<NN>.jpg` for the range only. Never open other ranges' scans.
- Story file you write: one `{pgb}`-terminated page span per scan page, in scan order — each span the verbatim transcription of that page — followed by a tool-generated `## Joints` index. No sidecars, no scattered files, no `/tmp` copies.
- Format reference: `.agents/refs/chandamama/1984_04/p01.extract.md` with scans `01.jpg`–`04.jpg`. Before your first page, study the p01 span (file start through the first `{pgb}`) against `01.jpg`: the mid-section `{pb}` column joint, the `{wb}` page joint closed by `{pgb}`, the `{sug-ins:}` candidate, the unbalanced print quotes kept as seen.

## Method (per page, in order, while the image is open)

1. Survey the full page before reading a word: art blocks, gutters, column geometry. Declare the layout as one standalone `{x-com:layout: …}` chunk as the first chunk of each page span (file start, or right after the previous `{pgb}`) (e.g. `{x-com:layout: 2col, art top full-width}`; the `layout:` prefix keeps it greppable). The linter treats this chunk as transparent to `{pc}` pairing.
2. Transcribe in reading order: header/title, then columns top-to-bottom, left then right, then footer. Join wrapped lines into paragraphs; keep verse lines separate.
3. Close every asserted break with bare `{pb}`; close every page section with `{pgb}` as its last token, after footers (`...{pb}{pgb: ८}`, `सूर्यो{wb}{pgb}`, `{author: श्वेता}{pgb}`). Give `{pgb}` the printed folio in Devanagari numerals where visible, else bare `{pgb}` — never invent a folio from sequence. A cut inside a word takes `{wb}` (solid join, hyphenation mark dropped); any other joint takes `{pb}` with `{pc}` opening the continuation (spaced join) or a fresh paragraph for a clean break. Sanskrit decides — terminal punctuation (`। ? ! ॥`, plus closing quote) at the edge means a clean break, anything else means continuation.
4. Whether the chunk after a `{pgb}` opens with `{pc}` is decided by its first lines in print: straight continuation of the paragraph (no indent) takes `{pc}`; an indented new paragraph, a title, or a story break takes none.
5. After each page section, refresh the index and gate the whole file (Lint and verify). Verify every joint from both sides while the image is still open: a paragraph ending mid-sentence must offer a `{pb}` whose continuation forms a valid word or sentence on the adjacent column or page.

## Transcription rules (mirror p01.extract.md)

- `# <title>` heading only when a title is printed on the page, and only in the first page section of the story — a story has one title block. A standalone number in the top half of the page is a part number and nothing else; capture it in the title line with the same ` --- ` treatment (e.g. `# कांस्य-दुर्गम् --- २`).
- Blank line, then body paragraphs separated by blank lines.
- Preserve wording and dandas exactly as printed; never normalize, correct, or "fix" spellings, hyphens, quotes, sandhi openness, or apparent misprints. Record reading guesses with `{sug-ins:...}` and notes with `{x-com:...}`.
- Capture author/note/category and other footer metadata as `{author: विवेकः}` / `{note: …}` / `{category: …}`. Use `{misc: ...}` for non-specific footers. Node contents are transcribed as seen; the proofreader rules on them.
- Ignore handwriting, proofreader marks, margin scribbles (print only).
- All Unicode stored as NFC. Straight quotes only (`"` and `'`); no curly quotes, no em/en dashes (`---` with spaces), no `…`, no `|` for danda, no `:` for visarga, no space before `। , : ; ? !`, no double or trailing spaces. Ellipses are `...` with a space on the right; glued compounds keep `-`.
- A dash followed by whitespace, a quote, a parenthesis, or `?`/`!`/`।` is most probably a print mdash: transcribe `---` with spaces on both sides (usual case `उक्तवान्- "..."` → `उक्तवान् --- "..."`). A dash hugging word characters on both sides stays `-`; a dash at a wrap where the word continues is hyphenation (dropped, `{wb}`), never an mdash.
- Page furniture never enters the body: running heads, magazine names including spaced letterhead, bare numerals, illustrator words are stripped; only the closed `{...}` vocabulary may follow story text. The magazine name `चन्दमामा` in any spacing is hard rejected and must never appear.
- A wholly lost page is a page section containing only the block, e.g. `{x-missing: page 13 absent from scan}` or `{x-illegible: full page blur at 400 DPI}`, and nothing else. Never invent text.
- A wholly non-story page (advertisement, index, illustration with no story text) is a page section containing `{x-com:non-story-page: <what>}` closed with bare `{pgb}` — no `{pb}` needed, it still gates clean.

## Phase A quote rule (this phase only)

Record marks as seen; never normalize, upgrade, or supply. Quote sorts are era-dated house style: 1980s–early-90s Chandamama prints `‘‘...’’` (low double open, high double close) for reported speech; DTP standardizes marks from the mid/late-90s, so never project later conventions backwards. Two comma strokes are one mark — transcribe `''` as `"` (open) and `’’` as `"` (close), never re-split into a mixed `"'`/`'"` pair. ONE stroke where the era standard expects two is genuinely ambiguous (true single vs dropped second stroke): transcribe the single `'` as seen and flag it (`{sug-ins:'}` after the mark, or `{x-com:}`), never upgrade it silently. Sort is semantic and stable across eras: doubles mark spoken conversation, singles mark thought (interior monologue, the thought-bubble) or conversation nested inside conversation. An opening mark must close with the same mark and nesting is only `SQ DQ ... DQ SQ` or `DQ SQ ... SQ DQ` (a `"` cannot follow a `"`, an SQ cannot follow an SQ, pairs never cross). The Devanagari avagraha is always U+093D `ऽ` (as in कोऽपि), never ASCII `'`. An isolated mark that could be a speck, a danda fragment, or a quote is verified at 3x or tighter; what stays ambiguous is omitted as print noise only when clearly detached, else marked `{x-illegible: possible quote mark}`. Unbalanced print quotes are kept as seen — the gate reports them as notes-only residuals and Phase B rules on them. Do not record `{sug-ins:}` or `{sug-del:}` quote marks at a `{pb}` edge; the `{pc}` continuation holds the mate. (Phase B's readability rule lives in chandamama-proofread and nowhere else.)

## Blocks (closed vocabulary lives in `.agents/refs/chandamama-blocks.md`; the linter rejects anything else)

- Transcription emits structural, `x-`, author/note/category/misc, `{sug-…}`, and `{x-com:}` blocks — never `{del:}`/`{ins:}` verdicts (the extract gate rejects them).
- `{pb}` with a following `{pc}` means the paragraph continues (spaced join, `{wb}{pc}` solid); with a fresh opening it means a clean paragraph break at the edge. Only `{...}` blocks or whitespace may follow a joint marker inside the paragraph, never bare text.
- `{pgb}` closes the page as the last token of the final chunk, folio included if printed (`{pgb: ८}`) else bare (`{pgb}`). Never mid-span; `{pb}` carries join semantics, filename `<START>` plus `{pgb}` order carry scan identity (k-th span ↔ k-th JPG).
- A genuinely undecidable join takes `{pb}` plus `{x-com: join ambiguous: space or solid?}` for Phase B adjudication.

## Lint and verify

- After each page section: `python3 .agents/tools/chandamama/lint.py --refresh-joints <story.md>`, then `python3 .agents/tools/chandamama/lint.py --phase extract --story <story.md>`. Exit 0 is the gate.
- Fix every error. Legitimate residuals are notes-only: paired-continuation notes (`{pb}`/`{pc}` joins confirmed both sides) and crop-verified print quirks (unbalanced print quotes kept as seen). A green gate with unreviewed notes is not done — carry each residual in context into Phase B as a ruling task.
- Spot-check `head -c 400` of the story file (Devanagari + heading = good).

## Do not

- Do not run OCR tools or any grammar fixer during transcription; eyes and PIL crops only. Enlarge crops under `/tmp` and re-read to verify every ambiguous glyph with a second, tighter crop.
- Do not emit verdicts, tagged forms, summaries, or English prose — story text plus blocks only.
- Do not strip `{pb}`, `{pc}`, `{wb}`, or `{pgb}` markers; compile applies verdicts but the file keeps the markers as the audit trail.
- Do not open pages outside the assigned range; do not touch other ranges' files.
