# Proofread report — 1985_07, START=1 (p001.md)

## Summary

3 findings: 2 consistency errors (one-off proper-noun slips, corrected via `{del:}`/`{ins:}` with high confidence) and 1 quote-sort fix (mismatched thought-close, high confidence). The systematic issue is compositor slips in proper nouns (2 instances); otherwise the transcription is clean. `orth` scan on deblocked text reported no hits, and the text is a print transcription, not OCR output. No passages were left unchecked; no candidates held. Loc uses story coordinates `pNN:Pm` (NN = scan sequence, Pm = lint chunk number) with the chunk's first two words as anchor and the word index counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p02:P7:18 ('सामान्यतः समीपस्थस्य) | `मुखतः प्रष्टव्यः" इति चिन्तितवान्` | `मुखतः प्रष्टव्यः' इति चिन्तितवान्` | STY | likely | high | thought passage opened with single `'` must close with single `'`; print's double `"` is a sort slip |
| 2 | p02:P7:22 ('सामान्यतः समीपस्थस्य) | `प्रतापः। मुगन्धस्य गृहं` | `प्रतापः। सुगन्धस्य गृहं` | CNS | error | high | name appears as `सुगन्ध` ~20x elsewhere; single `मु` is a compositor slip, verified in print at crop |
| 3 | p02:P2:12 (अवश्यं चन्दनपुरम्) | `मल्लः च चन्दपुरम् आनीताः` | `मल्लः च चन्दनपुरम् आनीताः` | CNS | error | high | same sentence and story use `चन्दनपुर` 3x; dropped `न` is a compositor slip, verified in print at crop |

## Patterns

- Compositor slips in proper nouns (2): `मुगन्धस्य` for `सुगन्धस्य` (p02:P7), `चन्दपुरम्` for `चन्दनपुरम्` (p02:P2); each corrected where the story's own consistent spelling pins the form.

## Unverified

No held candidates. Every inherited Phase A note was routed to a verdict above; nothing was left as `{sug-ins:}`/`{sug-del:}`.

## Coverage

- p01:P1 {x-com:layout:} : skip layout-only chunk
- p01:P2 # सम्माननयोग्यता : skip title
- p01:P3 कस्मिंश्चित् ग्रामे : clean
- p01:P4 एकदा प्रतापः : clean
- p01:P5 अनन्तरं प्रतापः : clean
- p01:P6 तदा प्रतापः : clean
- p01:P7 "धनार्थं कृतं : clean
- p01:P8 एतदनन्तरं प्रतापः : clean
- p01:P9 {author: सुभद्रा} : skip metadata
- p02:P1 {x-com:layout:} : skip layout-only chunk
- p02:P2 अवश्यं चन्दनपुरम् : F3
- p02:P3 सुगन्धस्य एतेन : clean
- p02:P4 अतः प्रतापः : clean
- p02:P5 वान् भवान् : clean
- p02:P6 ग्रामप्रमुखस्य वचने : clean
- p02:P7 'सामान्यतः समीपस्थस्य : F1, F2
- p02:P8 गृहम् आगतं : clean
- p02:P9 सुगन्धः शान्तस्वरेण : clean
- p03:P1 {x-com:layout:} : skip layout-only chunk
- p03:P2 {pc}इति। : clean
- p03:P3 प्रतापः उक्तवान् : clean
- p03:P4 "कलां ज्ञातुं : clean
- p03:P5 प्रकोष्ठतः बहिः : clean
- p03:P6 सुगन्धः मन्दहासपूर्वकम् : clean
- p03:P7 {pc}मया अभ्यस्ताः : clean
- p03:P8 "भवान् तु : clean
- p03:P9 "अहं साधारणजनानां : clean
- p03:P10 तदा आश्चर्यचकितः : clean
- p04:P1 {x-com:layout:} : skip layout-only chunk
- p04:P2 {pc}"भवता येषां : clean
- p04:P3 सुगन्धः सदर्पं : clean
- p04:P4 प्रतापः मौनं : clean
- p04:P5 प्रतापः अपि : clean
- p04:P6 {pc}वामनमूर्तिः सुगन्धं : clean
- p04:P7 सुगन्धः शिरः : clean
- p04:P8 एतदनन्तरं प्रतापः : clean
- J1 p001:P3 {pb} -> p001:P4 fresh : ok (column turn, clean break आसीत्। / एकदा)
- J2 p001:P4 {pb} -> p001:P5 fresh : ok (column turn, clean break प्रतापः। / अनन्तरं)
- J3 p001:P8 {pb} -> p002:P2 {pc} : ok (page turn, तम् अवश्यं joins)
- J4 p002:P4 {wb} -> p002:P5 {pc} : ok (column turn, उक्त-वान् joins)
- J5 p002:P9 {pb} -> p003:P2 {pc} : ok (page turn, ?" + इति। completes reporting clause)
- J6 p003:P6 {pb} -> p003:P7 {pc} : ok (column turn, अपि मया joins)
- J7 p003:P10 {pb} -> p004:P2 {pc} : ok (page turn, पृष्टवान् --- + "भवता joins)
- J8 p004:P5 {pb} -> p004:P6 {pc} : ok (column turn, तदा वामनमूर्तिः joins)
- J9 p004:P8 {pb} -> END : ok (clean break मिलितवान्।)
