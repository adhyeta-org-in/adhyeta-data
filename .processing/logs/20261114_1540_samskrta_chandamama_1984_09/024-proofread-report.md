## Summary

Phase B proofread of `p024.md` (1984_09, scans 24-27, story "सूर्येण सह स्पर्धा", जातककथा). Proofread gate passes with 0 errors; `scan.py orth` reports 0 hits. Four findings: three quote-punctuation verdicts applied as blocks (F2-F4, all STY/style/high) and one held spelling candidate (F1 सूदूरे, SPL/likely/low*). Systematic problem: the print leaves speech/thought punctuation gappy in two places (missing open, mismatched open sort). Variant kept as seen: व्यामुग्धः (glyph verified 5x in Phase A, non-standard but certain). Phase A note for the compiler: this font renders ब/व identically (confirmed against बालहंसौ); बालकौ-type readings settled from context. Proper nouns spell consistently throughout; sandhi openness and house spellings kept as seen. `Loc` is story coordinates `pNN:Pm` plus anchor words, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p024:P5 एकदा राजहंसः (w6) | `सह सूदूरे स्थितम्` | `सह सुदूरे स्थितम्` | SPL | likely | low* | सूदूरे is not a Sanskrit word; सुदूरे (very far) fits the lake's distance |
| 2 | p024:P10 तद्दिनात् आरभ्य (w16) | `स्म। "यदा-` | `स्म। 'यदा-` | STY | style | high | interior thought closed by इति चिन्तयन् takes singles and already closes with ' |
| 3 | p025:P4 एतत् श्रुत्वा (w7) | `उक्तं रे!` | `उक्तं "रे!` | STY | style | high | direct speech after reporting verb उक्तं needs its opening double |
| 4 | p025:P4 एतत् श्रुत्वा (w45) | `क्रीडयताम्' इति` | `क्रीडयताम्" इति` | STY | style | high | iti-closure of an उक्तं-speech takes the double close to match F3 |

## Patterns

None.

## Unverified

F1: the print reading सूदूरे cannot be rechecked (images closed, no Phase A note on this word); settling needs a scan re-check or an editor's call between the minimal fix सुदूरे and leaving the sic form.

## Coverage

p024:P1 {x-com:layout:} : skip layout declaration
p024:P2 # सूर्येण : skip title
p024:P3 पूर्वकाले ब्रह्मदत्तः : clean
p024:P4 जनाः सर्वगुणसम्पन्नम् : clean
p024:P5 एकदा राजहंसः : F1
p024:P6 काशीराजः आश्चर्येण : clean
p024:P7 मानं राजहंसं : clean
p024:P8 राजलक्षणैः राजगाम्भीर्येण : clean
p024:P9 राजहंसेन महाराजस्य : clean
p024:P10 तद्दिनात् आरभ्य : F2
p024:P11 {category:} : skip metadata
p025:P1 {x-com:layout:} : skip layout declaration
p025:P2 कदापि राजहंसः : clean
p025:P3 एकदा चित्रकूटपर्वते : clean
p025:P4 एतत् श्रुत्वा : F3, F4
p025:P5 एतत् हितवचनं : clean
p025:P6 तृतीयवारम् अपि : clean
p025:P7 "राजहंसस्य अनुमतेः : clean
p025:P8 नास्ति इति : clean
p025:P9 तद्दिने यथापूर्वं : clean
p025:P10 किं प्रवृत्तं : clean
p026:P1 {x-com:layout:} : skip layout declaration
p026:P2 निश्चितम् शीघ्रम् : clean
p026:P3 सूर्योदयानन्तरं तौ : clean
p026:P4 बालहंसयोः अन्यतरः : clean
p026:P5 तदा राजहंसः : clean
p026:P6 राजहंसः पुनरपि : clean
p026:P7 "मम परिवारस्य : clean
p026:P8 एतेन सूर्यस्य : clean
p026:P9 राजहंसः सूर्यमण्डलस्य : clean
p027:P1 {x-com:layout:} : skip layout declaration
p027:P2 काशीराज्यं प्राप्नोत् : clean
p027:P3 सः राजहंसं : clean
p027:P4 महाराजस्य आतिथ्येन : clean
p027:P5 राजहंसः बालहंसयोः : clean
p027:P6 न विस्मरामि : clean
p027:P7 तदा राजा : clean
p027:P8 राजहंसेन एतत् : clean
p027:P9 महाराजस्य उद्याने : clean
J1 p024:P6 {wb} -> p024:P7 {pc} : ok
J2 p024:P10 {wb} -> p025:P2 {pc} : ok
J3 p025:P7 {pb} -> p025:P8 {pc} : ok
J4 p025:P10 {pb} -> p026:P2 {pc} : ok
J5 p026:P4 {pb} -> p026:P5 fresh : ok
J6 p026:P9 {pb} -> p027:P2 {pc} : ok
J7 p027:P5 {pb} -> p027:P6 {pc} : ok
J8 p027:P9 {pb} -> END : ok
