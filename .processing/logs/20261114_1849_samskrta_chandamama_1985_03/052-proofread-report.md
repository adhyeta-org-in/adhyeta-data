## Summary

Story `p052` (1985_03, scan 52 only, `महाबुद्धिमान्`, single-page story opening) proofread images-closed: 2 findings, both held word-level observations without blocks (F1 MRP, F2 KRK), and 2 held candidates (= F1-F2, both `*`). No corrections were placed: the file carries no Phase A `{sug-ins:}`/`{sug-del:}` queue (one `{x-com:}` print-noise note retained as-is), all six speeches already stand in era-correct doubles with balanced pairs, and both findings are print-vs-transcription undecidable with images closed, so per Phase B rules no new glyph claims were invented. Extract gate passed with 0 error paras; proofread gate passes with 0 error paras and 0 story findings; `scan.py orth` on deblocked text reports no findings. Loc below is `pNN:Pm:word` (scan-sequence page + chunk matching lint `P` numbers, word counted on the raw chunk from 1, `---` counted as a word) plus the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p052:P4:29 (मार्गं गच्छन्) | `बुद्धिमत्ता भवद्भ्यम् अङ्गीकरणीया` | `भवद्भ्याम्` | MRP | likely | medium* | `भवद्भ्यम्` is not a dual form; instrumental/dative dual needs `भवद्भ्याम्`, but a dropped ā-stroke in print vs a 3x misread is undecidable images-closed, so no block |
| 2 | p052:P5:18 ("अहम् अस्यां) | `मया अपि ... अहं पृच्छेयम्` | `?` | KRK | likely | medium* | pleonastic instrumental `मया` beside nominative `अहं` with one verb; intent readable as translationese emphasis but no minimal fix without new glyph claims, so no block |

## Unverified

U1 (= F1) `भवद्भ्यम्`: settle by reopening scan 52 mid text (`बुद्धिमत्ता भवद्भ्यम् अङ्गीकरणीया` line) — presence or absence of the ā-stroke on `भ्य` decides print slip vs transcription slip. U2 (= F2) `मया अपि ... अहं पृच्छेयम्`: settle by reopening scan 52 mid text (`मया अपि अज्ञातं प्रश्नम् अहं पृच्छेयम्` line) — `मया` vs `मम`/`ममापि` decides print-vs-transcription slip; author's intended construal of Vimaladāsa's reported thought stays a sense ruling either way.

## Coverage

p052:P1 {x-com:layout: : skip layout
p052:P2 # महाबुद्धिमान् : skip title
p052:P3 शङ्करस्य वेङ्कटस्य : clean
p052:P4 मार्गं गच्छन् : F1
p052:P5 "अहम् अस्यां : F2
p052:P6 अनन्तरं शङ्करः : clean
p052:P7 तदा वेङ्कटः : clean
J1 p052:P7 {pb} -> END : ok (range edge; final sentence complete, story may continue on p053 out of range)
