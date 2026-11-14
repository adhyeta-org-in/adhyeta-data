# Proofread report: 1984_06 p018 (START=18, END=20, 3 scans)

## Summary

One finding (STY error, high confidence), applied as a verdict block in the story file: the page-spanning speech `"अहं शीघ्रं गत्वा राजधान्यां प्रतीक्षां करोमि` opens with a double mark but print closes it with a single mark, so the close was corrected to `"`. No systematic problems. Orth scan (`scan.py orth` on deblocked text) reports zero findings. The full range (18.jpg-20.jpg) was transcribed from print in Phase A; nothing was left unchecked. Loc below is `pNN:Pm` (scan sequence + chunk number matching lint `P` numbers) plus the first two words as anchor, with the word index counted on the chunk from 1.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p20:P2 प्रतीक्षां करोमि (w2) | `करोमि'` | `करोमि"` | STY | error | high | spoken conversation takes doubles and the `"` mate is already on file at p19:P10, so the print single close is a sort mismatch at a sentence boundary pinned by `इति` |

## Patterns

None (single finding, no repeats).

## Unverified

None held. Checked-and-kept print readings (verified at 3x-6x in Phase A, no blocks emitted): `निर्धनिकानां` kept as the parallel formation to `धनिकानां` in the same sentence; `पादाभ्याम्` (p19) beside `पादाभ्यां` (p19/p20) kept as house spelling variants; `भीरुः` read with initial `भी` at 4x; open/joined sandhi (`मन्त्रस्य उपयोगः`, `तस्य सिद्धिप्रकारम्`) kept as house style, never normalized; one clearly detached mid-height dot between `नदीं` and `तीर्त्वा` (p19, verified at 6x) omitted as print noise; proper nouns (`मातङ्गः`, `सुभानुः`, `भैरवानन्दः`, `विरूपः`) spell consistently throughout.

## Coverage

p18:P1 : skip x-com-only (layout)
p18:P2 : skip title
p18:P3 विन्ध्यपर्वतस्य प्रान्ते : clean
p18:P4 विरूपः बुद्ध्या : clean
p18:P5 एकस्मिन् दिने : clean
p18:P6 पञ्चाशत्-वर्षेभ्यः पूर्वं : clean
p18:P7 भैरवानन्दस्य सुभानुः : clean
p18:P8 : skip metadata ({misc: भगिनी})
p19:P1 : skip x-com-only (layout)
p19:P2 न्तरम् एवम् : clean
p19:P3 गुरुणा उपदिष्टमन्त्रौ : clean
p19:P4 तदा मातङ्गः : clean
p19:P5 'अल्पकार्यार्थं मन्त्रशक्तिः : clean
p19:P6 तदा मातङ्गः : clean
p19:P7 न। भवान् : clean
p19:P8 किञ्चित्-समयानन्तरं सुभानुः : clean
p19:P9 अतः सः : clean
p19:P10 सुभानुः न : clean
p20:P1 : skip x-com-only (layout)
p20:P2 प्रतीक्षां करोमि : F1
p20:P3 मातङ्गः तदा : clean
p20:P4 तदा तस्मिन् : clean
p20:P5 भैरवानन्दः तं : clean
p20:P6 अनेकप्रकारां चिकित्सां : clean
p20:P7 गुरुः मातङ्गः : clean
p20:P8 कथां श्रुत्वा : clean
J1 p018:P4 -> p018:P5 fresh : ok
J2 p018:P7 -> p019:P2 {pc} : ok
J3 p019:P6 -> p019:P7 {pc} : ok
J4 p019:P10 -> p020:P2 {pc} : ok
J5 p020:P5 -> p020:P6 {pc} : ok
J6 p020:P8 -> END : ok
