## Summary
Seven findings: six `error` at high confidence (two glyph promotions from Phase A candidates, three quote-sort corrections on direct speech, one supplied opening quote for a lone print close) and one `likely` at medium confidence (sort correction of a double-quoted thought to house singles). Systematic issue is punctuation sort: era-standard doubles for speech vs singles for thought, with three speeches printed single and one thought printed double. Orth scan (`scan.py orth`) on deblocked text reported one hit (`शक्तिः!`, Latin-`!`-for-danda) dispositioned as print-faithful exclamation. No held candidates; nothing left unverified. Text is manual transcription, not OCR output.

## Findings
| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p31:P5 तस्यां रात्रौ | `मिखितवन्तौ` | `{del:मिखितवन्तौ}{ins:मिलितवन्तौ}` | OCR | error | high | `मिखित` is no word; dual `मिलितवन्तौ` agrees with `उभावपि` |
| 2 | p31:P5 तस्यां रात्रौ | `समीप्रे` | `{del:समीप्रे}{ins:समीपे}` | OCR | error | high | `समीप्रे` is no word; `समीपे गत्वा` recurs in this story |
| 3 | p31:P2 अलसः मित्रं | `'` open before `मित्र!` | `{del:'}{ins:"}` | STY | error | high | direct speech (`पृष्टवान्` + `इति`) needs era double; print close is already double |
| 4 | p32:P9 अलसः पूर्वं | `'` open before `भूरिभोजनम्` | `{del:'}{ins:"}` | STY | error | high | direct speech (`उक्तवान्` + `इति`); all other speeches print double |
| 5 | p32:P9 अलसः पूर्वं | `'` close after `आगतवान्` | `{del:'}{ins:"}` | STY | error | high | pairs with F4; speech needs era double |
| 6 | p32:P8 अनन्तरं रात्रौ | missing open before `यतः` | `{ins:'}` | STY | error | high | lone print close needs its mate; `यतः...सन्ति` is the only span `इति` closes |
| 7 | p31:P8 भूरिभोजनं समाप्तम् | `"मया अलसः वञ्चितः"` | `{del:"}{ins:'}` on both marks | STY | likely | medium | thought (`चिन्तयन्तौ`) and parallel thought print single; print shows clean doubles so emphasis remains possible |

## Patterns
- Proper-noun alternation `रजाक` / `राजक` for one character, kept as printed variants (e.g. `रजाकः पृष्टवान्` p31:P2 vs `राजकः उत्साहं` p31:P4, `राजकस्य गृहं` p31:P7 vs `रजाकस्य गृहम्` p30:P3). No finding; sense unaffected.
- Print `!` marks exclamatory sentences (3x: `पश्यति!` p29:P8, `शक्तिः!` p30:P8, `भो मित्र!` p31:P6); orth-scan hit on `शक्तिः!` checked print-faithful, not danda.
- Three line-wrap hyphens joined solid in transcription (`पञ्चरजतनाणकानि` p30:P4-P5, `पञ्चषष्टिरजतनाणकानि` p30:P5, `पञ्चत्रिंशत्नाणकानि` p30:P5); solid base forms attested in-story.

## Unverified
None. Every Phase A candidate was promoted to a verdict; no word held for the user.

## Coverage
p29:P1 layout : skip x-com-only chunk
p29:P2 कुशाग्रमतिः : skip title heading
p29:P3 फिराजनगरस्य समीपे : clean
p29:P4 रजाकः एकाकी : clean
p29:P5 किमपि नासीत् : clean
p29:P6 अतः एकस्मिन् : clean
p29:P7 एवं ज्ञात्वा : clean
p29:P8 अपरेधुः रजाकः : clean
p29:P9 category : skip category metadata chunk
p30:P1 layout : skip x-com-only chunk
p30:P2 पात्रं नास्ति : clean
p30:P3 अलसस्तु 'अहं : clean
p30:P4 दूरे आगच्छन्तम् : clean
p30:P5 नाणकानि द्वारे : clean
p30:P6 अलसः समीपे : clean
p30:P7 अलसस्य एवं : clean
p30:P8 'किन्तु प्रातःसमये : clean
p31:P1 layout : skip x-com-only chunk
p31:P2 अलसः मित्रं : F3
p31:P3 "समीपे स्थितां : clean
p31:P4 "किम्? एवं : clean
p31:P5 तस्यां रात्रौ : F1, F2
p31:P6 आदिशत्। अनन्तरं : clean
p31:P7 अलसः कुटीरं : clean
p31:P8 भूरिभोजनं समाप्तम् : F7
p31:P9 रजाकः भोजनशालातः : clean
p32:P1 layout : skip x-com-only chunk
p32:P2 अलसेन स्थापितं : clean
p32:P3 अलसः अपि : clean
p32:P4 ततः अष्टवादनसमये : clean
p32:P5 उपाहारमन्दिरतः प्रस्थाय : clean
p32:P6 जातः तदा : clean
p32:P7 शयितस्य लघु : clean
p32:P8 अनन्तरं रात्रौ : F6
p32:P9 अलसः पूर्वं : F4, F5
p32:P10 तत्क्षणे एव : clean
J1 p29:P4 {pb} -> p29:P5 {pc} : ok
J2 p29:P8 {pb} -> p30:P2 {pc} : ok
J3 p30:P4 {wb} -> p30:P5 {pc} : ok
J4 p30:P8 {pb} -> p31:P2 fresh : ok
J5 p31:P5 {pb} -> p31:P6 {pc} : ok
J6 p31:P9 {pb} -> p32:P2 {pc} : ok
J7 p32:P5 {pb} -> p32:P6 {pc} : ok
J8 p32:P10 {pb} -> END : ok
