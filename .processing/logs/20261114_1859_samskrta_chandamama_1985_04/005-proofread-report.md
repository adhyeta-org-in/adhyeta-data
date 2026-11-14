# Proofread report: 1985_04 p005 (कांस्य-दुर्गम् --- ३), RUN 20261114_1859_samskrta_chandamama_1985_04

## Summary

11 findings: 8 quote-mark verdicts (all applied in-file as `{del:}`/`{ins:}` blocks; STY/style) and 3 held word candidates (unverified, `*`). The systematic issue is the print's mixed quote strokes: two-stroke opens closed with one stroke and vice versa, plus two nested `""` spans where the nesting calls for `'...'`; all are fixed where speech-vs-thought sense and sentence boundary pin the sort. The orth scanner (stdlib, on deblocked text) reports no hits; nothing here looks like OCR output. Proper nouns (सुबाहु, सर्पकेतु, सूर्यवर्मन्, चन्द्रवर्मन्, वीरपुर, राक्षसगिरि) spell consistently. The three shouted जयघोष slogans print in singles ('सर्पकेतुमहाराजः जयतात्', 'शनिमर्दनः जयतात्', 'महाराजः सर्पकेतुः जयतात्') and are kept as a print house convention, not verdicts. Story continuity is unbroken across all 17 joints; no ruptures, no moves proposed. `Loc` below is `pNN:Pm w<k> (anchor)`: page span, lint chunk number, deblocked word number, first two words.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p007:P5 w14 (भवान् तान्) | `आगतवान् अस्मि' इति` | `आगतवान् अस्मि" इति` | STY | style | high | spoken reply (पृष्टवान् frame, `इति` closure) takes doubles; close corrected to match the two-stroke open |
| F2 | p007:P5 w1-w3 (भवान् तान्) | `"भवान् तान् अनुसरतु" इति` (inside outer `"तत्...अस्मि"` reply) | `'भवान् तान् अनुसरतु' इति` | STY | style | high | quoted order nested inside the reply takes singles (DQ SQ ... SQ DQ) |
| F3 | p008:P5 w14 (सुबाहोः उत्तरेण) | `पृष्टवन्तः --- 'अये मित्र!` | `पृष्टवन्तः --- "अये मित्र!` | STY | style | high | spoken question (reporting verb + `?` closure) takes doubles |
| F4 | p010:P3 w1 (सर्वे शासकाः) | `दृष्ट्या सर्वे शासकाः` (no open; `कर्तव्यम्' इति ... चिन्तयन्ति` closes) | `{ins:'}` before `सर्वे` | STY | style | medium | `इति` + `चिन्तयन्ति` pins a quoted thought; open supplied at the दृष्ट्या sentence boundary |
| F5 | p010:P3 w107-w112 (सर्वे शासकाः) | `"सर्पकेतुः ... कृतवान्" इति` (inside outer `"अत्यन्त...` address) | `'सर्पकेतुः ... कृतवान्' इति` | STY | style | high | quoted shout nested inside continuing instructions takes singles |
| F6 | p011:P3 w52 (एवं सुबाहुः) | `आरब्धवन्तः --- 'अये महानुभावाः!` | `आरब्धवन्तः --- "अये महानुभावाः!` | STY | style | high | आक्रोशनम् (shouted address) takes doubles |
| F7 | p012:P2 w13 (जनान् बहुधा) | `कुर्वन्तु ...' इति` | `कुर्वन्तु ..." इति` | STY | style | high | close of the F6 आक्रोशनम् speech takes doubles |
| F8 | p012:P2 w34 (जनान् बहुधा) | `कृतवन्तः --- 'भो भोः,` | `कृतवन्तः --- "भो भोः,` | STY | style | high | आक्रोशनम् (shouted address) takes doubles |
| F9 | p010:P3 w102 (सर्वे शासकाः) | `भवत्सु शतं जनैः ... गन्तव्यम्` | `शतेन जनैः` | MRP | likely | medium* | impersonal passive `गन्तव्यम्` needs an instrumental agent; `शतं` (acc.) cannot stand with `जनैः` |
| F10 | p011:P2 w109 (सहसा नगरं) | `तर्हि अगायतः सः राजा` | `अवगतः` | SPL | error | low* | `अगायतः` is no Sanskrit word; the slot needs a nominative adjective (`सः राजा ... भवेत्`), and `अवगतः` (having learnt [the plot]) fits the warning sense |
| F11 | p010:P3 w76 (सर्वे शासकाः) | `भवन्तः दारिद्र्यपिशाचितः उन्मुक्ताः` | `दारिद्र्यपिशाचात्` | MRP | likely | low* | `उन्मुक्त` governs the ablative (freed *from* the poverty-demon); the print form also mismatches plural `भवन्तः` |

## Patterns

- Mixed quote strokes at speech edges (4 spans): two-stroke opens closed with one stroke (F1, F7) and one-stroke opens closed with two (F3, F6/F8); corrected to doubles wherever a reporting verb (`पृष्टवन्तः`, `उक्तवान्`), आक्रोशनम् context, or `इति` closure pins speech. Kept as print convention: जयघोष slogans in singles (p007:P2, p009:P2, p011:P2) and thought-singles (`'अये'`, `'मृत्युः...एव'`, `'भगवन्!...रक्षतु'`, `'भिक्षुकरूपेण...शक्नोमि'`, `'यदि...एव'`).

## Unverified

- F9 `शतं` / `शतेन`: held because the alternative parse (`शतं जनाः` + finite verb) would require rewriting `गन्तव्यम्`; settled by user choice of minimal fix. No glyph re-check available (images closed per phase rule).
- F10 `अगायतः` / `अवगतः`: held because the replacement needs two glyph changes (ग→व, dropped य) with no Phase A flag on file; `अवगतः` is a sense-fit hypothesis (warned king, freed city), not a reading claim. A fresh look at the print at 3x would settle the glyphs.
- F11 `दारिद्र्यपिशाचितः` / `दारिद्र्यपिशाचात्`: held because the replacement changes both vowel and final; the print form fails case (ablative needed) and number (plural subject) alike. A fresh look at the print ending (`-तः` vs `-त्`) would settle it.
- Deliberately not flagged (house variants, parseable as seen): open sandhi throughout (`यत्-मम`, `तैः सह`, `दीपधारिणां शनिपीडा`); `शनेः अनुचरः` (a follower of Saturn, fitting the mockery); `तन्नामकारणतः` (तत्-नाम-कारण-तः, "by reason of that name"); `भवतः प्रदर्श्य` (possessive genitive with the absolutive); `गुरुः दीपधारिणः`; `नाम्नः`, `पङ्क्तिशः`, `काञ्चन`, `बन्धितवन्तः`, `जयघोषं`, `एकसप्ताहतः`, `पञ्चवर्षेभ्यः`.

## Coverage

- p005:P1 {x-com:layout} : skip layout-only chunk
- p005:P2 # कांस्य-दुर्गम् : skip title chunk
- p005:P3 [सूर्यवर्मणः मरणं : clean
- p005:P4 'अये' इति : clean
- p005:P5 अश्वारोहिणाम् आक्रमणतः : clean
- p005:P6 "अये, भवान् : clean
- p005:P7 तदा समूहे : clean
- p006:P1 {x-com:layout} : skip layout-only chunk
- p006:P2 क्षया पिपासया : clean
- p006:P3 एतद्वचनस्य श्रवणेन : clean
- p006:P4 "आर्य! खादितुं : clean
- p006:P5 "छी, छी! : clean
- p006:P6 रोही अश्वं : clean
- p006:P7 "एषः कथं : clean
- p006:P8 "महाराज! अरण्ये : clean
- p006:P9 सुबाहोः एतत् : clean
- p006:P10 "महानुभावाः! किञ्चित् : clean
- p007:P1 {x-com:layout} : skip layout-only chunk
- p007:P2 सुबाहुवचनविषये अश्वारोहिषु : clean
- p007:P3 अश्वारोहिणां निर्गमनानन्तरं : clean
- p007:P4 "तत् अहम् : clean
- p007:P5 भवान् तान् : F1, F2
- p007:P6 सुबाहोः वचनं : clean
- p008:P1 {x-com:layout} : skip layout-only chunk
- p008:P2 प्रस्थानं कुर्मः" : clean
- p008:P3 'यदि नवीनानि : clean
- p008:P4 नूतनवस्त्राणि धारयामि : clean
- p008:P5 सुबाहोः उत्तरेण : F3
- p008:P6 "मम नामः : clean
- p009:P1 {x-com:layout} : skip layout-only chunk
- p009:P2 कदापि स्वनाम : clean
- p009:P3 "वीरपुरविषये अहं : clean
- p009:P4 तदा कश्चित् : clean
- p009:P5 "एवं तर्हि : clean
- p010:P1 {x-com:layout} : skip layout-only chunk
- p010:P2 प्रविष्टवन्तः। ते : clean
- p010:P3 सर्वे शासकाः : F4, F5, F9, F11
- p011:P1 {x-com:layout} : skip layout-only chunk
- p011:P2 सहसा नगरं : F10
- p011:P3 एवं सुबाहुः : F6
- p012:P1 {x-com:layout} : skip layout-only chunk
- p012:P2 जनान् बहुधा : F7, F8
- p012:P3 उत्प्लुतवान्। द्वारं : clean
- J1 p005:P3 {pb} -> p005:P4 fresh : ok
- J2 p005:P4 {pb} -> p005:P5 {pc} : ok
- J3 p005:P7 {wb} -> p006:P2 {pc} : ok (बुभुक्षया)
- J4 p006:P5 {wb} -> p006:P6 {pc} : ok (अश्वारोही)
- J5 p006:P10 {pb} -> p007:P2 fresh : ok
- J6 p007:P4 {pb} -> p007:P5 {pc} : ok
- J7 p007:P6 {pb} -> p008:P2 {pc} : ok (इतः प्रस्थानं कुर्मः)
- J8 p008:P3 {pb} -> p008:P4 {pc} : ok (अहं नूतनवस्त्राणि)
- J9 p008:P6 {pb} -> p009:P2 {pc} : ok (मया कदापि)
- J10 p009:P2 {pb} -> p009:P3 fresh : ok
- J11 p009:P5 {pb} -> p010:P2 {pc} : ok (मध्ये प्रविष्टवन्तः)
- J12 p010:P2 {pb} -> p010:P3 {pc} : ok (दृष्ट्या सर्वे शासकाः)
- J13 p010:P3 {pb} -> p011:P2 {pc} : ok (सैनिकाः सहसा)
- J14 p011:P2 {pb} -> p011:P3 fresh : ok
- J15 p011:P3 {pb} -> p012:P2 {pc} : ok (ते जनान्)
- J16 p012:P2 {pb} -> p012:P3 {pc} : ok (एकवारम् उत्प्लुतवान्)
- J17 p012:P3 {pb} -> END : ok (अनुवर्तते, serial continues)
