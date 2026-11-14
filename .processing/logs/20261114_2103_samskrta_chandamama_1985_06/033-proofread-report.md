# Proofread report: samskrta_chandamama 1985_06, p033 (scan pages 33–38)

## Summary

Story `नर्तनसमर्थः अजः` transcribed from pages 33–38 and proofread with images closed. Three findings, all `STY` style readability corrections promoting single-quoted spoken utterances to the era double-quote sort; no word changes. Systematic issue: the print marks three spoken speeches with single quotes (`'तस्य मूल्यं...'`, `'अर्धं भाटकम्...'`, `'भोजनतः पूर्वं...'`) where 1980s house uses doubles for reported speech, while thought singles are kept as seen. `scan.py orth` on deblocked text reports zero hits; the text is human transcription, not OCR output. Proper nouns (`मुकुन्दः`, `भूपतिः`, `गजपतिः`, `नागपुरम्`) spell consistently throughout. Print quirks kept as seen per fidelity: `समुद्रं ग्रामं` (p033), open sandhi (`तत् पूर्णतया`, `यत् धनम्`), `विक्रमणं` for the sale (p034), `कश्चित् अजं` (p035). Loc below is `pNN:Pm:word` (words counted on the chunk from 1) with the anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p034:P2:17 `वणिक् तस्य मूल्यं` | `वणिक् 'तस्य मूल्यं दशरूप्यकात्मकम्' इति` | `वणिक् "तस्य मूल्यं दशरूप्यकात्मकम्" इति` | STY | style | high | reporting verb `उक्तवान्` plus complete utterance pins spoken speech, which takes doubles |
| 2 | p037:P2:30 `शाकटिकः अर्धं भाटकम्` | `शाकटिकः 'अर्धं भाटकम् अग्रिमधनरूपेण दातव्यम्' इति` | `शाकटिकः "अर्धं भाटकम् अग्रिमधनरूपेण दातव्यम्" इति` | STY | style | high | reporting verb `उक्तवान्` plus complete demand pins spoken speech, which takes doubles |
| 3 | p038:P3:9 `आगतवन्तः। भोजनतः पूर्वं` | `'भोजनतः पूर्वं कश्चन अपूर्वः मनोरञ्जनकार्यक्रमः व्यवस्थापितः अस्ति' इति` | `"भोजनतः पूर्वं कश्चन अपूर्वः मनोरञ्जनकार्यक्रमः व्यवस्थापितः अस्ति" इति` | STY | style | high | reporting verb `सूचितवान्` plus complete announcement pins spoken speech, which takes doubles |

## Patterns

Single-quoted speech where doubles are expected: 3x (F1 p034:P2, F2 p037:P2, F3 p038:P3). Each is a top-level spoken utterance with `उक्तवान्`/`सूचितवान्` plus `इति`; thought singles (`'इतः परम्...'`, `'अहम्...'`, `'नटः...'`, `'कथम्...'`, `'एतदतिरिच्य...'`, `'अजे...'`) are kept as print.

## Unverified

None held. No inherited `{sug-ins:}`/`{sug-del:}` queue existed in Phase A; no new glyph claims were invented in Phase B.

## Coverage

- p033:P1 `{x-com:layout:` : skip layout declaration
- p033:P2 `# नर्तनसमर्थः` : skip title heading
- p033:P3 `नागपुरे मुकुन्दः` : clean
- p033:P4 `क्रमशः नागपुरीयाः` : clean
- p033:P5 `मुकुन्दः नागपुरतः` : clean (open joins across columns via J3, residual verified)
- p033:P6 `न प्रत्यर्पितं` : clean (close pairs with p033:P5 open via J3)
- p033:P7 `अहम् अतीव` : clean (thought single kept as print)
- p033:P8 `भूपतिः नागपुरम्` : clean
- p033:P9 `भूपतिः विपणिं` : clean
- p033:P10 `{author: सुभद्रा}` : skip footer metadata
- p034:P1 `{x-com:layout:` : skip layout declaration
- p034:P2 `एकस्य अजस्य` : F1
- p034:P3 `किम् एषः` : clean
- p034:P4 `तदा वणिक्` : clean
- p034:P5 `गजपतिः किं` : clean
- p034:P6 `विपणेः पार्श्वे` : clean (open pairs across columns via J12, residual verified)
- p034:P7 `शिबिरम् अस्ति।` : clean (close pairs with p034:P6 open via J12)
- p034:P8 `भूपतिः गजपतिसमीपं` : clean
- p034:P9 `भूपतिं परीक्षादृष्ट्या` : clean
- p034:P10 `नटः अजः` : clean (thought single kept as print)
- p034:P11 `सः अजः` : clean
- p034:P12 `एतत्सर्वं दृष्ट्वा` : clean
- p034:P13 `वस्तुतः एतस्य` : clean
- p034:P14 `अश्रुतपूर्वा वार्ता` : clean
- p035:P1 `{x-com:layout:` : skip layout declaration
- p035:P2 `पृष्टवान् भूपतिः।` : clean (close pairs with p034:P14 open via J20)
- p035:P3 `एतस्य मूल्यं` : clean
- p035:P4 `गायनसमर्थः अजः!` : clean
- p035:P5 `अहम् असत्यं` : clean
- p035:P6 `भूपतिः शतं` : clean
- p035:P7 `अजः मनुष्यस्वरेण` : clean (thought single `कथम्` kept as print)
- p035:P8 `गायनस्य अन्ते` : clean
- p035:P9 `पञ्चसहस्रं रूप्यकाणि` : clean
- p036:P1 `{x-com:layout:` : skip layout declaration
- p036:P2 `पञ्चसहस्रं रूप्यकाणि!` : clean
- p036:P3 `किमर्थम्? भवान्` : clean
- p036:P4 `तादृशः अपि` : clean
- p036:P5 `किमर्थं न?` : clean
- p036:P6 `भूपतिः नर्तनगायनसमर्थम्` : clean
- p036:P7 `तस्य अजस्य` : clean (thought single `एतदतिरिच्य` kept as print)
- p036:P8 `एतस्य अजस्य` : clean
- p036:P9 `एतत् मूल्यं` : clean
- p036:P10 `भूपतिः चिन्तितवान्` : clean
- p036:P11 `एवं चिन्तयित्वा` : clean
- p037:P1 `{x-com:layout:` : skip layout declaration
- p037:P2 `चर्चाविचर्चा प्रवृत्ता।` : F2
- p037:P3 `इदानीं किं` : clean
- p037:P4 `अन्ते अनन्योपायः` : clean
- p037:P5 `एवं वा?` : clean (open pairs across columns via J42, residual verified)
- p037:P6 `भूस्वामी सचिवः` : clean (close pairs with p037:P5 open via J42)
- p037:P7 `एतत् वचनं` : clean
- p037:P8 `पुत्रस्य मुखात्` : clean (word-break `उत्साह{wb}` continues via J45, residual verified)
- p038:P1 `{x-com:layout:` : skip layout declaration
- p038:P2 `पूर्णवचनानि श्रुत्वा` : clean (close joins solid via J45; thought single `अजे काऽपि` kept as print)
- p038:P3 `अपरस्मिन् दिने` : F3
- p038:P4 `द्वित्राः निमेषाः` : clean
- p038:P5 `अपमानेन लज्जितः` : clean
- p038:P6 `हसितवन्तः।` : clean (close pairs with p038:P5 open via J49)
- p038:P7 `भूस्वामी भूपतिं` : clean
- p038:P8 `आम्! अहं` : clean
- p038:P9 `सः जन्मना` : clean
- p038:P10 `जातां महावञ्चनां` : clean
- p038:P11 `तद्दिनस्य भोजनकूटार्थम्` : clean
- J1 p033:P3 {pb} -> p033:P4 fresh : ok (complete sentence, clean column break)
- J2 p033:P4 {pb} -> p033:P5 fresh : ok (complete sentence, clean column break)
- J3 p033:P5 {pb} -> p033:P6 {pc} : ok (`यैः ऋणं न प्रत्यर्पितं` joins across columns)
- J4 p033:P6 {pb} -> p033:P7 fresh : ok (complete sentence, clean column break)
- J5 p033:P7 {pb} -> p033:P8 fresh : ok (complete sentence, clean column break)
- J6 p033:P8 {pb} -> p033:P9 fresh : ok (complete sentence, clean column break)
- J7 p033:P9 {pb} -> p034:P2 {pc} : ok (`तेषु दिनेषु एकस्य अजस्य मूल्यं` joins across pages)
- J8 p034:P2 {pb} -> p034:P3 fresh : ok (complete sentence, clean column break)
- J9 p034:P3 {pb} -> p034:P4 fresh : ok (complete sentence, clean column break)
- J10 p034:P4 {pb} -> p034:P5 fresh : ok (complete sentence, clean column break)
- J11 p034:P5 {pb} -> p034:P6 fresh : ok (complete sentence, clean column break)
- J12 p034:P6 {pb} -> p034:P7 {pc} : ok (`तीरे तस्य शिबिरम् अस्ति` joins across columns)
- J13 p034:P7 {pb} -> p034:P8 fresh : ok (complete sentence, clean column break)
- J14 p034:P8 {pb} -> p034:P9 fresh : ok (complete sentence, clean column break)
- J15 p034:P9 {pb} -> p034:P10 fresh : ok (complete sentence, clean column break)
- J16 p034:P10 {pb} -> p034:P11 fresh : ok (complete sentence, clean column break)
- J17 p034:P11 {pb} -> p034:P12 fresh : ok (complete sentence, clean column break)
- J18 p034:P12 {pb} -> p034:P13 fresh : ok (complete sentence, clean column break)
- J19 p034:P13 {pb} -> p034:P14 fresh : ok (complete sentence, clean column break)
- J20 p034:P14 {pb} -> p035:P2 {pc} : ok (`इति आश्चर्येण पृष्टवान् भूपतिः` joins across pages)
- J21 p035:P2 {pb} -> p035:P3 fresh : ok (complete sentence, clean column break)
- J22 p035:P3 {pb} -> p035:P4 fresh : ok (complete sentence, clean column break)
- J23 p035:P4 {pb} -> p035:P5 fresh : ok (complete sentence, clean column break)
- J24 p035:P5 {pb} -> p035:P6 fresh : ok (complete sentence, clean column break)
- J25 p035:P6 {pb} -> p035:P7 fresh : ok (complete sentence, clean column break)
- J26 p035:P7 {pb} -> p035:P8 fresh : ok (complete sentence, clean column break)
- J27 p035:P8 {pb} -> p035:P9 fresh : ok (complete sentence, clean column break)
- J28 p035:P9 {pb} -> p036:P2 fresh : ok (complete sentence, clean column break)
- J29 p036:P2 {pb} -> p036:P3 fresh : ok (complete sentence, clean column break)
- J30 p036:P3 {pb} -> p036:P4 fresh : ok (complete sentence, clean column break)
- J31 p036:P4 {pb} -> p036:P5 fresh : ok (complete sentence, clean column break)
- J32 p036:P5 {pb} -> p036:P6 fresh : ok (complete sentence, clean column break)
- J33 p036:P6 {pb} -> p036:P7 fresh : ok (`अन्यम् अजम् आनीतवान्। तस्य अजस्य शरीरं` clean column turn)
- J34 p036:P7 {pb} -> p036:P8 fresh : ok (complete sentence, clean column break)
- J35 p036:P8 {pb} -> p036:P9 fresh : ok (complete sentence, clean column break)
- J36 p036:P9 {pb} -> p036:P10 fresh : ok (complete sentence, clean column break)
- J37 p036:P10 {pb} -> p036:P11 fresh : ok (complete sentence, clean column break)
- J38 p036:P11 {pb} -> p037:P2 {pc} : ok (`बहुधा चर्चाविचर्चा प्रवृत्ता` joins across pages)
- J39 p037:P2 {pb} -> p037:P3 fresh : ok (complete sentence, clean column break)
- J40 p037:P3 {pb} -> p037:P4 fresh : ok (complete sentence, clean column break)
- J41 p037:P4 {pb} -> p037:P5 fresh : ok (complete sentence, clean column break)
- J42 p037:P5 {pb} -> p037:P6 {pc} : ok (`मया भूस्वामी सचिवः च आहूतौ` joins across columns)
- J43 p037:P6 {pb} -> p037:P7 fresh : ok (complete sentence, clean column break)
- J44 p037:P7 {pb} -> p037:P8 fresh : ok (complete sentence, clean column break)
- J45 p037:P8 {wb} -> p038:P2 {pc} : ok (`उत्साहपूर्णवचनानि` solid word join across pages)
- J46 p038:P2 {pb} -> p038:P3 fresh : ok (complete sentence, clean column break)
- J47 p038:P3 {pb} -> p038:P4 fresh : ok (complete sentence, clean column break)
- J48 p038:P4 {pb} -> p038:P5 fresh : ok (complete sentence, clean column break)
- J49 p038:P5 {pb} -> p038:P6 {pc} : ok (`उच्चैः हसितवन्तः` joins across columns)
- J50 p038:P6 {pb} -> p038:P7 fresh : ok (complete sentence, clean column break)
- J51 p038:P7 {pb} -> p038:P8 fresh : ok (complete sentence, clean column break)
- J52 p038:P8 {pb} -> p038:P9 fresh : ok (complete sentence, clean column break)
- J53 p038:P9 {pb} -> p038:P10 fresh : ok (complete sentence, clean column break)
- J54 p038:P10 {pb} -> p038:P11 fresh : ok (complete sentence, clean column break)
- J55 p038:P11 {pb} -> END : ok (story closes complete, no folio printed)
