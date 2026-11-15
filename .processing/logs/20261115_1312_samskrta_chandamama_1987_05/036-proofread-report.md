# Proofread report: 1987_05 p036 (मत्स्यकन्या, scans 36.jpg-40.jpg)

## Summary

Six findings, all STY quote-supply verdicts (three multi-para direct speeches closed and reopened one pair per paragraph; no sort changes, no word changes). No inherited `{sug-ins:}`/`{sug-del:}` queue existed in Phase A output, and the Sanskrit orth scanner reported zero hits on deblocked text. Proper nouns are consistent throughout (वीरसिंहः, सिंहाचलः, लवङ्गी); sandhi openness and house spellings kept as printed. The byline `{author: विवेकः"}` keeps its print-kept closing mark with no mate (documented below, not a finding). Nothing held unverified; the proofread gate is green (0 error paras, 0 story findings).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p037:P6 सञ्चरन्ती आसीत्। w22 | `वृक्षाणां मध्ये सञ्चरन्ती आसीत्।` | `वृक्षाणां मध्ये सञ्चरन्ती आसीत्।{ins:"}` | STY | error | high | Multi-para direct speech (opened p037:P5 `"गतसप्ताहे`) closes its own pair per para at the sentence boundary; next paras stand on their own dialogue pairs. |
| F2 | p038:P5 अत्र आगन्तुम् w1 | `अत्र आगन्तुं मम ग्रामतः` | `{ins:"}अत्र आगन्तुं मम ग्रामतः` | STY | error | high | Closing segment of the fisherman's tale (print close `" इति` kept); multi-para rule supplies the matching per-para open. |
| F3 | p039:P9 समीपबन्धुः अपि। w19 | `सा मम समीपबन्धुः अपि।` | `सा मम समीपबन्धुः अपि।{ins:"}` | STY | error | high | Confession speech (opened `"महाराज्ञ्याः`) closes its own pair per para at the sentence boundary. |
| F4 | p039:P10 अहं ताम् w1 | `अहं तां परिणेतुम् इच्छामि।` | `{ins:"}अहं तां परिणेतुम् इच्छामि।` | STY | error | high | Confession continues; multi-para rule supplies the per-para open (pairs with the page-turn continuation into p040:P2). |
| F5 | p040:P2 उक्तवती लवङ्गी। w5 | `{pc}इति कदाचित् खेदेन उक्तवती लवङ्गी।` | `{pc}इति कदाचित् खेदेन उक्तवती लवङ्गी।{ins:"}` | STY | error | high | Closes the per-para pair opened by F4 where the frame narration resumes. |
| F6 | p040:P5 अहम् एतदनन्तरम् w1 | `अहम् एतदनन्तरं बहु चिन्तितवान्।` | `{ins:"}अहम् एतदनन्तरं बहु चिन्तितवान्।` | STY | error | high | Closing segment of the confession (print close `" इति` kept); multi-para rule supplies the matching per-para open. |

## Patterns

- Multi-para direct speech supplied one pair per paragraph: 3 speech spans, 6 marks (F1-F2 fisherman's tale setting/close across the p037 column turn and p038 close; F3-F6 Simhachala's confession across the p039-p040 page turn). All other speech sorts re-derived and kept: outer doubles for direct speech with `---` reporting verbs and इति-closures, inner singles for quoted thought/maxim (`'लोके यत् यत्...वदामि'`, `'मत्स्यकन्यातः...किल?'`, `'यदा अहं भोजनं...एव'`, `'विवाहानन्तरं...एव'`, `'इतोऽपि पायसम् अपेक्षितम्'`, `'पर्याप्तम्'`).

## Unverified

None. No held candidates; nothing below high confidence. The author-chunk mark (`{author: विवेकः"}` keeps a print-kept closing `"` with no mate) is a crop-verified print quirk, not a speech sort, so no verdict was added; the compiler keeps it as seen.

## Coverage

- p036:P1 `{x-com:layout:` : skip layout-only chunk
- p036:P2 `# मत्स्यकन्या` : skip title
- p036:P3 `धवलगिरिराजः वीरसिंहः` : clean
- p036:P4 `तदा महाराजः` : clean
- p036:P5 `भटः ततः` : clean
- p036:P6 `वीरसिंहः असमाधानेन` : clean
- p036:P7 `किञ्चित्कालानन्तरं पञ्चविंशतिवर्षीयं` : clean
- p036:P8 `धीवरः युवकः` : clean
- p036:P9 `वीरसिंहः तम्` : clean
- p036:P10 `"क्षन्तव्यः अहम्` : clean
- p036:P11 `"मत्स्यकन्या! कुत्र` : clean (page-end visarga travels with {pc} continuation J2)
- p036:P12 `{author: विवेकः"}` : skip footer metadata + pgb (print-kept closing mark, no mate, kept as seen)
- p037:P1 `{x-com:layout:` : skip layout-only chunk
- p037:P2 `{pc}वीरसिंहस्य मुखतः।` : clean (completes J2 across the page turn)
- p037:P3 `"मम ग्रामसमीपे` : clean (outer double with inner single intact)
- p037:P4 `"मत्स्यकन्या भवता` : clean
- p037:P5 `तदा सिंहाचलः` : clean (opens outer, travels with {pc} continuation J3)
- p037:P6 `{pc}हासध्वनिः श्रुतः।` : F1
- p037:P7 `सा मत्स्यकन्या` : clean (own dialogue pair)
- p037:P8 `अहं विचित्ररूपिणीम्` : clean (own dialogue pair)
- p037:P9 `तदा सा` : clean (own dialogue pair)
- p037:P10 `"एवं वा?` : clean
- p037:P11 `मत्स्यकन्या क्षणकालम्` : clean (outer double with inner single intact)
- p037:P12 `"भवती किमपि` : clean (edge-spanning pair closes p038:P2 across the page turn J4)
- p038:P1 `{x-com:layout:` : skip layout-only chunk
- p038:P2 `{pc}पश्यामि" इति` : clean (closes J4 pair)
- p038:P3 `सा माम्` : clean (outer double with inner single intact)
- p038:P4 `तद्दिने रात्रौ` : clean (thought in singles kept)
- p038:P5 `अत्र आगन्तुम्` : F2
- p038:P6 `सिंहाचलेन उक्तम्` : clean (thought opens in singles, travels with {pc} continuation J5)
- p038:P7 `{pc}प्रति मया` : clean (closes thought pair)
- p038:P8 `सिंहाचलः महाराजम्` : clean
- p038:P9 `"अस्तु, भवान्` : clean
- p038:P10 `अनन्तरदिने एव` : clean (genitive travels with {pc} continuation J6)
- p039:P1 `{x-com:layout:` : skip layout-only chunk
- p039:P2 `{pc}प्रयाणम् आरब्धम्।` : clean (completes J6)
- p039:P3 `राजधानीतः महाराज्ञ्या` : clean
- p039:P4 `तद्दिने अनन्तरदिने` : clean (genitive travels with {pc} continuation J7)
- p039:P5 `{pc}दर्शनं नास्ति।` : clean (completes J7)
- p039:P6 `"वस्तुस्थितिः? निवेदयतु,` : clean
- p039:P7 `"मत्स्यकन्या मया` : clean
- p039:P8 `वीरसिंहः कोपमिश्रितेन` : clean
- p039:P9 `तदा सिंहाचलः` : F3
- p039:P10 `अहं ताम्` : F4 (inner single quoted maxim intact; travels with {pc} continuation J8)
- p040:P1 `{x-com:layout:` : skip layout-only chunk
- p040:P2 `{pc}इति कदाचित्` : F5
- p040:P3 `तदा अहम्` : clean (own dialogue pair)
- p040:P4 `"भवदुक्तं सत्यम्` : clean (own dialogue pair)
- p040:P5 `अहम् एतदनन्तरम्` : F6
- p040:P6 `सिंहाचलेन उक्तम्` : clean
- p040:P7 `"कदाचित् वार्तालापसन्दर्भे` : clean (opens pair, travels with {pc} continuation J9)
- p040:P8 `{pc}उक्तवती। अहम्` : clean (closes J9 pair)
- p040:P9 `वीरसिंहः क्षणकालम्` : clean (story ends clean J10)
- J1 p036:P6 {pb} -> p036:P7 fresh : ok (clean break; guard's report ends)
- J2 p036:P11 {pb} -> p037:P2 {pc} : ok (आगतः वीरसिंहस्य मुखतः continues)
- J3 p037:P5 {pb} -> p037:P6 {pc} : ok (किलकिलेति हासध्वनिः continues mid-sentence)
- J4 p037:P12 {pb} -> p038:P2 {pc} : ok (तावत् पश्यामि continues; edge-spanning pair kept)
- J5 p038:P6 {pb} -> p038:P7 {pc} : ok (राज्ञीं प्रति continues; thought spans the column turn)
- J6 p038:P10 {pb} -> p039:P2 {pc} : ok (महाराजस्य प्रयाणम् continues)
- J7 p039:P4 {pb} -> p039:P5 {pc} : ok (मत्स्यकन्यायाः दर्शनं continues)
- J8 p039:P10 {pb} -> p040:P2 {pc} : ok (एव' इति continues; inner quote closes across the page turn, outer per-para pair F4/F5)
- J9 p040:P7 {pb} -> p040:P8 {pc} : ok (तत् उक्तवती continues)
- J10 p040:P9 {pb} -> END : ok (story ends clean; हार-gift closes the frame)
