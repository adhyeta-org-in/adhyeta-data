## Summary

Phase A transcribed scans 48-50 into 3 `{pgb}`-terminated spans with a 6-joint index; `lint.py --phase extract` passed (exit 0) before the phase boundary closed, and no scan was reopened afterwards. One Phase B mechanical fix was applied directly (Bengali-script contamination `समाधानেন` -> Devanagari `समाधानेन`, text-obvious, no glyph question). Phase B proofread gate passes clean (`lint.py --phase proofread`: 3 pages, 0 error paras, 0 story findings, exit 0); `scan.py orth` on deblocked text reports 0 hits across 28 lines. Findings table: 0 verified verdicts, 3 held candidates (F1 agreement, F2 compound sandhi, F3 agreement, all medium*). Print keeps open sandhi (`नैव इति`), symmetric double quotes for all reported speech and thought, and singles only for the shouted `'चोरः चोरः'`; all are kept as seen. Loc below is keyed `pNN:Pm:w` (NN = scan sequence 48 + `{pgb}`-span ordinal, Pm = lint chunk number, w = word in chunk from 1) plus the chunk's first two words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p049:P6:25 चोरः इदानीं | `आपत् क्षणमात्रेण निवृत्तः` | `निवृत्ता` | AGR | likely | medium* | feminine आपद् needs a feminine participle; no masculine subject is available (re-segmentation tested) |
| 2 | p050:P3:19 एकदा एषः | `स्वमत्यानुसारं` | `स्वमत्यनुसारं` | SND | likely | medium* | मति + अनुसार gives मत्यनुसार by yaṇ; the long आ leaves an ungrammatical compound |
| 3 | p050:P7:12 एतत् श्रुत्वा | `तदीयं पादौ` | `तदीयौ` | AGR | likely | medium* | dual पादौ needs a dual adjective; तदीयं cannot modify any other noun here (re-segmentation tested) |

## Unverified

F1 `निवृत्तः` (p049:P6:25) is held as `{sug-del:निवृत्तः}{sug-ins:निवृत्ता}`, not a verdict: the thought sentence `पर्वतोपमा आपत् क्षणमात्रेण निवृत्तः` has no masculine nominative for निवृत्तः to agree with, and आपद् is feminine, but with images closed the print-error vs author-slip question cannot be settled and Phase A left no flag, so no verdict block is made. What would settle it: a scan re-check of the त्तः/त्ता akṣara, or user acceptance of निवृत्ता. F2 `स्वमत्यानुसारं` (p050:P3:19) is held as `{sug-del:स्वमत्यानुसारं}{sug-ins:स्वमत्यनुसारं}`: the filed long आ may be a transcription slip for short त्य (मत्यनुसार), equally it may be the print's own spelling; a scan re-check of the त्य/त्या akṣara would settle which. F3 `तदीयं` (p050:P7:12) is held as `{sug-del:तदीयं}{sug-ins:तदीयौ}`: पादौ is unambiguously dual (twice in the line) while तदीयं is singular, but images are closed and Phase A left no flag, so it stays a candidate; a scan re-check of the यं/यौ akṣara would settle it.

## Coverage

p048:P1 {x-com:} : skip layout-only chunk
p048:P2 # चोरः : skip title
p048:P3 पूर्वम् इस्फहान् : clean
p048:P4 एकदा रात्रौ : clean
p048:P5 कमलुद्दीन् किञ्चिद्दूरं : clean
p048:P6 दिग्भ्रान्तः कमलुद्दीन् : clean
p048:P7 {pc}गृहीतवन्तः। : clean
p048:P8 कमलुद्दीन् स्वकीयं : clean
p048:P9 युवकः चोरः : clean
p048:P10 किन्तु नगररक्षकः : clean
p048:P11 एतेन चोरः : clean
p049:P1 {x-com:} : skip layout-only chunk
p049:P2 अग्रे धावन् : clean
p049:P3 यदा सः : clean
p049:P4 अल्पे एव : clean
p049:P5 चोरः गम्भीरः : clean
p049:P6 चोरः इदानीं : F1
p049:P7 अत्रान्तरे तद्गुहानिवासी : clean
p049:P8 {pc}आगतः। : clean
p049:P9 दयालुः धर्मगुरुः : clean
p049:P10 तद्दिनात् आरभ्य : clean
p050:P1 {x-com:} : skip layout-only chunk
p050:P2 चोरः एव : clean
p050:P3 एकदा एषः : F2
p050:P4 अत्रान्तरे कश्चित् : clean
p050:P5 {pc}निर्दयं : clean
p050:P6 "सहोदर! : clean
p050:P7 एतत् श्रुत्वा : F3
J1 p048:P6 {pb} -> p048:P7 {pc} : ok (continues दृढं गृहीतवन्तः)
J2 p048:P11 {pb} -> p049:P2 fresh : ok (clean page turn, escape to mountain flight)
J3 p049:P7 {pb} -> p049:P8 {pc} : ok (continues तत्र आगतः)
J4 p049:P10 {pb} -> p050:P2 fresh : ok (clean page turn, guru dies to successor)
J5 p050:P4 {pb} -> p050:P5 {pc} : ok (continues old guard's speech across columns)
J6 p050:P7 {pb} -> END : ok (range ends on last scan; reads as tale resolution)
