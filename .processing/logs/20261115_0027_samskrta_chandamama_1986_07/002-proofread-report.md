# Proofread report — 1986_07, START=002 (पुण्यफलम्, scans 2–7)

## Summary

Range p002–p007 (6 scans, story पुण्यफलम्, title through the guru's verdict which continues into the next range). 14 findings: 9 error, 5 likely; no held candidates. Loc is `pNN:Pm` (NN = scan sequence, Pm = lint chunk number) plus chunk anchor words, word counted on the chunk from 1. The systematic defect is bare `-त्` where the imperative requires `-तु`/`-Ø` (6 loci: F1, F6, F7, F8, F10, F12); the rest are single-glyph print confusions (क/त, ञ्च/ञ्च, दृ/दृ, ह/रुह, ङ/ड, य/स). Transcription is eyes-on-print (no OCR); `scan.py orth` on deblocked text reports zero hits. The final open quote (p007:P9) closes in the next range and could not be pair-checked here.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p003:P3 [समीकृतां पादरक्षां] w26 | `समर्पणभाण्डे स्थापयत्` | `स्थापयतु` | MRP | error | high | 2sg imperative addressed to प्रबोधः needs स्थापयतु; cf. printed तिष्ठतु, ददातु |
| F2 | p003:P4 [प्रबोधः एतत्] w5 | `रजकनाणकं` | `रजतनाणकं` | CNS | error | high | रजकः is washerman; story term is रजतनाणक- throughout (13 other loci) |
| F3 | p003:P4 [प्रबोधः एतत्] w8 | `दृढं बद्ध्वा` | `दृढं बद्ध्वा` | SPL | likely | medium | दृढ is not a word; दृढम् is the adverbial form |
| F4 | p003:P5 [एवं गमनसमये] w11 | `अश्वम् आरुह्य` | `आरुह्य` | MRP | likely | medium | ल्यप् of आ√रुह् is आरुह्य |
| F5 | p003:P6 [सः प्रबोधं] w6 | `हूड्कारं कुर्वन्` | `हुङ्कारं` | SPL | likely | medium | हुङ्कारः is the anger-roar; हूड्कार is unattested |
| F6 | p003:P6 [सः प्रबोधं] w10 | `अये! तिष्ठत्` | `तिष्ठतु` | MRP | error | high | robber's halt order needs 2sg imperative; print itself gives तिष्ठतु at p004:P5 |
| F7 | p003:P6 [सः प्रबोधं] w20 | `हस्ते अर्पयत्` | `अर्पयतु` | MRP | error | high | command to hand over needs 2sg imperative अर्पयतु |
| F8 | p003:P6 [सः प्रबोधं] w30 | `इति स्मरत्` | `स्मर` | MRP | error | high | singular addressee needs 2sg imperative स्मर |
| F9 | p003:P6 [सः प्रबोधं] w23 | `प्राणैः वञ्चितः` | `वञ्चितः` | SPL | error | high | deprived is वञ्चितः (वञ्च्); वञ्चितः is not a form |
| F10 | p004:P2 [{pc}--- "मम] w11 | `भाण्डे स्थापयत्` | `स्थापयतु` | MRP | error | high | same vow formula as F1, imperative स्थापयतु |
| F11 | p004:P4 [पुनः एकमासं] w14 | `रुधिरकर्णो नाम` | `रुधिरकर्णः` | CNS | error | high | name spells रुधिरकर्णः/रुधिरकर्णम् at all four other loci |
| F12 | p004:P6 [{pc}भविष्यामि।] w18 | `कृपया अनुगृह्णात्` | `अनुगृह्णातु` | MRP | likely | medium | plea for favour needs imperative; अनुगृह्णातु is the closest-glyph fix (अनुगृहाण also possible) |
| F13 | p007:P8 ["नगरे केचन] w64 | `धने कञ्चन` | `कञ्चन` | SPL | error | high | indefinite is कञ्चन; कञ्चन is not a word |
| F14 | p007:P9 [जीवानन्दः मन्दहासं] w3 | `मन्दहासं प्रकटसन्` | `प्रकटयन्` | MRP | likely | medium | displaying a smile needs causative participle प्रकटयन्; प्रकटसन् is not a form |

## Patterns

Pattern A (imperative `-त्`, 6 loci): bare dental where the imperative needs `-तु` or `-Ø` — F1 p003:P3, F6 p003:P6, F7 p003:P6, F8 p003:P6, F10 p004:P2, F12 p004:P6. Pattern B (single-glyph confusions, 5 loci): क/त (F2), दृ/दृ (F3), ह/रुह (F4), ङ/ड (F5), ञ्च/ञ्च (F9, F13). काशीविश्वेश्वर/काशीविश्वनाथ spellings are kept as printed variants, not findings.

## Unverified

None. Every Phase A candidate was promoted to a verdict above; nothing is held for the user from this range.

## Coverage

p002:P1 {x-com:layout:: skip layout chunk
p002:P2 # पुण्यफलम् : skip title
p002:P3 पूर्वं कौमुदीराज्ये : clean
p002:P4 जीवानन्दः सम्भाषणसन्दर्भे : clean
p002:P5 शिष्यस्य एतं : clean
p002:P6 प्रबोधः तद्दिने : clean
p002:P7 तस्य चर्मकारस्य : clean
p002:P8 "अहं कौमुदीराज्यतः : clean
p002:P9 एतत् वचनं : clean
p002:P10 {author: श्रीमाता} : skip metadata/footer chunk
p003:P1 {x-com:layout:: skip layout chunk
p003:P2 दर्शनार्थं प्रस्थितः! : clean
p003:P3 समीकृतां पादरक्षां : F1
p003:P4 प्रबोधः एतत् : F2, F3
p003:P5 एवं गमनसमये : F4
p003:P6 सः प्रबोधं : F5, F6, F7, F8, F9
p003:P7 भीतः प्रबोधः : clean
p003:P8 "वस्त्रस्य अन्ते : clean
p003:P9 प्रबोधः वस्त्रबन्धनं : clean
p003:P10 तदा अग्निशिखः : clean
p003:P11 अतः सः : clean
p004:P1 {x-com:layout:: skip layout chunk
p004:P2 {pc}--- "मम : F10
p004:P3 "एतत् धनं : clean
p004:P4 पुनः एकमासं : F11
p004:P5 प्रबोधः भीत्या : clean
p004:P6 {pc}भविष्यामि। कर्तव्यच्युतः : F12
p004:P7 ब्रह्मराक्षसः रुधिरकर्णः : clean
p004:P8 अनन्तरं प्रबोधं : clean
p004:P9 पुनः अपि : clean
p005:P1 {x-com:layout:: skip layout chunk
p005:P2 तत्सन्दर्भे कश्चन : clean
p005:P3 सः व्याधः : clean
p005:P4 प्रबोधः रुधिरकर्णम् : clean
p005:P5 आसन्। प्रबोधः : clean
p005:P6 सः प्रबोधं : clean
p006:P1 {x-com:layout:: skip layout chunk
p006:P2 प्रबोधः एकदिनं : clean
p006:P3 पूर्वं चर्मकारः : clean
p006:P4 प्रबोधः तस्य : clean
p006:P5 सः महाजनः : clean
p006:P6 निर्मितानां पादरक्षाणां : clean
p006:P7 'आत्मनः कारणतः : clean
p006:P8 "एते त्रयः : clean
p007:P1 {x-com:layout:: skip layout chunk
p007:P2 प्राप्तम् एव। : clean
p007:P3 एवं बहुधा : clean
p007:P4 जीवानन्दः तस्य : clean
p007:P5 "गुरुदेव! काशीप्राप्तिपर्यन्तम् : clean
p007:P6 निवारिता भवति : clean
p007:P7 "किमर्थं तथा : clean
p007:P8 "नगरे केचन : F13
p007:P9 जीवानन्दः मन्दहासं : F14
J1 p002:P9 {pb} -> p003:P2 {pc} : ok (काशीविश्वेश्वरस्य दर्शनार्थं joins)
J2 p003:P5 {pb} -> p003:P6 fresh : ok (clean break, arrival then glare)
J3 p003:P11 {pb} -> p004:P2 {pc} : ok (अर्पयन् speech continues)
J4 p004:P5 {pb} -> p004:P6 {pc} : ok (आहारः भविष्यामि joins)
J5 p004:P9 {pb} -> p005:P2 fresh : ok (clean break, return to forest)
J6 p005:P4 {pb} -> p005:P5 {pc} : ok (आचरन्तः आसन् joins)
J7 p005:P6 {pb} -> p006:P2 fresh : ok (clean break, next episode)
J8 p006:P5 {pb} -> p006:P6 {pc} : ok (मया निर्मितानां joins)
J9 p006:P8 {pb} -> p007:P2 {pc} : ok (किमपि न प्राप्तम् joins)
J10 p007:P5 {pb} -> p007:P6 {pc} : ok (बुभुक्षा निवारिता joins)
J11 p007:P9 {pb} -> END : continues-next-range (इति खेदम् mid-sentence, closes in p008 outside this range)

## Continuation 2026-11-15 — scan 8 appended (p008, story end)

Scan 8 (orphan, art bottom full-width) transcribed print-faithfully and appended after `{pgb: १६}` with `{pc}` continuation joint; no existing span altered. Images closed after transcription; this section proofreads the new span only.

- Proofread gate: `lint.py --phase proofread --story p002.md` → green (7 pages, 0 error paras). Extract gate notes only pre-existing `{del:}/{ins:}` verdicts in old spans (expected in Phase B).
- Orth: `scan.py orth` on deblocked story text → 0 hits.
- Findings: none. No `{del:}/{ins:}` or `{sug-…}` added to p008; print readings kept (स्वत्वं, इतोऽपि with ऽ for the S-shaped avagraha, पण्डितः/पाण्डित्यं, `.....` ellipsis before the closing quote).
- Quotes: P2 closes the p007:P9 speech across the page turn; P5→P6 speech spans the column turn via `{pb}/{pc}`; P3, P4, P7 open/close within their paras. All balanced.

Coverage (p008 only):
p008:P1 {x-com:layout: : skip layout chunk
p008:P2 {pc}अनुभवति किल? : clean (closes p007:P9 speech)
p008:P3 "धनव्ययविषये : clean
p008:P4 जीवानन्दः क्षणकालं : clean (..... kept as printed ellipsis)
p008:P5 "तन्नाम अहं : clean (opens, continues via column turn)
p008:P6 {pc}कारणतः मया : clean
p008:P7 "तथा न। : clean
p008:P8 कालान्तरे जीवानन्दस्य : clean
p008:P9 प्रबोधस्य पाण्डित्यं : clean (story ends; clean break)
J11 p007:P9 {pb} -> p008:P2 {pc} : ok (इति खेदम् अनुभवन् joins; prior "continues-next-range" now resolved)
J12 p008:P5 {pb} -> p008:P6 {pc} : ok (इति कारणतः joins across columns)
J13 p008:P9 {pb} -> END : ok (clean break, story end)
