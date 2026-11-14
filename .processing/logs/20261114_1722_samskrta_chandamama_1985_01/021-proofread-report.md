# Proofread report: 1985_01 p021 (असन्तृप्तिः, single page)

## Summary

Single-page complete story in 8 body paragraphs plus title; Phase A transcribed with images open (layout `1col, art bottom full-width`, no folio visible, bare `{pgb}`), Phase B ruled with images closed. Two findings: one `error` (dropped visarga, corrected by verdict) and one `style` (thought passage printed in speech sorts, corrected by verdict). No systematic defect; the edition mixes open and joined sandhi (`इति उक्तवान्` beside `इत्युक्तवान्`) and mixes weak/strong grades of प्रच्छ् (`पृष्टवान्` beside `प्रष्टुम्`, `प्रष्टव्याः`), all kept as house variants per print-fidelity doctrine. `scan.py orth` reports no hits on deblocked text; the proofread lint gate is green. Loc below is `p21:Pm:word` (word counted on the chunk from 1) with the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p21:P6:11 (परेद्युः केशवः) | `तदा धनिक। म्लानेन` | `तदा धनिकः। म्लानेन` | OCR | error | high | Dropped visarga in print (clean danda verified at 3x in Phase A); nominative subject of उक्तवान् needs धनिकः; filed as `धनिक{ins:ः}।` |
| 2 | p21:P5:5,17 (तदा केशवः) | `"मया ... शक्यते"` | `'मया ... शक्यते'` | STY | style | high | Interior monologue pinned by चिन्तयन् with इति closure takes thought sorts; print's doubles corrected to singles at both marks (`{del:"}{ins:'}` open and close) |

## Patterns

None (single page, no repeats).

## Checked print-faithful (no block)

- `करोतु'इत्युक्तवान्` (P4) is glued in print while `ददातु' इत्युक्तवान्` in the same paragraph is spaced; kept as seen, inconsistent print spacing.
- `पृष्टवान्` (weak grade) beside `प्रष्टुम्`, `प्रष्टव्याः` (strong grade) kept as house variants, not normalized.
- Mixed open/joined sandhi (`सः एकदा`, `तथा उक्तम्`, `इति उक्तवान्` beside `इत्युक्तवान्`, `सो`-less forms) kept as house style.
- Short spoken quotes kept in print's singles (`'भवतः इच्छा'`, `'तथा मास्तु ...'`, `'द्विशतं ...'`, `'तथास्तु ...'`, `'किमर्थम्'`), matching the kept singles in the 1984_04 reference; all pairs balanced, no edge-spanning on this single page.

## Unverified

- U1 at p21:P9 (कारणं न), word `निश्चितोतु` in `तेषां वेतनं निश्चितोतु`: expected classical lot form is `निश्चिनोतु` (नि + √चि 5th class); no clause-level re-segmentation rescues the printed form. No file block placed because no Phase A `{x-com:}`/`{sug-…}` flag exists for this word and Phase B invents no new glyph claims. Settles by re-examining the print at 3x for `निश्चितोतु` vs `निश्चिनोतु` (चि + तो vs चि + नो).

## Coverage

p21:P1 {x-com:layout: : skip x-com-only chunk
p21:P2 # असन्तृप्तिः : skip title
p21:P3 कस्मिंश्चित् ग्रामे : clean
p21:P4 केशवः 'भवतः : clean
p21:P5 तदा केशवः : F2
p21:P6 परेद्युः केशवः : F1
p21:P7 केशवः दशरूप्यकाणि : clean
p21:P8 'किमर्थम्' इति : clean
p21:P9 "कारणं न : clean
p21:P10 केशवेन किमर्थं : clean
J1 p021:P10 {pb} -> END (clean break) : ok
