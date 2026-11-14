## Summary

4 findings: 1 style pattern applied as verdicts at 8 speech spans (print singles upgraded to doubles, high confidence), and 3 held grammar candidates (medium confidence, unverified). The systematic issue is the print's quote sort: single quotes mark all reported speech here, against the era house doubles, so speech spans were upgraded wherever a reporting verb plus इति-closure pins them; two thought spans keep print singles. The Sanskrit orth scanner reported 0 hits on deblocked text and both lint gates (extract, proofread) exit 0, so the text reads as clean composed print with no OCR damage; the three held items are print-faithful oddities needing user decision. Loc below is word-level: `pNN:Pm` chunk plus word index counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p039:P6 दूरदर्शी महाद्वारम् w15 (+7 spans, see Patterns) | `'भोः! ... प्रविशतु'` | `"भोः! ... प्रविशतु"` | STY | style | high | reporting verb उक्तवान् plus इति-closure pins speech, so print singles upgrade to doubles for readability |
| 2 | p039:P3 द्वीपेषु पुष्करद्वीपः w51 | `मम मद्राज्यस्य च` | `मम मदीयराज्यस्य च` | MRP | likely | medium* | मद् plus राज्यस्य is no valid genitive; dittography of मम/मत् or slip for मदीयराज्यस्य; held for user |
| 3 | p040:P3 दूरदर्शी अतीव w25-27 | `भवतां राज्यस्य जनताः` | `भवतो राज्यस्य जनाः` | AGR | likely | medium* | genitive plural भवतां with genitive singular राज्यस्य and plural जनताः mixes number; sense needs people of your kingdom; held |
| 4 | p040:P8 भोः! कौञ्चमन्त्रिन्! w4 | `राज्यस्याः` | `राज्यस्थाः` | SPL | likely | medium* | non-word as seen; one-conjunct slip स्य/स्थ for those in the kingdom agreeing with सर्वे; held |

## Patterns

- P1 quote-sort singles-for-speech (8 spans upgraded open+close, 16 blocks): p039:P6 दूरदर्शी महाद्वारम् w15/w34, p039:P7 दूरदर्शी राजानं w8/w32, p040:P3 दूरदर्शी अतीव w20/w30, p040:P4 राजन्! अस्माकं w1/w25, p040:P7 उक्तवन्तः --- w3/w16, p040:P8 भोः! कौञ्चमन्त्रिन्! w1/w8, p040:P9 कौञ्चमन्त्री उत्तरं w5/w39, p040:P10 पराजितः पुष्करराजः w5/w10. Thought spans keep print singles: p039:P3 w45/w69 (भावना), p039:P4 w1/w12 (विचिन्त्य).

## Unverified

- F2 `मद्राज्यस्य`: a classical-parallel search (मत्54852राज्य compounds) or the user's acceptance of `मदीयराज्यस्य` would settle it; print verified as seen at 4x in Phase A.
- F3 `भवतां राज्यस्य जनताः`: checking whether this issue ever prints plural जनताः for जनता elsewhere, or accepting `भवतो राज्यस्य जनाः`, would settle it.
- F4 `राज्यस्याः`: accepting `राज्यस्थाः` (agreeing with सर्वे ... चोराः) would settle it; glyphs verified as स्याः at 4x in Phase A.

## Coverage

- p039:P3 द्वीपेषु पुष्करद्वीपः : F2
- p039:P4 'किन्तु आवयोः : clean
- p039:P5 वान्। प्रपञ्चे : clean
- p039:P6 दूरदर्शी महाद्वारम् : F1
- p039:P7 दूरदर्शी राजानं : F1
- p039:P1 {x-com:layout...} : skip layout-only chunk
- p039:P2 # चतुरः : skip title chunk
- p039:P8 {note:...} : skip footer metadata chunk (reprint line, quotes balanced inside node)
- p040:P2 एतत् श्रुत्वा : clean
- p040:P3 दूरदर्शी अतीव : F1, F3
- p040:P4 'राजन्! अस्माकं : F1
- p040:P5 उत्तरं श्रुत्वा : clean
- p040:P6 तदा पुरुषम् : clean
- p040:P7 उक्तवन्तः प्रभो : F1
- p040:P8 'भोः! कौञ्चमन्त्रिन्! : F1, F4
- p040:P9 कौञ्चमन्त्री उत्तरं : F1
- p040:P10 पराजितः पुष्करराजः : F1
- p040:P11 एवं वामनः : clean
- p040:P1 {x-com:layout...} : skip layout-only chunk
- J1 p039:P3 {pb} -> p039:P4 fresh (clean break) : ok
- J2 p039:P4 {wb} -> p039:P5 {pc} (continues) : ok (प्रेषितवान् joins across column turn; thought quote balanced across the join)
- J3 p039:P5 {pb} -> p039:P6 fresh (clean break) : ok
- J4 p039:P6 {pb} -> p039:P7 fresh (clean break) : ok
- J5 p039:P7 {pb} -> p040:P2 fresh (clean break) : ok (page turn; edge ends with terminal punct plus close quote)
- J6 p040:P2 {pb} -> p040:P3 fresh (clean break) : ok
- J7 p040:P3 {pb} -> p040:P4 fresh (clean break) : ok
- J8 p040:P4 {pb} -> p040:P5 fresh (clean break) : ok
- J9 p040:P5 {pb} -> p040:P6 fresh (clean break) : ok
- J10 p040:P6 {pb} -> p040:P7 {pc} (continues) : ok (भटाः उक्तवन्तः joins across column turn; speech quote opens in P7)
- J11 p040:P7 {pb} -> p040:P8 fresh (clean break) : ok
- J12 p040:P8 {pb} -> p040:P9 fresh (clean break) : ok
- J13 p040:P9 {pb} -> p040:P10 fresh (clean break) : ok
- J14 p040:P10 {pb} -> p040:P11 fresh (clean break) : ok
- J15 p040:P11 {pb} -> END (clean break) : ok
