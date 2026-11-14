# Proofread report: 1985_04 story p034 (START 34, scans 34–39)

## Summary

9 findings: 1 SPL error (घ/ध slip against 20+ consistent न्यायाधीशः) and 8 STY style fixes (3 supplied per-para quote marks, 1 stray-mark deletion, 4 single-to-double sort corrections over 7 blocks). 1 item held unverified (धर्मात्मा address). Systematic issue is the print's quote handling: singles for short spoken utterances and speeches left open across fresh column breaks. Full story read sentence by sentence for continuity; no ruptures, no moves proposed, all 12 joints text-continuous. Orth scanner clean (0 hits); text is a print transcription, not OCR output. Loc = story coordinates pNN:Pm (lint chunk numbers) with first-two-word anchor; w = word index in chunk (blocks excluded).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p34:P5 (ग्रामस्थेषु एकः) w13 | `किमर्थं वदति?{pb}` open `"` unclosed | `{ins:"}` after `वदति?` | STY | style | high | multi-para speech must close its own pair; J1 is a fresh break, not a `{pc}` continuation |
| 2 | p34:P6 (वस्तुतः किं) w1 | `वस्तुतः किं ... आगतवान्?"` close without open | `{ins:"}` before `वस्तुतः` | STY | style | high | same speech continued; per-para pairing needs its own open at the sentence boundary |
| 3 | p35:P7 (अस्य नगरस्य) w1 | `अस्य नगरस्य ... करणीयम्"` speech with no open | `{ins:"}` before `अस्य` | STY | style | high | direct speech (first-person statement, `उक्तवती` + `इति`) needs an opening pair |
| 4 | p35:P10 (रक्षकभटः तां) w9 | `ताडितवान्। 'यदा` lone single open | `{del:'}`; drop `{sug-ins:'}` | STY | style | high | `यदा`-clause is third-person narration, not speech; inner `"श्रीमन् ... कल्पयतु"` is the real utterance, so doubling would leave 3 doubles |
| 5 | p36:P4 (रक्षकभटः क्रोधेन) w5 | `'कः विशेषः'` singles | `{del:'}{ins:"}कः विशेषः{del:'}{ins:"}` | STY | style | high | spoken exchange (`पृष्टवान्` + `इति`) takes doubles |
| 6 | p36:P4 (रक्षकभटः क्रोधेन) w9 | `'शीघ्रं ... आगच्छतु"` single open | `{del:'}{ins:"}` before `शीघ्रं` | STY | style | high | spoken order (`इति` + `उक्तवन्तः`) takes doubles; close already double |
| 7 | p37:P8 ("किमपि किमपि) w8 | `न्यायघीशस्य` | `{del:न्यायघीशस्य}{ins:न्यायाधीशस्य}` | SPL | error | high | घ/ध confusable pair; `न्यायाधीश` spelled with धी 20+ times elsewhere in this story |
| 8 | p38:P6 ('तथा अस्तु) w1 | `'तथा अस्तु'` singles | `{del:'}{ins:"}तथा अस्तु{del:'}{ins:"}` | STY | style | high | spoken assent (`अङ्गीकृत्य` + `इति`) takes doubles |
| 9 | p39:P9 (एवंरीत्या उक्तां) w11 | `'हन्त! हन्त! वराकः एषः!'` singles | `{del:'}{ins:"}हन्त! हन्त! वराकः एषः!{del:'}{ins:"}` | STY | style | high | villagers' spoken exclamation (`उक्तवन्तः` + `इति`) takes doubles |

## Patterns

- Singles-for-speech print habit (4 locs: F5, F6, F8, F9): short spoken utterances set in single marks where the era standard wants doubles; all corrected to doubles since speech sense plus sentence boundary pins each one.
- Per-para pairing supplies (3 locs: F1, F2, F3): speeches split across fresh breaks or printed without an opener, each paragraph given its own pair via `{ins:"}`; genuine `{pc}`-continuation pairs (J2, J5–J10) were never forced closed.

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why / settler |
|---|---|---|---|---|---|---|---|
| U1 | p36:P9 (रक्षकभटः भीत्या) w31 | `धर्मात्मा भवान्` | `धर्मात्मन् भवान्` | MRP | likely | low* | address to the 2nd person wants vocative `धर्मात्मन्`; settler: only `-आत्मन्` address in the text, while `स्वामिन्`/`श्रीमन्` use true vocatives; holding for a human editor |

## Coverage

p34:P1 {x-com:layout: : skip layout
p34:P2 # अपूर्वः : skip title
p34:P3 बागदादनगरस्य समीपे : clean
p34:P4 सः वृक्षस्य : clean
p34:P5 ग्रामस्थेषु एकः : F1
p34:P6 वस्तुतः किं : F2
p34:P7 "मम जीवनानुभवेन : clean
p34:P8 सः पुरुषः : clean
p34:P9 सः तां : clean
p34:P10 {category: अरेबिया : skip metadata
p35:P1 {x-com:layout: : skip layout
p35:P2 {pc}समीपे किम् : clean
p35:P3 सा स्त्री : clean
p35:P4 "अहं न : clean
p35:P5 सा मञ्जुलस्वरेण : clean
p35:P6 "कीदृशम् उत्तमकार्यं : clean
p35:P7 अस्य नगरस्य : F3
p35:P8 "तत् कथं : clean
p35:P9 "यदि भवान् : clean
p35:P10 रक्षकभटः तां : F4
p36:P1 {x-com:layout: : skip layout
p36:P2 सः न्यायाधीशः : clean
p36:P3 अनन्तरं सः : clean
p36:P4 रक्षकभटः क्रोधेन : F5, F6
p36:P5 तत्र नगराधिकारिणा : clean
p36:P6 {pc}न्यायाधीशः क्रोधेन : clean
p36:P7 तस्य प्रश्नं : clean
p36:P8 "रे रे : clean
p36:P9 रक्षकभटः भीत्या : U1
p36:P10 तदा नगराधिकारी : clean
p36:P11 किन्तु तृतीये : clean
p37:P1 {x-com:layout: : skip layout
p37:P2 {pc}गृहस्य वातायनद्वारा : clean
p37:P3 सा तु : clean
p37:P4 "रे दुष्टे! : clean
p37:P5 "भवद्द्वारा अहम् : clean
p37:P6 "मत्कारणतः भवत्याः : clean
p37:P7 सा किञ्चित् : clean
p37:P8 "किमपि किमपि : F7
p37:P9 {pc}अपि मम : clean
p37:P10 "न्यायाधीशः अधर्ममार्गेण : clean
p37:P11 तत्सर्वं दृष्ट्वा : clean
p38:P1 {x-com:layout: : skip layout
p38:P2 {pc}अस्मि। न्यायाधीशस्य : clean
p38:P3 "एतावदेव खलु! : clean
p38:P4 अनन्तरं रक्षकभटः : clean
p38:P5 {pc}कल्पयतु" इति : clean
p38:P6 'तथा अस्तु' : F8
p38:P7 रक्षकभटः गृहं : clean
p38:P8 "सा हरितवर्णीयं : clean
p38:P9 तदा झटिति : clean
p38:P10 तत् दृष्ट्वा : clean
p38:P11 अनन्तरं नगराधिकारी : clean
p38:P12 "स्त्रीहत्या वा? : clean
p39:P1 {x-com:layout: : skip layout
p39:P2 {pc}हृतवान् इति : clean
p39:P3 नगराधिकारी तं : clean
p39:P4 "स्वामिन्! भवतः : clean
p39:P5 तस्याः सौन्दर्यं, : clean
p39:P6 यदा रक्षकभटः : clean
p39:P7 "किं भोः, : clean
p39:P8 तदारभ्य रक्षकभटः : clean
p39:P9 एवंरीत्या उक्तां : F9
J1 p034:P5 -> p034:P6 fresh : ok (same speech, per-para pairs supplied F1/F2)
J2 p034:P9 -> p035:P2 {pc} : ok (मम समीपे किम् अस्ति कार्यम्?)
J3 p035:P9 -> p035:P10 fresh : ok (new sentence)
J4 p035:P10 -> p036:P2 fresh : ok (next-day events)
J5 p036:P5 -> p036:P6 {pc} : ok (रक्षकभटं दृष्ट्वा न्यायाधीशः ... single sentence)
J6 p036:P11 -> p037:P2 {pc} : ok (एकस्य गृहस्य वातायनद्वारा)
J7 p037:P8 -> p037:P9 {pc} : ok (इतःपरम् अपि मम समीपे)
J8 p037:P11 -> p038:P2 {pc} : ok (पतितः अस्मि)
J9 p038:P4 -> p038:P5 {pc} : ok (अवकाशं कल्पयतु)
J10 p038:P12 -> p039:P2 {pc} : ok (अहमेव तां हृतवान्)
J11 p039:P5 -> p039:P6 fresh : ok (guard goes to her house next)
J12 p039:P9 -> END : ok (frame closes, villagers console)
