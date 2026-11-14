# Proofread report — p022 (1985_02, RUN 20261114_1849_samskrta_chandamama_1985_02)

## Summary
Range scans 22.jpg–24.jpg; complete story `पर्वतसदृशं धैर्यम्` in 3 page spans (p022–p024), 6 joints, closing `{pb}{pgb}` bare. Extract gate and proofread gate both pass; `scan.py orth` on deblocked text reports 0 findings. Four findings: 1 SPL error, 1 CNS likely, 2 STY quote-sort corrections (both single-open-for-speech upgraded to double). Systematic issue is single-stroke opens where the era standard expects doubles (2x, corrected). No passages left unchecked; text is print-faithful transcription with verdict blocks, not OCR output.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p022:P5:5 तान् दृष्ट्वा | `'अस्माकं` | `"अस्माकं` | STY | style | high | spoken report with `इति उक्तवान्` takes doubles; print single open vs double close mismatched |
| 2 | p023:P2:14 स्वीयं धनं | `'रे!` | `"रे!` | STY | style | high | loud spoken address with `तीव्रस्वरेण ... इति उक्त्वा` takes doubles; print single open vs double close mismatched |
| 3 | p023:P2:33 स्वीयं धनं | `भूस्वामीना` | `भूस्वामिना` | SPL | error | high | instrumental sg of `-इन्` stem is `-िना`; all other tokens use short `ि` |
| 4 | p023:P2:35 स्वीयं धनं | `गुप्तचरः` | `गूढचरः` | CNS | likely | high | same referent spelled `गूढचरः` 5x elsewhere including the next line; unify spelling |

## Patterns

| Pattern | Count | Examples |
|---|---|---|
| single-stroke open `'` where era speech standard expects `"` | 2 | p022:P5 तान् दृष्ट्वा; p023:P2 स्वीयं धनं |

## Unverified

None — nothing held for the user; all findings high confidence from grammar, era quote standard, and in-story consistency.

## Coverage

p022:P1 {x-com:layout: 2col, : skip x-com-only
p022:P2 # पर्वतसदृशं : skip title
p022:P3 रात्रौ द्वितीययामः : clean
p022:P4 चत्वारः अपि : clean
p022:P5 तान् दृष्ट्वा : F1
p022:P6 अन्यत् किमपि : clean
p022:P7 तस्य वचनसमनन्तरम् : clean
p022:P8 त्रयः अपि : clean
p022:P9 {category: श्रीमाता} : skip metadata
p023:P1 {x-com:layout: 2col, : skip x-com-only
p023:P2 स्वीयं धनं : F2, F3, F4
p023:P3 'भूस्वामिनः गूढचारः' : clean
p023:P4 यावत् धैर्यम् : clean
p023:P5 मार्गे पथिकेषु : clean
p024:P1 {x-com:layout: 2col, : skip x-com-only
p024:P2 लभ्यते स्म। : clean
p024:P3 विक्रमपुरं प्राप्तम्। : clean
p024:P4 ग्रामाधिकारिणः वचनं : clean
p024:P5 चेत् अस्माकं : clean
p024:P6 तेषां वचनं : clean
p024:P7 शकटचालकः प्रवृत्तं : clean
p024:P8 ग्रामाधिकारी शकटचालकं : clean
J1 p022:P5 {pb} -> p022:P6 {pc} : F1
J2 p022:P8 {pb} -> p023:P2 {pc} : ok
J3 p023:P3 {pb} -> p023:P4 {pc} : ok
J4 p023:P5 {pb} -> p024:P2 {pc} : ok
J5 p024:P4 {pb} -> p024:P5 {pc} : ok
J6 p024:P8 {pb} -> END : ok
