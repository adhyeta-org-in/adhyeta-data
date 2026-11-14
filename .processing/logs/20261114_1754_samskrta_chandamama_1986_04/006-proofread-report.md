# Proofread report: 1986_04, story p006 (pp. 6–9, लोभी वणिक्)

## Summary

Two findings: one SPL error (high) and one STY likely (high); no repeats, so no Patterns section. The orth scanner reports no character-level hits on deblocked text, and the proofread gate is green (4 pages, 0 error paras, 0 story findings). The text is a print transcription, not OCR output. Images stayed closed throughout Phase B; glyph readings were verified at 3x in Phase A. Loc is `pNN:Pm` (NN = scan sequence, Pm = lint chunk number) plus the chunk's first two words, with 1-based whitespace-token word numbers (--- and quote/block-attached tokens counted).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p007:P3 कानिचन दिनानि w44 | `चेत् एकोन्ते आगत्य` | `चेत् एकान्ते आगत्य` | SPL | error | high | एकोन्ते is not a Sanskrit word; the same page prints एकान्ते (एकान्ते एकैकशः) and private-audience sense requires it |
| 2 | p008:P2 हिते सिध्यति। w17 | `कारणम्" इति'` | `कारणम्" इति` (delete the stray single mark, filed as {del:'}) | STY | likely | high | the DQ speech already closes at कारणम्"; the lone single has no mate and no thought-role before following narration |

## Unverified

None held; both findings are high confidence and filed as blocks above.

## Coverage

- p006:P3 रामपुरग्रामस्य पार्श्वे : clean
- p006:P4 आनन्दस्वामिनः शिष्येषु : clean
- p006:P5 शान्तारामस्य मनः : clean
- p006:P6 आनन्दस्वामी कदाचित् : clean
- p006:P7 एतत् श्रुत्वा : clean
- p006:P8 आनन्दस्वामी उक्तवान् : clean
- p006:P9 शान्तारामः स्वामिनः : clean
- p007:P2 भक्तिपूर्वकं शृणोति : clean
- p007:P3 कानिचन दिनानि : F1
- p007:P4 गुरोः शरीरपरिस्थितिं : clean
- p007:P5 शोकसागरे निमग्नाः : clean
- p007:P6 अन्ते लोभी : clean
- p007:P7 आनन्दस्वामी शान्ततया : clean
- p007:P8 शान्तारामः पुनः : clean
- p007:P9 शान्तारामस्य एतां : clean
- p007:P10 स्वामिन्! मया : clean
- p008:P2 हिते सिध्यति। : F2
- p008:P3 'एतस्मै उपदेशेन : clean
- p008:P4 शान्तारामः अतीव : clean
- p008:P5 किञ्चित्कालानन्तरम् आनन्दस्वामी : clean
- p008:P6 चेत् एषः : clean
- p008:P7 एकः सप्ताहः : clean
- p009:P2 शान्तारामः एकसप्ताहानन्तरं : clean
- p009:P3 एवम् एव : clean
- p009:P4 लोभी वणिक् : clean
- p009:P5 एवं सर्वं : clean
- p009:P6 वर्षद्वयं यावत् : clean
- p009:P7 लोहसङ्ग्रहणचिन्तने मग्नः : clean
- p009:P8 अल्पे एव : clean
- J1 p006:P5 {pb} -> p006:P6 {pc} (continues) : ok
- J2 p006:P9 {pb} -> p007:P2 {pc} (continues) : ok
- J3 p007:P4 {pb} -> p007:P5 {pc} (continues) : ok
- J4 p007:P10 {pb} -> p008:P2 {pc} (continues) : ok
- J5 p008:P5 {pb} -> p008:P6 {pc} (continues) : ok
- J6 p008:P7 {pb} -> p009:P2 fresh (clean break) : ok
- J7 p009:P4 {pb} -> p009:P5 fresh (clean break) : ok
- J8 p009:P8 {pb} -> END (clean break) : ok
