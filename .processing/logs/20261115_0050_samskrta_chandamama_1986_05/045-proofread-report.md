# Proofread report — 1986_05, pages 45–48 (story file `p045.md`)

## Summary

7 findings: 1 error (F6 typo अद्याः), 6 style (F1–F5 quote-sort corrections, F7 supplied note close). Systematic defect: print drops the second stroke of double quotes inside direct speech (5 spots, all corrected via verdicts). Print singles for reported or indirect quotation are a separate systematic sort (8 spots) and are kept as print. Uncheckable: the reprint line is cut at the scan edge (tail text held, U3); two held words (U1, U2). The text is a print transcription, not OCR output. Loc below is `pNN:Pm:wN`: page span, lint chunk number, word index on deblocked chunk text from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p045:P5:w24 ("अस्माकं दुर्गम्") | `शक्नुवन्ति' इति` | `{del:'}{ins:"}` | STY | style | high | Direct speech closed by इति takes the double close; print shows one stroke where the opens show two |
| F2 | p046:P6:w36 (जितवर्मा क्रोधेन) | `--- 'भोः` | `{del:'}{ins:"}` | STY | style | high | Speech open takes the double open; print shows one stroke before भोः |
| F3 | p047:P3:w19 ("अये नीच!) | `भवन्तः?' इति` | `{del:'}{ins:"}` | STY | style | high | Speech close takes the double close; print shows one stroke |
| F4 | p047:P8:w26 (एवम् एव) | `उद्घाटयतु' इति` | `{del:'}{ins:"}` | STY | style | high | Speech close takes the double close; print shows one stroke |
| F5 | p047:P9:w14 ("इदानीं विवेकः) | `अभविष्यत्' इति` | `{del:'}{ins:"}` | STY | style | high | Speech close takes the double close; print shows one stroke |
| F6 | p046:P6:w39 (जितवर्मा क्रोधेन) | `अद्याः` | `{del:अद्याः}{ins:अद्य}` | SPL | error | high | अव्यय अद्य cannot take visarga; print अद्याः is a typeset slip |
| F7 | p045:P8:w47 (ततोऽपि अधिकम्) | reprint note opens `"` with no close | `{ins:"}` after `प्रकाशिता` | STY | style | high | Note is cut at the scan edge; close supplied at the certain end position |

## Patterns

- P1 — dropped second stroke of `"` in direct speech, 5 spots (F1–F5): opens and closes verified at 2–3x in Phase A; each corrected to the double via verdict.
- P2 — kept print sort, 8 spots: singles mark reported or indirect quotation (`'भवान् इन्द्रः, भवान् चन्द्रः'`, `'जितवर्मणः पौरुषं कीदृशम्'`, `'जितवर्मा युद्धार्थम् आगत अस्ति'`, `'वङ्गराज्यं जित्वा आगच्छामि'`, `'जितवर्मणा समग्रा सेना नाशिता'`, `'कलिङ्गसेनायाः अर्धभागः मया एव नाशितः'`, `'जितवर्मणा यत् उच्यते ...'`, `'वीराधिवीरः'`). Systematic, so kept as print with no blocks.

## Unverified

- U1 — `अस्मद्धरो` (p047:P2 "एवं तर्हि", `दुर्गाधिकारम् अस्मद्धरो यच्छन्तु`): print reads अस्मद्धरो (verified 3x in Phase A); no grammatical reading found. Tried: (a) अस्मद्धस्ते — no स्ते in the glyphs; (b) अस्मदधीने — धरो against धीने; (c) अस्मभ्यम् — no match. Held with the Phase A `{x-com:}` kept. Settles with a rescan of page 47 or another issue's reprint of this story.
- U2 — `कृत्रकम्` (p046:P2 पत्नी सम्यक्, `कृत्रकम् अनुकम्पं`): read from the full page only; likely `कृत्रिमम्` (feigned). No Phase A block on file, so no verdict per the no-new-glyph-claims rule. Settles with a 3x rescan.
- U3 — reprint-line tail (p045:P8 note): text cut at the scan edge after प्रकाशिता; probable `कथा।` plus close per sister issues, but the tail is unrecoverable from this scan. Mark supplied (F7); tail held.

## Coverage

- p045:P1 {x-com:layout: …} : skip (layout chunk, no story text)
- p045:P2 # वीराधिवीरः : skip (title)
- p045:P3 पूर्वं कलिङ्गदेशस्य : clean
- p045:P4 एतत् दुर्गं : clean
- p045:P5 "अस्माकं दुर्गम् : F1
- p045:P6 सामान्याः जनाः : clean
- p045:P7 जितवर्मा आत्मनः : clean
- p045:P8 ततोऽपि अधिकम् : F7
- p046:P1 {x-com:layout: …} : skip (layout chunk, no story text)
- p046:P2 पत्नी सम्यक् : clean (U2 noted, no block per no-new-glyph-claims)
- p046:P3 "मम सम्मुखे : clean
- p046:P4 एकदा प्रातःकाले : clean
- p046:P5 सिद्धता करणीया" : clean
- p046:P6 जितवर्मा क्रोधेन : F2, F6
- p046:P7 कलिङ्गसेनया 'जितवर्मा : clean
- p046:P8 "किमिति पृच्छन्ति? : clean
- p047:P1 {x-com:layout: …} : skip (layout chunk, no story text)
- p047:P2 "एवं तर्हि : clean (U1 noted, x-com kept, no block)
- p047:P3 "अये नीच! : F3
- p047:P4 सेनापतेः आज्ञानुसारं : clean
- p047:P5 एवम् एकघण्टां : clean
- p047:P6 वस्तुतः कलिङ्गसेना : clean
- p047:P7 स्थापितवन्तः। अनन्तरदिनतः : clean
- p047:P8 एवम् एव : F4
- p047:P9 "इदानीं विवेकः : F5
- p048:P1 {x-com:layout: …} : skip (layout chunk, no story text)
- p048:P2 वान्। कलिङ्गसेनापतिं : clean
- p048:P3 "तत् सद्यःकाले : clean
- p048:P4 जितवर्मा तथैव : clean
- p048:P5 वस्तुस्थितिः एवम् : clean
- p048:P6 कृत्वा युद्धम् : clean
- p048:P7 जितवर्मा अन्ये : clean
- p048:P8 एतत् युद्धं : clean
- J1 p045:P5 {pb} -> p045:P6 fresh : ok (column turn, clean break at terminal ।)
- J2 p045:P8 {pb} -> p046:P2 {pc} : ok (page turn; इति तस्य पत्नी सम्यक् जानाति joins with space)
- J3 p046:P4 {pb} -> p046:P5 {pc} : ok (column turn; प्रत्याक्रमणार्थं सिद्धता करणीया joins with space)
- J4 p046:P8 {pb} -> p047:P2 fresh : ok (page turn, clean break at terminal ।)
- J5 p047:P6 {pb} -> p047:P7 {pc} : ok (column turn; सेनाशिबिरं स्थापितवन्तः joins with space)
- J6 p047:P9 {wb} -> p048:P2 {pc} : ok (page turn; आदिष्टवान् joins solid)
- J7 p048:P5 {pb} -> p048:P6 {pc} : ok (column turn; आक्रमणं कृत्वा joins with space)
- J8 p048:P8 {pb} -> END : ok (story ends at terminal ।)
