# Proofread report: 1986_04 p018 (pp. 18-24, नागकन्या / वेतालकथा)

## Summary

Range p018-p024 (7 page spans, 48 body chunks) proofread with images closed; extract gate and proofread gate both pass (exit 0), orth scanner reports zero hits on deblocked text. 8 findings: 2 error (agreement/formation), 4 style (quote punctuation), 2 likely (held candidates). The systematic issues are quote-sort slips (one interior thought printed in doubles, one long nested instruction missing inner singles) and two gender/formation slips in predicates. Two low-certainty forms are held as `{sug-…}` candidates for human review. `जातिवैरः` (p023:P9) was checked and left as printed. No passages left unchecked; the text is a manual transcription, not OCR output. Loc below is `pNN:Pm` (scan-sequence page + lint chunk) with the chunk's first two words and the 1-based word number on the raw chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p019:P4 तस्य युवकस्य w10 | `बाल्यं सर्वैभवं यापयित्वा` | `बाल्यं सवैभवं यापयित्वा` | OCR | likely | medium* | `सर्वैभवं` is not a Sanskrit word; smallest fix is `सवैभवं` (with luxury), alt `सर्ववैभवं` |
| 2 | p019:P7 गृहे माता w43 | `च "अहो!` (thought) | `च 'अहो!` | STY | style | high | interior thought closed by `इति चिन्तितवती` takes singles, not doubles |
| 3 | p019:P7 गृहे माता w48 | `अस्ति!" इति चिन्तितवती` | `अस्ति!' इति चिन्तितवती` | STY | style | high | close of the F2 thought pair must match its single open |
| 4 | p020:P3 "मम नाम w6 | `अहं न मानवस्त्रीः,` | `अहं न मानवस्त्री,` | MRP | error | high | predicate nominative of feminine `स्त्री` has no visarga; neighbours `कौमुदी`/`नागकन्या` are bare |
| 5 | p021:P5 धीरचन्द्रः मातुः w53 | `कौमुदी असमर्थाः भवति` | `कौमुदी असमर्था भवति` | AGR | error | high | feminine singular subject needs `असमर्था`, not masculine plural `असमर्थाः` |
| 6 | p022:P5 शूरगुप्तः आगत्य w30 | `अतः यावत् पिता` | `अतः 'यावत् पिता` | STY | style | high | first-person `शक्नोमि` utterance nested in speech takes inner single open |
| 7 | p022:P5 शूरगुप्तः आगत्य w37 | `न शक्नोमि इति तां` | `न शक्नोमि' इति तां` | STY | style | high | close of the F6 inner pair at its `इति` boundary |
| 8 | p023:P4 "भवन्तं परिणीय w41 | `कृपया मां क्षाम्यतु` | `कृपया मां क्षमतु` | MRP | likely | medium* | `क्षाम्यतु` is no form of `क्षम्`; expected 3rd-sg imperative `क्षमतु` (with `भवान्`), alt passive `क्षम्यताम्` |

## Patterns

- Quote punctuation (4x: F2, F3, F6, F7): one thought printed in speech doubles and one nested first-person instruction left without inner singles; both fixed per the speech-vs-thought sort rule.
- Predicate formation (2x: F4, F5): a visarga added to a feminine `ई`-stem predicate and a masculine-plural adjective on a feminine subject.

## Unverified

- F1 (`सर्वैभवं`): medium* — two single-glyph fixes compete (`सवैभवं` vs `सर्ववैभवं`); no dictionary check done. Settles with an enlarged glyph re-check of the scan plus a lexicon check of the `सवैभवं` idiom.
- F8 (`क्षाम्यतु`): medium* — `क्षमतु` vs passive `क्षम्यताम्` both fit the `भवान्` address. Settles with a scan re-check of the `क्षाम्य` conjunct plus a paradigm check of `क्षम्` imperatives.

## Coverage

- p018:P1 {x-com:layout:} : skip layout-only
- p018:P2 # नागकन्या : skip title
- p018:P3 'एषः राजा : clean
- p018:P4 {category: वेतालकथा} : skip metadata
- p019:P1 {x-com:layout:} : skip layout-only
- p019:P2 एकदा कौमुदी : clean
- p019:P3 'अहो! अत्रत्याः : clean
- p019:P4 तस्य युवकस्य : F1
- p019:P5 औषधार्थं धनं : clean
- p019:P6 किङ्कर्तव्यतामूढः धीरचन्द्रः : clean
- p019:P7 गृहे माता : F2, F3
- p020:P1 {x-com:layout:} : skip layout-only
- p020:P2 कौमुदी तम् : clean
- p020:P3 "मम नाम : F4
- p020:P4 धीरचन्द्रः स्वीयकष्टानि : clean
- p020:P5 नागकन्यायाः वचनं : clean
- p020:P6 "अस्तु तावत्। : clean
- p020:P7 एतावत्पर्यन्तं दृष्टं : clean
- p020:P8 नागकन्या प्रत्यक्षीभूय : clean
- p020:P9 "एतेन धनेन : clean
- p020:P10 तद्दिनादारभ्य धीरचन्द्रस्य : clean
- p021:P1 {x-com:layout:} : skip layout-only
- p021:P2 दासानुदासीजनाः नियुक्ताः। : clean
- p021:P3 धीरचन्द्रः किमपि : clean
- p021:P4 शूरगुप्तः स्वार्थपरः। : clean
- p021:P5 धीरचन्द्रः मातुः : F5
- p021:P6 दशमीदिने धीरचन्द्रः : clean
- p021:P7 तस्य वचनसमनन्तरमेव : clean
- p022:P1 {x-com:layout:} : skip layout-only
- p022:P2 रोगाणां निवारणं : clean
- p022:P3 तथा उक्त्वा, : clean
- p022:P4 नागमूलद्वारा धीरचन्द्रस्य : clean
- p022:P5 शूरगुप्तः आगत्य, : F6, F7
- p022:P6 पूर्णिमादिने धीरचन्द्रः : clean
- p022:P7 तस्याम् एव : clean
- p022:P8 प्रत्यागतवान्। पत्युः : clean
- p022:P9 शूरगुप्तः एतान् : clean
- p023:P1 {x-com:layout:} : skip layout-only
- p023:P2 नियमान् न : clean
- p023:P3 पञ्चमीदिने धीरचन्द्रः : clean
- p023:P4 "भवन्तं परिणीय : F8
- p023:P5 "अहम् इच्छामि : clean
- p023:P6 तस्याः अङ्गीकारं : clean
- p023:P7 "अहं तु : clean
- p023:P8 "तस्य कारणम् : clean
- p023:P9 तस्य वचनं : clean
- p023:P10 धीरचन्द्रः तस्याः : clean
- p024:P1 {x-com:layout:} : skip layout-only
- p024:P2 ष्यामि" इति : clean
- p024:P3 वेतालः अत्र : clean
- p024:P4 तदा त्रिविक्रमः : clean
- p024:P5 प्रधानम्। धनाभावात् : clean
- p024:P6 एवंरीत्या यदा : clean
- J1 p018:P3 -> p019:P2 fresh : ok
- J2 p019:P4 -> p019:P5 fresh : ok
- J3 p019:P7 -> p020:P2 fresh : ok
- J4 p020:P7 -> p020:P8 {pc} : ok
- J5 p020:P10 -> p021:P2 {pc} : ok
- J6 p021:P3 -> p021:P4 fresh : ok
- J7 p021:P7 -> p022:P2 {pc} : ok
- J8 p022:P7 -> p022:P8 {pc} : ok
- J9 p022:P9 -> p023:P2 {pc} : ok
- J10 p023:P4 -> p023:P5 fresh : ok
- J11 p023:P10 -> p024:P2 {pc} : ok
- J12 p024:P4 -> p024:P5 {pc} : ok
- J13 p024:P6 -> END : ok
