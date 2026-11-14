## Summary

Story `p048` (1985_03, scan 48 only, `अन्तिमा इच्छा`, story opening page) proofread images-closed: 2 findings, both held word-level observations without blocks (F1 LEX, F2 AGR), and 2 held candidates (= F1-F2, both `*`). No corrections were placed: the file carries no Phase A `{sug-ins:}`/`{sug-del:}` queue (transcription confident throughout), all four speeches already stand in era-correct doubles with balanced pairs, and both findings are print-vs-transcription undecidable with images closed, so per Phase B rules no new glyph claims were invented. Extract gate passed with 0 error paras (16 print-spacing ` ।`/` ?` normalizations applied to house style before gating); proofread gate passes with 0 error paras and 0 story findings; `scan.py orth` on deblocked text reports no findings. Loc below is `pNN:Pm:word` (scan-sequence page + chunk matching lint `P` numbers, word counted on the raw chunk from 1, `---` counted as a word) plus the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p048:P4:19 (कृष्णाचार्यः योगधनस्य) | `आरोग्यं विषमितम् अस्ति` | `विषमम्` or `विषमस्थितम्` | LEX | likely | medium* | `विषमितम्` is unattested as a word for a patient's condition; smallest-change construals undecidable images-closed, so no block |
| 2 | p048:P5:20 (वैद्यस्य गमनानन्तरं) | `रक्षणं ततोऽपि कष्टकरः` | `कष्टकरम्` | AGR | likely | medium* | masculine adjective with neuter `रक्षणम्`; print slip vs transcription slip undecidable images-closed, so no block |

## Unverified

U1 (= F1) `विषमितम्`: settle by reopening scan 48 upper text (`आरोग्यं विषमितम् अस्ति` line) — `मितम्` vs `मम्`/`मस्थितम्` decides print-vs-transcription slip; dictionary check of `विषमित` as a possible formation. U2 (= F2) `कष्टकरः`: settle by reopening scan 48 mid text (`रक्षणं ततोऽपि कष्टकरः` line) — visarga vs anusvāra decides print-vs-transcription slip.

## Coverage

p048:P1 {x-com:layout: : skip layout
p048:P2 # अन्तिमा : skip title
p048:P3 योगधनः नाम : clean
p048:P4 कृष्णाचार्यः योगधनस्य : F1
p048:P5 वैद्यस्य गमनानन्तरं : F2
p048:P6 तदा शुभदासः : clean
p048:P7 योगधनः क्षणं : clean
p048:P8 एतत् श्रुत्वा : clean
J1 p048:P8 {pb} -> END : ok (range edge; cliffhanger + art show the story continues on p049, out of range)
