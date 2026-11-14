# Proofread report — 1984_04, START=024 (scan pages 24–28, story 'दानपात्रम्', complete story)

## Summary

9 findings: 8 error (2 quote-supply/sort, 6 word verdicts) and 1 likely held unverified. Systematic problem: print nests the quoted question in `""` inside `""` speech and drops one outer mark per speech (F1, F2). Title singles kept as printed (both Phase A `{sug-ins: '}` dropped with reason: single-stroke title quotes are print style, not speech). `scan.py orth` on deblocked text reports 0 hits. Text is fresh human transcription from scans (not OCR output). Loc below is `pNN:Pm` (scan span + lint chunk) with anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p025:P5 `द्वारपालकं ---` | `"आर्य, ... "महाश्वारोहिणः गृहं कुत्र?" ... भवतु इति।` | `{ins:"}` after `भवतु`; inner `"..."` to `'...'` | STY | error | high | outer speech needs its closing pair at the iti-closure; a question nested inside speech takes singles |
| F2 | p025:P6 `रहसि उक्तवान्` | `--- अये, ... "महाश्वारोहिणः गृहं कुत्र?" ... स्मर्तव्यम्" इति।` | `{ins:"}` after `---`; inner `"..."` to `'...'` | STY | error | high | each para opens and closes its own pair and the reporting verbs pin the speech; nested question takes singles |
| F3 | p026:P2 `वयं नूतप्रायाः` | `वयं नूतप्रायाः स्मः।` | `{del:नूतप्रायाः}{ins:मृतप्रायाः}` | OCR | error | high | `नूतप्रायाः` is not a word; `करभारेण मृतप्रायाः` is the idiom and print `नू` for `मृ` is a sort confusion |
| F4 | p027:P4 `आनीतानि खाद्यादीनी` | `खाद्यादीनी स्वीकृत्य` | `{del:खाद्यादीनी}{ins:खाद्यादीनि}` | SPL | error | high | neuter plural of the `खाद्यादि` group is `खाद्यादीनि`; long `ी` is impossible in the `-नि` ending |
| F5 | p027:P11 `निर्वन्धपूर्वकं राज्यदानं` | `निर्वन्धपूर्वकं` | `{del:निर्वन्धपूर्वकं}{ins:निर्बन्धपूर्वकं}` | SPL | error | high | `निर्बन्ध` (coercion) is the word and `निर्वन्ध` is not; `व`/`ब` print slip |
| F6 | p028:P4 `अतः नत्समीपे` | `अतः नत्समीपे यथा` | `{del:नत्समीपे}{ins:तत्समीपे}` | OCR | error | high | `नत्` is impossible; the ministers addressed the prince, so "as said in their (तत्) presence" for the assembly |
| F7 | p028:P8 `मा राजानम्` | `मा राजानम् अजानानः` | `{del:मा}{ins:मां}` | OCR | error | high | prohibitive `मा` cannot govern the participle; `मां राजानम्` (me, unrecognized as king) is required, anusvara dropped in print |
| F8 | p028:P8 `अजानानः ग्रामीणः` | `अजानानः` | `{sug-del:अजानानः}{sug-ins:अजानन्}` kept | MRP | likely | low* | `ज्ञा` forms शतृ, so `अजानन्`; शानच् `अजानानः` is ungrammatical but the print glyph is clear, so held |
| F9 | p028:P8 `मदोयाय अर्धराज्याय` | `मदोयाय` | `{del:मदोयाय}{ins:मदीयाय}` | SPL | error | high | `मदोयाय` is not a word; dative `मदीयाय अर्धराज्याय` (for my kingdom) is required |

## Patterns

Pattern A — nested-quote correction (F1, F2): both royal speeches quote the `महाश्वारोहिणः गृहं कुत्र?` question in print doubles inside print doubles, each missing one outer mark; both now read DQ outer with SQ inner per the speech-vs-thought sort. Kept-as-seen variants, no findings: glued `वसन्तिस्म।` (p024:P3) and `यःकश्चित्` (p027:P9), open sandhi `पितुसमीपं` (p028:P3) and `दुर्गस्य अन्तः` (p025:P5), retained visarga in `उदारबुद्धिःनामकः` (p024:P4), glued `विनायासं` (p027:P9) and `इत्ययं` (p027:P9), exclamations `स्म!` (p024:P4) and `सह!` (p028:P8), odd but intelligible `कतिपयदिनानाम् अनन्तरं` (p026:P5) and `अस्माकं कथं ... निवेदयतु` (p026:P2, read as "report our condition"). Proper nouns (`उदारबुद्धिः`, `महाश्वारोहिणः` 3x, `काशीनगरम्`) spell consistently throughout.

## Unverified

F8: settle `अजानन्` against a dictionary or grammar reference for शतृ of `ज्ञा`; the alternative `अजानता` is already excluded by subject agreement (`ग्रामीणः` nominative). Images stay closed in this phase so no glyph re-check applies.

## Coverage

p024:P1 skip layout-only chunk
p024:P2 skip title chunk
p024:P3 काशी बहुविशालं : clean
p024:P4 {pc}ग्रामीणाः सर्वे : clean
p024:P5 स्नेहपरः सः : clean
p024:P6 "आर्य! अहं : clean
p024:P7 एतत् श्रुत्वा : clean
p024:P8 skip author metadata chunk
p025:P1 skip layout-only chunk
p025:P2 गृहे तस्य : clean
p025:P3 समीचीनं भोजनं : clean
p025:P4 राजाश्वस्य कृते : clean
p025:P5 राजा तस्य : F1
p025:P6 इतः महाराजस्य : F2
p025:P7 {pc}आगत्य महाश्वारोहिणः : F2
p025:P8 बहुदिनपर्यन्तं राजा : clean
p026:P1 skip layout-only chunk
p026:P2 {pc}वयं मृतप्रायाः : F3
p026:P3 ग्रामीणः उक्तवान् : clean
p026:P4 ग्रामजनाः मिलित्वा : clean
p026:P5 कतिपयदिनानाम् अनन्तरं : clean
p026:P6 तत्क्षणम् एव : clean
p027:P1 skip layout-only chunk
p027:P2 ग्रामीणं दृष्ट्वा : clean
p027:P3 ग्रामीणः आनीतानि : clean
p027:P4 महाराजः अत्यन्तसन्तोषेण : F4
p027:P5 स्वयम् अपि : clean
p027:P6 अनन्तरम् ग्रामीणस्य : clean
p027:P7 {pc}दूरीकर्तुम् एव : clean
p027:P8 अनन्तरं राजा : clean
p027:P9 "यःकश्चित् ग्रामीणः : clean
p027:P10 ग्रामीणस्य कृते : clean
p027:P11 ग्रामीणः राज्यं : F5
p027:P12 किन्तु महाराजं : clean
p028:P1 skip layout-only chunk
p028:P2 {pc}बोधितवन्तः --- : clean
p028:P3 एतत्सर्वं अन्याय्यम् : clean
p028:P4 एतत्सर्वं श्रुत्वा : F6
p028:P5 अपरस्मिन् दिने : clean
p028:P6 {pc}अयं ग्रामीणः : clean
p028:P7 अनन्तरं सीमाप्रान्ते : clean
p028:P8 अन्ते एवम् : F7, F8, F9
p028:P9 महाराजस्य वचनं : clean
p028:P10 तदारभ्य स्वजीवितान्तं : clean
J1 p024:P3 {pb} -> p024:P4 {pc} (continues) : ok (तत्र + ग्रामीणाः, mid-sentence column turn)
J2 p024:P7 {pb} -> p025:P2 fresh (clean break) : ok (नीतवान्। closes the arrival; गृहे opens the household scene)
J3 p025:P6 {pb} -> p025:P7 {pc} (continues) : ok (समीपम् + आगत्य, king-to-doorkeeper speech spans the turn)
J4 p025:P8 {pb} -> p026:P2 {pc} (continues) : ok (करभारेण + वयं मृतप्रायाः, villagers' speech spans the page)
J5 p026:P3 {pb} -> p026:P4 fresh (clean break) : ok (करिष्यामि" इति। closes; ग्रामजनाः opens with a new subject)
J6 p026:P6 {pb} -> p027:P2 fresh (clean break) : ok (नीतवान्। closes; ग्रामीणं दृष्ट्वा opens the court scene)
J7 p027:P6 {pb} -> p027:P7 {pc} (continues) : ok (करभारं + दूरीकर्तुम्, column turn inside the purpose clause)
J8 p027:P12 {pb} -> p028:P2 {pc} (continues) : ok (गत्वा + बोधितवन्तः, the ministers' approach spans the page)
J9 p028:P5 {pb} -> p028:P6 {pc} (continues) : ok (कदाचित् + अयं ग्रामीणः, the king's speech spans the columns)
J10 p028:P10 {pb} -> END (clean break) : ok (terminal ।, story conclusive)
