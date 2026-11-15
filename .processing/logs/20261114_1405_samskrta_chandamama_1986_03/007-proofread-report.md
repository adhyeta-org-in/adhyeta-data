# Proofread report: 1986_03 p007 (scans 7-9, मन्त्रिपरीक्षा)

## Summary

4 findings, all STY / style / high: one quote-sort fix (F1), one stray-mark deletion (F2), and two supplied mates closing/opening a four-paragraph speech span (F3, F4). The systematic issue is era-print quote gaps: a single-stroke open where speech expects DQ, and a speech opened once and closed four paragraphs later. Kept as print-faithful with reasons: महत्व with single त (verified at 3x in Phase A, flagged on file), the SQ proclamation quote and SQ doubt-murmur quotes (sense does not pin DQ), and the पोषिताः। danda before इति. One mechanical fix to my own typing (stray ZWJ in महत्वरहितस्य, removed); orth scan clean; extract gate exit 0 and proofread gate exit 0. No held candidates. Loc is `pNN:Pm:word` with the chunk's first two words as anchor, words counted on the deblocked chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p008:P2:12 (आनीतवान्। सभायां) | `'मासत्रयं` | `"मासत्रयं` | STY | style | high | Minister's spoken order takes DQ doubles; print close is DQ |
| F2 | p009:P7:6 (अस्यां परीक्षायां) | `"मार्जारस्य` | delete mark | STY | style | high | DQ open inside an already-open DQ speech span with no close-plus-reopen |
| F3 | p009:P4:55 (एतत् श्रुत्वा) | `अनुचितः एव।` (speech unclosed) | `अनुचितः एव।"` | STY | style | high | Multi-para speech: every paragraph closes its own pair; position is the paragraph end |
| F4 | p009:P7:1 (अस्यां परीक्षायां) | `अस्यां` (speech reopened) | `"अस्यां` | STY | style | high | Multi-para speech: every paragraph opens its own pair; position is the paragraph start |

## Patterns

Print quote gaps (4x: F1-F4): single-stroke opens and unclosed multi-paragraph speech, all in reported speech closed by इति with a verb of speaking (उक्तवान्), so sorts are pinned by speech-vs-thought sense.

## Unverified

None. No candidates held; महत्व single-त is kept print-faithful (verified at 3x), not held.

## Coverage

p007:P3 पूर्वं विद्याधरः : clean
p007:P4 श्रीपुरराज्यस्य पार्श्वे : clean
p007:P5 कालवशात् सुदर्शनः : clean
p007:P6 अतः एकदा : clean
p007:P7 विश्रान्तिं यत् : clean
p007:P8 मन्त्री सुदर्शनः : clean
p007:P9 एतेन बहवः : clean
p007:P10 प्रारम्भिकपरीक्षासु विजयं : clean
p008:P2 आनीतवान्। सभायां : F1
p008:P3 मन्त्रिणः वचनानुसारं : clean
p008:P4 विनयस्य मार्जारः : clean
p008:P5 सुदर्शनः त्रीन : clean
p008:P6 प्रथमं विनयः : clean
p008:P7 अनन्तरं श्रीधरः : clean
p008:P8 मार्जारं मम : clean
p008:P9 अन्ते चन्द्रकान्तः : clean
p009:P2 किल इति : clean
p009:P3 सभायां स्थिताः : clean
p009:P4 एतत् श्रुत्वा : F3
p009:P5 चन्द्रकान्तः तु : clean
p009:P6 अपि शून्या : clean
p009:P7 अस्यां परीक्षायां : F2, F4
p009:P8 एतेन विवरणेन : clean
J1 p007:P6 -> p007:P7 : ok
J2 p007:P10 -> p008:P2 : ok
J3 p008:P7 -> p008:P8 : ok
J4 p008:P9 -> p009:P2 : ok
J5 p009:P5 -> p009:P6 : ok
J6 p009:P8 -> END : ok
