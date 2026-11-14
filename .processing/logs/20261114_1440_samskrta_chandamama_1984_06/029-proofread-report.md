# Proofread report: 1984_06 p029 (अविवेकः, pp. 29–32)

## Summary

Range START=29, END=32 (4 scan pages, story अखण्ड: title p29 through सुखान्तम् ending p32). 3 findings: 1 error (MRP, high), 2 style (STY quote punctuation, high). Systematic: print uses single-stroke quotes for both speech and thought (kept as seen; only defective marks corrected); open-sandhi variants (व्यापारार्थम्, एतत् द्वीपम्) kept as house style; रजाकः used consistently as short form of अब्दुर्रजाकः after the introduction. No OCR used at any stage (eyes + PIL crops only); Phase B worked images-closed from text. Loc is `pNN:Pm` (scan sequence + chunk number within page span, chunks counted with layout/title/footer per the in-file `## Joints` index) plus the first two words as anchor, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p030:P9 एकस्मिन् दिने | `पत्नीं तं बालकं दृष्ट्वा` | `पत्नी तं बालकं दृष्ट्वा` | MRP | error | high | क्त्वा/उक्त्वा share one subject (the wife); the agent must be nominative |
| 2 | p032:P2 राजा किञ्चित्कालं | `इति अहं जानामि। एनं प्रथमं` | `इति अहं जानामि। 'एनं प्रथमं` | STY | style | high | direct speech resumes after जानामि। with no opening mark; supplied at the certain position |
| 3 | p032:P5 राजा तत् | `'अहो! तर्हि` | `"अहो! तर्हि` | STY | style | high | opening single mismatched with the double close in P6; speech takes the double |

## Patterns

- P1 single-stroke print quotes kept (17 balanced pairs): speech and thought both print as `'...'` (e.g. p029:P5 `'रजाकः समुद्रव्यापारे...`, p030:P7 `'यदा कदा वा...`, p031:P8 `'...जागरूकः भवामि'`); only the defective marks F2/F3 were touched.
- P2 open-sandhi house variants kept, never flagged: `व्यापारार्थम् नौकया` (p031:P3), `एतत् द्वीपम् प्राप्तवान्` (p032:P8).

## Unverified

None held; every Phase A residual was ruled from text (F1–F3 above, rest kept as print-faithful).

## Coverage

p029:P1 {x-com:layout: : skip (layout)
p029:P2 # अविवेकः : skip (title)
p029:P3 बेल्ला-नगरे अब्दुर्रजाकः : clean
p029:P4 तस्य समीपे : clean
p029:P5 'रजाकः समुद्रव्यापारे : clean
p029:P6 विचारान् श्रुतवान् : clean
p029:P7 एवम् एव : clean
p029:P8 कानिचित् दिनानि : clean
p029:P9 {category: अरेबिया : skip (footer)
p030:P1 {x-com:layout: : skip (layout)
p030:P2 तौ यमलौ : clean
p030:P3 तौ यमलौ : clean
p030:P4 अत्यन्तं कुपितः : clean
p030:P5 रजाकस्य पत्नी : clean
p030:P6 रजाकः आकस्मिकतया : clean
p030:P7 तथापि 'यदा : clean
p030:P8 एवम् एव : clean
p030:P9 एकस्मिन् दिने : F1
p031:P1 {x-com:layout: : skip (layout)
p031:P2 सा बालकम् : clean
p031:P3 एवम् एव : clean
p031:P4 कनिष्ठः पुत्रः : clean
p031:P5 सः राजा : clean
p031:P6 एतत् दृष्ट्वा : clean
p031:P7 एकस्मिन् दिने : clean
p031:P8 इति कृत्वा : clean
p031:P9 प्रातः ते : clean
p032:P1 {x-com:layout: : skip (layout)
p032:P2 राजा किञ्चित्कालं : F2
p032:P3 रजाकः अपि : clean
p032:P4 "किं वदामि : clean
p032:P5 राजा तत् : F3
p032:P6 कारागृहे निक्षिप्तः : clean
p032:P7 ज्येष्ठः पुत्रः : clean
p032:P8 एषः च : clean
p032:P9 एवं तेषां : clean
J1 p029:P5 {wb} -> p029:P6 {pc} : ok (विशेषविचारान्, column turn)
J2 p029:P8 {pb} -> p030:P2 fresh : ok (page turn, clean break)
J3 p030:P3 {pb} -> p030:P4 fresh : ok (column turn, accusation then wrath in narrative order)
J4 p030:P9 {pb} -> p031:P2 {pc} : ok (page turn, उक्त्वा continues)
J5 p031:P7 {pb} -> p031:P8 {pc} : ok (column turn, thought continues)
J6 p031:P9 {pb} -> p032:P2 fresh : ok (page turn, clean break)
J7 p032:P5 {pb} -> p032:P6 {pc} : ok (column turn, speech continues)
J8 p032:P9 {pb} -> END : ok (story ends सुखान्तम्/यापितवान्)
