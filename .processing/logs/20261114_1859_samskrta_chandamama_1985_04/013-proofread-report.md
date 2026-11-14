# Proofread report: 1985_04 p013 अन्धविश्वासः (वेतालकथा)

## Summary

Four findings, all of one kind: Trivikrama's closing speech opens on scan 17 (printed folio 22) and runs multi-paragraph across the page turn into scan 18, so each paragraph needed its own supplied double-quote pair for modern readability (print carries a single spanning pair). The Sanskrit orth scanner reported zero hits on deblocked text, and no word, sandhi, or morphology verdicts were issued because Phase A left no glyph flags and print spellings read grammatical in context. Extract residuals (Vetala frame quote spanning scans 14→15, Somasekhara speech spanning the scan 16 column turn, Trivikrama opening spanning scans 17→18) were all verified as print-faithful continuations. Nothing is held for the user.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p017:P2 तदा सः | तदा सः न जानाति स्म ... प्राप्नुयुः। (Trivikrama outer speech opened p016:P10, continued here via {pc}, paragraph ends with no close) | append {ins:"} at paragraph end | STY | style | high | Multi-para speech: every paragraph closes its own pair; page-turn halves stay joined via {pb}/{pc} but the paragraph still closes before the next fresh paragraph. |
| 2 | p017:P3 सोमशेखरः कश्चित् | सोमशेखरः कश्चित् ... ज्ञातवान् एव। (inside Trivikrama outer speech, no outer marks, contains inner '...' belief pair) | wrap paragraph with {ins:"} open at start and {ins:"} close at end | STY | style | high | Multi-para speech stands alone per paragraph; outer DQ pair required around the inner SQ belief so the paragraph is not read as narrator text. |
| 3 | p017:P4 सः चिन्तितवान् | सः चिन्तितवान् --- 'पुनः ... एव' इति। (thought report inside Trivikrama outer speech, no outer marks) | wrap paragraph with {ins:"} open at start and {ins:"} close at end | STY | style | high | Thought (चिन्तितवान्) correctly takes inner SQ; the containing Trivikrama paragraph needs its own outer DQ pair (DQ SQ ... SQ DQ nesting). |
| 4 | p017:P5 यदा लक्ष्मीधरेण | यदा लक्ष्मीधरेण ... विशेषज्ञानी"। (print close with no open in this paragraph) | prepend {ins:"} at paragraph start, pairing with the print close | STY | style | high | Closing paragraph of the multi-para Trivikrama speech; supplied open restores the per-paragraph DQ pair. |

## Patterns

- Multi-para Trivikrama speech (p016:P10 → p017:P2–P5): 4 locations (F1–F4). Print carries one spanning outer DQ pair across the page turn and fresh paragraph breaks; each paragraph now opens and closes its own pair via {ins:"}, with inner thoughts/beliefs kept as SQ ('रत्नकारणतः ...', 'पुनः ...'). Example locations: p017:P2 तदा सः, p017:P5 यदा लक्ष्मीधरेण.

## Unverified

None. No candidates held; orth scan clean and every residual resolved from text and house rules.

## Coverage

- p013:P1 : skip x-com:layout-only chunk
- p013:P2 : skip title heading
- p013:P3 त्रिविक्रमस्य पीडां : clean
- p014:P1 : skip x-com:layout-only chunk
- p014:P2 मार्गायासनिवारणार्थं कथां : clean
- p014:P3 एवं वदता : clean
- p014:P4 हानिवार्तां श्रुत्वा : clean
- p014:P5 अनन्तरं सः : clean
- p014:P6 सद्यः एव : clean
- p014:P7 भाग्यकारकं भवतु : clean
- p014:P8 एतस्य धारणेन : clean
- p014:P9 एतस्य रत्नस्य : clean
- p015:P1 : skip x-com:layout-only chunk
- p015:P2 लक्ष्मीधरस्य स्नेहितः : clean
- p015:P3 मित्रस्य वचनानां : clean
- p015:P4 इदानीं लक्ष्मीधरस्य : clean
- p015:P5 सोमशेखरः लक्ष्मीधरस्य : clean
- p015:P6 मञ्जूषातः नीलवर्णीयम् : clean
- p015:P7 क्रमशः एतस्य : clean
- p015:P8 लक्ष्मीधरः सहस्रं : clean
- p015:P9 केषाञ्चित् दिनानाम् : clean
- p015:P10 सत्यप्रभावः तु : clean
- p016:P1 : skip x-com:layout-only chunk
- p016:P2 इति उत्तरं : clean
- p016:P3 हानिः अनुभूता : clean
- p016:P4 लक्ष्मीधरः उदासीनभावनया : clean
- p016:P5 तदा सोमशेखरः : clean
- p016:P6 आम्, तत् : clean
- p016:P7 लक्ष्मीधरः। "मया : clean
- p016:P8 एतत् श्रुत्वा : clean
- p016:P9 वेतालः एवं : clean
- p016:P10 तदा त्रिविक्रमः : clean
- p017:P1 : skip x-com:layout-only chunk
- p017:P2 तदा सः : F1
- p017:P3 सोमशेखरः कश्चित् : F2
- p017:P4 सः चिन्तितवान् : F3
- p017:P5 यदा लक्ष्मीधरेण : F4
- p017:P6 एवं वदता : clean
- J1 p013:P3 {pb} -> p014:P2 {pc} (continues) : ok
- J2 p014:P4 {pb} -> p014:P5 fresh (clean break) : ok
- J3 p014:P9 {pb} -> p015:P2 {pc} (continues) : ok
- J4 p015:P6 {pb} -> p015:P7 {pc} (continues) : ok
- J5 p015:P10 {pb} -> p016:P2 {pc} (continues) : ok
- J6 p016:P6 {pb} -> p016:P7 fresh (clean break) : ok
- J7 p016:P10 {pb} -> p017:P2 {pc} (continues) : ok
- J8 p017:P3 {pb} -> p017:P4 fresh (clean break) : ok
- J9 p017:P6 {pb} -> END (clean break) : ok
