## Summary

Story `p023` (1985_03, scans 23-28, `दानस्य प्रभावः`) proofread images-closed: 8 findings (3 `STY`/error quote verdicts with blocks, 3 likely `OCR`/`SPL` held without blocks, 2 `CNS`/variant name-spelling notes) and 3 held candidates (the no-block items). Extract gate and proofread gate both pass with 0 error paras and 0 story findings after the verdicts; `scan.py orth` on deblocked text reports no findings. No Phase A `{sug-…}` queue was inherited (layout lines only), so no routing was due and no new word-glyph claims were invented; the three quote residuals were ruled from speech-vs-thought sense per the quote pass. Loc below is `pNN:Pm:word` (scan-sequence page + chunk matching lint `P` numbers, word counted on the chunk from 1) plus the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p023:P4:19 (तदा राजा) | `करोतु'" इति` | `करोतु'` (stray `"` removed via `{del:"}`) | STY | error | high | page's three speeches are all singles; trailing `"` is an unmatched extra stroke |
| 2 | p025:P6:44 (किन्तु तस्य) | `भवन्तु नाम' इति` | `भवन्तु नाम"` (sort corrected via `{del:'}{ins:"}`) | STY | error | high | reported speech takes era doubles; `इति`-closure pins the double close, single is a dropped second stroke |
| 3 | p026:P2:11 ({pc}पात्राणि अपि) | `करिष्यामि' इति` | `करिष्यामि"` (sort corrected via `{del:'}{ins:"}`) | STY | error | high | same miser's speech opened with `"` at p025:P11; `इति`-closure pins the double close across the `{pb}`/`{pc}` span |
| 4 | p025:P3:39 (किन्तु तत्क्षणात्) | `सर्वदा एतद्द्विपये एव` | `एतद्विषये` | SPL | likely | medium* | `एतद्द्विपये` is not a Sanskrit word; sense demands the locative `in this matter`; no block placed (no Phase A flag on file, images closed) |
| 5 | p026:P9:5 ("भोजनं सत्कारः) | `निर्गच्छतु इतः` | `निर्गच्छतु` | OCR | likely | medium* | `निर् + गच्छतु` needs repha; single-repha drop is the smallest change; print vs transcription slip undecidable images-closed, so no block |
| 6 | p026:P5:55 ({pc}नश्वरकोशीयस्य विषये) | `मातुलिं पञ्चशिखाग्निन् च` | `पञ्चशिखाग्निम्` | OCR | likely | medium* | `अग्नि`-stem accusative is `-ग्निम्` (cf. nom. `पञ्चशिखाग्निः` p027:P5); `न्`/`म्` nasal-sign confusion; held without block |
| 7 | p023:P6:23 (धर्मशालाचालनपूर्वकेण धर्माचरणेण) | `मातलीरूपेण` vs `मातुलिं` (p026:P5), `मातुलिः` (p027:P5) | ? (keep printed variants) | CNS | variant | high | same referent (Indra's charioteer) in three spellings; print fidelity, no emendation |
| 8 | p023:P6:25 (धर्मशालाचालनपूर्वकेण धर्माचरणेण) | `पञ्चशिखागिन-रूपेण` vs `पञ्चशिखाग्नि`- (p026:P5, p027:P5) vs `पञ्चाग्निः` (p027:P10) | ? (keep printed variants) | CNS | variant | high | same deity with `गिन`/`ग्नि` alternation plus short form; print fidelity, no emendation |

## Patterns

Name-spelling drift (F7, F8): `मातलि` appears as `मातली`/`मातुलि`, and `पञ्चशिखाग्नि` as `पञ्चशिखागिन`/`पञ्चाग्नि`; each form is internally readable and the referents are unambiguous, so all are kept as printed variants with no blocks.

## Unverified

U1 (= F4) `एतद्द्विपये`: settle by reopening scan 25 left column (`सर्वदा … एव चिन्तयन्` line) — `द्विप` vs `द्विष` plus single/double `द` decides print-vs-transcription slip. U2 (= F5) `निर्गच्छतु`: settle by reopening scan 26 right column (`निर्गच्छतु इतः` line) — presence/absence of repha on `र्ग`. U3 (= F6) `पञ्चशिखाग्निन्`: settle by dictionary/grammar check of the intended stem plus scan 26 right column (`मातुलिं … च आहूय` line) — final `न्` vs `म्`.

## Coverage

p023:P1 {x-com:layout: 2col, : skip layout
p023:P2 # दानस्य : skip title
p023:P3 ब्रह्मदत्तः काशीराज्यं : clean
p023:P4 तदा राजा : F1
p023:P5 अनन्तरं कोषाध्यक्षः : clean
p023:P6 धर्मशालाचालनपूर्वकेण धर्माचरणेण : F7, F8
p023:P7 एते स्वमानवजीवने, : clean
p023:P8 किन्तु तदनन्तरं : clean
p023:P9 {category: जातककथा}{pgb} : skip metadata
p024:P1 {x-com:layout: 2col, : skip layout
p024:P2 {pc}आसीत्। जनाः : clean
p024:P3 एषः पितुः : clean
p024:P4 यदा अन्नशालाः : clean
p024:P5 {pc}वयं कथञ्चित् : clean
p024:P6 तेषां प्रार्थनां : clean
p024:P7 नश्वरकोशीयः पूर्वजाः : clean
p024:P8 एकदा एषः : clean
p024:P9 तदा नश्वरकोशीयः : clean
p025:P1 {x-com:layout: 2col, : skip layout
p025:P2 {pc}बुभुक्षा एव : clean
p025:P3 किन्तु तत्क्षणात् : F4
p025:P4 तदा नश्वरकोशीयस्य : clean
p025:P5 "भवती अस्वस्था : clean
p025:P6 किन्तु तस्य : F2
p025:P7 "आम् आम्, : clean
p025:P8 {pc}मातृगृहीयाः धनिकाः : clean
p025:P9 "अथवा अस्माकं : clean
p025:P10 "भवतः एकस्य : clean
p025:P11 "वस्तुतः गृहे : F3
p026:P1 {x-com:layout: 2col, : skip layout
p026:P2 {pc}पात्राणि अपि : F3
p026:P3 पत्नी सर्वाणि : clean
p026:P4 एतन्मध्ये इन्द्रः : clean
p026:P5 {pc}नश्वरकोशीयस्य विषये : F6
p026:P6 अनन्तरम् इन्द्रः : clean
p026:P7 "रे, काशिगमनार्थं : clean
p026:P8 "किमर्थं कोपः? : clean
p026:P9 "भोजनं सत्कारः : F5
p026:P10 "पुत्र! कुपितः : clean
p027:P1 {x-com:layout: 2col, : skip layout
p027:P2 {pc}किञ्चित् मह्यं : clean
p027:P3 "अहं भवते : clean
p027:P4 "यावत् अस्ति : clean
p027:P5 एतावति काले : clean
p027:P6 शीघ्रम् एव : clean
p027:P7 "अरे! एतावत् : clean
p027:P8 ते मन्दारपत्राणि : clean
p027:P9 {pc}तानि पत्राणि : F8
p027:P10 एतन्मध्ये पञ्चाग्निः : F8
p027:P11 तदा सः : clean
p027:P12 "मया सज्जीकृतं : clean
p028:P1 {x-com:layout: 2col, : skip layout
p028:P2 {pc}एवं स्थिते : clean
p028:P3 कुपितः नश्वरकोशीयः : clean
p028:P4 तदा ते : clean
p028:P5 "वयं भवतः : clean
p028:P6 इन्द्रस्य वचनं : clean
J1 p023:P5 {pb} -> p023:P6 fresh (clean break) : ok
J2 p023:P8 {pb} -> p024:P2 {pc} (continues) : ok
J3 p024:P4 {pb} -> p024:P5 {pc} (continues) : ok
J4 p024:P9 {pb} -> p025:P2 {pc} (continues) : ok
J5 p025:P7 {pb} -> p025:P8 {pc} (continues) : ok
J6 p025:P11 {pb} -> p026:P2 {pc} (continues) : ok (same speech continues across the page turn)
J7 p026:P4 {pb} -> p026:P5 {pc} (continues) : ok
J8 p026:P10 {pb} -> p027:P2 {pc} (continues) : ok
J9 p027:P8 {pb} -> p027:P9 {pc} (continues) : ok
J10 p027:P12 {pb} -> p028:P2 {pc} (continues) : ok (same speech continues across the page turn)
J11 p028:P3 {pb} -> p028:P4 fresh (clean break) : ok
J12 p028:P6 {pb} -> END (clean break) : ok
