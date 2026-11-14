# Proofread report — 1984_10 p033 (RUN 20261114_1627_samskrta_chandamama_1984_10)

## Summary

2 findings: 1 verified quote-sort correction (STY / style / high, F1) and 1 held spelling candidate (SPL / likely / medium*, F2). The systematic pattern is the print's quote sorts (doubles for speech and some thoughts, singles for thought and sound bursts) with one mismatched close corrected in F1. `scan.py orth` on deblocked story text gave 0 hits; word, sandhi, quote, and flow passes found nothing else; no passages were left unchecked. The text was transcribed by eye from scans (not OCR), with uncertain glyphs and all quote strokes verified under enlarged crops in Phase A. Loc below is `pNN:Pm` (NN = scan sequence from filename `p033` plus `{pgb}`-span order; Pm = chunk number in that span, matching lint `P` numbers) plus the chunk's first two words as anchor; corrections travel only as blocks in the story file, never as silent edits. Print forms kept as seen with no block: open-sandhi spellings (`वस्तुतः आर्द्राणि`, `हिमः इव`, `किञ्चित् इव`, `शेखरः इव`), glued colloquial `इदमिदानीं`, and the narrative oddity `ग्रीष्मः कालः। शैत्यम् अत्यधिकम् आसीत्।` (glyph verified; story-logic observation only, not a language defect).

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p034:P12 «ऊर्णवस्त्राणाम् आशया» | `दयालुः!" इति` | `दयालुः!{del:"}{ins:'} इति` | STY | style | high | thought (`मनसि एव चिन्तितवान्`) takes singles; open verified single-stroke at 3x, close pinned at the `!"` boundary |
| F2 | p036:P4 «किन्तु बालशुनकस्य» | `अपराधाणां फलम्` | `अपराधानाम् फलम्` | SPL | likely | medium* | dental ध blocks natva (cf. प्रधान, आराधना); glyph re-check is closed so held for the user |

## Patterns

PAT-1 print quote sorts: doubles for reported speech (verified two-stroke opens/closes, e.g. p034:P6, p035:P4, p036:P8–P9, p037:P3–P8) and for some thoughts (`"बाल्ये कृतानाम्..."`, `"अहं निवेदयामि..."`); singles for thought and sound bursts (`'कुँ कुँ'`, `'कथां वदतु'`, `'एकस्य...'`, `'शेखरः माम् एव...पीडयेत्?'`, `'अहम् एव...करोमि।'`). 1 mismatch corrected (F1: single open with double close). The Phase A `{sug-ins:'}` dropped-second-stroke hypothesis for F1's open was rejected (true single, sort-appropriate) and dropped.

## Unverified

F2 `अपराधाणां` → `अपराधानाम्` (SPL, medium*): the natva rule is certain, but the print's ण/न glyph cannot be re-checked with images closed (Phase A read ण at display size); a print re-check at 3x of `बाल्ये कृतानाम् अपराधाणां` would settle it. The candidate travels as `{sug-del:अपराधाणां}{sug-ins:अपराधानाम्}` in the story file.

## Coverage

p033:P1 «{x-com:layout:» : skip layout
p033:P2 «# पाप-परिहारः» : skip title
p033:P3 «नटवरः बाल्यतः» : clean
p033:P4 «कदाचित् एकं» : clean
p033:P5 «बुभुक्षया व्याकुलः» : clean
p033:P6 «किञ्चित्कालानन्तरं नटवरः» : clean
p033:P7 «कदाचित् नटवरः» : clean
p033:P8 «क्रमशः नटवरः» : clean
p033:P9 «वृष्टेः अभावतः» : clean
p033:P10 «सौभाग्येन सः» : clean
p033:P11 «{author: विवेकः}{pgb}» : skip metadata
p034:P1 «{x-com:layout:» : skip layout
p034:P2 «धनिकस्य गृहे» : clean
p034:P3 «धनिकः सज्जनः» : clean
p034:P4 «धनिकस्य पुत्रः» : clean
p034:P5 «यदा नटवरः» : clean
p034:P6 «धनिकः चिन्तयति» : clean
p034:P7 «उत्साहः नास्ति» : clean
p034:P8 «नटवरः भीत्या,» : clean
p034:P9 «तद्दिनात् आरभ्य» : clean
p034:P10 «ग्रीष्मः कालः।» : clean
p034:P11 «एकस्मिन् दिने» : clean
p034:P12 «ऊर्णवस्त्राणाम् आशया» : F1
p034:P13 «धनिकस्य गृहे» : clean
p035:P1 «{x-com:layout:» : skip layout
p035:P2 «धावतु। अन्यथा» : clean
p035:P3 «नटवरः भीतः।» : clean
p035:P4 «अन्ते शेखरः» : clean
p035:P5 «तानि वस्त्राणि» : clean
p035:P6 «शेखरविषये नटवरः» : clean
p035:P7 «तस्मिन् समये» : clean
p035:P8 «एव। शेखरः» : clean
p035:P9 «नटवरः एतत्» : clean
p035:P10 «धनिकस्य गृहे» : clean
p035:P11 «एकस्मिन् दिने» : clean
p036:P1 «{x-com:layout:» : skip layout
p036:P2 «शेखरः भवन्तं» : clean
p036:P3 «मित्रस्य अनुकम्पं» : clean
p036:P4 «किन्तु बालशुनकस्य» : F2
p036:P5 «इदानीं पुनः» : clean
p036:P6 «एतावत् पीडयति।» : clean
p036:P7 «सः तत्क्षणे» : clean
p036:P8 «एतत् दृष्ट्वा» : clean
p036:P9 «"अहं न» : clean
p036:P10 «नटवरः शेखरहस्ततः» : clean
p036:P11 «एतत् सर्वं» : clean
p037:P1 «{x-com:layout:» : skip layout
p037:P2 «वान्। किमर्थम्» : clean
p037:P3 «नटवरः शान्तरीत्या» : clean
p037:P4 «एवं वदतः» : clean
p037:P5 «नटवरस्य वचनैः» : clean
p037:P6 «धनिकस्य एतं» : clean
p037:P7 «वचनानि उक्तवान्।» : clean
p037:P8 «धनिकः शान्तस्वरेण» : clean
p037:P9 «अनन्तरकाले नटवरस्य» : clean
J1 p033:P5 {pb} -> p033:P6 fresh (clean break) : ok
J2 p033:P10 {pb} -> p034:P2 {pc} (continues) : ok (एकस्मिन् + धनिकस्य, spaced page turn)
J3 p034:P6 {pb} -> p034:P7 {pc} (continues) : ok (भवतः + उत्साहः, spaced column joint)
J4 p034:P13 {pb} -> p035:P2 {pc} (continues) : ok (इतः + धावतु, spaced page turn)
J5 p035:P7 {pb} -> p035:P8 {pc} (continues) : ok (करणीयः + एव, spaced column joint)
J6 p035:P11 {pb} -> p036:P2 {pc} (continues) : ok (इतःपरं + शेखरः, spaced page turn)
J7 p036:P5 {pb} -> p036:P6 {pc} (continues) : ok (एव + एतावत्, spaced column joint; left-below-art column read before right column is the unique fit: quote opened in P5 closes in P6 and narrative order requires it)
J8 p036:P11 {wb} -> p037:P2 {pc} (continues) : ok (आहूत + वान् = आहूतवान्, solid page turn)
J9 p037:P6 {wb} -> p037:P7 {pc} (continues) : ok (हित + वचनानि = हितवचनानि, solid column joint)
J10 p037:P9 {pb} -> END (clean break) : ok
