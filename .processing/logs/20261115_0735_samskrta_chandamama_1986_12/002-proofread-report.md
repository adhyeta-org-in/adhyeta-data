# Proofread report — 1986_12, p002 (pp. 2–6): कृपणः गोपीनाथः

## Summary

Seven verdict blocks applied (F1–F7), all quote-mark supply or sort corrections pinned by `इति`/reporting verbs and nesting sense; three holds kept for the user (U1–U3: one likely dropped `ई`, one stray visarga, one stray anusvara). The `orth` scanner reported zero hits on the deblocked text; word-level, sandhi, morphology, agreement, gerund/क्त choice, correlatives and the joints/flow pass are otherwise clean. Loc below is `pNNN:Pm:w` (lint page tag and chunk, `w` = word index in the deblocked chunk from 1) with the chunk's first two words as anchor. The `भगिनी` box on p. 2 is preserved as `{misc: "भगिनी"}` for the compiler/user to keep or drop.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p002:P8:15 (तदा माता) | `बाधन्ते। आगताः रोगाः … कुर्वन्तु' इति` | insert `'` before `आगताः` (`{ins:'}`) | STY | likely | high | Embedded exhortation inside `DQ` speech needs its own `SQ` pair; print gives only the close |
| F2 | p003:P8:25 ('दानरूपेण दत्ता) | `'तर्णकं …` (open) | `"` (`{del:'}{ins:"}`) | STY | likely | high | Speech governed by `उक्त्वा … इति` takes doubles; singles here mark thought (cf. `चिन्तितवान्` in the same para) |
| F3 | p003:P8:27 ('दानरूपेण दत्ता) | `… पोषयन्तु'` (close) | `"` (`{del:'}{ins:"}`) | STY | likely | high | Mate of F2; closes the `उक्त्वा`-governed speech |
| F4 | p004:P3:2 (रामशर्मा "आम्) | `'आम् …` (open) | `"` (`{del:'}{ins:"}`) | STY | likely | high | Hypothetical speech governed by `वदेत् … इति` takes doubles |
| F5 | p004:P3:6 (रामशर्मा "आम्) | `… एव'` (close) | `"` (`{del:'}{ins:"}`) | STY | likely | high | Mate of F4 |
| F6 | p005:P11:44 ("भोः, भवतः) | `… पुनः आगतः।` (no close) | append `"` (`{ins:"}`) | STY | likely | high | Closes the `""भोः, …` sannyasi speech at the page-turn sentence boundary |
| F7 | p006:P2:1 (भवतः रोगः) | `भवतः रोगः …` (no open) | prepend `"` (`{ins:"}`) | STY | likely | high | Per-para pair for the continuing sannyasi speech closed by `… आचरति" इति` |

## Patterns

1. Dropped or mis-sorted quote strokes (7 marks, F1–F7): the print omits one stroke of a pair (`कुर्वन्तु'`, p002:P8; page-turn pair, p005:P11/p006:P2) or sorts spoken quotes as singles (`'तर्णकं … पोषयन्तु'`, p003:P8; `'आम् … एव'`, p004:P3). All resolved from `इति`, speech verbs (`उक्त्वा`, `वदेत्`) and `DQ/SQ` nesting.
2. Anusvara/dental-nasal print variation in `संन्यासी` forms, kept as printed: `संन्यासी` (6×), `सन्यासिनम्` (p005:P8, accusative without bindu), `संन्यासिनः` (p006:P10, P12). No action.

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| U1 | p003:P6:14 (गता। अल्पेषु) | `तदयिपत्नीपुत्रादयः` | `तदीयपत्नीपुत्रादयः`? | SPL | likely | medium* | `तदयि` is no word; sense needs `तदीय` (his); needs glyph re-check at 3x |
| U2 | p005:P11:40 ("भोः, भवतः) | `तेनः पूर्वतनः` | `तेन पूर्वतनः`? | ENC | likely | medium* | Instrumental `तेन` cannot take visarga; smallest change drops it |
| U3 | p006:P2:16 (भवतः रोगः) | `उत्पन्नां भीतिः` | `उत्पन्ना भीतिः`? | ENC | likely | medium* | Nominative `भीतिः` needs nominative `उत्पन्ना`; smallest change drops the anusvara |

## Coverage

p002:P1 layout : skip x-com-only chunk
p002:P2 कृपणः गोपीनाथः : skip title
p002:P3 नागवनग्रामीणस्य गोपीनाथस्य : clean
p002:P4 तदा गोपीनाथस्य : clean
p002:P5 "मम रोगस्य : clean
p002:P6 वस्तुतः गोपीनाथः : clean
p002:P7 इच्छति। मातुः : clean
p002:P8 तदा माता : F1
p002:P9 गोपीनाथस्य पत्नीपुत्राः : clean
p002:P10 अन्ते गोपीनाथः : clean
p002:P11 "भगिनी" : skip metadata (footer box, keep-or-drop for user)
p003:P1 layout : skip x-com-only chunk
p003:P2 मह्यं प्रत्यर्पयतु। : clean
p003:P3 तदा सम्भ्रान्तः : clean
p003:P4 "गावः अन्याः, : clean
p003:P5 रामशर्मा प्रतिवचनं : clean
p003:P6 गता। अल्पेषु : U1
p003:P7 एतदनन्तरं केषुचित् : clean
p003:P8 'दानरूपेण दत्ता : F2, F3
p003:P9 दश-द्वादशदिनानि अतीतानि। : clean
p003:P10 रामशर्मा तु : clean
p003:P11 वस्तुतः गौः : clean
p003:P12 किन्तु तथाकथनम् : clean
p003:P13 "धेनुः तावत् : clean
p004:P1 layout : skip x-com-only chunk
p004:P2 तावत् रुचिकरं : clean
p004:P3 रामशर्मा "आम् : F4, F5
p004:P4 सरलः रामशर्मा : clean
p004:P5 तदा गोपीनाथः : clean
p004:P6 "किमर्थ न?" : clean
p004:P7 खिन्नः गोपीनाथः : clean
p004:P8 अनन्तरदिने प्रातः : clean
p004:P9 एव। तस्याः : clean
p004:P10 एतस्य वचनस्य : clean
p004:P11 गोपीनाथस्य वचनं : clean
p004:P12 "यदि सङ्गृहीतं : clean
p005:P1 layout : skip x-com-only chunk
p005:P2 अपि रोगः : clean
p005:P3 तद्दिनतः रामशर्मा : clean
p005:P4 अल्पे एव : clean
p005:P5 "रामशर्मणः सकाशात् : clean
p005:P6 प्राप्तव्यम् आसीत् : clean
p005:P7 एकदा गोपीनाथस्य : clean
p005:P8 तत् श्रुत्वा : clean
p005:P9 संन्यासी गोपीनाथं : clean
p005:P10 तदा गोपीनाथः : clean
p005:P11 "भोः, भवतः : F6, U2
p006:P1 layout : skip x-com-only chunk
p006:P2 भवतः रोगः : F7, U3
p006:P3 "एवं तर्हि : clean
p006:P4 "दानरूपेण दत्तायाः : clean
p006:P5 "तर्हि भवते : clean
p006:P6 "अहं तु : clean
p006:P7 "तर्हि कस्मै : clean
p006:P8 "अस्मिन् ग्रामे : clean
p006:P9 सज्जनः रामशर्मा : clean
p006:P10 संन्यासिनः कथनं : clean
p006:P11 तदा संन्यासी : clean
p006:P12 संन्यासिनः वचनानुसारम् : clean
p006:P13 एतदनन्तरं गोपीनाथस्य : clean
J1 p002:P6 {pb} -> p002:P7 {pc} (continues) : ok
J2 p002:P10 {pb} -> p003:P2 {pc} (continues) : ok
J3 p003:P5 {pb} -> p003:P6 {pc} (continues) : ok
J4 p003:P13 {pb} -> p004:P2 {pc} (continues) : ok
J5 p004:P8 {pb} -> p004:P9 {pc} (continues) : ok
J6 p004:P12 {pb} -> p005:P2 {pc} (continues) : ok
J7 p005:P5 {pb} -> p005:P6 {pc} (continues) : ok
J8 p005:P11 {pb} -> p006:P2 fresh (clean break) : F6, F7
J9 p006:P8 {pb} -> p006:P9 {pc} (continues) : ok
J10 p006:P13 {pb} -> END (clean break) : ok
