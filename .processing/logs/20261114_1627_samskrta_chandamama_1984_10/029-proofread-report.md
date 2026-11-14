# Proofread report: विवेकोदयः (1984_10, p29--32)

## Summary

Story file `.processing/samskrta_chandamama/1984_10/p029.md` (4 page spans, 8 joints) passes the proofread gate with 4 quote-punctuation findings, all STY/style with high confidence. The systematic issue is print-era quote economy: one two-paragraph speech opens once and never re-opens, one speech opens never, and one nested label uses double marks inside doubles. No inherited `{sug-ins:}`/`{sug-del:}` queue existed from Phase A, the orth scanner reported zero hits on deblocked text, and no word-level verdicts were available to invent (no Phase A `{x-com:}` glyph note on file), so text is otherwise byte-identical to Phase A. Loc below is keyed `pNN:Pm` (scan sequence + lint chunk) with the chunk's first two words as anchor.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p30:P6 (नागरिकाणां वचने) | `किमर्थम् आगच्छेयुः? ¶ अस्माभिः` | close the first para with `?{ins:"}` | STY | style | high | multi-para speech: every paragraph opens and closes its own pair |
| F2 | p30:P7 (अस्माभिः नगरे) | `¶ अस्माभिः नगरे सुव्यवस्था` | open the second para with `{ins:"}अस्माभिः` | STY | style | high | same speech continued; opener pinned by sentence boundary plus `इति` closure |
| F3 | p32:P8 (चोरविषयकेण भयेन) | `¶ चोरविषयकेण भयेन` | open the speech with `{ins:"}चोरविषयकेण` | STY | style | high | `भवान्` address plus closing `स्यात्?" इति` pin a speech opening at para start |
| F4 | p32:P8 (चोरविषयकेण भयेन) | `सज्जनं "चोरः" इति` | `{del:"चोरः"}{ins:'चोरः'}` | STY | style | high | label nested inside spoken speech takes singles (`DQ SQ ... SQ DQ`) |

## Patterns

Print drops speech re-openers after a paragraph break (F1/F2 two halves of one ruling; F3 the same habit one page later), and sets a nested speech label in doubles (F4). All four are supplied or re-sorted in blocks; no text touched.

## Unverified

No held candidates. Every inherited ambiguity was ruled from text; nothing is parked for the user.

## Coverage

p29:P1 ({x-com:layout:}): skip layout-only chunk
p29:P2 (# विवेकोदयः): skip title chunk
p29:P3 (पुलिन्दराज्ये उदयगिरिनामकं): clean
p29:P4 (एकदा पुरन्दरः): clean
p29:P5 (नागरिकाणां वचनं): clean
p29:P6 (कारागारे स्थापिताः): clean
p29:P7 ("प्रमो! भवतः): clean
p29:P8 ({author: सुभद्रा}): skip metadata chunk
p30:P1 ({x-com:layout:}): skip layout-only chunk
p30:P2 (गाम्भीर्यं प्रतिबिम्बयितुं): clean
p30:P3 (एतेन पूर्वापेक्षया): clean
p30:P4 (पुरन्दरस्य वचनेन): clean
p30:P5 (पुरन्दरस्य आत्मीयेषु): clean
p30:P6 (नागरिकाणां वचने): F1
p30:P7 (अस्माभिः नगरे): F2
p30:P8 (पुरन्दरः तु): clean
p30:P9 (एकसप्ताहानन्तरं एकदा): clean
p30:P10 ({pgb: ४०}): skip page-close chunk
p31:P1 ({x-com:layout:}): skip layout-only chunk
p31:P2 (नायासः किञ्चित्): clean
p31:P3 (पुरन्दरः नागराजेन): clean
p31:P4 (मार्गः निर्जनः): clean
p31:P5 (पुरन्दरः नागराजं): clean
p31:P6 (पुरन्दरः किञ्चिद्दूरं): clean
p31:P7 (तं कोपेन): clean
p31:P8 (नागराजः एतत्): clean
p31:P9 ({pgb}): skip page-close chunk
p32:P1 ({x-com:layout:}): skip layout-only chunk
p32:P2 (चेत् भवतः): clean
p32:P3 (पुरन्दरः उक्तवान्): clean
p32:P4 (नागराजः पुरन्दरं): clean
p32:P5 (रक्षणप्रमुखः अपि): clean
p32:P6 (पुरन्दरः एतत्): clean
p32:P7 (तदा नागराजः): clean
p32:P8 (चोरविषयकेण भयेन): F3, F4
p32:P9 (नागराजस्य वचनानि): clean
p32:P10 (पुरन्दरः अपरस्मिन्): clean
p32:P11 (अल्पे एव): clean
p32:P12 ({pgb}): skip page-close chunk
J1 p029:P5 {pb} -> p029:P6 {pc} (continues): ok
J2 p029:P7 {wb} -> p030:P2 {pc} (continues): ok
J3 p030:P5 {pb} -> p030:P6 {pc} (continues): ok
J4 p030:P9 {wb} -> p031:P2 {pc} (continues): ok
J5 p031:P5 {pb} -> p031:P6 fresh (clean break): ok
J6 p031:P8 {pb} -> p032:P2 {pc} (continues): ok
J7 p032:P6 {pb} -> p032:P7 fresh (clean break): ok
J8 p032:P11 {pb} -> END (clean break): ok
