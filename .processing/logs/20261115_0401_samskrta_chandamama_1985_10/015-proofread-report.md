## Summary

Story 1985_10 pp. 15-17 (महावञ्चकौ): 2 findings — 1 style quote-sort verdict applied as a block (F1), 1 likely low-confidence held candidate (F2, unverified). No systematic defect; proper nouns (वेङ्कटः, सिद्धः) consistent throughout, sandhi openness and अजावलिं / अजायाः बलिं variation kept as print-faithful house style. Orth scanner (sanskrit/scan.py orth on deblocked text, 31 lines): 0 hits; text reads as clean print, not OCR output. Balanced print doubles kept without a block at p017:P6 (मनसि content, inward soliloquy vs thought undecidable from text alone). Extract gate and proofread gate both pass (exit 0). Loc below is story coordinates pNN:Pm plus the first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p017:P2 स्थितं वृक्षम् | `'रे चोर! ... पूजयामि च"` | `"रे चोर! ... पूजयामि च"` | STY | style | high | print pairs single open with double close; गर्जितवान् plus vocative, imperatives and इति-closure pins spoken threat, era standard is doubles; open corrected via {del:'}{ins:"}, close kept |
| 2 | p017:P7 अनन्तरदिने वेङ्कटः | `नास्ति भव्याः"` | `नास्ति भवत्याः"` | MRP | likely | low* | भव्याः fits no address slot here (fem ā-stem genitive would be भव्यायाः, vocative भव्ये); tried भवी ī-stem genitive, भवतः, and vocative re-segmentations and neither yields a clean reading, so held as both-uncertain {sug-del:}{sug-ins:} with {x-com:} on file |

## Unverified

F2 only: `भव्याः` vs `भवत्याः` at p017:P7. Not checked against a dictionary or the Heritage Platform, and the print cannot be reopened (Phase B). Would settle with a lexicon check for an ī-stem भवी (genitive भव्याः) or a print re-check for a dropped त.

## Coverage

p015:P1 {x-com:layout: 2col, : skip layout chunk
p015:P2 # महावञ्चकौ : skip title
p015:P3 पूर्वं कस्मिंश्चित् : clean
p015:P4 कालान्तरे सुन्दरम् : clean
p015:P5 "इदानीं वा? : clean
p015:P6 नारिकेलवृक्षाः फलिताः। : clean
p015:P7 तदा वेङ्कटः : clean
p015:P8 {pc}उक्तवान् --- : clean
p015:P9 सिद्धः इदानीम् : clean
p015:P10 वेङ्कटस्य कठोरस्वभावेन : clean
p015:P11 एकसप्ताहाभ्यन्तरे एव : clean
p015:P12 {note: पञ्चविंशतिवर्षेभ्यः : skip footer metadata
p016:P1 {x-com:layout: 2col, : skip layout chunk
p016:P2 वेङ्कटः सिद्धं : clean
p016:P3 "एवं तर्हि : clean
p016:P4 "रूप्यकद्वयं वेतनम् : clean
p016:P5 "तत् तु : clean
p016:P6 तत्समये देवीं : clean
p016:P7 {pc}चिन्तितवान् --- : clean
p016:P8 अतः सः : clean
p016:P9 तद्दिने रात्रौ : clean
p016:P10 किन्तु वेङ्कटः : clean
p017:P1 {x-com:layout: 2col, : skip layout chunk
p017:P2 {pc}स्थितं वृक्षम् : F1
p017:P3 वृक्षे स्थितः : clean
p017:P4 सः त्वरया : clean
p017:P5 अन्धकारे इतस्ततः : clean
p017:P6 चोरस्य आघातेन : clean
p017:P7 अनन्तरदिने वेङ्कटः : F2
p017:P8 तदा देवी : clean
p017:P9 देव्याः वचनेन : clean
J1 p015:P7 {pb} -> p015:P8 {pc} (continues) : ok
J2 p015:P11 {pb} -> p016:P2 fresh (clean break) : ok
J3 p016:P6 {pb} -> p016:P7 {pc} (continues) : ok
J4 p016:P10 {pb} -> p017:P2 {pc} (continues) : ok
J5 p017:P5 {pb} -> p017:P6 fresh (clean break) : ok
J6 p017:P9 {pb} -> END (clean break) : ok
