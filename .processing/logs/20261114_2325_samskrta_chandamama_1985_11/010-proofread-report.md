## Summary

12 findings: 6 error, 1 likely, 1 variant, 4 style. Systematic issues are vowel-sign slips in print (missing/extra matras, 4 instances) and print single-open/double-close dialogue sorts corrected to doubles where speech sense pins them (2 instances) plus one spurious tale-opening quote deleted. The whole range was read sentence by sentence for continuity with no ruptures; the `orth` scanner is clean (0 findings). Loc uses story coordinates `pNN:Pm` (lint chunk numbers) with the word index in the chunk plus anchor words; no corrected-text section (corrections travel as blocks).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p011:P3:w6 (अनन्तरं वेतालेन) | `कथा आरब्धा --- "रामपुरे` | `{del:"}` (drop the open) | STY | style | high | tale narration runs unquoted across fresh breaks (sibling issues print no mark here); a lone spanning open can never balance per-para, so the print mark is deleted rather than paired |
| 2 | p012:P3:w1 ({del:'}{ins:"}तर्हि भवान्) | `'तर्हि भवान् ... किल" इति उक्तवान्` | `"तर्हि भवान् ... किल"` | STY | style | high | direct speech pinned by `इति उक्तवान्` takes doubles; print mixes single-open/double-close, so the open sort is corrected |
| 3 | p012:P6:w13 (तदिने रात्रौ) | `प्रभावः पर्याप्तमात्रेण अस्ति` | `पर्याप्तः` | LEX | variant | medium* | odd formation, but interpretable as `पर्याप्त-मात्रेण`, so kept; the parallel same-page quote reads `पर्याप्तः` |
| 4 | p014:P4:w47 (शीतलस्य व्यवहारेण) | `नाम। विनायासं भवतः` | `विनायासेन` | MRP | likely | medium* | fused `विना आयासं` or instrumental `विनायासेन`; print ending unverified (crop cut), both hypotheses recorded |
| 5 | p014:P5:w19 (मन्त्रिणः वचनं) | `एतत् न अङ्गीकरोति` | `अङ्गीकरोति` | SPL | error | medium* | the denominative needs long `ी` (`अङ्गीकृ`) as in p016 `अङ्गीकृत्य` |
| 6 | p014:P7:w3 (मन्त्री एतत्) | `मन्त्री एतत् अङ्गीकृतवान्` | `अङ्गीकृतवान्` | SPL | error | medium* | same long-`ी` rule as F5 |
| 7 | p014:P7:w7 (मन्त्री एतत्) | `आगत्य उत्सहेन श्रीपालाय` | `उत्साहेन` | SPL | error | high* | `उत्सहेन` is not a word; `उत्साहेन` (instrumental of `उत्साह`) certain from context |
| 8 | p014:P8:w14 ('शीतलः यदि) | `भविष्यति' इति चिन्तितवान्` | `चिन्तितवान्` | SPL | error | high* | `चिन्तितवान्` is not a form; `चिन्तितवान्` (`चिन्त्` + `क्तवतु`) certain, and the same text prints `चिन्तितवान्` at p016 |
| 9 | p015:P10:w30 (श्रीपालस्य वचनेन) | `स्वबन्धुविषये निर्लिप्सः` | `निर्लिप्तः` | SPL | error | high* | `निर्लिप्स` is unattested; `निर्लिप्तः` (detached) certain from context |
| 10 | p015:P11:w10 (गृहम् आगतः) | `पूर्वं किम्` + `किन्तु भवतः` across J11 | `?` | STY | style | medium | Shitala interrupts Sripala (`मम` = Shitala's; `आवेशेन` supports it); print shows no break, kept as seen |
| 11 | p016:P4:w8 (वेतालः एवं) | `"राजन्! श्रापालस्य` | `श्रीपालस्य` | CNS | error | high* | `श्रापालः` occurs nowhere else; `श्रीपालः` everywhere else in the story |
| 12 | p016:P5:w5 (तदा त्रिविक्रमः, →p016:P7) | `'श्रीपालसदृशाः ... ते चिन्तयन्ति। / शीतलः यदा ... इत्येव" इति।` | `{del:'}{ins:"}...{ins:"} / {ins:"}..."` (open corrected, per-para close/open supplied) | STY | style | high | outer Trivikrama speech pinned by `उक्तवान्` + closing `इति` takes doubles: open sort corrected at P5, per-para close supplied at P6 end and per-para open at P7 start; P7 inner `'...'` pairs nest validly inside |

## Patterns

- Vowel-sign slips in print (count 4: F7, F8, F5, F6-in-part): a missing `ा` (`उत्सहेन`), an extra `ति` (`चिन्तितवान्`), short `ि` for `ी` twice (`अङ्गीकरोति`, `अङ्गीकृतवान्` against p016 `अङ्गीकृत्य`).
- Print single/double sort slips corrected to doubles (count 2: F2, F12): spoken `इति उक्तवान्` spans opening with `'` closed with `"`; p015:P5 `"भवान् निराशः न' ... एव'"` already parses as valid `DQ SQ ... SQ DQ` nesting and needed no change.

## Unverified

- F3 `पर्याप्तमात्रेण`: native-speaker judgment on the formation; kept as variant either way.
- F4 `विनायासं`: re-examine the print ending at 3x or tighter (`सं` vs `सेन` vs split `विना आयासं`).
- F5/F6 `अङ्गीकरोति`, `अङ्गीकृतवान्`: print re-check (`ङ्गि` vs `ङ्गी`) with p016 `अङ्गीकृत्य` as control.
- F7 `उत्सहेन`: dictionary check of `उत्साह` aside, print re-check of `हे` vs `हो` already crop-verified; user acceptance of the held pair settles it.
- F8 `चिन्तितवान्`: print re-check of the `ति`/`तवान्` boundary at 3x or tighter.
- F9 `निर्लिप्सः`: dictionary check (`निर्लिप्त` attested, `निर्लिप्स` not) plus print re-check (`प्त` vs `प्स`).
- F11 `श्रापालस्य`: story consistency (`श्रीपाल` x20+) already settles the reading; user acceptance of the held pair settles it.

## Coverage

p010:P1 skip (x-com) / p010:P2 skip (title) / p010:P3 'आरब्धम् उत्तमजनाः : clean / p010:P4 skip (category) / p011:P1 skip (x-com) / p011:P2 {pc}परिहृतः भवेत् : clean / p011:P3 अनन्तरं वेतालेन : F1 / p011:P4 कदाचित् ग्रामे : clean / p011:P5 एतत् सिंहासनं : clean / p011:P6 सार्वजनिकतया एतस्य : clean / p011:P7 'तत् सिंहासनं : clean / p011:P8 अत्रान्तरे सिंहासनविषये : clean / p011:P9 शीतलस्य बन्धुः : clean / p011:P10 तदा श्रीपालः : clean / p012:P1 skip (x-com) / p012:P2 {pc}भवतः प्रयत्नः : clean / p012:P3 {del:'}{ins:"}तर्हि भवान् : F2 / p012:P4 तदा मन्दहासपूर्वकं : clean / p012:P5 शीतलः श्रीपालस्य : clean / p012:P6 तदिने रात्रौ : F3 / p012:P7 {pc}लघुसाहाय्यं भवान् : clean / p012:P8 "एतत् तु : clean / p012:P9 'श्रीपालद्वारा कार्यं : clean / p013:P1 skip (x-com) / p013:P2 तदिने रात्रौ : clean / p013:P3 शीतलस्य वचनं : clean / p013:P4 अनन्तरदिने सः : clean / p013:P5 {pc}वान् सा : clean / p013:P6 महाराजः तत्क्षणे : clean / p013:P7 सन्तुष्टः श्रीपालः : clean / p013:P8 निराशः शीतलः : clean / p013:P9 वीरभद्रः उक्तवान् : clean / p013:P10 अनन्तरदिने प्रातःकाले : clean / p014:P1 skip (x-com) / p014:P2 {pc}विचित्रव्यवहारेण मन्त्रिणः : clean / p014:P3 "महानुभाव! मान्त्रिकसिंहासनं : clean / p014:P4 शीतलस्य व्यवहारेण : F4 / p014:P5 मन्त्रिणः वचनं : F5 / p014:P6 {pc}तत् प्रकोष्ठं : clean / p014:P7 मन्त्री एतत् : F6, F7 / p014:P8 'शीतलः यदि : F8 / p015:P1 skip (x-com) / p015:P2 {pc}उक्तवान् इति : clean / p015:P3 श्रीपालस्य वचनेन : clean / p015:P4 शीतलः श्रीपालस्य : clean / p015:P5 "भवान् निराशः : clean / p015:P6 "यदि भवान् : clean / p015:P7 "मम तु : clean / p015:P8 "वस्तुतः भवतः : clean / p015:P9 {pc}मान्त्रिकसिंहासनस्य दर्शनार्थम् : clean / p015:P10 श्रीपालस्य वचनेन : F9 / p015:P11 गृहम् आगतः : F10 / p016:P1 skip (x-com) / p016:P2 {pc}किन्तु भवतः : F10 / p016:P3 एतेन उत्तरेण : clean / p016:P4 वेतालः एवं : F11 / p016:P5 तदा त्रिविक्रमः : F12 / p016:P6 {pc}व्यवहारे प्रवेशः : F12 / p016:P7 {ins:"}शीतलः यदा : F12 / p016:P8 एवं वदता : clean.

J1 p010:P3 {pb} -> p011:P2 {pc} (continues) : ok / J2 p011:P5 {pb} -> p011:P6 fresh (clean break) : ok / J3 p011:P10 {pb} -> p012:P2 {pc} (continues) : ok / J4 p012:P6 {pb} -> p012:P7 {pc} (continues) : ok / J5 p012:P9 {pb} -> p013:P2 fresh (clean break) : ok / J6 p013:P4 {wb} -> p013:P5 {pc} (continues) : ok / J7 p013:P10 {pb} -> p014:P2 {pc} (continues) : ok / J8 p014:P5 {pb} -> p014:P6 {pc} (continues) : ok / J9 p014:P8 {pb} -> p015:P2 {pc} (continues) : ok / J10 p015:P8 {pb} -> p015:P9 {pc} (continues) : ok (pc-after-complete confirmed: same open quote, no indent) / J11 p015:P11 {pb} -> p016:P2 {pc} (continues) : ok (speaker shift Shitala-interrupts-Sripala, see F10) / J12 p016:P5 {pb} -> p016:P6 {pc} (continues) : ok (multi-para speech per-para pair supplied, see F12) / J13 p016:P8 {pb} -> END (clean break) : ok.

Gate-note dispositions: proofread gate is fully clean (0 error paras, 0 story findings, all pages clean). Per-para notes verify against the joints above: paired-continuations at p011:P2, p012:P2/P7, p013:P5, p014:P6, p015:P2/P9, p016:P2; quotes-open-past-pb at p010:P3, p011:P10, p012:P6, p013:P4, p014:P5/P8, p015:P11 pairing into their {pc} continuations; mid-para-imbalance notes are intra-para nesting states resolved at story level (p011:P3, p012:P3, p016:P3, p016:P5, p016:P7 now balanced via F1, F2, F12); pc-after-complete at p015:P8 confirmed at J10.
