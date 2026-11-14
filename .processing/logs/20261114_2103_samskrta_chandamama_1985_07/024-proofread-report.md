# Proofread report: samskrta_chandamama 1985_07, p024 देवधर्मः (scans 24–27)

## Summary

Two verdicts, both quote-mark repairs (STY/error/high): F1 promotes the Phase A `{sug-ins:'}` flag to a `{del:'}{ins:"}` sort correction on the king's first speech, whose print open is a verified single stroke against a verified double close; F2 drops the misplaced Phase A flag on the nested single open (correct sort) and supplies the dropped inner close via a lone `{ins:'}` at its certain position, which also resolves the page-spanning DQ[SQ] nest the extract gate reported as crossed-quotes. No held block candidates remain; one report-only unverified item (U1, possible रु/रव misread, no story block placed since images are closed and Phase A left no flag). `scan.py orth` on deblocked text is clean (0 hits); the proofread gate is green (exit 0, 0 error paras, 0 findings). Loc below is story coordinates `pNN:Pm` plus the chunk's first two words and the word number counted on the chunk from 1. Print's balanced self-contained single pairs for thought and short replies ('एषा पट्टमहिषी ...', 'पुरतः ...', 'वदतु तावत्') are kept as seen per the proofread reference's handling of spoken singles.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p24:P4 अल्पे एव w36 | `उक्तवान् --- 'भवती पुत्रार्थं ... पृच्छतु" इति` | `उक्तवान् --- "भवती पुत्रार्थं ... पृच्छतु" इति` | STY | error | high | reported speech (उक्तवान्) takes doubles; print open verified single at 3x against verified double close, so one open stroke dropped |
| F2 | p25:P2 प्रलयान्तिका किल? w18 | `सा भवतोः 'किमपि ... शक्यते" इति` | `सा भवतोः 'किमपि ... शक्यते'" इति` | STY | error | high | nested reported content inside the king's `"..."` speech takes singles; the single open is correct and the inner close is dropped at the certain clause end before the speech close |

## Patterns

- House instrumental-dual `-भ्यां` for classical `-भ्याम्`, kept as print (variant, 2x): p25:P3 सूर्यकुमारः एतत् (`अग्रजाभ्यां निवार्यमाणः`), p27:P9 एतदनन्तरम् अपि (`सहोदराभ्यां सह`).

## Unverified

- U1 (p26:P13 `"निन्दाभीरवः,` w1): `निन्दाभीरवः` reads as "blame-fearing" only on a भीरु stem (expected `निन्दाभीरवः` → `निन्दाभीरुः` against the parallel bahuvrīhis `शुभकर्मकारिणः, प्रेमजीविनः, शान्तप्रकृतयः`); possibly a रु/रव print misread. No story block placed (images closed, no Phase A flag on file). Settles by re-examining the print glyph at 3x. | Cat OCR | Sev likely | Conf medium* |

## Coverage

- p24:P1 {x-com:layout: : skip layout-chunk
- p24:P2 # देवधर्मः : skip title
- p24:P3 पूर्वं कश्चित् : clean
- p24:P4 अल्पे एव : F1
- p24:P5 "अद्य किमपि : clean
- p24:P6 कानिचन वर्षाणि : clean
- p24:P7 {pc}विश्रान्तिसुखम् अनुभवन्न् : clean
- p24:P8 राजा क्रुद्धः। : clean
- p24:P9 इदानीं महाराजस्य : clean
- p24:P10 {category: जातककथा} : skip metadata
- p25:P1 {x-com:layout: : skip layout-chunk
- p25:P2 {pc}प्रलयान्तिका किल? : F2
- p25:P3 सूर्यकुमारः एतत् : clean
- p25:P4 त्रयः अपि : clean
- p25:P5 {pc}आवयोः कृते : clean
- p25:P6 तस्मिन् सरोवरे : clean
- p25:P7 यदा सूर्यकुमारः : clean
- p25:P8 "आम्, अहं : clean
- p25:P9 "भवान् देवधर्मं : clean
- p25:P10 सूर्यकुमारस्य अनागमनं : clean
- p25:P11 चन्द्रकुमारः उक्तवान् : clean
- p25:P12 यक्षः "भवान् : clean
- p26:P1 {x-com:layout: : skip layout-chunk
- p26:P2 चन्द्रकुमारः अपि : clean
- p26:P3 बहुकालपर्यन्तम् अपि : clean
- p26:P4 'पुरतः ब्राह्मणवेषेण : clean
- p26:P5 "आम्, अहम् : clean
- p26:P6 "एवं किमर्थं : clean
- p26:P7 "ये अस्मिन् : clean
- p26:P8 "सरोवरं प्रविष्टाः : clean
- p26:P9 {pc}भवेयुः वा?" : clean
- p26:P10 "न यः : clean
- p26:P11 "देवधर्मं ज्ञातुम् : clean
- p26:P12 'वदतु तावत्' : clean
- p26:P13 "निन्दाभीरवः, शुभकर्मकारिणः, : U1
- p26:P14 एतेन उत्तरेण : clean
- p27:P1 {x-com:layout: : skip layout-chunk
- p27:P2 {pc}तुष्टः अस्मि। : clean
- p27:P3 "अहं सूर्यकुमारम् : clean
- p27:P4 "किमर्थम् एवं : clean
- p27:P5 "सहोदरयोः ज्येष्ठं : clean
- p27:P6 "यक्ष! कनिष्ठम् : clean
- p27:P7 {pc}स्थिते यदि : clean
- p27:P8 "साधु! महानुभाव! : clean
- p27:P9 एतदनन्तरम् अपि : clean
- J1 p024:P6 {pb} -> p024:P7 {pc} (continues) : ok
- J2 p024:P9 {pb} -> p025:P2 {pc} (continues) : ok
- J3 p025:P4 {pb} -> p025:P5 {pc} (continues) : ok
- J4 p025:P12 {pb} -> p026:P2 fresh (clean break) : ok
- J5 p026:P8 {pb} -> p026:P9 {pc} (continues) : ok
- J6 p026:P14 {pb} -> p027:P2 {pc} (continues) : ok
- J7 p027:P6 {pb} -> p027:P7 {pc} (continues) : ok
- J8 p027:P9 {pb} -> END (clean break) : ok
