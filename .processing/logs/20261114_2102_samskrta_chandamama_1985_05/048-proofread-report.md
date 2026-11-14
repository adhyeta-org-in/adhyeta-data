# Proofread report: 1985_05 p048 (साक्षी खञ्जरीटः, scans 48–51)

## Summary

4 findings, all STY / style / high: print shows a single quote-mark where direct speech requires doubles (dropped second strokes), each corrected via `{del:'}{ins:"}` per the readability rule (reporting verb plus `इति`-closure pins the sort). No other defects: `scan.py orth` on deblocked text reports zero hits, sandhi openness and house spellings are retained as printed, and joints J1–J8 check out. No held candidates; nothing left unverified. Text is hand transcription from scans, not OCR output. `Loc` is `pNN:Pm` (scan-sequence page + lint chunk number) with the chunk's first two words as anchor and the finding's word index counting Devanagari words on the chunk from 1 (blocks excluded).

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p050:P5 एकदा रात्रौ w31 | `'अये खञ्जरीट! किं साक्ष्यं … भवान्"` | `"अये खञ्जरीट! किं साक्ष्यं … भवान्"` | STY | style | high | drunken taunt closed by `इति … उक्तवान्` is direct speech, which takes doubles |
| F2 | p051:P2 वदतु अहम् w5 | `… अनुभवामि' इति उक्तवान्।` | `… अनुभवामि" इति उक्तवान्।` | STY | style | high | page-turn continuation of the `"किमर्थं…` speech closed by `इति उक्तवान्` takes doubles |
| F3 | p051:P6 सम्भ्रान्तः चोरः w45 | `"किं जातम् इति? … भवेत् एव' इति वदन्` | `"किं जातम् इति? … भवेत् एव" इति वदन्` | STY | style | high | maharaja's exposure speech closed by `इति वदन्` takes doubles |
| F4 | p051:P7 आगतान् सेवकान् w6 | `'एतं नराधमं … आरोपयन्तु" इति।` | `"एतं नराधमं … आरोपयन्तु" इति।` | STY | style | high | execution order closed by `इति` is direct speech, which takes doubles |

## Patterns

P1 print single-for-double in speech (4x: F1–F4). The issue's print drops one stroke of several speech marks (opens in F1/F4, closes in F2/F3); each is pinned by its reporting verb and `इति`-closure, so all four are corrected to doubles while thought-singles (`'एतस्य…व्यर्थम्'`, `'केचन…कुर्वन्ति'`, nested `'अये…साक्षी'` / `'गतजन्मनि…किल?'`) are kept as printed.

## Unverified

None. No candidates held; every print oddity noticed in Phase A was either verified in-print (दिग्भ्रान्तः, विकटाट्टहासं, नियमः।", मारितवान्", अनुभवामि, मध्ये, सन्तुष्टः, शूलम्) and retained, or resolved by the four findings above.

## Coverage

p048:P1 {x-com:layout} : skip layout-only chunk
p048:P2 साक्षी खञ्जरीटः : skip title
p048:P3 बाग्दादसमीपे पर्वतप्रदेशे : clean
p048:P4 तत्पर्वतप्रदेशस्य मार्गे : clean
p048:P5 एकदा सायङ्काले : clean
p048:P6 शिलानां मध्यतः : clean
p048:P7 "किं वदति : clean
p048:P8 भयेन कम्पमानः : clean
p048:P9 वृद्धस्य वचनं : clean
p049:P1 {x-com:layout} : skip layout-only chunk
p049:P2 यात्रिकस्य हस्ते : clean
p049:P3 'एतस्य पुरतः : clean
p049:P4 अतः सः : clean
p049:P5 चोरः धनं : clean
p049:P6 "कः एषः : clean
p049:P7 मारयति अपि : clean
p049:P8 "पापं पुण्यम् : clean
p049:P9 एवम् उक्त्वा : clean
p049:P10 इदानीं भगवतः : clean
p049:P11 वृद्धः उच्चस्वरेण : clean
p049:P12 वृद्धस्य वचनं : clean
p049:P13 एतदनन्तरं वर्षद्वयम् : clean
p050:P1 {x-com:layout} : skip layout-only chunk
p050:P2 समुत्पन्ना अतः : clean
p050:P3 कालान्तरे मैत्री : clean
p050:P4 मध्ये कदापि : clean
p050:P5 एकदा रात्रौ : F1
p050:P6 तदा महाराजः : clean
p051:P1 {x-com:layout} : skip layout-only chunk
p051:P2 वदतु अहम् : F2
p051:P3 "विशेषः कोऽपि : clean
p051:P4 एतत् श्रुतवतः : clean
p051:P5 तस्य वासः : clean
p051:P6 सम्भ्रान्तः चोरः : F3
p051:P7 आगतान् सेवकान् : F4
p051:P8 चोरस्य शिरश्छेदः : clean
J1 p048:P5 -> p048:P6 fresh : ok
J2 p048:P9 -> p049:P2 {pc} : ok
J3 p049:P6 -> p049:P7 {pc} : ok
J4 p049:P13 -> p050:P2 {pc} : ok
J5 p050:P3 -> p050:P4 {wb} : ok
J6 p050:P6 -> p051:P2 {pc} : ok
J7 p051:P4 -> p051:P5 {pc} : ok
J8 p051:P8 -> END : ok
