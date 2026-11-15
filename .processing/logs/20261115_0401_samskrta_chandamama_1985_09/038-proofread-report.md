# Proofread report — 1985_09 p038 भीतिकारणम् (pp. 38–40)

## Summary

4 findings: 3 errors (print misprints, all high confidence) and 1 style (quote nesting in the Padmāmbā speech). No systematic pattern; `scan.py orth` is clean and open/joined sandhi plus house spellings are kept as variants throughout. One remark without a block: p038:P9 `आक्रोशेनं कृतवती` (accusative `आक्रोशनम्` expected) looks suspect, but Phase A left no flag on it, so Phase B issues no verdict — left for the compiler. Loc is `pNN:Pm:word`, counted on whitespace tokens of the print-form chunk from 1; anchors are the chunk's first two words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p039:P2:5 घृतपात्रं पतितम् | `घृतं सर्वं मृत्तिकायाः` | `मृत्तिकायां` | MRP | error | high | `विलीनम्` takes the locative; print `ः` for `ं` |
| 2 | p039:P7:18 अपरस्मिन् दिने | `प्रथतं पिण्याकः` | `प्रथमं` | OCR | error | high | `प्रथतं` is no word; print drops `म` (`म`/`त` slip) |
| 3 | p039:P9:4 तदा बहिस्तात् | `सूर्यनारणः स्नुषाम्` | `सूर्यनारायणः` | CNS | error | high | name spells `सूर्यनारायणः` 4x elsewhere; print drops `ाय` |
| 4 | p040:P8:24,34 "आं भगिनि! | `"अस्माभिः … भविष्यति"` | `'अस्माभिः … भविष्यति'"` | STY | style | high | maxim nested inside speech takes singles; outer double close supplied |

## Unverified

None — every Phase A candidate was promoted on certain evidence; nothing held.

## Coverage

p038:P1 : skip x-com layout
p038:P2 : skip title
p038:P3 सूर्यनारायणस्य पुत्रः : clean
p038:P4 गृहम् आगतां : clean
p038:P5 स्वर्णलता मौनेन : clean
p038:P6 एकदा कूपतः : clean
p038:P7 कमलाम्बायाः गर्जनेन : clean
p038:P8 भीत्या कम्पमाना : clean
p038:P9 एतेन क्रुद्धा : clean
p038:P10 कम्पमाना स्वर्णलता : clean
p038:P11 पुनः एकदा : clean
p038:P12 भीत्या कम्पमानायाः : clean
p038:P13 : skip author
p039:P1 : skip x-com layout
p039:P2 घृतपात्रं पतितम् : F1
p039:P3 "अये अनागरिके! : clean
p039:P4 स्नुषायाः परिस्थितिं : clean
p039:P5 पुनः अन्यदा : clean
p039:P6 स्वर्णलता भीता। : clean
p039:P7 अपरस्मिन् दिने : F2
p039:P8 कमलाम्बायाः कोलाहलेन : clean
p039:P9 तदा बहिस्तात् : F3
p039:P10 स्वर्णलता शिरः : clean
p040:P1 : skip x-com layout
p040:P2 तदा सूर्यनारायणः : clean
p040:P3 कमलाम्बा कोपं : clean
p040:P4 अनन्तरदिने पार्श्वगृहस्था : clean
p040:P5 स्वर्णलता कार्यान्तरे : clean
p040:P6 स्वर्णलतायाः शरीरे : clean
p040:P7 अकार्यैः अहं : clean
p040:P8 "आं भगिनि! : F4
p040:P9 पद्माम्बायाः वचनं : clean
p040:P10 स्वर्णलता बुद्धिमती। : clean
J1 p038:P7 -> p038:P8 fresh : ok
J2 p038:P12 -> p039:P2 pc : ok
J3 p039:P7 -> p039:P8 fresh : ok
J4 p039:P10 -> p040:P2 fresh : ok
J5 p040:P6 -> p040:P7 pc : ok
J6 p040:P10 -> END : ok
