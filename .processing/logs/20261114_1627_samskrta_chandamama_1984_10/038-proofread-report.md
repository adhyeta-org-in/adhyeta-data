# Proofread report: वञ्चकः (1984_10, p038, RUN 20261114_1627_samskrta_chandamama_1984_10)

## Summary

Story वञ्चकः spans scans 38--40 (3 page sections, 20 body chunks). Two findings, both punctuation (STY, style severity, high confidence), each carried as a verdict block in the story file; no silent changes. Three orthographic observations (वणिक्, कृषिकः, दारिद्रयकारणतः) are held as unverified without blocks since their print glyphs were settled in Phase A. The orth scanner (`scan.py orth`) is clean (29 lines, 0 hits); the text is hand transcription, not OCR. Proper nouns (राघवः, रामनाथः) are consistent and open/joined sandhi mix is kept as house style throughout.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p038:P8 w1 (पञ्चाशतरूप्यकाणि दातुम्) | `पञ्चाशतरूप्यकाणि दातुम् अपि राघवः मयि न विश्वसिति" इति` (closing mark with no opening mark) | `{ins:"}` at para start, i.e. `"पञ्चाशतरूप्यकाणि दातुम् ... विश्वसिति"` | STY | style | high | Reported thought closed by इति needs an opening mark; position pinned at para start like the reference `{ins:"}` case |
| F2 | p039:P5 end (anchor भवतः बुद्धिः) | `उक्तवान् रामनाथः।'` (lone single mark after the danda) | `{del:'}` (mark carried in the block alone, per the `{del:'}{ins:"}` precedent) | STY | style | high | Single stroke verified at 3x in Phase A but with no open, no speech/thought role and a complete `"` pair already closed before इति; no mate can be supplied so the stray is deleted |

## Patterns

None (no repeats; the two findings are distinct singletons).

## Unverified

| # | Loc | Form | Note | Conf | What would settle it |
|---|---|---|---|---|---|
| U1 | p038:P3 (गोविन्दपुरे राघवः) | `वणिक्` | Nonstandard for `वणिज्` (merchant); no block emitted since the print glyph was settled as वणिक् in Phase A and Phase B invents no new glyph claims | medium* | Editor ruling whether to hold print or direct a `{sug-del:वणिक्}{sug-ins:वणिज्}` candidate; dictionary confirms only वणिज् |
| U2 | p038:P4 (तस्मिन् ग्रामे) | `कृषिकः` | Nonstandard for `कृषकः` (farmer); no block for the same reason as U1 | medium* | Same as U1; dictionary confirms only कृषकः/कर्षकः |
| U3 | p038:P4 (तस्मिन् ग्रामे) | `दारिद्रयकारणतः` | Nonstandard for `दारिद्र्यकारणतः`; minimal change य to ्य; no block for the same reason as U1 | medium* | Same as U1; dictionary confirms दारिद्र्य |

## Coverage

p038:P1 {x-com:layout} : skip layout-only chunk
p038:P2 # वञ्चकः : skip title
p038:P3 गोविन्दपुरे राघवः : clean
p038:P4 तस्मिन् ग्रामे : clean
p038:P5 एकदा रामनाथः : clean
p038:P6 राघवः अतीव : clean
p038:P7 {pc}नीया अस्ति : clean
p038:P8 पञ्चाशतरूप्यकाणि दातुम् : F1
p038:P9 राघवः कथं : clean
p038:P10 {note} : skip footer metadata
p039:P1 {x-com:layout} : skip layout-only chunk
p039:P2 अन्ते एकः : clean
p039:P3 एकस्मिन् दिने : clean
p039:P4 एषः रामनाथः : clean
p039:P5 भवतः बुद्धिः : F2
p039:P6 पञ्चाशत् षष्टिः : clean
p039:P7 {pc}श्रुत्वा तत्र : clean
p039:P8 जनसमूहम् उद्दिश्य : clean
p039:P9 रामनाथस्य प्रतिपादनशैलीं : clean
p040:P1 {x-com:layout} : skip layout-only chunk
p040:P2 {pc}समीपे धनं : clean
p040:P3 तदा रामनाथः : clean
p040:P4 रामनाथस्य अभिनयः : clean
p040:P5 सर्वे मिलित्वा : clean
p040:P6 {pc}सर्वस्वापहारः तु : clean
p040:P7 इतोऽपि विवादः : clean
p040:P8 यदा धनं : clean
p040:P9 एतेन प्रसङ्गेन : clean
J1 p038:P6 {wb} -> p038:P7 {pc} : ok (शोच + नीया solid word join)
J2 p038:P9 {pb} -> p039:P2 fresh : ok (clean break, new para)
J3 p039:P6 {pb} -> p039:P7 {pc} : ok (विवादं श्रुत्वा spaced join)
J4 p039:P9 {pb} -> p040:P2 {pc} : ok (मम समीपे completes the question)
J5 p040:P5 {pb} -> p040:P6 {pc} : ok (same crowd speech continues, open mark at प्रथमं closes at ददातु)
J6 p040:P9 {pb} -> END : ok (story ends complete)
