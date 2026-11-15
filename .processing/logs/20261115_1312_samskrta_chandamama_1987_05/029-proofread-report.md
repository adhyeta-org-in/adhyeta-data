# Proofread report: 1987_05 p029 (उत्तररामायणम्)

## Summary

Seven-page 2col serial (`उत्तररामायणम्`, `८. सीतापरित्यागः।`): Agastya narrates Riksaraja's birth and Valin-Sugriva's origin, Rama's coronation guests depart, Sita's pregnancy and longing for the ascetics' groves, Bhadra's report of the people's slander, Rama's order to Laksmana, and the abandonment of Sita at the Tamasa with her message to her kin. Four findings (all `STY`/style, high confidence): the closing Sita speech spans three paragraphs and print carries only one open and one close, so three paragraph-edge marks were supplied via `{ins:"}` to make each paragraph stand alone. No inherited `{sug-ins:}`/`{sug-del:}` queue existed in Phase A. Orth scan (`scan.py orth` on deblocked text) returned zero hits. Proofread gate is green with all quote pairs balanced and all fourteen joints verified continuous. Loc below is `pNN:Pm:word`, words counted on the chunk from 1 (`---` and quote marks excluded). The text is print transcription, not OCR output.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p035:P4:34 (किञ्चित्कालानन्तरं सा) | `मम समीपे एव` | `मम समीपे एव{ins:"}` | STY | style | high | multi-para speech stands alone per para; supply the paragraph close for the opening `"लक्ष्मण!` before the `{pb}` column turn |
| F2 | p035:P5:1 (स्थित्वा सान्त्वनवचनानि) | `{pc}स्थित्वा` | `{pc}{ins:"}स्थित्वा` | STY | style | high | continuation paragraph of the same Sita speech needs its own open; page-turn is the only exception and this is an intra-page column turn |
| F3 | p035:P5:52 (स्थित्वा सान्त्वनवचनानि) | `अधिकतरा भविष्यति।` | `अधिकतरा भविष्यति।{ins:"}` | STY | style | high | close of the same paragraph pair opened by F2, pinned by the sentence boundary before the fresh paragraph |
| F4 | p035:P6:1 (पूर्वपक्षया अधिकः) | `पूर्वपक्षया` | `{ins:"}पूर्वपक्षया` | STY | style | high | final paragraph of the same speech keeps print's close `" इति उक्तवती।` and needs its own open; speech sense plus sentence boundary pins it |

## Patterns

None (no repeats; the four insertions belong to one three-paragraph speech).

## Unverified

None. No form was flagged below high confidence. Examined and kept as print-faithful per the fidelity doctrine (no blocks emitted): open-sandhi junctions (`तत्रैव सृष्टिकर्तुः`, `तथा पुनः`, `यदा योगध्यानमग्नः`, `पुनः तीरं`, `इतःपरं तदेव`), print commas (`ब्रह्मा तं दृष्ट्वा,`, `भूत्वा, जलम्`, `समालिङ्ग्य,`), the house forms `सम्पूर्णं`/`संपूर्ण` variation kept as printed, `वर्तान्` in `सान्त्वनवचनानि वर्तान् मम` (sense strained, `वर्षन्` conceivable, but no Phase A `{x-com:}`/`{sug-…}` flag exists so no glyph verdict is issued from text alone), `नमस्कारोमि` kept as printed, and `पूर्वपक्षया` kept as printed. Proper nouns are consistent throughout (`ऋक्षरजाः`, `किष्किन्धा`, `वालि`/`वालिने`/`वालिनं` as stem forms, `सुमन्त्र`, `भद्र`, `तमसा`/`तमसि` as case forms). A faint detached speck near the folio on p035 was omitted as print noise in Phase A.

## Coverage

p029:P1 {x-com:layout : skip x-com-only chunk
p029:P2 उत्तररामायणम् : skip title chunk
p029:P3 अगस्त्यमहामुनिः वालिसुग्रीवयोः : clean
p029:P4 मेरुपर्वतस्य उपरि : clean
p029:P5 एकस्मिन् दिने : clean
p029:P6 ब्रह्मा तं : clean
p029:P7 तदनुसारेण सः : clean
p029:P8 एवंरीत्या बहुदीर्घः : clean
p029:P9 तस्मिन् सरोवरे : clean
p029:P10 {category: ८. : skip footer metadata
p030:P1 {x-com:layout : skip x-com-only chunk
p030:P2 सम्पूर्णं सरोवरम् : clean
p030:P3 सः सरोवरे : clean
p030:P4 जगन्मोहनाकारा सा : clean
p030:P5 जातः। इन्द्रः : clean
p030:P6 एतदनन्तरं तत् : clean
p030:P7 ब्रह्मा कदाचित् : clean
p030:P8 भोः राम : clean
p030:P9 रामपट्टाभिषेकस्य समापनानन्तरम् : clean
p030:P10 जनकमहाराजस्य प्रस्थानसमये : clean
p031:P1 {x-com:layout : skip x-com-only chunk
p031:P2 आपृच्छनं कृतवान्। : clean
p031:P3 लङ्कातः रामेण : clean
p031:P4 लङ्कायां रावणमारणसमये : clean
p031:P5 अनन्तरं रामः : clean
p031:P6 अनन्तरं कदाचित् : clean
p031:P7 सीता मन्दहासं : clean
p031:P8 तत्र को : clean
p031:P9 सीताम् एतत् : clean
p032:P1 {x-com:layout : skip x-com-only chunk
p032:P2 अस्ति। अस्माकं : clean
p032:P3 भद्रः अञ्जलिबद्धः : clean
p032:P4 भद्रः किमपि : clean
p032:P5 निर्भयं निश्शङ्कं : clean
p032:P6 रामः समुद्रस्य : clean
p032:P7 तस्य वचनं : clean
p032:P8 सर्वे अवनतमुखाः : clean
p032:P9 रामः तान् : clean
p032:P10 ते त्रयः : clean
p033:P1 {x-com:layout : skip x-com-only chunk
p033:P2 आसनेषु उपवेश्य : clean
p033:P3 सीता दोषरहिता : clean
p033:P4 परेद्युः सूर्योदयसमये : clean
p033:P5 सुमन्त्रः अविलम्बेन : clean
p033:P6 तस्य वचनानि : clean
p033:P7 वेगेन रथे : clean
p034:P1 {x-com:layout : skip x-com-only chunk
p034:P2 तस्याः वचनेन : clean
p034:P3 सम्पूर्णं दिनं : clean
p034:P4 तं दृष्ट्वा : clean
p034:P5 मम सन्तोषभङ्गम् : clean
p034:P6 लक्ष्मणः अश्रूणि : clean
p034:P7 तमसानद्याः अन्यस्मिन् : clean
p034:P8 तस्य परिस्थितिं : clean
p034:P9 तदा लक्ष्मणः : clean
p035:P1 {x-com:layout : skip x-com-only chunk
p035:P2 अग्रजस्य हृदयं : clean
p035:P3 एतानि वचनानि : clean
p035:P4 किञ्चित्कालानन्तरं सा : F1
p035:P5 स्थित्वा सान्त्वनवचनानि : F2, F3
p035:P6 पूर्वपक्षया अधिकः : F4
J1 p029:P6 {pb} -> p029:P7 fresh (clean break) : ok
J2 p029:P9 {pb} -> p030:P2 {pc} (continues) : ok
J3 p030:P4 {pb} -> p030:P5 {pc} (continues) : ok
J4 p030:P10 {pb} -> p031:P2 {pc} (continues) : ok
J5 p031:P6 {pb} -> p031:P7 fresh (clean break) : ok
J6 p031:P9 {pb} -> p032:P2 {pc} (continues) : ok
J7 p032:P4 {pb} -> p032:P5 {pc} (continues) : ok
J8 p032:P10 {pb} -> p033:P2 {pc} (continues) : ok
J9 p033:P4 {pb} -> p033:P5 fresh (clean break) : ok
J10 p033:P7 {pb} -> p034:P2 fresh (clean break) : ok
J11 p034:P4 {pb} -> p034:P5 {pc} (continues) : ok
J12 p034:P9 {pb} -> p035:P2 {pc} (continues) : ok
J13 p035:P4 {pb} -> p035:P5 {pc} (continues) : ok
J14 p035:P6 {pb} -> END (clean break) : ok
