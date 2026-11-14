# Proofread report: 1985_04 story p040 (START 40, scans 40–40)

## Summary

5 findings, all error/high, and every verdict is already applied in the story file; both the extract gate and the proofread gate pass. The systematic problem is small print slips in the opening paragraph and in the hero's name (dropped ौ, dropped म, intrusive व, ी/ा swap). All 8 speeches print in balanced doubles and needed no quote work; no passage was left unchecked and nothing is held unverified. The text is a human print transcription from a 300 DPI scan, not OCR output; the Sanskrit orth scan reports 0 hits. Loc = story coordinates p40:Pm (lint chunk numbers) with first-two-word anchor; w = word index in chunk (blocks excluded).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p40:P3 (समुद्रगुप्तः धनगुप्तः) w4 | `च सिरिपुरस्थ वणिजौ` | `{del:सिरिपुरस्थ}{ins:सिरिपुरस्थौ}` | AGR | error | high | dual वणिजौ needs the dual adjective सिरिपुरस्थौ; print lacks ौ (bare stem verified at 6x, no visarga) |
| 2 | p40:P3 (समुद्रगुप्तः धनगुप्तः) w9 | `परस्परं मैत्रा आसीत्` | `{del:मैत्रा}{ins:मैत्री}` | SPL | error | high | मैत्री (f.) is the nominative subject of आसीत्; मैत्रा is no nominative form (ी/ा matra slip) |
| 3 | p40:P3 (समुद्रगुप्तः धनगुप्तः) w18 | `सञ्चारं कुर्वतः स्म` | `{del:कुर्वतः}{ins:कुरुतः}` | SPL | error | high | तौ dual with स्म needs the finite dual कुरुतः (present+स्म past idiom); participle कुर्वतः has no slot here (intrusive व) |
| 4 | p40:P5 ("भीतिः मास्तु।) w12 | `इति ससुद्रगुप्तः सूचितवान्` | `{del:ससुद्रगुप्तः}{ins:समुद्रगुप्तः}` | SPL | error | high | ससुद्रगुप्तः is meaningless; समुद्रगुप्तः 6x elsewhere in this story (dropped म, verified at 5x) |
| 5 | p40:P9 (तदा कटिभागे) w2 | `तदा ससुद्रगुप्तः कटिभागे` | `{del:ससुद्रगुप्तः}{ins:समुद्रगुप्तः}` | SPL | error | high | same dropped-म slip as F4; same character, same fix |

## Patterns

- Dropped-म in the hero's name (2 cases: F4, F5): both mid-story समुद्रगुप्तः tokens print as ससुद्रगुप्तः while the other six tokens (including समुद्रगुप्तं in the adjacent sentence) print समुद्र-; both corrected to समुद्रगुप्तः.
- House forms kept as seen (no findings): mixed open/joined sandhi (`तत् वज्रद्वयम्`, `सोऽपि`-free text uses इतोऽपि with avagraha), print hyphens (`तदा-आवयोः`, `अपहृत्य-गच्छेत्`), mdash pauses (`धनगुप्तं --- "प्राणानाम्`, `उक्तवान् --- तस्य`), double-accusative प्रदर्श्य + समुद्रगुप्तं, and ad-sensum `विंशतिः वज्राणि सन्ति`.

## Unverified

None — every Phase A candidate was promoted to a verdict on grammar plus story-context evidence; no item is held for the user.

## Coverage

- p040:P1 {x-com:layout} : skip layout-only
- p040:P2 वास्तविकं रहस्यम् : skip title
- p040:P3 समुद्रगुप्तः धनगुप्तः : F1, F2, F3
- p040:P4 एकदा तौ : clean
- p040:P5 "भीतिः मास्तु। : F4
- p040:P6 परेद्युः धनगुप्तस्य : clean
- p040:P7 समुद्रगुप्तः धनगुप्तः : clean
- p040:P8 तदा समुद्रगुप्तः : clean
- p040:P9 तदा कटिभागे : F5
- p040:P10 समुद्रगुप्तः स्वीयकट्यां : clean
- J1 p040:P10 -> END : ok (clean break; story closes with इति।, no rupture, no moves)
