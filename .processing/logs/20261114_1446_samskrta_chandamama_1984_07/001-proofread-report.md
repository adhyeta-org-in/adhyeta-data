# Proofread report: 1984_07 p001 विकलाङ्गाः (scans 1–4)

## Summary

Three findings: one `error` (missing quote open supplied via `{ins:'}`), one `style` (fused words split by direct spacing fix), one `likely` held candidate (`ममकारण`, unverified). The systematic issue is print punctuation: 1980s single-stroke speech quotes kept as seen, one dropped inner open restored. All six `{pb}`/`{wb}`+`{pc}` continuations and both clean breaks checked text-continuous against the asserted 2col layouts. Orth scanner clean; text is human transcription, not OCR. Loc is `pNN:Pm w<word>` (scan sequence page, lint chunk number, 1-based word index on the chunk) plus a two-word anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p004:P4 w34 (तदा ते) | `सत्यं चेत्, वयं मनःपूर्वकं` | `सत्यं चेत्, {ins:'}वयं मनःपूर्वकं` | STY | error | high | quoted promise closed by `इति` has no open; sentence boundary after `चेत्` pins it |
| 2 | p002:P8 w24 (तद्दिने रात्रौ) | `पङ्गुःवृद्धः` | `पङ्गुः वृद्धः` | STY | style | high | two nominatives in apposition fused in print; space restored directly |
| 3 | p003:P4 w30 (तद्दिनादारभ्य सुधीरः) | `ममकारण` | `मम कारणात्` or `मत्कारणात्` | LEX | likely | low* | bare stem used adverbially (calque of "on my account"?); no classical parse, fix uncertain |

## Unverified

- F3 `ममकारण` (p003:P4): tried `मम कारणात्` (for my sake, ablative) and `मत्कारणात्` (standard "on my account"); both need a glyph decision the closed-image phase cannot make. Held as `{sug-del:ममकारण}{sug-ins:मम कारणात्}` with note in file. Settles with: coordinator print check or a second witness of this issue.

## Coverage

p001:P1 {x-com:layout: ...} : skip layout-only chunk
p001:P2 # विकलाङ्गाः : skip title
p001:P3 सुधीरः जन्मतः : clean
p001:P4 तस्मिन् ग्रामे : clean
p001:P5 सुधीरस्य माता : clean
p001:P6 पीडा इत्यादिकं : clean
p001:P7 एकदा ते : clean
p001:P8 तदा ते : clean
p001:P9 {category: माणवकः}{pgb} : skip footer metadata
p002:P1 {x-com:layout: ...} : skip layout-only chunk
p002:P2 किमर्थम् अस्मान् : clean
p002:P3 तेषाम् एतद्वचनं : clean
p002:P4 केषुचित् एव : clean
p002:P5 गच्छति काले, : clean
p002:P6 गतौ। किन्तु : clean
p002:P7 सुधीरः पत्नीं : clean
p002:P8 तद्दिने रात्रौ : F2
p002:P9 अल्पे एव : clean
p002:P10 किन्तु सुधीरस्य : clean
p003:P1 {x-com:layout: ...} : skip layout-only chunk
p003:P2 आलिङ्गितवती। : clean
p003:P3 काकः अपि : clean
p003:P4 तद्दिनादारभ्य सुधीरः : F3
p003:P5 यथा यथा : clean
p003:P6 बाल्ये विकलाङ्गानां : clean
p003:P7 जातः इति : clean
p003:P8 एतेषु एव : clean
p003:P9 सुधीरः सन्यासिनं : clean
p003:P10 सन्यासी बालकं : clean
p003:P11 सुधीरः पुत्रं : clean
p004:P1 {x-com:layout: ...} : skip layout-only chunk
p004:P2 एतत्सर्वं श्रुत्वा : clean
p004:P3 सुधीरः तद्दिने : clean
p004:P4 तदा ते : F1
p004:P5 तेषां प्रीतिपूर्वकेन : clean
p004:P6 सुधीरः एकैकस्य : clean
p004:P7 "तात! अहं : clean
p004:P8 अपरस्मिन् क्षणे : clean
p004:P9 एतदनन्तरं एकसप्ताहाभ्यन्तरे : clean
p004:P10 सुधीरः सद्यः : clean
J1 p001:P5 {pb} -> p001:P6 {pc} (continues) : ok
J2 p001:P8 {pb} -> p002:P2 {pc} (continues) : ok
J3 p002:P5 {wb} -> p002:P6 {pc} (continues) : ok
J4 p002:P10 {pb} -> p003:P2 {pc} (continues) : ok
J5 p003:P6 {pb} -> p003:P7 {pc} (continues) : ok
J6 p003:P11 {pb} -> p004:P2 fresh (clean break) : ok
J7 p004:P5 {pb} -> p004:P6 {pc} (continues) : ok
J8 p004:P10 {pb} -> END (clean break) : ok
