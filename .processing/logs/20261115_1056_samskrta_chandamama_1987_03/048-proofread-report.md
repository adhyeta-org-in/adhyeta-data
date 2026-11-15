# Proofread report: 1987_03 p048 (`समर्थः ज्योतिषिकः`)

## Summary

Single-page complete story (8 body chunks, 1 joint to END); transcription from the 48.jpg scan, extract gate green with one notes-only residual carried in. Two findings, both shipped as verdict blocks in the story file: a mismatched thought-quote close corrected to a single quote, and a dropped ु-मात्रा supplied on तु. Orth scanner run on deblocked text returned zero hits. No candidates held; house spellings (ज्योतिर्षक body vs ज्योतिषिक title, तदानीम्) stand as print. Loc below is `p48:Pm wW` (chunk number plus word position in the chunk).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p48:P6 w31 | `'एतेषु ... कः स्यात्?" इति` (opens `'`, closes `"`) | `कः स्यात्?' इति` | STY | error | high | Mismatched pair in print; interior thought (चिन्तितवान्) takes single quotes, so the close is corrected via `{del:"}{ins:'}` |
| 2 | p48:P10 w12 | `रामशास्त्रिणः त अदृष्टबलम्` | `रामशास्त्रिणः तु अदृष्टबलम्` | OCR | error | high | Bare `त` is ungrammatical; किन्तु...तु contrast requires `तु`; print verified bare-त at 4x, मात्रा supplied via `{ins:ु}` |

## Unverified

None held. The Phase A `{sug-ins:ु}` queue is empty (promoted to F2); no new glyph claims were invented in Phase B.

## Notes (print-faithful, no blocks)

- House spellings kept as seen, never normalized: body `ज्योतिर्षक` (र्ष) throughout vs title `ज्योतिषिक`, `ज्योतिषे` (P6, no र) vs `ज्योतिःशास्त्रे` (P4, P8); `तदानीम्` (P6).
- P10 `प्राप्तवान्?` keeps the print `?` mid-speech as seen (rhetorical turn before `अतः`).
- P3 `श्रीनिवासपरराज्यस्य` read clearly at 2x; kept as the printed kingdom name.

## Coverage

- p48:P1 `{x-com:layout:` : skip (layout declaration, read against full page)
- p48:P2 `समर्थः ज्योतिषिकः` : skip (title)
- p48:P3 `श्रीनिवासपरराज्यस्य आस्थाने` : clean
- p48:P4 `परीक्षानन्तरम् आगतेषु` : clean
- p48:P5 `"तादृशः योगः` : clean
- p48:P6 `इदानीं राजा` : F1
- p48:P7 `मन्त्री राज्ञः` : clean
- p48:P8 `तदा मन्त्री` : clean
- p48:P9 `"केन आधारेण` : clean
- p48:P10 `"महाराज! सत्यं` : F2
- J1 p048:P10 {pb} -> END (clean break) : ok (story ends with ।, clean break at issue's last page, no folio printed)
