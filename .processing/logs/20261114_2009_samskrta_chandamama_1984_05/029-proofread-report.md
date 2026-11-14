# Proofread report: 1984_05 story p029 (विश्वासार्हः, scans 29–31)

## Summary

Seven findings: one `likely` (F6, visarga dropped in `गृहस्थाः`) and six `style` (F1–F5 quote-sort rulings, F7 hyphen inconsistency). The systematic problem is unstable printed quote sorts: singles for reported speech twice, one missing thought-open, one single-open/double-close pair across the p30 column joint, and doubles for interior thought once. Every finding is routed to a `{del:}`/`{ins:}` verdict block in the story file except F7, which is kept as print. No passages were left unchecked (all 25 chunks read sentence by sentence; Phase A verified glyphs at up to 3x); the text is a print transcription, not OCR output. `Loc` below is `pNN:Pm` (scan page + chunk, matching lint `P` numbers) with the chunk's first two words and the finding's word index on the deblocked chunk.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p29:P4 लोपराजस्य पुत्रः w18+w50 | `'बधिरेण … वरम्'` | `"बधिरेण … वरम्"` | STY | style | high | reported speech (`वदति स्म…इति`) takes doubles; print singles corrected at both marks |
| 2 | p29:P5 लोपराजः एतत् w9+w24 | `'बधिरः … उचितम्'` | `"बधिरः … उचितम्"` | STY | style | high | reported speech (`वदति स्म…इति`) takes doubles; print singles corrected at both marks |
| 3 | p29:P6 वस्तुतः शरभः w18 | (no open) `यथाकथञ्चित्…निष्कासनीयः'` | `'यथाकथञ्चित्…निष्कासनीयः'` | STY | style | high | thought (`मनसि…इति`) missing its open; supplied, print close kept |
| 4 | p30:P5 अनन्तरं शरभः w19 → p30:P6 प्रथमम् एव | `'अये! … श्रुतम्"` | `"अये! … श्रुतम्"` | STY | style | high | speech (`उक्तवन्तः…इति`) spanning the column joint; open corrected to double to match the print close |
| 5 | p30:P3 कः अपराधः w1+w6 | `"कः … नष्टः?"` | `'कः … नष्टः?'` | STY | style | medium | interior questioning (`न ज्ञातवान्`, no addressee) is thought; print doubles corrected to singles |
| 6 | p30:P8 वृषभयोः कलहः w4 | `सर्वे गृहस्थ वितर्दिकायां` | `सर्वे गृहस्थाः वितर्दिकायां` | MRP | likely | high | masculine nominative plural subject (`सर्वे…स्थिताः`) needs `-ाः`; print drops the visarga (Phase A `{x-com:}` on file) |
| 7 | p31:P4 वीरराजः तत्रत्यैः w7 / p31:P8 स्व-पौत्रः अपायतः w5 | `शरभविषये` / `शरभ-विषये` | `?` (keep both as print variants) | CNS | style | high | hyphenation of one compound varies within the story; fidelity keeps both |

## Patterns

Quote-sort instability (5 findings, F1–F5): this print uses singles where the era standard expects doubles for reported speech (F1: p29:P4 `वदति स्म`; F2: p29:P5 `वदति स्म`), drops a thought-open (F3: p29:P6 `मनसि`), mixes sorts across the p30 column joint (F4: single open, double close), and uses doubles for interior thought (F5: p30:P3). All five are ruled by speech-vs-thought sense plus reporting verb and `इति` closure; kept sorts are the certain-speech doubles (`"हन्त!…"` p30:P8, `"भोः…"` p31:P4, `"एतस्य…"` p31:P6, `"शरभः…"` p31:P7) and the certain-thought singles (`'शरभं…'` p30:P2, `'यथाकथञ्चित्…'` p29:P6 after F3).

## Unverified

None. Every Phase A candidate was routed: both `{sug-ins:'}` flags promoted to `{del:'}{ins:"}` verdicts (F1, F2), both extract residuals supplied (F3, F4), and no new held candidate was created.

## Coverage

p29:P1 `{x-com:layout:}` : skip layout-declaration
p29:P2 `# विश्वासार्हः` : skip title
p29:P3 एकस्मिन् ग्रामे : clean
p29:P4 लोपराजस्य पुत्रः : F1
p29:P5 लोपराजः एतत् : F2
p29:P6 वस्तुतः शरभः : F3
p29:P7 एकदा लोपराजः : clean
p29:P8 `{author: माणवकः}` : skip metadata
p30:P1 `{x-com:layout:}` : skip layout-declaration
p30:P2 वीरराजः चिन्तितवान् : clean
p30:P3 कः अपराधः : F5
p30:P4 अतः सः : clean
p30:P5 अनन्तरं शरभः : F4
p30:P6 प्रथमम् एव : F4
p30:P7 एकस्मिन् दिने : clean
p30:P8 वृषभयोः कलहः : F6
p30:P9 शरभः एतत् : clean
p31:P1 `{x-com:layout:}` : skip layout-declaration
p31:P2 सः उत्थातुम् : clean
p31:P3 पुत्रस्य प्राणापायपरिस्थितिं : clean
p31:P4 वीरराजः तत्रत्यैः : F7
p31:P5 पुनः एकसप्ताहानन्तरं : clean
p31:P6 `"एतस्य किम्` : clean
p31:P7 `"शरभः बधिरः` : clean
p31:P8 स्व-पौत्रः अपायतः : F7
J1 p29:P4 -> p29:P5 fresh (column turn) : ok
J2 p29:P7 -> p30:P2 fresh (page turn) : ok
J3 p30:P5 -> p30:P6 {pc} (column turn mid-quote) : F4
J4 p30:P9 -> p31:P2 fresh (page turn) : ok
J5 p31:P4 -> p31:P5 fresh (column turn) : ok
J6 p31:P8 -> END (clean break) : ok
