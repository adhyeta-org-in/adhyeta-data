## Summary

One finding (F1: STY error, high confidence): a double-quoted speech opening at p014:P7 (`"तत् भवदधीनम्।...`) is never closed in print across the page turn, so the close is supplied via `{ins:"}` after `इव।` at p015:P2. The 1980s quote house style is otherwise kept as seen: singles stand for thought, roar-challenge and formulaic utterances (p010:P4, p011:P3, p011:P7, p014:P3), and the nested `'किमर्थं...'` inside `"महोदय!...` (p012:P5) is correct DQ/SQ nesting. Orth scan of deblocked text is clean (0 hits on 58 lines); the text is a manual transcription, not OCR output. Glyph shapes were not rechecked (images closed in Phase B); open/joined sandhi and house spellings are kept as print variants.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p015:P2:1 (`इव।`) | `"तत् भवदधीनम्। ... अन्यथा` + `इव।` (open `"` at p014:P7, no close) | `इव।` + `{ins:"}` (close supplied at paragraph end) | STY | error | high | opening double quote of a direct speech never closed in print; paragraph end pins the close |

## Unverified

None held. No `{sug-del:}`/`{sug-ins:}` candidates were emitted or inherited in this range.

## Coverage

p010:P1 layout : skip layout declaration
p010:P2 कांस्य-दुर्गम् : skip title
p010:P3 चन्द्रवर्मा पर्वतमूले : clean
p010:P4 कुटीरतः तेजस्विनं : clean
p010:P5 सुलभतया एतं : clean
p010:P6 इति। शीघ्रं : clean
p010:P7 भवन्तः कं : clean
p011:P1 layout : skip layout declaration
p011:P2 उत्प्लुत्य अग्रे : clean
p011:P3 चन्द्रवर्मणा उक्तं : clean
p011:P4 एतत्सर्वं क्षणमात्रे : clean
p011:P5 स्वरेण उक्तवान् : clean
p011:P6 चन्द्रवर्मणः ध्वनेः : clean
p011:P7 परिस्थितिम् इतोऽपि : clean
p011:P8 इति उक्तवान् : clean
p012:P1 layout : skip layout declaration
p012:P2 तदा चन्द्रवर्मा : clean
p012:P3 चन्द्रवर्मणः वचनेन : clean
p012:P4 चन्द्रवर्मा कृतकम् : clean
p012:P5 भटनायकः स्वसहकारिणः : clean
p013:P1 layout : skip layout declaration
p013:P2 वान् इति। : clean
p013:P3 तत्सर्वं गोप्यम् : clean
p013:P4 कांस्यदुर्गम् भवान् : clean
p013:P5 अये किम् : clean
p013:P6 तावतः आश्चर्यस्य : clean
p013:P7 तदा चन्द्रवर्मा : clean
p013:P8 भटनायकः चन्द्रवर्माणं : clean
p013:P9 भवताम् आश्चर्यम् : clean
p014:P1 layout : skip layout declaration
p014:P2 भवन्तः तत्र : clean
p014:P3 एवं सधैर्यं : clean
p014:P4 उच्चैः आह्वानं : clean
p014:P5 वृद्ध इति : clean
p014:P6 भवतः वचने : clean
p014:P7 तत् भवदधीनम् : F1
p015:P1 layout : skip layout declaration
p015:P2 इव। : F1
p015:P3 चन्द्रवर्मा चित्रं : clean
p015:P4 एतं कांस्यदुर्गम् : clean
p015:P5 तदा चन्द्रवर्मा : clean
p015:P6 वृद्धः विशेषसन्तोषं : clean
p015:P7 भवन्तं भवतः : clean
p015:P8 तम् अपि : clean
p016:P1 layout : skip layout declaration
p016:P2 चन्द्रवर्मा शिलाराशेः : clean
p016:P3 एतत् दृष्ट्वा : clean
p016:P4 चन्द्रवर्माणं स्वाभिमुखम् : clean
p016:P5 कासाञ्चित् शक्तीनाम् : clean
p016:P6 महाराजः न : clean
p016:P7 तथा किमपि : clean
p016:P8 मया शिवसिंहेन : clean
p017:P1 layout : skip layout declaration
p017:P2 साहाय्यं शिवसिंहतः : clean
p017:P3 एवं यदा : clean
p017:P4 तौ द्वौ : clean
p017:P5 एतत् श्रुतवतः : clean
p017:P6 अनुवर्तते : clean
J1 p010:P4 {pb} -> p010:P5 fresh : ok
J2 p010:P5 {pb} -> p010:P6 {pc} : ok
J3 p010:P6 {pb} -> p010:P7 fresh : ok
J4 p010:P7 {wb} -> p011:P2 {pc} : ok
J5 p011:P2 {pb} -> p011:P3 fresh : ok
J6 p011:P3 {pb} -> p011:P4 fresh : ok
J7 p011:P4 {pb} -> p011:P5 {pc} : ok
J8 p011:P5 {pb} -> p011:P6 fresh : ok
J9 p011:P6 {pb} -> p011:P7 fresh : ok
J10 p011:P7 {pb} -> p011:P8 {pc} : ok
J11 p011:P8 {pb} -> p012:P2 fresh : ok
J12 p012:P2 {pb} -> p012:P3 fresh : ok
J13 p012:P3 {pb} -> p012:P4 fresh : ok
J14 p012:P4 {pb} -> p012:P5 fresh : ok
J15 p012:P5 {pb} -> p013:P2 {pc} : ok
J16 p013:P2 {pb} -> p013:P3 fresh : ok
J17 p013:P3 {pb} -> p013:P4 fresh : ok
J18 p013:P4 {pb} -> p013:P5 fresh : ok
J19 p013:P5 {pb} -> p013:P6 fresh : ok
J20 p013:P6 {pb} -> p013:P7 fresh : ok
J21 p013:P7 {pb} -> p013:P8 fresh : ok
J22 p013:P8 {pb} -> p013:P9 fresh : ok
J23 p013:P9 {wb} -> p014:P2 {pc} : ok
J24 p014:P2 {pb} -> p014:P3 fresh : ok
J25 p014:P3 {pb} -> p014:P4 fresh : ok
J26 p014:P4 {pb} -> p014:P5 fresh : ok
J27 p014:P5 {pb} -> p014:P6 fresh : ok
J28 p014:P6 {pb} -> p014:P7 fresh : ok
J29 p014:P7 {wb} -> p015:P2 {pc} : ok
J30 p015:P2 {pb} -> p015:P3 fresh : ok
J31 p015:P3 {pb} -> p015:P4 fresh : ok
J32 p015:P4 {pb} -> p015:P5 fresh : ok
J33 p015:P5 {pb} -> p015:P6 fresh : ok
J34 p015:P6 {pb} -> p015:P7 fresh : ok
J35 p015:P7 {pb} -> p015:P8 {pc} : ok
J36 p015:P8 {pb} -> p016:P2 fresh : ok
J37 p016:P2 {pb} -> p016:P3 fresh : ok
J38 p016:P3 {pb} -> p016:P4 fresh : ok
J39 p016:P4 {pb} -> p016:P5 fresh : ok
J40 p016:P5 {pb} -> p016:P6 {pc} : ok
J41 p016:P6 {pb} -> p016:P7 fresh : ok
J42 p016:P7 {pb} -> p016:P8 fresh : ok
J43 p016:P8 {pb} -> p017:P2 {pc} : ok
J44 p017:P2 {pb} -> p017:P3 fresh : ok
J45 p017:P3 {pb} -> p017:P4 fresh : ok
J46 p017:P4 {pb} -> p017:P5 fresh : ok
J47 p017:P5 {pb} -> p017:P6 fresh : ok
J48 p017:P6 {pb} -> END : ok
