# Proofread report: 1985_10 p044 (START=44, scans 44--48, last story of issue)

## Summary

10 findings, all landed as blocks in the story file (no corrected-text section): 6 quote-mark rulings (1 supplied opening, 2 sort corrections, 1 stray-mark deletion, 2 paired sort corrections), 1 spelling verdict (निश्चयः), and 3 glyph verdicts promoted from Phase A candidates (प्राणेशस्य, नाटकं, ग्रामाधिकारः). Systematic problem: print uses the wrong quote sort or a defective mark at 6 speech/thought edges. One form (नाटकं) stays medium-confidence for want of a sharper glyph read. Loc below is word-level counting words on the chunk from 1. Text is print transcription, not OCR output; orth scan was clean.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p44:P5 (प्राणेशः यद्यपि):w11 | `स्मरति। अतः ... प्रदर्शनीया'` | `{ins:'}अतः` | STY | error | high | interior thought with चिन्तितवान् + इति pins singles; opening mark dropped in print |
| 2 | p45:P3 ('मम उपदंशस्य):w19 | `'कीदृशः ... खादतु नाम"` | `{del:'}{ins:"}कीदृशः` | STY | error | high | spoken utterance with उक्तवती pins doubles; print opens single |
| 3 | p046:P7 (प्राणेशः मौनं):w27 | `अनुभवानि' इति` | `अनुभवानि{del:'}{ins:"}` | STY | error | high | spoken threat with उक्तवान् + इति pins doubles; print closes single |
| 4 | p047:P7 ("ये अपराधं):w17 | `एव"' इति` | `एव"{del:'}` | STY | error | high | speech close is one double mark; the trailing single has no role |
| 5 | p045:P6 (निश्चायः ग्रामाधिकारी):w1 | `निश्चायः ग्रामाधिकारी` | `{del:निश्चायः}{ins:निश्चयः}` | SPL | error | high | निश्चायः is not a word; smallest glyph change (extra आ-stroke) gives निश्चयः |
| 6 | p047:P4 (तत्र प्राणेशः):w7-8 | `'न्यायदानं कुर्वन्तु'` | `"न्यायदानं कुर्वन्तु"` | STY | error | high | direct address with प्रार्थितवान् + इति pins doubles, as in this story's other प्रार्थितवान् speeches |
| 7 | p048:P5 ("इदानीं किं):w1,w3 | `"इदानीं किं करणीयम्?"` | `'इदानीं किं करणीयम्?'` | STY | error | high | interior question with चिन्तयन् pins singles, as in this story's other चिन्तितवान् thoughts |
| 8 | p048:P2 (प्राणशस्य एतत्):w1 | `प्राणशस्य एतत्` | `{del:प्राणशस्य}{ins:प्राणेशस्य}` | OCR | error | high | dropped े-matra; genitive required and every other instance in the story reads प्राणेश |
| 9 | p048:P2 (प्राणशस्य एतत्):w3 | `एतत् नन्त्रं,` | `{del:नन्त्रं}{ins:नाटकं}` | OCR | error | medium* | conjunct blurred at 4x; नाटकं is the idiomatic reveal-word for a feigned fit |
| 10 | p048:P7 (भूमौ पतितवान्):w17 | `न्यूनीकृत्य ग्रामाधिकार्ग ५०` | `{del:ग्रामाधिकार्ग}{ins:ग्रामाधिकारः}` | OCR | error | high | ददाति needs a nominative subject; only ग्रामाधिकारः fits |

## Patterns

- Wrong quote sort or defective mark at speech/thought edges (6: F1, F2, F3, F4, F6, F7). Print mixes singles and doubles; era sort (doubles speak, singles think) plus the governing verb pins each case.
- Blurred or defective glyphs in p048 lines 1--2 and the doctor's loud speech (3: F8, F9, F10). Weak impression in this region dropped a matra and blurred two aksharas.

## Unverified

- F9 `नन्त्रं` -> `नाटकं` (medium*): नटनं (acting) and यन्त्रं (plot) also fit the grammar and the conspiracy context; नाटकं wins on idiom for a feigned illness. Settles by: inspecting 48.jpg first text line at high magnification (word after एतत्).

## Coverage

- p44:P1 {x-com:layout} : skip layout-only chunk
- p44:P2 # उपकारस्मरणम् : skip title
- p44:P3 कोणपुरे प्राणेशः : clean
- p44:P4 वस्तुतः ग्रामाधिकारी : clean
- p44:P5 प्राणेशः यद्यपि : F1
- p44:P6 एतद्विषये प्राणेशः : clean
- p44:P7 ददाति? अथवा : clean
- p44:P8 उपदंशस्य निर्माणे : clean
- p44:P9 'एषः एव : clean
- p44:P10 ग्रामाधिकारी उपदंशं : clean
- p44:P11 {author: विवेकः}{pgb} : skip metadata + page-end
- p45:P1 {x-com:layout} : skip layout-only chunk
- p45:P2 वान्। प्राणेशेन : clean
- p45:P3 'मम उपदंशस्य : F2
- p45:P4 ग्रामाधिकारी तद्दिने : clean
- p45:P5 वैद्यः ग्रामाधिकारिणं : clean
- p45:P6 निश्चायः ग्रामाधिकारी : F5
- p45:P7 ग्रामाधिकारी दिनद्वये : clean
- p45:P8 ग्रामाधिकारी स्वभावेन : clean
- p45:P9 एकदा सः : clean
- p45:P10 अनारोग्यसमये वैद्यस्य : clean
- p46:P1 {x-com:layout} : skip layout-only chunk
- p46:P2 वैद्यः ग्रामाधिकारिणः : clean
- p46:P3 अनन्तरं ग्रामाधिकारी : clean
- p46:P4 तदा प्राणेशः : clean
- p46:P5 "कुतश्चित् आनयतु : clean
- p46:P6 भवता दातव्यम् : clean
- p46:P7 प्राणेशः मौनं : F3
- p46:P8 "मां मारयति : clean
- p46:P9 "भवान् सामान्यरोगार्थम् : clean
- p46:P10 तदा वैद्यः : clean
- p46:P11 तदा प्राणेशः : clean
- p47:P1 {x-com:layout} : skip layout-only chunk
- p47:P2 अहम् अन्यथा : clean
- p47:P3 अनन्तरं प्राणेशः : clean
- p47:P4 तत्र प्राणेशः : F6
- p47:P5 कोऽपि ग्रामप्रमुखः : clean
- p47:P6 तदा प्राणेशः : clean
- p47:P7 "ये अपराधं : F4
- p47:P8 एतत् श्रुत्वा : clean
- p47:P9 वैद्यः प्राणेशस्य : clean
- p47:P10 "अकस्मात् आगतेन : clean
- p47:P11 ग्रामप्रमुखाः परस्परं : clean
- p47:P12 ग्रामाधिकारिणः इदानीम् : clean
- p48:P1 {x-com:layout} : skip layout-only chunk
- p48:P2 प्राणशस्य एतत् : F8, F9
- p48:P3 ग्रामाधिकारी वैद्यं : clean
- p48:P4 वैद्यः विनयेन : clean
- p48:P5 "इदानीं किं : F7
- p48:P6 तदा वैद्यः : clean
- p48:P7 भूमौ पतितवान् : F10
- p48:P8 तदा प्राणेशः : clean
- p48:P9 ग्रामाधिकारी अवमानेन : clean
- J1 p044:P6 {pb} -> p044:P7 {pc} : ok ("भवान् किं वा ददाति?" continuous question)
- J2 p044:P10 {wb} -> p045:P2 {pc} : ok (स्वीकृत + वान् = स्वीकृतवान्, solid join)
- J3 p045:P6 {pb} -> p045:P7 {pc} : ok ("वैद्यस्य उपचारेण ग्रामाधिकारी दिनद्वये स्वस्थः अभवत्")
- J4 p045:P10 {pb} -> p046:P2 fresh : ok (terminal ? then indented new paragraph)
- J5 p046:P5 {pb} -> p046:P6 {pc} : ok ("धनं तु भवता दातव्यम् एव")
- J6 p046:P11 {pb} -> p047:P2 {pc} : ok ("पूर्वम् अहम् अन्यथा चिन्तितवान् आसम्")
- J7 p047:P9 {pb} -> p047:P10 {pc} : ok ("उक्तवान् --- "अकस्मात् आगतेन ...")
- J8 p047:P12 {pb} -> p048:P2 fresh : ok (terminal । then fresh paragraph)
- J9 p048:P6 {pb} -> p048:P7 {pc} : ok ("आघातेन भूमौ पतितवान्")
- J10 p048:P9 {pb} -> END : ok (clean story end, no folio on last scan)
