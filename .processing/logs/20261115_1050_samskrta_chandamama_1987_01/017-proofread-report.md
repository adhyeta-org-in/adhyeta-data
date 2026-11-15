# Proofread report: 1987_01 p017 (महासाहसवीरः)

## Summary

Phase B (images closed) on `.processing/samskrta_chandamama/1987_01/p017.md`, eight page spans p017--p024. No Phase A `{sug-ins:}`/`{sug-del:}` candidates were inherited, so the suggestion queue was empty and none were held. The orth scanner (`scan.py orth` on deblocked text) returned zero findings. Three quote findings (one supplied opening mark, two nested-sort corrections covering four marks) were ruled from speech-vs-thought sense and added as verdict blocks; all are punctuation/readability (STY, style severity), high confidence. Loc below is `pNN:Pm:W` (scan sequence page, chunk number matching lint `P` numbers, word index on the deblocked chunk from 1) plus anchor words. Both gates pass: extract exit 0 (1 notes-only residual carried in and ruled here as F1) and proofread exit 0 with 0 errors and 0 notes. Print keeps open sandhi throughout (e.g. `सः प्रजारञ्जकः`, `शवम् अवतार्य`, `कश्चन राक्षसः`); per doctrine these stand as house-style variants and are not flagged. Checked print-faithful and kept as seen: `कुञ्चकासदृशः` (p017:P3, key-like epithet of Trivikrama; glyphs verified 2x in Phase A), trailing `भोः?` (p023:P5), and the `यत् ... इति` pleonasm (p024:P6).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p020:P4:5 किम् इदम् | `कृत्वा किम् इदम् ... गच्छेयुः" इति` | `{ins:"}` before `किम्` | STY | style | high | Print closes with `"` + `इति उक्तवान्` but opens with no mark; reporting verb plus iti-closure pins direct speech, so the opening mark is supplied for readability |
| 2 | p023:P6:30 पराक्रमेण माम् | `"पराक्रमेण ... स्थास्यामि" इति` (inside open `"` span) | inner pair to `'...'` | STY | style | high | Nested reported resolve (`निवेदितवान्` + `इति`) inside the rakshasa's open `"` speech; house nesting is DQ SQ ... SQ DQ, so inner sort corrected |
| 3 | p023:P6:52 भवान् भूलोकसञ्चारं | `"भवान् ... भवेत्" इति` (inside open `"` span) | inner pair to `'...'` | STY | style | high | Nested reported order (`उक्तवान्` + `इति`) inside the same open `"` span; inner sort corrected to match the `'`-nested judgment in p024:P6 |

## Patterns

Inner-speech doubles corrected to singles: 2 pairs, both in p023:P6 (F2 at w30/w45, F3 at w52/w58); the same nested function already prints as `'चतुरसेनः एव वीरतरः'` in p024:P6, confirming the house sort.

## Unverified

None. No candidate was held for human review.

## Coverage

p017:P1 {x-com:layout: : skip x-com-only layout chunk.
p017:P2 महासाहसवीरः : skip title chunk.
p017:P3 कथानां मञ्जूषासदृशस्य : clean.
p017:P4 {category: : skip metadata chunk (node content proofread: series label as printed).
p018:P1 {x-com:layout: : skip x-com-only layout chunk.
p018:P2 न्यूनः भवति" : clean.
p018:P3 पूर्वं कदाचित् : clean.
p018:P4 कुत्रापि युद्धभयस्य : clean.
p018:P5 युद्धसम्बन्ध-व्यायामादिकं परित्यजन्ति : clean.
p018:P6 स्पर्धायाः आरम्भार्थं : clean.
p018:P7 किन्तु सः : clean.
p018:P8 महाराजं दृष्ट्वा : clean.
p018:P9 गत्यन्तराभावात् चतुरसेनमहाराजः : clean.
p019:P1 {x-com:layout: : skip x-com-only layout chunk.
p019:P2 राक्षसस्य निर्गमनमनन्तरम् : clean.
p019:P3 एतत् उद्घोषणं : clean.
p019:P4 "अहं तूष्णीम् : clean.
p019:P5 "प्रभो, एषः : clean.
p019:P6 वारयतुं च, : clean.
p019:P7 चतुरसेनः खिन्नवदनः : clean.
p019:P8 परेद्युः पुनः : clean.
p019:P9 "चक्रवर्तिना मया : clean.
p020:P1 {x-com:layout: : skip x-com-only layout chunk.
p020:P2 अत्यन्तदुःखितः अभवत्। : clean.
p020:P3 चतुरसेनः राक्षसेन : clean.
p020:P4 साम्बकः अञ्जनद्वारा : F1.
p020:P5 स्वीयजीवनस्य आशाम् : clean.
p020:P6 तस्याम् एव : clean.
p020:P7 अनन्तरं पद्मचित्रसहितां : clean.
p020:P8 अपरेद्युः राक्षसः : clean.
p020:P9 सर्वे सचिवाः : clean.
p021:P1 {x-com:layout: : skip x-com-only layout chunk.
p021:P2 आरब्धवन्तः। इदानीं : clean.
p021:P3 "महान्तं बलशालिनम् : clean.
p021:P4 "तेन विषेण : clean.
p021:P5 राजवैद्यः स्मयमानः : clean.
p021:P6 तस्यां रात्रौ : clean.
p021:P7 परस्मिन् दिने : clean.
p021:P8 भक्षणसमये तयोः : clean.
p022:P1 {x-com:layout: : skip x-com-only layout chunk.
p022:P2 कालकूटविषम् अपि : clean.
p022:P3 किन्तु तेन : clean.
p022:P4 एतत् सर्वं : clean.
p022:P5 एकः राक्षसः : clean.
p022:P6 एतत् कार्यं : clean.
p022:P7 "एतं राक्षसं : clean.
p022:P8 परेद्युः राक्षसस्य : clean.
p023:P1 {x-com:layout: : skip x-com-only layout chunk.
p023:P2 चतुरसेनः राक्षसस्य : clean.
p023:P3 तेन प्रहारेण : clean.
p023:P4 तस्य वचनं : clean.
p023:P5 भोः? किमर्थम् : clean.
p023:P6 तदा राक्षसः : F2, F3.
p024:P1 {x-com:layout: : skip x-com-only layout chunk.
p024:P2 सञ्चारं कृतवान्। : clean.
p024:P3 इत्थं वेतालः : clean.
p024:P4 तदा त्रिविक्रमः : clean.
p024:P5 "पाताललोकस्य राजा : clean.
p024:P6 सैन्याधिपतिपदवीं दातुं : clean.
p024:P7 एवंरीत्या यदा : clean.
J1 p017:P3 {pb} -> p018:P2 {pc} (continues) : ok.
J2 p018:P4 {pb} -> p018:P5 {pc} (continues) : ok.
J3 p018:P9 {pb} -> p019:P2 fresh (clean break) : ok.
J4 p019:P5 {pb} -> p019:P6 {pc} (continues) : ok.
J5 p019:P9 {pb} -> p020:P2 {pc} (continues) : ok.
J6 p020:P3 {pb} -> p020:P4 fresh (clean break) : ok.
J7 p020:P9 {pb} -> p021:P2 {pc} (continues) : ok.
J8 p021:P5 {pb} -> p021:P6 fresh (clean break) : ok.
J9 p021:P8 {pb} -> p022:P2 {pc} (continues) : ok.
J10 p022:P4 {pb} -> p022:P5 {pc} (continues) : ok.
J11 p022:P8 {pb} -> p023:P2 {pc} (continues) : ok.
J12 p023:P4 {pb} -> p023:P5 {pc} (continues) : ok.
J13 p023:P6 {pb} -> p024:P2 {pc} (continues) : ok.
J14 p024:P5 {pb} -> p024:P6 {pc} (continues) : ok.
J15 p024:P7 {pb} -> END (clean break) : ok.
