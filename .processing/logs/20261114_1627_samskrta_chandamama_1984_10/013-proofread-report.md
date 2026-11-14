# Proofread report: 1984_10 p013 `भिक्षुकस्य भाग्यम्` (वेतालकथा)

## Summary

Eye-transcribed print text (not OCR); orth scanner clean (0 hits); proofread gate green. 7 findings, all print-punctuation quote gaps at multi-para speech boundaries (6 supplied `"` via `{ins:"}`, 1 stray `"` removed via `{del:"}`); no word, sandhi, morphology, or syntax verdicts and no held candidates. Loc below is story coordinates `pNN:Pm` (NN = scan sequence from `p013.md` plus `{pgb}`-span ordinal, Pm = lint chunk number) plus the chunk's first two words as anchor, words counted on the deblocked chunk from 1. Print variants kept as seen (`त्रिविक्रमः`/`विक्रमेण`, `क्षाम्यतु`, `गच्छावः`, `मिलामः`, `भवतोः`, `दिवङ्गतः`, `वणिक्`, `बलयुतं`); no passage left unread.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p014:P2 [णार्थम् अहम्] after w12 | `परिहृतः भवेत्।` (वेताल introduction speech never closed) | `परिहृतः भवेत्।{ins:"}` | STY | likely | high | print drops the close at a speech-to-tale boundary; next chunk opens a new `"` tale, so a `"` cannot follow without this close |
| F2 | p014:P3 ["एकस्मिन् ग्रामे] after w34 | `तस्य जीवनं प्रचलति स्म।` (tale-opening `"` never closed) | `तस्य जीवनं प्रचलति स्म।{ins:"}` | STY | likely | high | tale continues unquoted in print; per-para pair rule pins the close at this para end |
| F3 | p019:P7 [मम भाग्ये] after w17 | `प्रसिद्धः धनिकः सञ्जातः च।` (भिक्षुक speech open since p019:P6, para ends clean) | `प्रसिद्धः धनिकः सञ्जातः च।{ins:"}` | STY | likely | high | next chunk is a fresh para of the same speech, so each para carries its own pair |
| F4 | p019:P8 [ललाटे लिखितं] before w1 | `ललाटे लिखितं...` (same speech continues, print's close `"` stands at its end) | `{ins:"}ललाटे लिखितं...` | STY | likely | high | mates the print close at `शक्नोति" इति`; speech-vs-thought sense (भिक्षुक on भाग्य) is continuous |
| F5 | p020:P4 [वेतालः एवं] after w29 | `एतत् द्वयम् अपि दौर्भाग्यवशात् जातम्।` (वेताल question speech open, para ends clean) | `एतत् द्वयम् अपि दौर्भाग्यवशात् जातम्।{ins:"}` | STY | likely | high | next chunk continues the same speech fresh, so each para carries its own pair |
| F6 | p020:P5 [किन्तु सर्वम्] before w1 | `किन्तु सर्वम् अपि...` (same speech, print's close `"` stands at p020:P6 end) | `{ins:"}किन्तु सर्वम् अपि...` | STY | likely | high | mates the print close at `भग्नं भवेत्।"`; `{pb}`/`{pc}` joint to p020:P6 stays unforced |
| F7 | p020:P7 ["भिक्षुकः रमणेन] after w45 | `पीडयति'" इति` (inner `'यदि...` correctly closed, surplus print `"` doubles the close) | `पीडयति'{del:"} इति` | STY | likely | high | nesting admits only DQ SQ ... SQ DQ; outer `"` pair (`"भिक्षुकः...न गतवान्।"`) is complete without it, so the middle `"` is stray |

## Patterns

- Print drops quote marks at multi-para speech boundaries throughout (7 positions, F1--F7): speeches open with `"` but individual paras are left unclosed/unopened; all repaired with `{ins:"}`/`{del:"}` per the readability rule while print wording stands byte-identical.

## Unverified

None. Every candidate is a mechanical quote-balance verdict pinned by nesting plus speech sense; no word-level holds.

## Coverage

p013:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p013:P2 भिक्षुकस्य भाग्यम् : skip title heading
p013:P3 सा च : clean
p013:P4 सः पुनः : F1
p013:P5 skip category-plus-pgb metadata chunk : skip metadata, no story text
p014:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p014:P2 णार्थम् अहम् : F1
p014:P3 "एकस्मिन् ग्रामे : F2
p014:P4 एकदा पार्श्वग्रामे : clean
p014:P5 तदा कश्चित् : clean
p014:P6 न दृष्टवान् : clean
p014:P7 "न भोः : clean
p014:P8 अपरिचितस्य साहाय्येन : clean
p014:P9 "भवतः वचनं : clean
p014:P10 "मदीयम् अर्धम् : clean
p014:P11 "अहं कस्यापि : clean
p014:P12 skip bare-pgb page-end chunk : skip page end, no story text
p015:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p015:P2 आगतवान्।" : clean
p015:P3 "भवतः माता : clean
p015:P4 "मातापितरौ बाल्ये : clean
p015:P5 "भवता सूचितस्य : clean
p015:P6 "चिरं जीवतु : clean
p015:P7 "मम नाम : clean
p015:P8 भिक्षुकस्य प्रीतिपूर्वकं : clean
p015:P9 रमणः प्रतिदिनं : clean
p015:P10 सायं रमणः : clean
p015:P11 एकदा मध्याह्नसमयः। : clean
p015:P12 "स्यूते खाद्यवस्तूनि : clean
p015:P13 अरे! किम् : clean
p015:P14 "धनिकः प्रमादवशात् : clean
p015:P15 skip bare-pgb page-end chunk : skip page end, no story text
p016:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p016:P2 धनिकः उक्तवान् : clean
p016:P3 रमणः इदानीम् : clean
p016:P4 "कदाचित् वाणिज्ये : clean
p016:P5 इति उक्त्वा : clean
p016:P6 एतदनन्तरं रमणस्य : clean
p016:P7 रमणः नगरमार्गम् : clean
p016:P8 सुलोचना बुद्धिमती : clean
p016:P9 एतत् श्रुत्वा : clean
p016:P10 सायङ्काले रमणः : clean
p016:P11 skip bare-pgb page-end chunk : skip page end, no story text
p017:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p017:P2 सुलोचनायाः वचनेन : clean
p017:P3 रमणस्य मौनं : clean
p017:P4 पत्न्याः समीपे : clean
p017:P5 तदा सुलोचना : clean
p017:P6 समालोचनया कोऽपि : clean
p017:P7 सुलोचनायाः वचनेन : clean
p017:P8 सुलोचना चिन्तितवती : clean
p017:P9 skip bare-pgb page-end chunk : skip page end, no story text
p018:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p018:P2 एव करणीयम् : clean
p018:P3 "सः अत्र : clean
p018:P4 "तदा अहम् : clean
p018:P5 रमणः झटिति : clean
p018:P6 ग्रामप्राप्तौ रात्रिसमयः : clean
p018:P7 तत्र भिक्षुकः : clean
p018:P8 "किं पश्यति : clean
p018:P9 रमणः वेगेन : clean
p018:P10 सः ग्रामीणः : clean
p018:P11 रमणः शिवालयस्य : clean
p018:P12 अल्पे एव : clean
p018:P13 skip bare-pgb page-end chunk : skip page end, no story text
p019:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p019:P2 वेदनाम् असहमानः : clean
p019:P3 'इतः गमने : clean
p019:P4 भिक्षुकः प्रथमं : clean
p019:P5 "वदतु तात! : clean
p019:P6 तदा भिक्षुकः : F3
p019:P7 मम भाग्ये : F3
p019:P8 ललाटे लिखितं : F4
p019:P9 रमणः किमपि : clean
p019:P10 प्रातःकाले दैन्यं : clean
p019:P11 skip bare-pgb page-end chunk : skip page end, no story text
p020:P1 skip x-com-layout-only chunk : skip layout declaration, no story text
p020:P2 भिक्षुकः निराकृतिं : clean
p020:P3 "तात! इतःपरं : clean
p020:P4 वेतालः एवं : F5
p020:P5 किन्तु सर्वम् : F6
p020:P6 कस्य दोषः? : F6
p020:P7 "भिक्षुकः रमणेन : F7
p020:P8 भिक्षुकः रमणं : clean
p020:P9 एवं वदता : clean
p020:P10 skip bare-pgb story-end chunk : skip page end, no story text
J1 p013:P4 {wb} -> p014:P2 {pc} (continues) : ok (उदाहर + णार्थम् = उदाहरणार्थम्, word join verified both sides)
J2 p014:P5 {pb} -> p014:P6 {pc} (continues) : ok (कुल्यां + न दृष्टवान्, column turn inside one speech)
J3 p014:P11 {pb} -> p015:P2 {pc} (continues) : ok (समीपम् + आगतवान्।", page turn inside one speech)
J4 p015:P9 {pb} -> p015:P10 {pc} (continues) : ok (column turn inside routine narration, fresh sentence but same block)
J5 p015:P14 {pb} -> p016:P2 fresh (clean break) : ok (रमण speech ends, धनिक replies)
J6 p016:P4 {pb} -> p016:P5 {pc} (continues) : ok (किल?" + इति उक्त्वा, reporting clause continues)
J7 p016:P10 {pb} -> p017:P2 fresh (clean break) : ok (निवेदितवती।, scene moves to सुलोचना dialogue)
J8 p017:P5 {pb} -> p017:P6 {pc} (continues) : ok (सह + समालोचनया, column turn inside one speech)
J9 p017:P8 {pb} -> p018:P2 {pc} (continues) : ok (पूर्वम् + एव, page turn inside one speech)
J10 p018:P6 {pb} -> p018:P7 {pc} (continues) : ok (किन्तु + तत्र, column turn mid-sentence)
J11 p018:P12 {pb} -> p019:P2 fresh (clean break) : ok (चौर्यं speech ends, temple scene opens)
J12 p019:P6 {pb} -> p019:P7 {pc} (continues) : ok (अनुभोगः + मम, column turn inside one speech)
J13 p019:P10 {pb} -> p020:P2 fresh (clean break) : ok (question ends, भिक्षुक refuses with gesture)
J14 p020:P5 {pb} -> p020:P6 {pc} (continues) : ok (अत्र + कस्य, column turn inside one speech)
J15 p020:P9 {pb} -> END (clean break) : ok (frame closes, वेताल returns to tree)
