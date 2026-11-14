# Proofread report: 1984_06 p048 (समर्थः), RUN 20261114_1440_samskrta_chandamama_1984_06

## Summary

5 findings: 2 verified quote-sort verdicts (both marks of one nested speech-in-speech corrected single-to-double, outer single kept as print) plus 3 held candidates (2 lexical/orthographic, 1 anusvāra). Systematic issue is only the nested-quote sort in the closing tale-within-tale; the rest are isolated. No passages left unchecked; images stayed closed for the whole phase per the Phase B rule. The text was transcribed from print (not OCR output); `scan.py orth` on deblocked text reports no hits. Loc below is `pNN:Pm:wN` (NN = scan-sequence page, Pm = lint chunk number, wN = word index on the deblocked chunk) plus the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p49:P2:w30 [चिन्तां न] | `अविमृष्यकारी` | `अविमृश्यकारी` | SPL | likely | medium* | विमृश् root takes श; no sandhi rule yields ष here |
| 2 | p51:P2:w1 [कानिचन दिनानि] | `कानिचन` | `कतिचन` | SPL | likely | low* | कानिचन is not standard; कतिचन (`a few') fits; न/त is a known confusion pair so confirm the glyph from the scan |
| 3 | p52:P3:w44 [तद्दिनतः दण्डकस्य] | `उक्तवान्--- 'भवतः` | `उक्तवान्--- "भवतः` | STY | error | high | inner reported speech nested in open single-quoted speech must take the double sort (SQ DQ ... DQ SQ) |
| 4 | p52:P3:w64 [तद्दिनतः दण्डकस्य] | `निष्कासयामि' इति।` | `निष्कासयामि" इति।` | STY | error | high | mate of F3: the inner speech closes with its own iti, so the close must match the corrected open |
| 5 | p52:P3:w77 [तद्दिनतः दण्डकस्य] | `अनन्तर सः` | `अनन्तरं सः` | OCR | likely | medium* | bare अनन्तर against six अनन्तरं/अनन्तरम् in-story; the time-adverbial needs the accusative |

## Patterns

Nested single-in-single quotation (2 marks, F3-F4, one speech in p52:P3): the compositor sets every speech in singles, so the inner reported utterance inherits the wrong sort; corrected minimally to doubles, outer pair kept as print.

## Unverified

F1 (`अविमृष्यकारी`): held `{sug-del:}/{sug-ins:}` in file; settle with a dictionary check that no house spelling with ष exists. F2 (`कानिचन`): held in file; settle by re-examining the scan glyph (न vs त) and confirming कतिचन. F5 (`अनन्तर सः`): held in file; settle by scan check for a dropped anusvāra.

## Coverage

p48:P1 {x-com:layout: : skip layout note
p48:P2 # समर्थः : skip title
p48:P3 दन्तपुरे पद्मनन्दः : clean
p48:P4 अनन्तरं पद्मनन्दः : clean
p48:P5 इति सः : clean
p48:P6 पद्मनन्दः उक्तवान् : clean
p48:P7 {author: विवेकः} : skip metadata
p49:P1 {x-com:layout: : skip layout note
p49:P2 चिन्तां न : F1
p49:P3 राजास्थाने शमन्तकः : clean
p49:P4 शमन्तकः उक्तवान् : clean
p50:P1 {x-com:layout: : skip layout note
p50:P2 करोमि। प्रतिमासं : clean
p50:P3 भवान् न : clean
p51:P1 {x-com:layout: : skip layout note
p51:P2 कानिचन दिनानि : F2
p51:P3 अधिकारी दण्डकेन : clean
p52:P1 {x-com:layout: : skip layout note
p52:P2 वान्--- 'भवान् : clean
p52:P3 तद्दिनतः दण्डकस्य : F3, F4, F5
J1 p048:P4 {pb} -> p048:P5 {pc} (continues) : ok
J2 p048:P6 {pb} -> p049:P2 {pc} (continues) : ok
J3 p049:P2 {pb} -> p049:P3 fresh (clean break) : ok
J4 p049:P4 {pb} -> p050:P2 {pc} (continues) : ok
J5 p050:P2 {pb} -> p050:P3 {pc} (continues) : ok
J6 p050:P3 {pb} -> p051:P2 fresh (clean break) : ok
J7 p051:P2 {pb} -> p051:P3 {pc} (continues) : ok
J8 p051:P3 {wb} -> p052:P2 {pc} (continues) : ok
J9 p052:P2 {pb} -> p052:P3 fresh (clean break) : ok
J10 p052:P3 {pb} -> END (clean break) : ok
