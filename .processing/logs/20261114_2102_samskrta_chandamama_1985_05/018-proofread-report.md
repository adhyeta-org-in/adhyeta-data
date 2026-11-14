# Proofread report: 1985_05 p018 (उत्तमः शिष्यः, pp. 18–20)

## Summary

Three findings: one print misprint corrected by verdict (ताहशी for तादृशी, high), two print punctuation gaps corrected by verdict (single-sort quote pair upgraded to doubles; one missing close quote supplied, both high). The Sanskrit orth scanner reports no hits on deblocked text. No candidates held: every Phase A residual was ruled from text. Loc below is story coordinates pNN:Pm (NN = scan sequence, Pm = lint chunk number) plus the first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p019:P5 चन्द्रसेनः विनयेन | `ताहशी विशेषश्रद्धा` | `तादृशी विशेषश्रद्धा` | OCR | error | high | `ताहशी` is not a Sanskrit word; `तादृशी ... श्रद्धा` ("such faith") fits the reply exactly; ह/द type confusion, verified ह in print at 5x |
| 2 | p020:P4 कथम्? इति | `'कथम्?'` in singles | `"कथम्?"` in doubles | STY | style | high | direct speech pinned by reporting verb plus sentence boundary; every other speech span in this story uses doubles |
| 3 | p020:P8 "तर्हि चन्द्रसेनस्य | `वा? इति पृष्टवान्` (no close mark) | `वा?" इति पृष्टवान्` | STY | style | high | open `"` has no mate in print; quote-plus-इति boundary pins the close position |

## Patterns

None (no repeats).

## Unverified

None — no candidates held.

## Coverage

p018:P1 : skip x-com-layout
p018:P2 उत्तमः शिष्यः : skip title
p018:P3 कोसलदेशस्य राजधान्याः : clean
p018:P4 आचार्यकमलानन्दस्य कश्चन : clean
p018:P5 शक्तिः सम्पादनीया। : clean
p018:P6 कमलानन्दस्य शिष्यगणे : clean
p018:P7 कालान्तरे उभौ : clean
p018:P8 एकदा कमलानन्दः : clean
p018:P9 आचार्यः प्रथमं : clean
p019:P1 : skip x-com-layout
p019:P2 तत्र अन्नदानं : clean
p019:P3 राजा चन्द्रसेनः : clean
p019:P4 आचार्यः चन्द्रसेनं : clean
p019:P5 चन्द्रसेनः विनयेन : F1
p019:P6 "तर्हि राज्ये : clean
p019:P7 "गुरुदेव! मदीयाः : clean
p019:P8 विशेषश्रद्धां प्रदर्शयन्ति। : clean
p019:P9 आचार्यः कमलानन्दः : clean
p019:P10 कमलानन्दः काञ्चित् : clean
p019:P11 "अस्माकं तु : clean
p019:P12 सूर्यसेनः अपि : clean
p020:P1 : skip x-com-layout
p020:P2 तदा आचार्यः : clean
p020:P3 "सूर्यसेनः एव : clean
p020:P4 कथम्? इति : F2
p020:P5 रामदासः उक्तवान् : clean
p020:P6 कमलानन्दः किञ्चित्कालं : clean
p020:P7 वन्तौ वा : clean
p020:P8 "तर्हि चन्द्रसेनस्य : F3
p020:P9 "आम्। प्रजानाम् : clean
J1 p018:P4 {wb} -> p018:P5 {pc} : ok (मानसिक + शक्तिः = मानसिकशक्तिः)
J2 p018:P9 {pb} -> p019:P2 fresh : ok (terminal ।, new scene)
J3 p019:P7 {pb} -> p019:P8 {pc} : ok (विषये + विशेषश्रद्धां, spaced join)
J4 p019:P12 {pb} -> p020:P2 fresh : ok (terminal ।, new para)
J5 p020:P6 {wb} -> p020:P7 {pc} : ok (ज्ञात + वन्तौ = ज्ञातवन्तौ)
J6 p020:P9 {pb} -> END : ok (terminal ।, story span ends)
