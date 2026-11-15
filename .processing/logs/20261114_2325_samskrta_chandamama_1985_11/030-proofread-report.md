## Summary

Five-scan story `मार्गदर्शकः` (scans 30-34, 39 chunks, 32 body paragraphs, six joints). Nine findings: four `STY` quote-sort/supply verdicts at style severity and high confidence (print opens thought with single but closes with double, and opens speech with single; corrected to house sort with mates supplied), plus five held candidates (all `*`, unverified, images closed): `परेध्युः`, `काल्पनिकम्`, `सङ्गीत`, `दुर्व्यसनं/निवारणीयम्`, and `बहिः` for `वहिः`. Scanner `orth` run on deblocked text reports no hits. No passage was left unchecked; the text is a manual transcription, not OCR output. Loc counts print words on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p030:P5 सुवर्णसदृशी फलवती :15 | `भूमिं क्रेष्यन्ति" इति` | `भूमिं क्रेष्यन्ति' इति` | STY | style | high | thought (`चिन्तितवान्`) takes single; print opens `'` but closes `"` |
| F2 | p031:P7 तत् किमपि :1 | `'तत् किमपि` | `"तत् किमपि` | STY | style | high | speech (`उक्तवान्`, outer) takes double; print opens `'` while inner `'...'` and close `"` are double-outer |
| F3 | p034:P5 आस्थानम् आगतं :11 | `'महाप्रभो,` | `"महाप्रभो,` | STY | style | high | speech (`उक्तवान्`, outer) takes double; print opens `'` while close `"` stands |
| F4 | p034:P5 आस्थानम् आगतं :49 | `अस्ति। वहिः अनारोग्यम्` | `अस्ति। 'वहिः अनारोग्यम्` | STY | style | high | inner proclamation content takes single; sentence boundary after `अस्ति।` pins the missing open |
| F5 | p032:P8 परेषुः कश्चन :1 | `परेषुः कश्चन` | `परेध्युः कश्चन` | LEX | likely | medium* | `परेषुः` (loc. pl.) fits poorly; `परेध्युः` (next day) fits the episode onset; needs 3x glyph check |
| F6 | p034:P5 आस्थानम् आगतं :15 | `केवलं कालनिक्रम्।` | `केवलं काल्पनिकम्।` | OCR | likely | medium* | `कालनिक्रम्` is no word; `काल्पनिकम्` (imaginary) fits `अस्वास्थ्यं`; needs 3x conjunct check |
| F7 | p034:P5 आस्थानम् आगतं :45 | `तु मङ्गीतसाहित्यनृत्यादिविलासे` | `तु सङ्गीतसाहित्यनृत्यादिविलासे` | OCR | likely | medium* | `मङ्गीत` is no word in this stock phrase; `सङ्गीत` (music) fits `साहित्यनृत्यादिविलास`; needs 3x `म/स` check |
| F8 | p033:P6 शिवस्य वार्ता :26 | `तस्य दुर्व्यसनः कथं निवारणीयः?` | `तस्य दुर्व्यसनं कथं निवारणीयम्?` | AGR | error | medium* | `व्यसन` is neuter; masculine pair mismatches the noun; needs dictionary/usage check |
| F9 | p034:P5 आस्थानम् आगतं :49 | `वहिः अनारोग्यम्` | `बहिः अनारोग्यम्` | OCR | error | high* | `वहिः` is no word; `बहिः/अन्तः` (outside/inside) is the fixed pair; needs 3x `व/ब` glyph check |

## Patterns

- Print opens thought/speech with single but closes with double, or opens outer speech with single where house expects double, 4x: F1 (p030:P5), F2 (p031:P7), F3/F4 (p034:P5). Each corrected/supplied via `{del:}/{ins:}` to house sort (thought `'`, speech `"`, nesting `DQ SQ...SQ DQ`); no new pairs invented.
- `ब/व` and `म/स` look-alikes plus one `न्त/न्त` conjunct form held for the user, 3x: F7, F9 (p034:P5), F6 (p034:P5). All need image re-check; none applied.

## Unverified

- F5 `परेषुः/परेध्युः`: held as `{sug-del:}/{sug-ins:}`; settle with 3x crop of p032:P8 word 1 (`षु` vs `ध्यु`) and story sense (next-day onset vs locative).
- F6 `कालनिक्रम्/काल्पनिकम्`: held; settle with 3x crop of p034:P5 word 15 (`लय` vs `ल्प`) and dictionary (`काल्पनिक` imaginary).
- F7 `मङ्गीत/सङ्गीत`: held; settle with 3x crop of p034:P5 word 45 (`म` vs `स`) and stock-phrase check (`सङ्गीतसाहित्य`).
- F8 `दुर्व्यसनः/दुर्व्यसनं`: held; settle with dictionary gender of `व्यसन` (neuter) and image check of visarga vs anusvara (`ः` vs `ं`) at p033:P6 words 26/28.
- F9 `वहिः/बहिः`: held though sense is certain (`बहिः/अन्तः` pair); settle with 3x crop of p034:P5 word 49 (`व` vs `ब`); images stayed closed per Phase B.

## Coverage

p030:P1 {x-com:layout: : skip (layout declaration, transparent to pairing)
p030:P2 # मार्गदर्शकः : skip (title)
p030:P3 पूर्वं रामपुरग्रामे : clean
p030:P4 एवं कालचक्रं : clean
p030:P5 सुवर्णसदृशी फलवती : F1
p030:P6 तदा किंकर्तव्यतामूढः : clean
p030:P7 {author: सुभद्रा} : skip (metadata)
p031:P1 {x-com:layout: : skip (layout declaration, transparent to pairing)
p031:P2 इति। : clean (page-turn `इति` closing p030:P6 `"` thought/speech; terminal, continuation verified)
p031:P3 प्रभुदेवं दृष्ट्वा : clean
p031:P4 कानिचन दिनानि : clean
p031:P5 अनन्तरं प्रभुदेवः : clean
p031:P6 शिवः नेत्रं : clean
p031:P7 तत् किमपि : F2
p032:P1 {x-com:layout: : skip (layout declaration, transparent to pairing)
p032:P2 भवान् योग्यः : clean
p032:P3 तदा शिवः : clean
p032:P4 तत्सर्वस्य निर्णयं : clean
p032:P5 अनन्तरं सः : clean
p032:P6 कः एषः : clean
p032:P7 शिव त्वरा : clean
p032:P8 परेषुः कश्चन : F5
p032:P9 प्रभुदेवः उक्तवान् : clean
p032:P10 एवं वा : clean
p033:P1 {x-com:layout: : skip (layout declaration, transparent to pairing)
p033:P2 इदानीं ग्रामं : clean
p033:P3 शिवः भित्तिम् : clean
p033:P4 अहो युक्तः : clean
p033:P5 शिवस्य सूचनया : clean
p033:P6 शिवस्य वार्ता : F8
p033:P7 स्वामिन् एवं : clean
p033:P8 ग्रामाधिकारी तस्यां : clean
p034:P1 {x-com:layout: : skip (layout declaration, transparent to pairing)
p034:P2 ग्रामाधिकारिणः जामाता : clean
p034:P3 एतस्याः घटनायाः : clean
p034:P4 यतः राजा : clean
p034:P5 आस्थानम् आगतं : F3, F4, F6, F7, F9
p034:P6 राजा महेन्द्रपालः : clean
p034:P7 राजा महेन्द्रपालः : clean
J1 p030:P4 {pb} -> p030:P5 {pc} (continues) : ok (column turn inside thought: `तु सुवर्ण...`, spaced join, adjective follows)
J2 p030:P6 {pb} -> p031:P2 {pc} (continues) : ok (page turn closing speech: `एव" इति।`, quote+`इति`, valid closure)
J3 p031:P7 {pb} -> p032:P2 {pc} (continues) : ok (page turn inside speech after F2: `तु भवान् योग्यः...`, spaced join, subject follows)
J4 p032:P10 {pb} -> p033:P2 {pc} (continues) : ok (page turn mid-sentence: `सर्वे इदानीं ग्रामं...`, subject+adverb, spaced join)
J5 p033:P8 {pb} -> p034:P2 fresh (clean break) : ok (episode ends with Gopala night-watch success; new episode jāmātā reform; terminal `।`, fresh para)
J6 p034:P7 {pb} -> END (clean break) : ok (story complete: minister appointed, name famous; terminal `।`, fresh end)
