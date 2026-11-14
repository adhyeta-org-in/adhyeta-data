# Proofread report: 1985_01 p001 (pages 1-4), story प्रतिभाप्रदर्शनम्

## Summary

Three findings, all high confidence, all applied as verdict blocks in the story file: two dropped second-strokes of double quote marks (minister's speeches, one open and one close) and one dropped ā-mātrā (निरीक्षमणः for निरीक्षमाणः). No held candidates. Proper nouns are consistent throughout (मुकुन्दवर्मा, ललितसेनः/ललितसेनराजः, विशाखः, प्लवङ्ग). Print keeps open sandhi at many word boundaries and an ASCII period once (महाराजस्य.); both verified against the scans at 3x and kept as house print. The footer 'श्रीमाता' (single quotes in print) is captured as {author: श्रीमाता}.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p02:P3 "सत्यम्, एतं" w21 | `जानीयुः'` | `जानीयुः"` | OCR | error | high | Speech opened with double mark so the close must be double; print dropped the second stroke |
| F2 | p03:P4 "ललितसेनराजः आश्चर्येण" w9 | `विनयेन 'प्रभो,` | `विनयेन "प्रभो,` | OCR | error | high | Spoken report needs era-double marks and the verified close is double; print dropped the second stroke of the open |
| F3 | p03:P5 "शङ्का अस्माकं" w37 | `निरीक्षमणः` | `निरीक्षमाणः` | SPL | error | high | निरीक्षमणः is not a word; the awaiting-time participle agreeing with the speaker is निरीक्षमाणः |

## Patterns

None (single instances only; no repeats to fold).

## Unverified

None held. Every inherited Phase A residual was ruled from text: the two unbalanced print quote pairs are corrected above (sense plus reporting verbs pin the sorts), and the flagged निरीक्षमणः is corrected above (only निरीक्षमाणः parses).

## Coverage

p01:P3 "पुरा ललितसेनराजः" : clean
p01:P4 "एकदा सायङ्काले" : clean
p01:P5 "अनन्तरम् महाराजस्य" : clean
p01:P6 "एकैकाम् आशुकवितां" : clean
p01:P7 "ललितसेनः असहनां" : clean
p01:P8 "तेषां गमनानन्तरं" : clean
p01:P9 "महाराजस्य वचनानि" : clean
p01:P10 "किञ्चित्कालानन्तरं पुनः" : clean
p02:P2 "अलङ्कर्तुं योग्यान्" : clean
p02:P3 "सत्यम्, एतं" : F1
p02:P4 "सचिवस्य वचने" : clean
p02:P5 "पञ्चकविरत्नानां पक्षपातरहितगुणस्य" : clean
p02:P6 "मन्त्री मुकुन्दवर्मा" : clean
p02:P7 "ललितसेनः तीक्ष्णदृष्ट्या" : clean
p02:P8 "कतिपयदिनानन्तरं विशाखः" : clean
p02:P9 "ललितसेनराजः विशाखकवेः" : clean
p03:P2 "कथं आगच्छति" : clean
p03:P3 "मन्त्री विशाखं" : clean
p03:P4 "ललितसेनराजः आश्चर्येण" : F2
p03:P5 "शङ्का अस्माकं" : F3
p03:P6 "कथं कथम्?" : clean
p03:P7 "मन्त्री विशाखं" : clean
p04:P2 "आस्थानम् अलङ्कर्तुम्" : clean
p04:P3 "एवं तर्हि" : clean
p04:P4 "तत्क्षणमेव विशाखः" : clean
p04:P5 "महाराजः महता" : clean
p04:P6 "सत्यं प्रभो!" : clean
p04:P7 "ललितसेनः पञ्चकविरत्नानां" : clean
J1 p001:P5 {pb} -> p001:P6 {pc} : ok
J2 p001:P10 {pb} -> p002:P2 {pc} : ok
J3 p002:P4 {pb} -> p002:P5 {pc} : ok
J4 p002:P9 {pb} -> p003:P2 {pc} : ok
J5 p003:P4 {pb} -> p003:P5 {pc} : ok
J6 p003:P7 {pb} -> p004:P2 {pc} : ok
J7 p004:P4 {pb} -> p004:P5 fresh : ok
J8 p004:P7 {pb} -> END : ok
