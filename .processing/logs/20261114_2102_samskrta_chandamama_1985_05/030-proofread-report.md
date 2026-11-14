# Proofread report: 1985_05, story START=30 (pp. 30-32, `p030.md`)

## Summary

Four findings (all severity error, all confidence high): three type-damage corrections (a dropped ण-loop in तत्क्षते, a stray anusvara in यावतं, an extra sort in विक्रयणं) and one ठ-for-ट sort confusion (सन्तोष्ठव्यम्). One item held for the user (H1): अन्ये has no plural referent and is likely a dropped temporal (अन्येद्युः or अन्यदा). Kept as print-faithful: open-sandhi spacing throughout (यत् अहं beside तदेव), स्नेहितः (2x consistent), मद्वशीकरोमि (subscript read as व at 3x), ममापादयितुं, अल्प-मूल्यकं (compound hyphen kept), निदर्शनपूर्वकं, दुर्लाभं, स्वदुराशायाः, and the print's single quotes on the two sharp outbursts ('हा', 'भवान् मां वञ्चितवान्'). No passages went unchecked: all three scans were transcribed in Phase A, the orth scanner ran on deblocked text with one false hit (the print exclamation in द्वितीयस्य हस्ते!), and every paragraph was read sentence by sentence for continuity. The text is hand-transcribed from print, not OCR output. Loc is `pNN:Pm` (scan sequence + chunk, matching lint P numbers) with the anchor's first two words and word number counting space-separated tokens on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p030:P9 ("अत्र कः) w16 | `स्नेहितः तत्क्षते एव` | `स्नेहितः तत्क्षणे एव` | OCR | error | high | तत्क्षते is not a word; तत्क्षणे (at that very moment) fits and print spells it so five lines above; dropped ण-loop |
| F2 | p031:P7 (प्रतिदिनं प्रथमस्य) w20 | `यावतं दातव्यं` | `यावत् दातव्यं` | OCR | error | high | यावत् is indeclinable here (यावत्...तावत् correlative); stray anusvara |
| F3 | p032:P3 (प्रथमः पुनरपि) w5 | `विक्रयणं करोमि` | `विक्रयं करोमि` | OCR | error | high | विक्रयण is not a word; विक्रयं कृ is the idiom (sell); extra sort |
| F4 | p032:P8 (उभयोः अपि) w31 | `तेन एव सन्तोष्ठव्यम्` | `तेन एव सन्तोष्टव्यम्` | OCR | error | high | सम् + तुष् + तव्य gives सन्तोष्टव्यम् (ष + त → ष्ट); ठ-for-ट sort confusion |

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| H1 | p031:P8 (द्वितीयः हसन्) w5 | `तिष्ठति। अन्ये प्रथमः` | `अन्येद्युः` or `अन्यदा` | OCR | error | low* | अन्ये has no plural referent in a two-character scene, so the print is defective, but अन्येद्युः (next day) and अन्यदा (another time) both fit; user picks the connective |

## Coverage

p030:P1 {x-com:layout:} : skip layout
p030:P2 # श्मश्रु : skip title
p030:P3 एकस्मिन् ग्रामे : clean
p030:P4 एकदा उभौ : clean
p030:P5 एतत् श्रुत्वा : clean
p030:P6 {pc}अङ्गुल्याभिः : clean
p030:P7 एतत् श्रुत्वा : clean
p030:P8 आशाग्रस्तस्य द्वितीयस्य : clean
p030:P9 "अत्र कः : F1
p030:P10 एतत् दृष्ट्वा : clean (मद्वशीकरोमि kept as print, x-com on file)
p030:P11 {note:} : skip metadata
p031:P1 {x-com:layout:} : skip layout
p031:P2 {pc}लेपनीयम् : clean
p031:P3 "एतत् किं : clean
p031:P4 प्रथमः पुनरपि : clean
p031:P5 द्वितीयः एतत् : clean
p031:P6 कदाचित् प्रथमः : clean (अल्प-मूल्यकं kept as print, x-com on file)
p031:P7 प्रतिदिनं प्रथमस्य : F2
p031:P8 द्वितीयः हसन् : H1
p031:P9 द्वितीयः असम्मतिं : clean
p032:P1 {x-com:layout:} : skip layout
p032:P2 {pc}तत् भवतः : clean
p032:P3 प्रथमः पुनरपि : F3
p032:P4 द्वितीयः एतत् : clean (ममापादयितुं kept as print, x-com on file)
p032:P5 किं करणीयम् : clean
p032:P6 द्वितीयः झटिति : clean (print singles 'हा' and 'भवान् मां वञ्चितवान्' kept as seen)
p032:P7 वस्तुतः न्यायाधीशः : clean
p032:P8 उभयोः अपि : F4
J1 p030:P5 {pb} -> p030:P6 {pc} (continues) : ok
J2 p030:P10 {pb} -> p031:P2 {pc} (continues) : ok
J3 p031:P6 {pb} -> p031:P7 fresh (clean break) : ok
J4 p031:P9 {pb} -> p032:P2 {pc} (continues) : ok
J5 p032:P5 {pb} -> p032:P6 fresh (clean break) : ok
J6 p032:P8 {pb} -> END (clean break) : ok
