# Proofread report: samskrta_chandamama 1986_06, story p002 (pp. 2-6, योग्यतापरीक्षा)

## Summary
Three findings, all `STY` / style with high confidence: the print drops one quote mark in each of three reported-speech paragraphs (two missing opens, one missing close), and each is supplied in the story file via `{ins:"}` where the `इति`-closure pins the position. The systematic issue is print punctuation gaps in quoted speech, not grammar: the orth scanner reports zero hits, sandhi/morphology/syntax passes are clean, and proper nouns (`सूवर्चला`, `रमापतिः`, `मोहनाङ्गः`, `रामभद्र`, `प्रभाकर`) are consistent throughout. No candidates are held for the user; nothing is unverified. The story file passes the proofread gate (exit 0, all pages clean). Loc below is `pNN:Pm` (scan sequence + chunk within that page span) with the first two words as anchor, words counted on the deblocked chunk from 1.

## Findings
| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p03:P3 (वक्तव्यं चेत्) w1 | `वक्तव्यं चेत् ... करोमि" इति।` (no opening mark) | `{ins:"}` at para start | STY | style | high | Direct speech closed by `इति` needs its opening mark; the old man's added utterance opens with none in print. |
| F2 | p06:P5 (तात! धनमदः) w19 | `...उत्तीर्णा' इति।` (inner `'` closes, outer `"` never closes) | `{ins:"}` after `उत्तीर्णा'` (supplied outer close) | STY | style | high | Outer reported speech (daughter to father) never closes in print; the `इति` pins the close after the nested quotes. |
| F3 | p06:P6 (मम इष्टानिष्टस्य) w1 | `मम ... सुलभलभ्या न" इति उक्तवती ...` (no opening mark) | `{ins:"}` at para start | STY | style | high | New paragraph of her continuing speech with `इति उक्तवती` closure; each multi-para speech paragraph opens its own pair. |

## Patterns
- Dropped quote marks in reported speech (3x: F1, F2, F3). Print's era-style two-stroke doubles are transcribed as single `"` throughout (not findings); only genuinely absent marks are supplied, each pinned by an `इति`-closure. No other repeats.

## Unverified
None. No `{sug-ins:}`/`{sug-del:}` was inherited from Phase A and none is added here; every ruling is high confidence and no form is held for the user.

## Coverage
- p02:P1 {x-com:layout...} : skip (layout chunk, no story text)
- p02:P2 योग्यतापरीक्षा : skip (title)
- p02:P3 रमापति नामकस्य : clean
- p02:P4 एवं स्थिते : clean
- p02:P5 भवान् मम : clean
- p02:P6 अन्धकारः व्याप्तः : clean
- p02:P7 वातायनद्वारेण पश्यन्तीं : clean
- p02:P8 {author...} : skip (metadata footer)
- p03:P1 {x-com:layout...} : skip (layout chunk, no story text)
- p03:P2 अग्रे गन्तुं : clean
- p03:P3 वक्तव्यं चेत् : F1
- p03:P4 भोजनं विना : clean
- p03:P5 सूवर्चला प्रकोष्ठे : clean
- p03:P6 अकस्मात् प्रवृत्तया : clean
- p03:P7 वृद्धः असहनं : clean
- p04:P1 {x-com:layout...} : skip (layout chunk, no story text)
- p04:P2 एव भोजनं : clean
- p04:P3 भोजनं परिवेषयन्त्या : clean
- p04:P4 वृद्धः उत्साहेन : clean
- p04:P5 वृद्धस्य दण्डनार्थं : clean
- p04:P6 उषःकाले पुनः : clean
- p04:P7 सूवर्चला तं : clean
- p04:P8 युवकः मन्दहासं : clean
- p04:P9 आम् आगतवान् : clean
- p04:P10 युवकः उच्चैः : clean
- p04:P11 सः भवतः : clean
- p05:P1 {x-com:layout...} : skip (layout chunk, no story text)
- p05:P2 कोपेन पृष्टवती : clean
- p05:P3 युवकः पुनः : clean
- p05:P4 तस्य युवकस्य : clean
- p05:P5 एतत् सर्वं : clean
- p05:P6 तत् कथम् : clean
- p05:P7 तदा युवकः : clean
- p05:P8 सेवकद्वारा एवं : clean
- p05:P9 तदा सूवर्चला : clean
- p06:P1 {x-com:layout...} : skip (layout chunk, no story text)
- p06:P2 अस्मि तत् : clean
- p06:P3 एतत् श्रुत्वा : clean
- p06:P4 रमापतिः पुत्र्याः : clean
- p06:P5 तात धनमदः : F2
- p06:P6 मम इष्टानिष्टस्य : F3
- p06:P7 रमापतिः किञ्चित्कालम् : clean
- p06:P8 जानामि किल : clean
- p06:P9 अङ्गीकारं प्रदर्शयन्ती : clean
- J1 p002:P4 -> p002:P5 fresh : ok
- J2 p002:P7 -> p003:P2 {pc} : ok
- J3 p003:P2 -> p003:P3 fresh : ok
- J4 p003:P3 -> p003:P4 fresh : ok
- J5 p003:P4 -> p003:P5 fresh : ok
- J6 p003:P5 -> p003:P6 fresh : ok
- J7 p003:P6 -> p003:P7 fresh : ok
- J8 p003:P7 -> p004:P2 {pc} : ok
- J9 p004:P2 -> p004:P3 fresh : ok
- J10 p004:P3 -> p004:P4 fresh : ok
- J11 p004:P4 -> p004:P5 fresh : ok
- J12 p004:P5 -> p004:P6 fresh : ok
- J13 p004:P6 -> p004:P7 fresh : ok
- J14 p004:P7 -> p004:P8 fresh : ok
- J15 p004:P8 -> p004:P9 fresh : ok
- J16 p004:P9 -> p004:P10 fresh : ok
- J17 p004:P10 -> p004:P11 fresh : ok
- J18 p004:P11 -> p005:P2 {pc} : ok
- J19 p005:P2 -> p005:P3 fresh : ok
- J20 p005:P3 -> p005:P4 fresh : ok
- J21 p005:P4 -> p005:P5 fresh : ok
- J22 p005:P5 -> p005:P6 fresh : ok
- J23 p005:P6 -> p005:P7 fresh : ok
- J24 p005:P7 -> p005:P8 fresh : ok
- J25 p005:P8 -> p005:P9 fresh : ok
- J26 p005:P9 -> p006:P2 {pc} : ok
- J27 p006:P2 -> p006:P3 fresh : ok
- J28 p006:P3 -> p006:P4 fresh : ok
- J29 p006:P4 -> p006:P5 fresh : ok
- J30 p006:P5 -> p006:P6 fresh : ok
- J31 p006:P6 -> p006:P7 fresh : ok
- J32 p006:P7 -> p006:P8 fresh : ok
- J33 p006:P8 -> p006:P9 fresh : ok
- J34 p006:P9 -> END : ok
