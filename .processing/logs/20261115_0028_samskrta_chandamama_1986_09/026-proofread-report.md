## Summary

Story `कथाकल्पनम्` (1986_09, p26--p29; 4 pages, 31 body chunks). Proofread gate passes; `scan.py orth` on deblocked text reports no hits. No `{sug-ins:}`/`{sug-del:}` queue was inherited from Phase A. Two findings, both `STY`/`style`: one column-turn speech pair (p028 P6--P7) split at a sentence boundary, closed per paragraph with supplied `{ins:"}` marks. Two print quirks are kept as seen with no blocks (Phase B invents no glyph claims without a Phase A marker on file): `विदूषकस्य मुख दृष्टवान्` (J2 join, accusative `-म्` absent in print) and `शीलेन्द्रवर्मणः` (p027:P3, single `शी-` against six `शैलेन्द्र-` elsewhere). Text is otherwise clean as printed; all remaining quote pairs are balanced (doubles throughout for reported speech, no thought-passages needing singles).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p028:P6 (तदा विदूषकः) | `राज्यं स्यात् नाम।` (speech left open at column turn) | `राज्यं स्यात् नाम।"` (supplied via `{ins:"}`) | STY | style | high | column-turn speech split at a sentence boundary; each paragraph closes its own pair |
| 2 | p028:P7 (किन्तु वर्धनः) | `किन्तु वर्धनः यथाशक्ति` (continuation opens without a mark) | `"किन्तु वर्धनः यथाशक्ति` (supplied via `{ins:"}`) | STY | style | high | mate of F1; each paragraph opens its own pair (page-turn continuation is the only exception) |

## Patterns

None.

## Unverified

None.

## Coverage

- p026:P1 {x-com:layout: ...} : skip layout-only chunk
- p026:P2 # कथाकल्पनम् : skip title chunk
- p026:P3 कोसलदेशस्य राजा : clean
- p026:P4 राजा पण्डितम् : clean
- p026:P5 यद्यपि वत्सदेशविषये : clean
- p026:P6 {pc}--- "एवं : clean
- p026:P7 तदा शोधकः : clean
- p026:P8 तस्य वचनेन : clean
- p026:P9 {author: श्रीमाता} : skip author metadata chunk
- p027:P1 {x-com:layout: ...} : skip layout-only chunk
- p027:P2 {pc}मुख दृष्टवान् : clean
- p027:P3 शीलेन्द्रवर्मणः वचनस्य : clean
- p027:P4 शोधकस्य वचनेन : clean
- p027:P5 {pc}किल प्रतिक्रिया : clean
- p027:P6 विदूषकस्य वचनं : clean
- p027:P7 तदा राजा : clean
- p027:P8 "प्रभो! कल्पितकथायाः : clean
- p027:P9 विदूषकस्य वचने : clean
- p028:P1 {x-com:layout: ...} : skip layout-only chunk
- p028:P2 {pc}एव। अतः : clean
- p028:P3 राजा विदूषकं : clean
- p028:P4 "महाराज! प्रियवाक्यकथनम् : clean
- p028:P5 "भवतः वचनस्य : clean
- p028:P6 तदा विदूषकः : F1
- p028:P7 {ins:"}किन्तु वर्धनः : F2
- p028:P8 राजा किमपि : clean
- p028:P9 राजा मन्दहासं : clean
- p028:P10 "तत् तु : clean
- p029:P1 {x-com:layout: ...} : skip layout-only chunk
- p029:P2 {pc}भवान् वत्सदेशविषये : clean
- p029:P3 "एवं प्रियवाक्यानि : clean
- p029:P4 "प्रकृतसन्दर्भविषये : clean
- p029:P5 {pc}विदूषकः। : clean
- p029:P6 शैलेन्द्रवर्मा किञ्चित्कालम् : clean
- p029:P7 भटः लतामण्डपसमीपं : clean
- p029:P8 एतद्विषये आश्चर्यं : clean
- p029:P9 "एवं तर्हि : clean
- J1 p026:P5 {pb} -> p026:P6 {pc} : ok (one sentence; mdash introduces the quoted reply)
- J2 p026:P8 {pb} -> p027:P2 {pc} : ok (spaced join विदूषकस्य मुख दृष्टवान्; accusative -म् absent in print, kept as seen, see Summary)
- J3 p027:P4 {pb} -> p027:P5 {pc} : ok (gerund ज्ञात्वा continues into the quoted question; one speech across the column turn)
- J4 p027:P9 {pb} -> p028:P2 {pc} : ok (ज्ञातवान् एव। sentence boundary across the page turn)
- J5 p028:P6 {pb} -> p028:P7 fresh : F1, F2 (clean break at terminal danda; quote pair supplied per paragraph)
- J6 p028:P10 {pb} -> p029:P2 {pc} : ok (अतः एव भवान् unique fit; page-turn speech pair left open per the exception)
- J7 p029:P4 {pb} -> p029:P5 {pc} : ok (उक्तवान् विदूषकः। speaker-name completion)
- J8 p029:P9 {pb} -> END : ok (terminal danda; story ends, next range starts p030)
