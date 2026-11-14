## Summary
11 findings: 6 quote verdicts (F1-F6, error), 2 kept print quirks (F7-F8, style), 3 held word candidates (F9-F11, unverified). Systematic problems: print drops the second stroke of speech-open doubles (3x, Pattern A); interior monologue opened SQ but closed DQ (2x, Pattern B). p005 (folio 22) is an orphan page from another story, so J8 asserts no continuity. Text is manual transcription, not OCR output. Loc is `pNN:Pm` plus the first two chunk words; Conf `*` marks unverified holds.

## Findings
| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p003:P3 द्वयोः अपि | `'चन्द्रपालः मम` | `"चन्द्रपालः मम` | STY | error | high | speech DQ pinned by उक्तवान् plus इति closure; print shows one open stroke so the second is supplied |
| 2 | p003:P6 प्रत्यक्षं यत् | `'प्रत्यक्षं यत्` | `"प्रत्यक्षं यत्` | STY | error | high | speech DQ pinned by the भवेत् close and मञ्जुनाथः reporting frame; one open stroke in print so the second is supplied |
| 3 | p004:P6 कस्मिंश्चित् अपि | `'कस्मिंश्चित् अपि` | `"कस्मिंश्चित् अपि` | STY | error | high | speech DQ pinned by इति उक्तवान् मञ्जुनाथः; single open in print so the second is supplied |
| 4 | p005:P5 स्वयं निर्णेतुं | `स्वीकारणीयः"` | `स्वीकारणीयः'` | STY | error | high | interior monologue governed by चिन्तितवान् takes SQ, pairing with the 'अहं open; the DQ close is corrected |
| 5 | p005:P7 महाराजाय यशोवर्धनाय | `परिहरणीया"` | `परिहरणीया'` | STY | error | high | king's disapproving thought governed by चिन्तितवान् takes SQ; the DQ close is corrected |
| 6 | p005:P8 एवं रीत्या | `प्रकटयिष्यामि।` | `प्रकटयिष्यामि"।` | STY | error | high | DQ opened at यत् never closes in print; the resolved-content boundary before fresh narration pins the close |
| 7 | p004:P4 मञ्जुनाथस्य वचनेन | `"आम्. भवतः` | `आम्. (keep)` | STY | style | high | print shows a full stop after आम्; kept as print punctuation, never normalized |
| 8 | p002:P4 मन्दारगुप्तः एतां | `'एषा पद्धतिः योग्या'` | `(keep)` | STY | style | high | balanced print SQ pair; अङ्गीकृतवती is not a strict reporting verb, so print's sort stands |
| 9 | p005:P4 राजा इदानीं | `अम्भे किं` | `अहो` | LEX | likely | low* | अम्भे fits nothing in context; अहो is the stock exclamation before किं करणीयम् but print cannot be rechecked |
| 10 | p005:P7 महाराजाय यशोवर्धनाय | `एषा समस्यां` | `समस्या` | SPL | likely | medium* | एषा and परिहरणीया are nominative so the accusative is ungoverned; likely an extra anusvara in print |
| 11 | p005:P8 एवं रीत्या | `नागरिकप्रमुखाणां` | `प्रमुखानां` | SPL | likely | medium* | णत्व has no trigger in प्रमुख; expected dental न but print cannot be rechecked |

## Patterns
- Dropped second stroke on speech opens (3x: F1 p003:P3, F2 p003:P6, F3 p004:P6). Each ruled DQ via {del:'}{ins:"} with the as-seen stroke kept in the del span.
- SQ thought closed with DQ (2x: F4 p005:P4->P5, F5 p005:P7). Each close corrected to SQ via {del:"}{ins:'}; opens kept.

## Unverified
- F9 अम्भे: held as {sug-del:अम्भे}{sug-ins:अहो}. Text exhaustion leaves only a strained अम्भा-vocative reading against the natural अहो. Settles with a 3x print recheck or a parallel edition.
- F10 समस्यां: held as {sug-del:समस्यां}{sug-ins:समस्या}. Grammar wants nominative; the extra anusvara is a glyph claim. Settles with a print recheck.
- F11 प्रमुखाणां: held as {sug-del:प्रमुखाणां}{sug-ins:प्रमुखानां}. Mechanical णत्व rule points to न; the ण is a glyph claim. Settles with a print recheck or a parallel edition.

## Coverage
p001:P1 : skip x-com layout
p001:P2 : skip title
p001:P3 साकेतपुरे मन्दारगुप्तः : clean
p001:P4 एतद्विषये सः : clean
p001:P5 बहोः कालतः : clean
p001:P6 अस्ति, अहं : clean
p001:P7 "वदतु नाम। : clean
p001:P8 "भवतोः उभयोः : clean
p001:P9 "कीदृशी परीक्षा : clean
p001:P10 "तौ द्वौ : clean
p001:P11 : skip category footer
p002:P1 : skip x-com layout
p002:P2 "किम्? सुवर्णद्वीपे : clean
p002:P3 "श्रीमन्! अतः : clean
p002:P4 मन्दारगुप्तः एतां : F8
p002:P5 कुमारदासः च : clean
p002:P6 "नवीनं वाणिज्यम् : clean
p002:P7 अनन्तरं मन्दारगुप्तः : clean
p003:P1 : skip x-com layout
p003:P2 विरलाः। न : clean
p003:P3 द्वयोः अपि : F1
p003:P4 तदा आश्चर्यं : clean
p003:P5 "एतत् कथम्? : clean
p003:P6 प्रत्यक्षं यत् : F2
p003:P7 शक्नोति। किन्तु : clean
p004:P1 : skip x-com layout
p004:P2 मन्दारगुप्तः स्वसम्मतिं : clean
p004:P3 "एतत्क्षणे एव : clean
p004:P4 मञ्जुनाथस्य वचनेन : F7
p004:P5 समीचीनः एव। : clean
p004:P6 कस्मिंश्चित् अपि : F3
p004:P7 'चन्द्रपालस्य बुद्धिः : clean
p004:P8 एतदनन्तरं वर्षद्वयाभ्यन्तरे : clean
p005:P1 : skip x-com layout
p005:P2 सिध्येत। यतः : clean
p005:P3 गुणवर्धनस्य स्वभावविशेषाः : clean
p005:P4 राजा इदानीं : F4, F9
p005:P5 स्वयं निर्णेतुं : F4
p005:P6 तत्र केचन : clean
p005:P7 महाराजाय यशोवर्धनाय : F5, F10
p005:P8 एवं रीत्या : F6, F11
J1 p001:P5 {pb} -> p001:P6 {pc} : ok
J2 p001:P10 {pb} -> p002:P2 fresh : ok
J3 p002:P4 {pb} -> p002:P5 {pc} : ok
J4 p002:P7 {pb} -> p003:P2 {pc} : ok
J5 p003:P6 {pb} -> p003:P7 {pc} : ok
J6 p003:P7 {pb} -> p004:P2 fresh : ok
J7 p004:P4 {pb} -> p004:P5 {pc} : ok
J8 p004:P8 {pb} -> p005:P2 {pc} : story-boundary, no continuity asserted (p004 ends वाणिज्यदक्षः; p005 is an orphan folio-22 page; {pc} pairing mechanical only; no move proposed)
J9 p005:P4 {pb} -> p005:P5 {pc} : ok
J10 p005:P8 {pb} -> END : F6, narrative continues past range
