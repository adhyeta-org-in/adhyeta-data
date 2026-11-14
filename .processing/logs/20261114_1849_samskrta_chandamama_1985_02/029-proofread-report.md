## Summary

10 findings, all severity style (quote-sort for modern readability; no text changed silently). Systematic problem: four spoken passages printed with single quotes where doubles are required (उच्चैः/आज्ञापितवान्/आक्रोशनं/पृष्टवान् + इति closures), and one thought passage printed with doubles where singles are required. Scanner orth run clean; story read sentence by sentence for continuity; proper-noun spelling पुष्कर/पुष्कल held for the user. Loc below is story coordinates pNN:Pm plus anchor words, word counted on the chunk from 1. Text is a print-faithful transcription, not OCR output.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p031:P6 w28 (पुष्कलः चिन्तितवान्) | `'कश्चित् पलायमानः` | `"कश्चित् पलायमानः` | STY | style | high | उच्चैः उक्तवान् + इति closure pins speech, which takes doubles |
| F2 | p031:P6 w32 (पुष्कलः चिन्तितवान्) | `गृह्णन्तु'` | `गृह्णन्तु"` | STY | style | high | closing sort must match the speech opening in F1 |
| F3 | p032:P2 w18 (महाबलः चिन्तितवान्) | `'एतं सजीवं` | `"एतं सजीवं` | STY | style | high | आज्ञापितवान् + इति closure pins speech, which takes doubles |
| F4 | p032:P2 w21 (महाबलः चिन्तितवान्) | `मारयन्तु'` | `मारयन्तु"` | STY | style | high | closing sort must match the speech opening in F3 |
| F5 | p032:P7 w12 (उदञ्चन्तं दुःखं) | `'अये ज्ञानधन!` | `"अये ज्ञानधन!` | STY | style | high | उच्चैः आक्रोशनं pins speech, which takes doubles |
| F6 | p032:P7 w14 (उदञ्चन्तं दुःखं) | `ज्ञानधन!'` | `ज्ञानधन!"` | STY | style | high | closing sort must match the speech opening in F5 |
| F7 | p032:P7 w22 (उदञ्चन्तं दुःखं) | `'ज्ञानधनः कः?` | `"ज्ञानधनः कः?` | STY | style | high | पृष्टवान् + इति closure pins speech, which takes doubles |
| F8 | p032:P7 w23 (उदञ्चन्तं दुःखं) | `कः?'` | `कः?"` | STY | style | high | closing sort must match the speech opening in F7 |
| F9 | p032:P5 w1 ("इदानीं किमपि) | `"इदानीं` | `'इदानीं` | STY | style | high | इति राजा चिन्तयन् pins thought, which takes singles |
| F10 | p032:P6 w14 (सत्यम् एव) | `योग्यानि"` | `योग्यानि'` | STY | style | high | closing sort must match the thought opening in F9 |

## Patterns

Quote-sort inconsistency: 5 passages / 10 marks. Print uses singles for spoken commands and exclamations (F1--F8: सेनापति command, महाबल order, आक्रोशन cry, प्रश्न) where the era standard and the rest of this story use doubles for speech, and doubles for the राजा-chought (F9--F10) where the story elsewhere uses singles for thought. Corrected per mark with {del:}/{ins:} verdicts; all other quote pairs already match their roles and nesting and are kept as seen.

## Unverified

| # | Loc | Question | Conf | What would settle it |
|---|---|---|---|---|
| U1 | p029:P3 (प्राचीनकाले मालवदेशे) vs p031:P3--p032:P9 | King named पुष्कर (पुष्करनामकः, पुष्करस्य) but पुष्कल everywhere else (11x). Which spelling is intended? | medium* | User decision; no direction chosen, no blocks emitted |
| U2 | p029:P7 (ज्ञानधनः एतत्सर्वं) | Stray period before ? in `दृष्टः वा.?` kept as printed with no block (no Phase A flag on file, images closed). Delete the `.`? | medium* | User decision on the print typo |

## Coverage

p029:P1 {x-com: layout} : skip layout-only chunk
p029:P2 # सुखी : skip title chunk
p029:P3 प्राचीनकाले मालवदेशे : clean
p029:P4 एवं मिथ्याप्रशंसां : clean
p029:P5 एकदा ज्ञानधनः : clean
p029:P6 राजा पूर्वम् : clean
p029:P7 ज्ञानधनः एतत्सर्वं : clean
p029:P8 तदा ज्ञानधनः : clean
p029:P9 {note: reprint} : skip metadata chunk
p030:P1 {x-com: layout} : skip layout-only chunk
p030:P2 प्रतापः नाम : clean
p030:P3 प्रतापः? कः : clean
p030:P4 प्रतापः भवान् : clean
p030:P5 प्राप्तवान् इति : clean
p030:P6 अस्तु नाम, : clean
p030:P7 नैव श्रीमन्, : clean
p030:P8 एतेन राजा : clean
p030:P9 ज्ञानधनः मन्दहासं : clean
p031:P1 {x-com: layout} : skip layout-only chunk
p031:P2 निर्गतः। : clean
p031:P3 प्रभो! वृद्धस्य : clean
p031:P4 एकवर्षम् अतीतम्। : clean
p031:P5 अपरक्षणे राजा : clean
p031:P6 पुष्कलः चिन्तितवान् : F1, F2
p031:P7 इति। एतन्मध्ये : clean
p031:P8 तस्मिन् समये : clean
p032:P1 {x-com: layout} : skip layout-only chunk
p032:P2 महाबलः चिन्तितवान् : F3, F4
p032:P3 महाबलस्य आदेशानुसारं : clean
p032:P4 पुष्कलः चतसृषु : clean
p032:P5 इदानीं किमपि : F9
p032:P6 सत्यम् एव : F10
p032:P7 उदञ्चन्तं दुःखं : F5, F6, F7, F8
p032:P8 तत्र उपस्थिताः : clean
p032:P9 एवं चिन्तयन् : clean
J1 p029:P5 {pb} -> p029:P6 {pc} (continues) : ok
J2 p029:P8 {pb} -> p030:P2 {pc} (continues) : ok
J3 p030:P4 {pb} -> p030:P5 {pc} (continues) : ok
J4 p030:P9 {pb} -> p031:P2 {pc} (continues) : ok
J5 p031:P6 {pb} -> p031:P7 {pc} (continues) : ok
J6 p031:P8 {pb} -> p032:P2 fresh (clean break) : ok
J7 p032:P5 {pb} -> p032:P6 {pc} (continues) : ok
J8 p032:P9 {pb} -> END (clean break) : ok
