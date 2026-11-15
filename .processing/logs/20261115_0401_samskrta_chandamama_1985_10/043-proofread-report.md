## Summary

Story 1985_10 p. 43 (वृत्ति धर्मः): 2 findings — 1 quote-sort verdict (F1, spoken report in singles corrected to doubles, high) and 1 word candidate (F2, bare त before चोरं with {del:त}{sug-ins:तं}, medium* held on the replacement). No systematic defect; ज्योतिषिकः/महाज्योतिषिकः (2x) and ज्योतिष्यबलेन (3x) are consistent in-story and kept as print-faithful house spellings, and मौनम् उपविष्टवान् reads as adverbial accusative and is kept. Orth scanner (sanskrit/scan.py orth on deblocked text, 9 lines): 0 hits; text reads as clean print, not OCR output. Extract gate and proofread gate both pass (exit 0). Loc below is story coordinates pNN:Pm plus the first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p043:P6 भद्रेश्वरः साक्षात् | `गत्वा 'छत्रं कश्चित् चोरितवान्' इति` | `गत्वा "छत्रं कश्चित् चोरितवान्" इति` | STY | style | high | top-level spoken report pinned by निवेदितवान् + इति takes doubles; both other speeches in-story use doubles |
| 2 | p043:P7 "भवान् तु | `अहं त चोरं` | `अहं तं चोरं` | OCR | likely | medium* | bare त has no grammatical role here; anusvara-drop yields demonstrative तं resuming चोरः, but contrastive तु fits as well so the replacement is held |

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf* | What would settle it |
|---|---|---|---|---|---|---|---|
| U1 | p043:P7 "भवान् तु | `त` | `तं` or `तु` | LEX | likely | medium* | तं (demonstrative anaphora on चोरः) and तु (contrastive "for my part", pairing finding vs punishing) both fit the clause; tried both against the यदि-पूर्ववाक्य window and neither wins on text alone. Held as {del:त}{sug-ins:तं} with तु recorded here; only a print re-check of dot vs उ-matra could settle it — images closed, so left for the user. |

## Coverage

p043:P1 {x-com:layout: 1col, : skip layout chunk
p043:P2 # वृत्ति : skip title
p043:P3 कृष्णपुरे भद्रेश्वरः : clean
p043:P4 एकदा सः : clean
p043:P5 श्रान्तिकारणतः सः : clean
p043:P6 भद्रेश्वरः साक्षात् : F1
p043:P7 "भवान् तु : F2
p043:P8 "तथैव कर्तुं : clean
p043:P9 ग्रामाधिकारी लज्जया : clean
J1 p043:P9 {pb} -> END (clean break) : ok
