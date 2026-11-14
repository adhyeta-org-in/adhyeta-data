## Summary

Story `p033` (1985_03, scans 33-37, `सौजन्यम्`) proofread images-closed: 9 findings (6 `STY`/error quote-sort verdicts placed as blocks F1-F6, 3 held grammar observations without blocks F7-F9) and 3 held candidates (= F7-F9, all `*`). Extract gate passed with 0 error paras (2 story-note residuals carried forward and ruled here as F4/F6); proofread gate passes with 0 error paras and 0 story findings after the verdicts; `scan.py orth` on deblocked text reports no findings. The 4 Phase A `{sug-ins:'}` lone-single flags were all promoted to `{del}/{ins}` sort verdicts; no new word-glyph claims were invented (every block is a quote mark). Loc below is `pNN:Pm:word` (scan-sequence page + chunk matching lint `P` numbers, word counted on the raw chunk from 1) plus the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p034:P8:17 (ये निर्धनिकाः) | `'धर्मशालायाः … नास्ति'` | `"…"` (sort corrected via `{del:'}{ins:"}` at both ends) | STY | error | high | spoken pretext (`व्याजं वदन्तः`) takes era doubles; `इति`-closure pins both double marks |
| 2 | p035:P2:17 ({pc}चिन्तितवान् ---) | `'भवतः … प्रत्यागच्छेत्?'` | `"…"` (sort corrected via `{del:'}{ins:"}` at both ends) | STY | error | high | spoken question (`पृष्टवान्`) takes era doubles; both singles are dropped second strokes |
| 3 | p036:P5:1 (आं भोः) | `'आं भोः'` | `"आं भोः"` (sort corrected via `{del:'}{ins:"}` at both ends) | STY | error | high | spoken reply (`इति वदन्`) takes era doubles; both singles are dropped second strokes |
| 4 | p036:P7:1 (भगवतः मन्दिरं) | `भगवतः … भवेत्"` (no opening mark) | `{ins:"}` supplied at para start | STY | error | high | speech closed with `"` plus `उक्तवान् आगन्तुकः` pins a double open; none printed |
| 5 | p037:P3:9 (भीतः सदानन्दः) | `"मया … अपि"` | `'मया … अपि'` (sort corrected via `{del:"}{ins:'}` at both ends) | STY | error | high | interior monologue (`इति चिन्तितवान्`) takes singles; doubles are the wrong sort |
| 6 | p037:P8:46 (तदा रत्नाकरः) | `पृष्टवान्'` | `पृष्टवान्"` (sort corrected via `{del:'}{ins:"}`) | STY | error | high | speech opened with `"`; `इति`-closure pins the double close, single is a dropped second stroke |
| 7 | p034:P2:19 (सदानन्दः उच्चैः) | `भवता यस्मात् शकटात् अवतीर्णं` | `भवतः …` | KRK | likely | medium* | `अवतीर्णं` as verbal noun (`your alighting`) needs the genitive agent; no block (no Phase A flag, images closed) |
| 8 | p037:P4:8 (रत्नाकरस्य दर्शनेन) | `नेत्रभ्यां` | `नेत्राभ्याम्` | MRP | likely | low* | dual ablative/instrumental of an `a`-stem needs `-ाभ्याम्`; print-vs-transcription slip undecidable images-closed, so no block |
| 9 | p037:P4:17 (रत्नाकरस्य दर्शनेन) | `मां क्षाम्यतु` | `क्षम्यताम्` | MRP | likely | low* | `क्षाम्यतु` (grow thin) makes no sense as `forgive me`; exact intended form uncertain images-closed, so no block |

## Patterns

Speech printed in singles (F1, F2, F3, F6): 7 lone single strokes at 4 speech boundaries (pretext quote, spoken question, short reply, long-reply close) where the era standard expects doubles; all corrected to doubles. Complementary sort slips in the same story: one missing double open (F4) and one thought printed in doubles (F5).

## Unverified

U1 (= F7) `भवता` vs `भवतः`: settle by reopening scan 34 left column (`भवता यस्मात् शकटात् अवतीर्णं` line) — `ता` vs `तः` decides print-vs-transcription slip; confirms the genitive-with-verbal-noun construal. U2 (= F8) `नेत्रभ्यां`: settle by reopening scan 37 left column (`नेत्रभ्यां अश्रूणि निर्गतानि` line) — short `अ` vs `आ` in the dual ending. U3 (= F9) `क्षाम्यतु`: settle by reopening scan 37 left column (`मां क्षाम्यतु कृपया` line) — vowel length and ending decide print-vs-transcription slip, plus dictionary check of `क्षम्यताम्` vs `क्षमतु`.

## Coverage

p033:P1 {x-com:layout: 2col, : skip layout
p033:P2 # सौजन्यम् : skip title
p033:P3 सदानन्दः स्वभावेन : clean
p033:P4 मौनस्य आश्रयणे : clean
p033:P5 भूस्वामी सदानन्दस्य : clean
p033:P6 एकदा सदानन्दः : clean
p033:P7 आगन्तुकः सामान्यतः : clean
p033:P8 सदानन्दः तम् : clean
p033:P9 सः सदानन्दस्य : clean
p033:P10 {author: भामहः}{pgb} : skip metadata
p034:P1 {x-com:layout: 2col, : skip layout
p034:P2 सदानन्दः उच्चैः : F7
p034:P3 "भवतः ऊहा : clean
p034:P4 {pc}पादरक्षायुगलं दत्तवान्। : clean
p034:P5 "ओह्, एवं : clean
p034:P6 "अस्याम् अवस्थायाम् : clean
p034:P7 यात्रिकाणां वसतिसौकर्यार्थं : clean
p034:P8 ये निर्धनिकाः : F1
p035:P1 {x-com:layout: 2col, : skip layout
p035:P2 {pc}चिन्तितवान् --- : F2
p035:P3 "अहं निश्चयेन : clean
p035:P4 सदानन्दः पुनः : clean
p035:P5 एतत् श्रुत्वा : clean
p035:P6 एतं प्रश्नं : clean
p035:P7 "सः मदीयानि : clean
p035:P8 "तर्हि किमर्थं : clean
p035:P9 "शृणोतु मित्र! : clean
p036:P1 {x-com:layout: art : skip layout
p036:P2 {pc}गीतद्वयं गातव्यम्। : clean
p036:P3 आगन्तुकः किञ्चित्कालं : clean
p036:P4 "अहं कदापि : clean
p036:P5 आं भोः : F3
p036:P6 "आगन्तुकस्य परिचयः : clean
p036:P7 भगवतः मन्दिरं : F4
p036:P8 "धर्मशालायाः सर्वोऽपि : clean
p036:P9 "के ते : clean
p037:P1 {x-com:layout: 2col, : skip layout
p037:P2 भूस्वामी --- : clean
p037:P3 भीतः सदानन्दः : F5
p037:P4 रत्नाकरस्य दर्शनेन : F8, F9
p037:P5 "किमर्थं क्षमा?" : clean
p037:P6 {pc}कर्तुम् इच्छति : clean
p037:P7 इदानीं सदानन्दस्य : clean
p037:P8 तदा रत्नाकरः : F6
p037:P9 एतेन प्रसङ्गेन : clean
J1 p033:P5 {pb} -> p033:P6 fresh : ok
J2 p033:P9 {pb} -> p034:P2 fresh : ok
J3 p034:P3 {pb} -> p034:P4 {pc} : ok
J4 p034:P8 {pb} -> p035:P2 {pc} : ok
J5 p035:P5 {pb} -> p035:P6 fresh : ok
J6 p035:P9 {pb} -> p036:P2 {pc} : ok
J7 p036:P6 {pb} -> p036:P7 fresh : ok
J8 p036:P9 {pb} -> p037:P2 fresh : ok
J9 p037:P5 {pb} -> p037:P6 {pc} : ok
J10 p037:P9 {pb} -> END : ok
