# Proofread report: 1986_11 p002 (scans 2–5, राजलक्षणम्)

## Summary

Range p002 (4 spans, scans 2–5) transcribes a complete royal-trial episode: Vikramasena's twin sons, a year of exile, the rescue of Pallavī from a well, the minister's garland test, and Vijaya's consecration. Two held candidates, both `likely` / `medium` / `unverified*`: a proper-noun spelling split (F1) and an adjective-noun gender mismatch (F2). No systematic problem, no unchecked passage (every chunk read sentence by sentence for continuity), and the text is hand transcription, not OCR. Orth scan (`scan.py orth`) is clean; `lint --phase proofread` exits 0. `Loc` is `pNN:Pm` plus the chunk's first two words, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p002:P5 यथा राजा w8 | `भद्रवती राज्ये` | `{sug-del:भद्रवती}{sug-ins:भद्रावती}` | CNS | likely | medium* | Same kingdom spelled `भद्रावती` in p002:P3 and p004:P7, so one form is a slip |
| 2 | p005:P5 विक्रमसेनः एतत्सर्वं w4 | `एकं सत्यसङ्गतिं` | `{sug-del:एकं}{sug-ins:एकां}` | AGR | likely | medium* | Feminine `सङ्गति` accusative needs feminine `एकाम्`, not neuter `एकम्` |

## Unverified

F1 held: `भद्रवती` vs `भद्रावती` is a one-matraa difference never flagged in Phase A and images stay closed, so the glyph cannot be re-settled; a gazetteer or the issue's later pages would fix the intended spelling. F2 held: `एकं` for `एकाम्` assumes `सत्यसङ्गति` is feminine (ति-stem abstracts are), but a lexicon check of `सङ्गति` gender plus the print glyph (ं vs ां) would settle it.

## Coverage

p002:P1 layout-only : skip x-com-only
p002:P2 title : skip title
p002:P3 विक्रमसेनराजः भद्रावतीराज्यं : clean
p002:P4 विक्रमसेनः यथा : clean
p002:P5 यथा राजा : F1
p002:P6 मम मरणानन्तरं : clean
p002:P7 विक्रमसेनः उत्तमगुरुं : clean
p002:P8 विजयः चतुरः : clean
p002:P9 कठिनाः समस्याः : clean
p002:P10 अनन्तः एतद्विरुद्धः : clean
p002:P11 author-only : skip metadata
p003:P1 layout-only : skip x-com-only
p003:P2 पुत्रयोः एतं : clean
p003:P3 देशे विद्यमानान् : clean
p003:P4 समीपे स्थितस्य : clean
p003:P5 झटिति तौ : clean
p003:P6 राजकुमारौ द्वौ : clean
p003:P7 तस्याः अद्भुतं : clean
p003:P8 विजयः तां : clean
p003:P9 तदा सा : clean
p004:P1 layout-only : skip x-com-only
p004:P2 आगतवती ताभिः : clean
p004:P3 तत्क्षणे एव : clean
p004:P4 अनन्तस्य अपि : clean
p004:P5 मनसि उत्पन्नां : clean
p004:P6 वर्षात्मकं प्रवासं : clean
p004:P7 तत् श्रुत्वा : clean
p004:P8 अनन्तविजययोः समक्षं : clean
p004:P9 पल्लवी शिरश्चालनपूर्वकम् : clean
p004:P10 तत् दृष्ट्वा : clean
p004:P11 पल्लवी शिरः : clean
p005:P1 layout-only : skip x-com-only
p005:P2 मन्दस्मितः विजयः : clean
p005:P3 अनन्तः शिरः : clean
p005:P4 पि मम : clean
p005:P5 विक्रमसेनः एतत्सर्वं : F2
p005:P6 कालक्रमेण विक्रमसेनः : clean
p005:P7 अनन्तः तु : clean
J1 p002:P6 {pb} -> p002:P7 {pc} continues : ok
J2 p002:P10 {pb} -> p003:P2 fresh clean break : ok
J3 p003:P3 {pb} -> p003:P4 fresh clean break : ok
J4 p003:P9 {pb} -> p004:P2 {pc} continues : ok
J5 p004:P7 {pb} -> p004:P8 fresh clean break : ok
J6 p004:P11 {pb} -> p005:P2 fresh clean break : ok
J7 p005:P3 {wb} -> p005:P4 {pc} continues : ok
J8 p005:P7 {pb} -> END clean break : ok
