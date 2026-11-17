# Proofread report: 1987_07 story p046 (pages 46-48, मूर्खः ज्योतिषिकः)

## Summary

5 findings: 4 error/high verdicts already landed as blocks in the story file (3 stray single quote marks deleted, 1 missing speech close supplied), plus 1 likely/medium* held candidate (चारनायकः vs चोरनायकः) left as `{sug-del:}`/`{sug-ins:}` for the user. Systematic problems: lone single quote strokes with no mate and no quotative frame (3x, Pattern P1); otherwise the file is clean — Sanskrit orth scan reports no hits, quote sorts follow house style (doubles speech, singles thought, one deliberation in doubles kept as printed per p01 precedent), and all six joints are continuous. Glyph questions were settled in Phase A with 3-5x crops (images stayed closed throughout Phase B); the text is a print transcription, not OCR output. Loc below is `pNN:Pm:wK` (scan page, lint chunk, word index on the chunk) with the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p046:P4:w23 [एतस्य ज्योतिषिकस्य] | `एते' यत्किमपि` | `एते यत्किमपि` | STY | error | high | Single mark with no mate inside an already paired single-quoted thought; readability drops it (verdict `{del:'}` in file). |
| F2 | p046:P7:w15 [चोरनायकस्य ज्योतिषे] | `भवेम। इति उक्तवान्` | `भवेम।" इति उक्तवान्` | STY | error | high | Speech opened with `"` must close before the इति-closure with the reporting verb (verdict `{ins:"}` in file). |
| F3 | p047:P9:w3 [भित्तौ रन्ध्रं] | `रन्ध्रं 'कृत्वा सर्वे` | `रन्ध्रं कृत्वा सर्वे` | STY | error | high | Lone single with no quotative frame; participial narration needs no mark (verdict `{del:'}` in file). |
| F4 | p048:P9:w5 [मुग्धः ज्योतिषिकः] | `सर्वं 'निवेदितवान्। तत्` | `सर्वं निवेदितवान्। तत्` | STY | error | high | Lone single opening an indirect report with no close; following तत् shows indirect narration (verdict `{del:'}` in file). |
| F5 | p047:P7:w1 [चारनायकः ज्योतिषिकस्य] | `चारनायकः ज्योतिषिकस्य` | `चोरनायकः ज्योतिषिकस्य` | CNS | likely | medium* | Same thief-leader is चोरनायकः three times elsewhere, but चार is a real word so print may intend it; held for human ruling (held `{sug-del:}`/`{sug-ins:}` in file). |

## Patterns

P1 lone stray singles (3x: F1, F3, F4): single high quote strokes verified in print at 3-5x but with no mate and no quotative frame; each deleted via `{del:'}` with the sentence reading cleanly without it.

## Unverified

F5 चारनायकः vs चोरनायकः (Conf medium*): glyphs verified as चार (no ो-matra at 2x); context favors चोरनायकः 3:1 for the same referent, but चार (spy/wanderer) is meaningful. Settles with an editor ruling or a check of how this character is titled elsewhere in the issue.

## Coverage

p046:P1 : skip layout x-com-only chunk
p046:P2 : skip title
p046:P3 कस्मिंश्चित् अरण्ये : clean
p046:P4 एतस्य ज्योतिषिकस्य : F1
p046:P5 इदानीं ज्योतिषिकस्य : clean
p046:P6 उपायः स्फुरितः : clean
p046:P7 चोरनायकस्य ज्योतिषे : F2
p046:P8 अस्तु तावत् : clean
p046:P9 एवं ज्योतिषिकः : clean
p047:P1 : skip layout x-com-only chunk
p047:P2 स्म। एवं : clean
p047:P3 एवम् एव : clean
p047:P4 स्वकीयाम् इच्छां : clean
p047:P5 तदा चोरनायकः : clean
p047:P6 ज्योतिषिकः एतत् : clean
p047:P7 चारनायकः ज्योतिषिकस्य : F5
p047:P8 निश्चिते समये : clean
p047:P9 भित्तौ रन्ध्रं : F3
p048:P1 : skip layout x-com-only chunk
p048:P2 तद्दिने एकादशीं : clean
p048:P3 किञ्चित्कालानन्तरं चोराः : clean
p048:P4 तदा चोराः : clean
p048:P5 तिष्ठन्तु भोः : clean
p048:P6 साग्रहम् उक्तवान् : clean
p048:P7 पूजार्हस्य ज्योतिषिकस्य : clean
p048:P8 घण्टानादं श्रुत्वा : clean
p048:P9 मुग्धः ज्योतिषिकः : F4
J1 p046:P5 -> p046:P6 : ok
J2 p046:P9 -> p047:P2 : ok
J3 p047:P6 -> p047:P7 : ok
J4 p047:P9 -> p048:P2 : ok
J5 p048:P5 -> p048:P6 : ok
J6 p048:P9 -> END : ok
