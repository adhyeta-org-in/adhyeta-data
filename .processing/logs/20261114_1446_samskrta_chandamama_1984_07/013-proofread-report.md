## Summary

Story बुद्धिपरिवर्तनम् (वेतालकथा), scans 13--18, 6 page spans, 11 joints. 9 findings: 1 error (print-glyph emendation, high confidence) and 8 style (supplied per-para quote marks for modern readability, all sense-pinned). Loc is `pNN:Pm:w` (scan sequence page, chunk number matching lint P numbers, word counted on the chunk from 1) plus a two-word anchor. The systematic issue is spanning print quote pairs: the sabotage-scene speeches use singles and the frame speeches doubles, each spanning several paragraphs, so the missing per-para mates were supplied via `{ins:'}`. Scanner `orth` gave 1 hit (a legitimate print `!`) dismissed after context check. No held candidates; nothing below high confidence.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p018:P7:32 `मैथिल्या गज्ञः` | `तदा मैथिल्या गज्ञः उपरि` | `{del:गज्ञः}{ins:राज्ञः}` | OCR | error | high | `गज्ञः` is meaningless; syntax needs `राज्ञः` (accusation upon the king), रā-stroke lost in type |
| 2 | p016:P6:38 `मम लज्जा` | `लज्जा आसीत्।` + close | `{ins:'}` after `आसीत्।` | STY | style | high | close the `यदि`-speech para so each para opens and closes its own pair |
| 3 | p016:P7:1 `सहपाठिनः पितामही` | para opens without mark | `{ins:'}` before `सहपाठिनः` | STY | style | high | open the continued `यदि`-speech para to pair with its print close in `कृतम्'` |
| 4 | p018:P3:13 `तस्य व्यवहारः` | `व्यवहारः अस्ति।` + close | `{ins:'}` after `अस्ति।` | STY | style | high | close trivikrama's opening para (reporting verb `उक्तवान्` pins the speech) |
| 5 | p018:P4:1 `दुष्टं बुद्धिहीनम्` | para has no marks | `{ins:'}` before `दुष्टं` and after `एव।` | STY | style | high | speech para needs its own pair between sentence boundaries |
| 6 | p018:P5:1 `अवमानयन्ती मैथिली` | para has no marks | `{ins:'}` before `अवमानयन्ती` (closes at P6 end via J10) | STY | style | high | speech para needs its own open; column-turn `{pc}` carries it to P6 |
| 7 | p018:P6:5 `च द्योतयति` | `द्योतयति।` + close | `{ins:'}` after `द्योतयति।` | STY | style | high | close the pair opened at P5 start across the J10 column turn |
| 8 | p018:P7:1 `राजसभायां सधैर्यम्` | para has no marks | `{ins:'}` before `राजसभायां` and after `एव।` | STY | style | high | speech para needs its own pair between sentence boundaries |
| 9 | p018:P8:1 `एतेन कारणेन` | para closes without open | `{ins:'}` before `एतेन` | STY | style | high | open to pair with the print close in `प्रसृता'` before the `इति` closure |

## Patterns

1. Spanning print quote pairs (8 of 9 findings, F2--F9): one opening mark serves 2--6 paragraphs in print (sabha speeches in singles at p015--p017, trivikrama's reply in singles at p018:P3--P8, वासन्तिका's reply at p016:P6--P7); each paragraph now carries its own pair, e.g. p016:P6:38, p018:P4:1, p018:P7:1. Sorts unchanged from print.
2. House/print spelling variants kept as seen, no blocks: `तद्दिने` (p014) vs `तद्दिने` (p017); `सधैर्यं` (p015) vs `सधैर्यम्` (p018); `वासन्तिका`/`वासन्तिका`; open sandhi `तद् दिने`-style forms and `यत्कृत` (p017) read as grammatical headless relative, left untouched.

## Unverified

None. The single Phase A candidate (`गज्ञः`/`राज्ञः`) was promoted to a verified verdict (F1); clause-level re-segmentation was tested for it and no rival reading fits. No item is held for the user.

## Coverage

p013:P2 बुद्धिपरिवर्तनम् : skip title
p013:P3 अन्यत्र कुत्रापि : clean
p013:P4 वेतालकथा : skip metadata
p014:P2 वासन्तिका इति : clean
p014:P3 मैथिली वासन्तिका : clean
p014:P4 एकदा वृष्ट्यभावात् : clean
p014:P5 युद्धं कृत्वा : clean
p014:P6 कीर्तिसेनः अपि : clean
p014:P7 कीर्तिसेनः एवम् : clean
p014:P8 नदी शुष्का : clean
p014:P9 एतत् श्रुत्वा : clean
p015:P2 आसीत् सा : clean
p015:P3 कीर्तिसेनः प्रवृत्तम् : clean
p015:P4 एकस्य उपरि : clean
p015:P5 कः सः : clean
p015:P6 यः असहायाम् : clean
p015:P7 वदामि भोः : clean
p015:P8 चकितः कीर्तिसेनः : clean
p015:P9 मैथिली दृढस्वरेण : clean
p015:P10 अपि संशयम् : clean
p015:P11 मैथिल्याः वचनम् : clean
p015:P12 राजसभायाम् सर्वेषाम् : clean
p016:P2 सभ्याः राजभीत्या : clean
p016:P3 किञ्चित्कालं चिन्तयित्वा : clean
p016:P4 मैथिल्याः सौन्दर्येण : clean
p016:P5 मैथिली यदा : clean
p016:P6 कलायाः सहपाठिनम् : F2
p016:P7 सहपाठिनः पितामही : F3
p016:P8 मैथिली भगिनीम् : clean
p017:P2 यत्कृत तद्विषये : clean
p017:P3 मैथिली नूतनवधूवरयोः : clean
p017:P4 कीर्तिसेनः हसन् : clean
p017:P5 प्रेषितवान् : clean
p017:P6 तद्दिने एव : clean
p017:P7 वेतालः एवम् : clean
p018:P2 यदि भवान् : clean
p018:P3 तदा त्रिविक्रमः : F4
p018:P4 दुष्टं बुद्धिहीनम् : F5
p018:P5 अवमानयन्ती मैथिली : F6
p018:P6 कीर्तिसेनस्य विवेकम् : F7
p018:P7 राजसभायां सधैर्यम् : F1, F8
p018:P8 एतेन कारणेन : F9
p018:P9 एवम् उक्त्वा : clean
J1 p013:P3 -> p014:P2 : ok (मैथिली वासन्तिका, spaced continuation)
J2 p014:P4 -> p014:P5 : ok (यथाशक्ति युद्धं, column turn)
J3 p014:P9 -> p015:P2 : ok (सभायाम् आसीत्, page turn)
J4 p015:P9 -> p015:P10 : ok (सर्वे अपि, column turn)
J5 p015:P12 -> p016:P2 : ok (clean break, new scene)
J6 p016:P5 -> p016:P6 : ok (सङ्गीतकलायाः, solid word-break)
J7 p016:P8 -> p017:P2 : ok (भवत्या यत्कृत, page turn, speech span kept)
J8 p017:P4 -> p017:P5 : ok (तां प्रेषितवान्, column turn)
J9 p017:P7 -> p018:P2 : ok (उत्तरं यदि, page turn, question span kept)
J10 p018:P5 -> p018:P6 : ok (एतत् कीर्तिसेनस्य, column turn)
J11 p018:P9 -> END : ok (clean story end, vetala flies off)
