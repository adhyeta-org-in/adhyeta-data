# Proofread report: 1985_04 p021 (pp. 21–23, हासकारणम्)

## Summary

Three findings, all quote-sort verdicts (STY, style, high confidence): the print's single/double quote sorts mismatch speech-vs-thought sense in three reported passages, corrected via `{del:}`/`{ins:}` with the print state kept in adjacent `{x-com:}` notes. The stdlib orth scan on deblocked text reported zero hits, and the sentence-by-sentence pass found no morphology, agreement, or syntax errors worth a block. Unquoted interior reasonings (six passages on p22) are kept as printed since no reporting verb or `इति` pins their boundaries. `Loc` below is `pNN:Pm` (scan sequence + lint chunk) with the chunk's first two words as anchor and 1-based word numbers inside the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p21:P5 शिवपुरस्य महाराजः (w29, w31) | `'आवां बान्धवौ भवावः'` print singles | `"आवां बान्धवौ भवावः"` doubles | STY | style | high | dispatched message content closed by `इति` is reported speech, which takes doubles |
| 2 | p22:P2 करोति स्म (w13, w24) | `"एतावती ... हसितवती"` print doubles | `'एतावती ... हसितवती'` singles | STY | style | high | शिवसेनः's conjectured motive (`तर्कितवान्`) is interior thought, which takes singles |
| 3 | p23:P7 मालती लज्जया (w6 open) | `'भवतः ...` print single open | `"भवतः ...` double open | STY | style | high | मालती's spoken reply (`उक्त्वा ... इति`) is direct speech; close already double in print |

## Patterns

Print quote sorts drift from the speech/thought convention (2 instances of single-for-speech: F1 open+close, F3 open; 1 instance of double-for-thought: F2). House spellings observed but left standing as variants: open/joined sandhi mix (`शिवपुरं स्वर्णपुरम्`), invariant `रत्नमझरी` (झ throughout, no consistency issue), `स्तब्ध`/`स्तम्भ` alternation as printed, `तूष्णीम्`/`तूष्णीं` as printed.

## Unverified

None held. Every below-certainty reading was settled from context: `दास्याः भवत्याः धैर्यं` (p23:P6) parses as appositional genitives ("your courage, as a maid's"), and `स्वीयमनोभावजातं` (p22:P9) as a regular tatpuruṣa, so neither required a candidate block.

## Coverage

p21:P1 {x-com:layout: : skip layout chunk
p21:P2 # हासकारणम् : skip title
p21:P3 बहुवर्षेभ्यः पूर्वं : clean
p21:P4 गच्छता कालेन : clean
p21:P5 शिवपुरस्य महाराजः : F1
p21:P6 विजयः रत्नमझर्याः : clean
p21:P7 विवाहसम्बन्धिनां विषयाणां : clean
p21:P8 भोजनसमारम्भस्य आरम्भः : clean
p21:P9 {author: श्रीमाता} : skip metadata
p22:P1 {x-com:layout: : skip layout chunk
p22:P2 करोति स्म : F2
p22:P3 शिवसेनस्य पत्नी : clean
p22:P4 विष्णुसेनस्य चिन्ता : clean
p22:P5 इदानीं बन्धुत्वं : clean
p22:P6 विष्णुसेनस्य पत्न्याः : clean
p22:P7 राजकुमार्याः रत्नमझर्याः : clean
p22:P8 राजकुमारः विजयः : clean
p22:P9 शिवसेनस्य सचिवः : clean
p23:P1 {x-com:layout: : skip layout chunk
p23:P2 तु यथार्थकारणम् : clean
p23:P3 किञ्चित्कालानन्तरं भोजनसमारम्भः : clean
p23:P4 तस्मिन् समये : clean
p23:P5 किन्तु मालती : clean
p23:P6 तदा सुधर्मा : clean
p23:P7 मालती लज्जया : F3
p23:P8 मल्लस्य हस्ते : clean
J1 p021:P5 {pb} -> p021:P6 {pc} : ok (कुमारः विजयः continues)
J2 p021:P8 {pb} -> p022:P2 {pc} : ok (वादविवादं करोति स्म completes)
J3 p022:P4 {pb} -> p022:P5 {pc} : ok (निवारयितुं इदानीं बन्धुत्वं infinitive plus main clause)
J4 p022:P9 {pb} -> p023:P2 {pc} : ok (हासस्य तु यथार्थकारणम् continues)
J5 p023:P6 {pb} -> p023:P7 fresh : ok (उक्तवान्। then new paragraph मालती)
J6 p023:P8 {pb} -> END : ok (clean story close)
