# Proofread report — 1984_05, START=005 (scan pages 5–12, story `त्रयः मान्त्रिकाः`, middle installment, ends `(अनुवर्तते)`)

## Summary

22 findings: 5 error, 17 likely (11 of them unverified holds). Two systematic problems: single-stroke speech opens closed with double marks (7 spans, opens upgraded to doubles per 1980s house standard) and multi-para speeches split across paras needing per-para marks (5 supplied). Six print-misprint candidates held as `{sug-}` for the user; two readings held with no suggestion. Text is a fresh human transcription from scans (not OCR output); the two `scan.py orth` hits (`!`) are house exclamation marks, dismissed. Loc below is `pNN:Pm` (scan span + lint chunk) with the first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p05:P6 `पुत्र!` | `"भवतः ... पुत्र!` + `{pb}` | `{ins:"}` after `पुत्र!` | STY | error | high | each para opens and closes its own pair; speech continues next page |
| 2 | p06:P2 `भवतः गमनानन्तरं` | `भवतः ... जानामि "` | `{ins:"}` before `भवतः` | STY | error | high | reopens the pair closed in F1; balances the para |
| 3 | p08:P3 `रक्तवर्णा।` | `"दुःखं ... रक्तवर्णा।` | `{ins:"}` after `रक्तवर्णा।` | STY | error | high | closes the `"दुःखं` speech at the column break |
| 4 | p08:P4 `यत् प्रवृत्तं` | `यत् ... आगच्छन्तु"` | `{ins:"}` before `यत्` | STY | error | high | reopens the pair closed in F3; balances the para |
| 5 | p08:P5 `सहोदर!` | `'सहोदर! ...` | `{del:'}{ins:"}` | STY | likely | high | speech with double close; open is a dropped second stroke |
| 6 | p09:P3 `सहोदर!` | `'सहोदर! ... निवेदयतु"` | `{del:'}{ins:"}` | STY | likely | high | same pattern as F5; close is clearly double |
| 7 | p10:P2 `इदानीं` | `'इदानीं ... सञ्जातौ"` | `{del:'}{ins:"}` | STY | likely | high | same pattern; spoken dialogue takes doubles |
| 8 | p10:P4 `पश्चात्तापः` | `पश्चात्तापः ... निश्चयः"` | `{ins:"}` before `पश्चात्तापः` | STY | error | high | mother's speech opens with no mark in print; supplied |
| 9 | p10:P7 `इतःपरं` | `'इतःपरं ... कुर्वन्तु"` | `{del:'}{ins:"}` | STY | likely | high | same pattern as F5 |
| 10 | p11:P6 `तन्नाम` | `'तन्नाम ... ज्ञायते एव"` | `{del:'}{ins:"}` | STY | likely | medium* | speech framing (`उक्तवान्`) wins over `चिन्तयामि`; needs scan check |
| 11 | p12:P6 `मम` | `'मम ... किल?"` | `{del:'}{ins:"}` | STY | likely | high | same pattern; nested `'यदि ... सिद्धः'` stays single inside |
| 12 | p12:P8 `आम्` | `'आम् ... पश्यावः"` | `{del:'}{ins:"}` | STY | likely | high | same pattern as F5 |
| 13 | p05:P3 `मल्लूककेतुः` | `मल्लूककेतुः पिशाचगणस्य` | `{sug-del:मल्लूककेतुः}{sug-ins:भल्लूककेतुः}` | CNS | likely | medium* | same person named `भल्लूककेतु` twice later; one-stroke म/भ slip |
| 14 | p08:P3 `ममग्रः` | `कोपः ममग्रः शान्तः` | `{sug-del:ममग्रः}{sug-ins:समग्रः}` | SPL | likely | medium* | `ममग्रः` is meaningless; `कोपः समग्रः शान्तः` fits perfectly |
| 15 | p07:P4 `मक्ष्य` | `मक्ष्य-भोज्यादिकं` | `{sug-del:मक्ष्य}{sug-ins:भक्ष्य}` | SPL | likely | medium* | `मक्ष्य` is meaningless; cf. `भक्ष्यभोज्यं` (p06), `भक्ष्याणि` (p10) |
| 16 | p08:P5 `भक्तः` | `भक्तः आगमनस्य` | `{sug-del:भक्तः}{sug-ins:भवतः}` | LEX | likely | medium* | valid-but-wrong word; sense needs `भवतः` (awaiting YOUR arrival) |
| 17 | p09:P2 `क्षायम्तु` | `अस्मान् क्षायम्तु` | `{sug-del:क्षायम्तु}{sug-ins:क्षाम्यतु}` | SPL | likely | medium* | sense is `forgive us`; print form is not a word |
| 18 | p05:P6 `सहस्रं` | `अहं सहस्रं दीनारान्` | `{sug-del:सहस्रं}{sug-ins:सहस्रं}` | CNS | likely | medium* | inconsistent with `सहस्रदीनारान्` (p06); needs scan check |
| 19 | p07:P2 `दूरङ्गतः` | `न दूरङ्गतः` | `{sug-del:दूरङ्गतः}{sug-ins:दूरगतः}` | SPL | likely | low* | odd form; needs scan and lexicon check |
| 20 | p07:P8 `आतृप्ति` | `अपि आतृप्ति भोजनं` | `{sug-del:आतृप्ति}{sug-ins:आतृप्तिम्}` | SPL | likely | low* | `to (her) satisfaction` fits the feast; `अतृप्ता` also possible |
| 21 | p08:P3 `रक्तवर्णा` | `माता रक्तवर्णा।` | `?` | SPL | likely | low* | no confident hypothesis; sense of the sentence is unclear |
| 22 | p12:P6 `पाल्लकतः` | `अपि पाल्लकतः युवकं` | `?` | SPL | likely | low* | unknown word; possibly a community term; needs lexicon and scan |

## Patterns

Pattern A — mixed single-open/double-close speech spans (7x: F5, F6, F7, F9, F10, F11, F12). Opens upgraded to doubles; closes kept. Era standard marks spoken dialogue with doubles, and all seven closes are unambiguous two-stroke marks, so the opens are dropped second strokes. F10 is the weakest (thought-flavoured content) and stays unverified.
Pattern B — multi-para speech split across paras (5 supplied marks: F1, F2, F3, F4, F8). Each para now opens and closes its own pair per doctrine; page-turn `{pb}`/`{pc}` spans were never forced closed, only completed per para.
Pattern C — print-misprint candidates held as `{sug-}` (6x: F13–F18). All are legible-as-seen transcriptions; none was verdict-converted because Phase A left no `{x-com:}` on them.
Patterns D — house variants kept as seen, no findings: open sandhi (`भवितुम् न`, `तत् सर्वं`), doubled consonants (`वदन्नी`, cf. 1984_04 `जीवम्मा`), `!` exclamations (`चकिता!`, `पदार्थाः!`), `एतत्सर्वं` openness, `तद्दिने`, `सधैर्यं`.

## Unverified

F10: settle by re-examining whether `'तन्नाम ... चिन्तयामि` is thought (keep single) or spoken musing (double); shaking-head cue vs `उक्तवान्` framing.
F13: settle against the previous installment's spelling of भल्लूककेतु; if the recap names two different persons, drop the candidate.
F14–F17: settle by 3x scan re-read of `ममग्रः`, `मक्ष्य`, `भक्तः`, `क्षायम्तु` (images stayed closed in this phase).
F18: settle by comparing the p005 glyph against p006 `सहस्रदीनारान्` on the scans.
F19: settle with a lexicon (`दूरङ्ग` vs `दूरग`) and scan check.
F20: settle with lexicon and scan; alternatives are `अतृप्ता` (dissatisfied, poor sense) and keeping print.
F21: settle from the next installment's context and scan; candidate word `वक्ष्यति` was considered and rejected as too distant.
F22: settle with a lexicon (community/caste term?) and scan check of `पाल्लकतः`.

## Coverage

p05:P1 skip layout-only chunk
p05:P2 skip title chunk
p05:P3 मल्लूककेतुः पिशाचगणस्य : F13
p05:P4 स्वमातुः दीनावस्थां : clean
p05:P5 तां सान्त्वयन् : clean
p05:P6 अभवत् प्रयाणतः : F1, F18
p06:P1 skip layout-only chunk
p06:P2 भवतः गमनानन्तरं : F2
p06:P3 जन्मदात्रीं मातरम् : clean
p06:P4 पिङ्गलः कृशशरीरां : clean
p06:P5 स्थापितवान् पिङ्गलस्य : clean
p06:P6 तदा पिङ्गलः : clean
p07:P1 skip layout-only chunk
p07:P2 पुत्रक कोऽयं : F19
p07:P3 पिङ्गलः मातृसमीपे : clean
p07:P4 मक्ष्य-भोज्यादिकं व्यञ्जन-पायसादिकं : F15
p07:P5 माता आश्चर्येण : clean
p07:P6 पिङ्गलः मन्त्रस्यूतं : clean
p07:P7 अनन्तरं पिङ्गलेन : clean
p07:P8 आतृप्ति भोजनं : F20
p07:P9 एवं माता : clean
p08:P1 skip layout-only chunk
p08:P2 पिङ्गलः विषयं : clean
p08:P3 अतिदीनावस्थायां स्थितम् : F3, F14, F21
p08:P4 यत् प्रवृत्तं : F4
p08:P5 पिङ्गलस्य वचनं : F5, F16
p09:P1 skip layout-only chunk
p09:P2 नमस्कारान् सूचयतु : F17
p09:P3 उभावपि उन्मत्तौ : F6
p09:P4 तावति काले : clean
p09:P5 पुत्रद्वयं दृष्ट्वा : clean
p09:P6 भवत्याः क्षमादानेन : clean
p10:P1 skip layout-only chunk
p10:P2 मातरं नमस्कृत्य : F7
p10:P3 पिङ्गलः मन्त्रस्यूतं : clean
p10:P4 पश्चात्तापः सर्वपापानि : F8
p10:P5 जीवदत्तः लक्षदत्तः : clean
p10:P6 लक्षदत्तेन सह : clean
p10:P7 तदा पिङ्गलः : F9
p11:P1 skip layout-only chunk
p11:P2 पिङ्गलस्य वचनं : clean
p11:P3 तद्दिने रात्रौ : clean
p11:P4 पाकशालां प्रविश्य : clean
p11:P5 पिङ्गलः कथमपि : clean
p11:P6 लक्षदत्तः शिरः : F10
p11:P7 णाम् अपि : clean
p11:P8 अनन्तरदिने कदाचित् : clean
p12:P1 skip layout-only chunk
p12:P2 प्रदर्शितवती : clean
p12:P3 सः मन्त्रः : clean
p12:P4 माता पुत्रव्यामोहेन : clean
p12:P5 तद्दिने रात्रौ : clean
p12:P6 मम एकः : F11, F22
p12:P7 स्थगितवान् वदति : clean
p12:P8 आम् समीचीनम् : F12
p12:P9 उभौ अपि : clean
p12:P10 अये नौकानायकमहोदय : clean
J1 p005:P3 -> p005:P4 fresh : ok
J2 p005:P5 -> p005:P6 {pc} : ok (single speech continued across columns)
J3 p005:P6 -> p006:P2 fresh : ok (F1 closes, F2 reopens per para)
J4 p006:P3 -> p006:P4 fresh : ok (left column read before right column; clean sentence break)
J5 p006:P4 -> p006:P5 {pc} : ok (सुरक्षितं + स्थापितवान् verified from both sides in Phase A)
J6 p006:P6 -> p007:P2 fresh : ok
J7 p007:P3 -> p007:P4 {pc} : ok (प्रसार्य + मक्ष्य spaced join)
J8 p007:P7 -> p007:P8 {pc} : ok (अपि + आतृप्ति spaced join)
J9 p007:P9 -> p008:P2 fresh : ok
J10 p008:P3 -> p008:P4 fresh : ok (F3 closes, F4 reopens per para)
J11 p008:P5 -> p009:P2 {pc} : ok (F5 open pairs with P2 close across the page turn)
J12 p009:P4 -> p009:P5 fresh : ok
J13 p009:P6 -> p010:P2 fresh : ok
J14 p010:P3 -> p010:P4 fresh : ok (F8 supplies the missing open)
J15 p010:P5 -> p010:P6 fresh : ok
J16 p010:P7 -> p011:P2 fresh : ok
J17 p011:P3 -> p011:P4 {pc} : ok (जीवदत्तः + पाकशालां verified)
J18 p011:P6 -> p011:P7 {pc} : ok (दरिद्रा + णाम् solid hyphenation join)
J19 p011:P8 -> p012:P2 {pc} : ok (कृते + प्रदर्शितवती verified)
J20 p012:P6 -> p012:P7 {pc} : ok (सः + स्थगितवान् verified)
J21 p012:P10 -> END : ok (serial continues next installment; `(अनुवर्तते)` kept)
