# Proofread report — 1985_02 p019 (scans 19–20) — RUN 20261114_1849_samskrta_chandamama_1985_02

## Summary

Range scans 19–20; two-page complete story `साधकलक्षणम्` (Keshavasvami interviews Ramabhadra then Shivachandra; landlord appoints Shivachandra). 5 findings, all inherited Phase A `{sug-del}/{sug-ins}` pairs held as written (story file left byte-identical; no verdict blocks promoted since the transcriber is gone and images stay closed): 3 error (F1, F2 OCR non-words; F5 MRP agreement) + 2 likely (F3, F4 repeated SPL spelling); the systematic problems are the non-word cluster in Shivachandra's first speech (F1/F2) and the twice-identical `प्राधम्यम्` for `प्राधान्यम्` in the same `कस्य ___` frame (F3/F4); no passage left unchecked and the sentence-by-sentence continuity read found no ruptures; the text is careful manual transcription, not OCR (`scan.py orth`: 0 findings on 19 deblocked lines). Loc below is story coordinates `pNN:Pm` (NN = scan-sequence page, Pm = lint chunk number in file order) plus word index w counted on the file chunk from 1 with each paired block occupying one slot (del side) plus the first two words as anchor; Conf `*` means procedurally held for the user (images stayed closed for all of Phase B; no new verdict without print re-check). Proofread gate exits 0 (`p019: clean`, `p020: clean`, `summary: 2 pages, 0 error paras, 0 story findings`); quote pass finds every speech span balanced (doubles for `उक्तवान्`-speech kept, two short `पृष्टवान्`-questions in singles kept print-faithful per the no-churn instruction, multi-page Ramabhadra speech closes across J2); proper nouns are consistent throughout (`केशवस्वामी/शिवचन्द्र/रामभद्र/भूस्वामिन्`).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p020:P4w7 (तदा शिवचन्द्रः) | `यस्याः कस्याः अपि ममस्यायाः` | `समस्यायाः` | OCR | error | high* | `ममस्यायाः` is no word and `यस्याः कस्याः अपि` demands the feminine genitive `समस्यायाः` (picked up by `तस्याः`); held. |
| F2 | p020:P4w8 (तदा शिवचन्द्रः) | `ममस्यायाः परिष्कारनः पूर्वं` | `परिष्कारात्` | OCR | error | high* | `परिष्कारनः` is no case form and the `X-ात् पूर्वम्` idiom pins the ablative `परिष्कारात्`; held. |
| F3 | p020:P4w32 (तदा शिवचन्द्रः) | `तेषु कस्य प्राधम्यम् इत्यादिक्रमम्` | `प्राधान्यम्` | SPL | likely | high* | `प्राधम्यम्` is unattested for "precedence" while the `कस्य ___ इत्यादिक्रमम् निर्धार्य` frame (same as F4) pins standard `प्राधान्यम्`; held. |
| F4 | p020:P8w6 ("वैशिष्ट्यम् अस्ति।) | `कस्य प्राधम्यम् उचितम्` | `प्राधान्यम्` | SPL | likely | high* | Same repeat as F3: `कस्य ___ उचितम्` needs "priority" = `प्राधान्यम्`; held. |
| F5 | p020:P8w14 ("वैशिष्ट्यम् अस्ति।) | `तत्सम्बन्धि प्रश्नान्` | `तत्सम्बन्धीन्` | MRP | error | high* | Bare-stem `तत्सम्बन्धि` cannot modify accusative plural `प्रश्नान्`; the `तत्सम्बन्धिन्` stem requires `तत्सम्बन्धीन्`; held. |

## Patterns

Repeated spelling `प्राधम्यम्` for `प्राधान्यम्` ×2 in the identical `कस्य ___` frame (F3 in Shivachandra's speech, F4 in Keshavasvami's report of it — the repetition itself corroborates one systematic press/author form, still held for print check). Print/house forms kept without blocks as variants: `एवंरीत्या` (lexicalised); open junctions `यस्याः कस्याः अपि`, `तस्याः सम्बन्धे`, `तस्याः निर्वहणरीतिं`, `एतत् एव`, `अन्वेषणे अपि` (consistent open-sandhi house style, cf. sibling ranges); doubles for `उक्तवान्`-statements with singles kept for the two short `पृष्टवान्`-questions (`'भवान् कथं परिष्करोति'`, `'किं द्वौ अपि समानौ वा?'`); detached-speech `---` before `"आर्य` kept as printed.

## Unverified

F1 `ममस्यायाः`→`समस्यायाः` (high*): settle by a 3× re-check that the initial glyph is truly `म` not `स`, or another copy of the issue. F2 `परिष्कारनः`→`परिष्कारात्` (high*): settle by a 3× re-check of `नः` versus `त्` in the conjunct. F3/F4 `प्राधम्यम्`→`प्राधान्यम्` (high*): settle by a 3× re-check of `धम्य` versus `धान्य` at both spots (rule out consistent authorial coinage against a dictionary). F5 `तत्सम्बन्धि`→`तत्सम्बन्धीन्` (high*): settle by a 3× re-check for a dropped `न्` after `तत्सम्बन्धि` before `प्रश्नान्`.

## Coverage

p019:P1 {x-com:layout: 2col, : skip (layout chunk, transparent to pairing).
p019:P2 # साधकलक्षणम् : skip (title).
p019:P3 चन्द्रपुरस्य भूस्वामिनः : clean (frame set; `क्तवतु` actives `अपेक्षितवान्/प्राप्तवान्/आरब्धवान्` correct).
p019:P4 एतं वृत्तान्तं : clean (dual `आगतवन्तौ/निवेदितवन्तौ/आदिष्टवान्` agreement intact).
p019:P5 केशवस्वामी प्रथमं : clean (doubles speech opens `पश्यतु भोः`, spans J1; `भिन्नभिन्नरूपाः` kept).
p019:P6 अन्यसमस्यायाः परिहारसमये : clean (J1 continuation; close `भवति" इति उक्तवान्` verified).
p019:P7 तदा रामभद्रः : clean (`--- "आर्य` balanced; `पर्याप्तम् अनुभवं` kept).
p019:P8 "सर्वे अपि : clean (long doubles question-speech opens, closes `वदति वा?" इति पृष्टवान्`; honorific `भवान् + अनुसरति/वदति` 3rd-sg correct).
p019:P9 "अहं परिष्कारयोग्याम् : clean (doubles speech opens; `गृहीत्वा/निश्चित्य` ल्यप् choice correct; spans J2).
p019:P10 {author: भामहः}{pgb} : skip (footer + page-end marker).
p020:P1 {x-com:layout: 2col, : skip (layout chunk).
p020:P2 निश्चित्य, अनन्तरम् : clean (J2 continuation `निर्वहणरीतिं→निश्चित्य` object→absolutive fit; Ramabhadra close `भवति" इति उक्तवान्` verified).
p020:P3 तं प्रेषयित्वा : clean (singles `'भवान् कथं परिष्करोति'` kept print-faithful as short reported question).
p020:P4 तदा शिवचन्द्रः : F1, F2, F3 (doubles speech `"अहं ... ग्रहीष्यामि" इति उक्तवान्` balanced; `कांश्चन/निर्धार्य/ग्रहीष्यामि` correct).
p020:P5 तम् अपि : clean (ends `{pb}`, spans J3; singles `'किं द्वौ अपि` opens, kept).
p020:P6 समानौ वा? : clean (J3 continuation `द्वौ अपि→समानौ` dual fit; singles close `वा?' इति पृष्टवान्` verified; doubles reply `"तथा न प्रभो! ... भविष्यति" इति उक्तवान्` balanced).
p020:P7 "एवं वा? : clean (doubles landlord question balanced, `तादृशवैशिष्ट्यं` kept).
p020:P8 "वैशिष्ट्यम् अस्ति। : F4, F5 (doubles Keshavasvami reply `"... भावयामि" इति उक्तवान्` balanced; `समालोच्य/तर्कयित्वा/उत्थाप्य` ल्यप् correct; `चिन्तनीयानि` agrees with `समाधानानि`).
p020:P9 वृद्धसचिवस्य वचनं : clean (closing sentence; J4 clean break at range end).
J1 p019:P5 {pb} -> p019:P6 {pc} : ok (एकस्याः समस्यायाः परिहारः + अन्यसमस्यायाः ..., subject→predicate spans column turn, spaced join).
J2 p019:P9 {pb} -> p020:P2 {pc} : ok (निर्वहणरीतिं + निश्चित्य, accusative object→absolutive, spaced join across page turn).
J3 p020:P5 {pb} -> p020:P6 {pc} : ok (किं द्वौ अपि + समानौ वा, dual subject→dual predicate spans column turn, spaced join).
J4 p020:P9 {pb} -> END : ok (clean break, story ends with ।; bottom art illustrates closing appointment scene).
