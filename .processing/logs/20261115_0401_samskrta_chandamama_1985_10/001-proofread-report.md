# Proofread report: 1985_10, START=1 END=1 (p001)

## Summary

Single-page story `अजामिळः` (one scan, 8 chunks, 5 body paragraphs). One finding: F1 `SPL` error at high confidence (print `काश्चित्` for required feminine `काञ्चित्`), routed as a `{del:}/{ins:}` verdict in the story file. Scanner `orth` hits (10x `non-classical-letter` for `ळ`) are the print's consistent house-spelling of the name `अजामिळः` and stand as seen. All quote spans are balanced in print with sorts kept; no flow rupture at the single joint. Loc counts deblocked words on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p001:P5 w20 (तेषां स्वेच्छान्यवहारेण) | `आचरन्तीं काश्चित् स्त्रियं` | `काञ्चित्` | SPL | error | high | feminine accusative agreeing with `स्त्रियं` needs `काञ्चित्`; print sets `श्चि` for `ञ्चि` (Phase A 3x crop) |

## Unverified

None. No candidates held; F1 is high-confidence (agreement rule plus Phase A glyph verification).

## Coverage

p001:P1 : skip layout declaration (x-com only, no story text)
p001:P2 : skip series-header metadata ({category: पुराणगाथावली})
p001:P3 # अजामिळः : skip story title
p001:P4 पूर्वम् कन्याकुब्जे : clean
p001:P5 तेषां स्वेच्छान्यवहारेण : F1
p001:P6 वार्धक्ये अजामिळः : clean
p001:P7 यमदूतदेवदूतानां सम्भाषणं : clean
p001:P8 तदारभ्य अजामिळस्य : clean
J1 p001:P8 {pb} -> END (clean break) : ok
