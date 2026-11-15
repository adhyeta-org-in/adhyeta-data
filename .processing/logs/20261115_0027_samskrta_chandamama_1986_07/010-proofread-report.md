# Proofread report: 1986_07 p010 (START=10 END=17)

RUN: 20261115_0027_samskrta_chandamama_1986_07. Story file `.processing/samskrta_chandamama/1986_07/p010.md` (7 page spans, p10--p16; `ज्वालाद्वीपः`, serial continues past END). Phase A gate (extract) and Phase B gate (proofread) both green. Images stayed closed throughout Phase B. `scan.py orth` on deblocked text: 0 hits. Three Phase A `{x-com:}` residuals routed (two dropped after verdicts, two kept as provenance for held candidates). Loc keyed `pNN:Pm` + anchor (words counted on the chunk from 1).

## Summary

Five findings, all style/punctuation: one stray print quote-mark deleted (F1), one mismatched thought-close corrected single (F2), two stray singles inside a thought deleted (F3, F4), and one inner sound-mention re-sorted to doubles (F5); all applied as verdict blocks in the file. Three held candidates for the user (U1--U3, `*` confidence): `आस्म्`, `बह्वेयः`, `आकाशाच्चुम्बि`. The systematic feature is messy print quote punctuation inside thought passages (stray singles, one mixed close), plus stable house spellings kept as seen (open sandhi, `भीकरं`, `अत्रान्तरे`, `विशिष्ठा`, `नकेवलं`). Text is a direct print transcription, not OCR output. Glyph questions beyond 2x crops were held, not rechecked (images closed).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p10:P9 राजकुमारयोः कनिष्ठस्य :19 | `पर्वतकन्दरे 'अपतत्।` | delete stray `'` | STY | error | high | narration, no speech/thought/mention role; 2x crop shows one detached stroke, no close in print |
| 2 | p11:P10 'प्रायशः मम :11 | `स्यात्" इति` | `स्यात्' इति` | STY | error | high | `इति + चिन्तितवान्` thought takes singles; mixed double close corrected to single |
| 3 | p11:P6 चित्रसेनः। अनाथः :24 | `एव 'शरणम्।` | delete stray `'` | STY | error | high | predicate noun inside thought, no quotative role; print speck kept through Phase A, deleted here |
| 4 | p11:P6 चित्रसेनः। अनाथः :39 | `इति 'शब्दः` | delete stray `'` | STY | error | high | `इति` already closes the `'जीर'` mention; second open has no role |
| 5 | p11:P6 चित्रसेनः। अनाथः :37 | `'जीर'` | `"जीर"` | STY | style | high | sound-mention nested inside thought-singles takes doubles by sort alternation |

## Patterns

Kept print forms (no blocks; print-faithful per open-sandhi/house-spelling doctrine): open vowel/visarga junctions throughout (`तारकेश्वरः नाम`, `तदा अटन्तौ`, `सः शून्यदृष्ट्या`); `भीकरं` (p10:P8), `तदा तदा` emphatic repetition (p10:P6, checked, no dittography basis); `अत्रान्तरे` twice (p12:P4, p15:P3); `विशिष्ठा` for विशिष्टा (p13:P8); `नकेवलं` fused (p14:P5); `आस्म्` held separately (U1). Shout elongation read as avagraha `अग्रजऽऽ, शूरसेनऽऽऽ` (p12:P3, 3x crop; strokes match ऽ, Latin rejected by gate).

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why / what would settle it |
|---|---|---|---|---|---|---|---|
| U1 | p12:P6 चित्रसेनस्य वचनं :22 | `प्रतीक्षायाम् आस्म् अहम्` | `आसम्` | OCR | likely | medium* | 1sg `आसम्` fits `अहम्` exactly; print `स्म्/स्म` transposition. Settles with a 3x glyph recheck (images closed to this agent). |
| U2 | p13:P3 पर्वतपादे बह्वेयः :2 | `बह्वेयः गुहाः` | `बह्व्यः` | OCR | likely | medium* | fem nom pl `बह्व्यः` agrees with `गुहाः`; `ेय/्य` confusion at scan resolution. Settles with a 3x glyph recheck. |
| U3 | p15:P5 नन्तरं यदा :13 | `आकाशाच्चुम्बि` | `आकाशचुम्बि` | OCR | likely | low* | extra `च` unclear at scan resolution (`च्च` vs `च`); standard compound is `आकाशचुम्बि`. Settles with a 3x glyph recheck. |

Held as `{sug-del:}{sug-ins:}` pairs in the file; never applied.

## Coverage

p10:P1 {x-com:layout: : skip x-com-only chunk, no story text.
p10:P2 # ज्वालाद्वीपः : skip title chunk.
p10:P3 नर्मदानद्याः तीरे : clean (dual `उभौ पुत्रौ`, `पाल्यति`-with-`स्म` idiom, folio absent so bare pgb).
p10:P4 ज्येष्ठस्य पुत्रस्य : clean (dual `उत्साहिनौ`, `विशेषासक्तिः` agreement, wrapped `अष्टादशवर्षीयः` joined solid).
p10:P5 एकदा उभौ : clean (क्त्वा participles same-subject `गतवन्तौ/दृष्टवन्तौ`, wrapped compounds joined).
p10:P6 राजकुमारौ स्वकीयम् : clean (`तदा तदा` kept as emphatic repetition, `तौ` + pc joins J1).
p10:P7 स्वपरिवारतः पृथक् : clean (short continuation closing J1, terminal ।).
p10:P8 एवं बहुदूरं : clean (`भीकरं` kept house form, `तावता एव` instrumental, dual verbs throughout).
p10:P9 राजकुमारयोः कनिष्ठस्य : F1 (instrumental `यजमानेन` with passive participle, `खलीन` bridle term kept; stray `'` deleted, no other quotative role on the page).
p10:P10 अधः पतितः : clean (absolutive `उत्थाय` opens J2).
p11:P1 {x-com:layout: : skip x-com-only chunk.
p11:P2 आगतवान् ततः : clean (absolutive + `आगतवान्` completes `उत्थाय`, pluperfect sense `मृतः आसीत्` closes J2).
p11:P3 अश्वस्य मरणं : clean (`दृश्येत वा` optative, thought-singles with `इति + आलोचितवान्`).
p11:P4 सः प्रदेशः : clean (instrumental of description `वृक्षैः`, `दृश्यन्ते स्म` idiom).
p11:P5 का दिक् : clean (`ज्ञातवान्` seeks subject, opens J3).
p11:P6 चित्रसेनः। अनाथः : F3, F4, F5 (long thought mapped mark by mark; outer singles kept, two strays deleted, inner mention re-sorted; `उत्कीर्णः` kept as seen with no glyph basis to change).
p11:P7 आत्मनः दुःस्थितिं : clean (क्त्वा pair same-subject, thought-singles with `इति + आलोचयन्`).
p11:P8 नदीं दृष्टवतः : clean (genitive absolute `दृष्टवतः`, `पिबन्` contemporaneous participle).
p11:P9 पिपासायाः निर्गमनेन : clean (ablative of cause, `चिन्तयितुम्` infinitive of purpose).
p11:P10 'प्रायशः मम : F2 (mixed close corrected; `पलायमानं अश्वम्` accusative opens J4).
p12:P1 {x-com:layout: : skip x-com-only chunk.
p12:P2 एषः दृष्टवान् : clean (nom `एषः` + `अश्वम्` closes J4, terminal ।).
p12:P3 "अग्रजः शूरसेनः : clean (doubles with `इत्यपि` hope-framing kept as print sort; shout elongation verified as ऽ at 3x with provenance x-com).
p12:P4 चित्रसेनस्य ध्वनिः : clean (locative `पर्वतकन्दरे`, mdash before speech-doubles, `आगच्छतु भोः` imperatives).
p12:P5 एतेन कण्ठध्वनिना : clean (instrumental of cause, mdash before speech-doubles, plural `आगच्छन्तु/प्रदर्शयन्तु` kept as print).
p12:P6 चित्रसेनस्य वचनं : U1 (speech-doubles with `इति` correct; `आस्म्` held, `आह्वयेत्` kept as seen).
p12:P7 वा न। : clean (short continuation closing J5, terminal `!` + `इति`).
p12:P8 चित्रसेनः क्षणमात्रेण : clean (thought-singles with `इति`, correlatives `यत्/तत्` intact).
p12:P9 एवं निश्चित्य : clean (locative `हस्ते` opens J6).
p13:P1 {x-com:layout: : skip x-com-only chunk.
p13:P2 खड्गं गृहीत्वा : clean (क्त्वा chain same-subject closes J6, `तीर्त्वा` kept print form).
p13:P3 पर्वतपादे बह्वेयः : U2 (comma after `आहूतवान्` kept as print; `बह्वेयः` held; mdash before speech-doubles).
p13:P4 चित्रसेनः युद्धार्थं : clean (`सिद्धः इव` predicative, `प्रसारितवान्` with accusative `दृष्टिं`).
p13:P5 गुहायां कश्चन : clean (locative + `उपविष्टः` opens J7, `पलितानि` neuter pl agreement).
p13:P6 आसीत् सः। : clean (short continuation closing J7, ablative `रन्ध्रात्` + `आगच्छति स्म` idiom).
p13:P7 गुहां प्रविष्टः : clean (accusative with `प्रविष्टः`, `नमस्कृत्य` ल्यप्, mdash before speech-doubles).
p13:P8 चित्रसेनस्य वचनं : clean (long speech-doubles with `इति`, `षष्टिवर्षाणां` genitive of measure, `सत्पात्रम्` t+प sandhi, `विशिष्ठा` kept).
p13:P9 सिद्धयोगिनः हस्ततः : clean (ablative of source, infinitive `उद्घाटयितुम्` + `उद्युक्तः`, opens J8).
p14:P1 {x-com:layout: : skip x-com-only chunk.
p14:P2 तदा सः : clean (fresh para closes J8; speech-doubles with `इति`, `सहनया` kept as instrumental of manner).
p14:P3 चित्रसेनः सिद्धयोगिनः : clean (instrumental `शिरश्चालनपूर्वकम्`, dative `अनुग्रहार्थं`).
p14:P4 तदा सिद्धयोगी : clean (speech-doubles with `इति`, `करिष्यमाणः` future participle, `पर्याप्तम्` closings).
p14:P5 सिद्धयोगिनं नमस्कृत्य : clean (क्त्वा chain same-subject, `नकेवलं` fused kept, fem `अशक्या` agrees with `स्थितिः`, opens J9).
p14:P6 चित्रसेनः तत्रैव : clean (fresh para closes J9; `पृष्टः` passive + instrumental `तेन`, `पृच्छेत्` optative, `प्रष्टुं` infinitive).
p14:P7 अनन्योपायः चित्रसेनः : clean (`कल्पयन्` contemporaneous, `आश्रितवान्` with accusative `दिशम्`, nom `चित्रसेनः` opens J10).
p15:P1 {x-com:layout: : skip x-com-only chunk.
p15:P2 तीव्रं बुभुक्षाम् : clean (accusative + `अनुभूतवान्` closes J10).
p15:P3 श्रमम् अनुभवन् : clean (contemporaneous participles, thought-singles with `इति`, `तावत्` + `न` idiom kept).
p15:P4 सः कण्डोलं : clean (`अवतार्य` ल्यप्, `निमील्य` ल्यप्, mid-word `क्षणद्वया` opens J11).
p15:P5 नन्तरं यदा : U3 (mid-word continuation closing J11; `आकाशाच्चुम्बि` held; doubled `तत्` kept as emphatic print).
p15:P6 आत्मनः पुरतः : clean (`दृष्ट्वा` same-subject, `स्मृतवान्` with accusative `वचनं`).
p15:P7 "हन्त! कीदृशी : clean (speech-doubles self-reproach with `इति`, `अजागरूकतया` instrumental, mid-word `अनुभूत` opens J12).
p16:P1 {x-com:layout: : skip x-com-only chunk.
p16:P2 वान् चित्रसेनः। : clean (mid-word continuation closing J12, terminal ।).
p16:P3 तस्मिन् समये : clean (`अजानन्` contemporaneous, `सिद्धः` predicative with dative `युद्धार्थं`, opens J13).
p16:P4 राक्षसः विकटाट्टहासं : clean (`आगत्य` ल्यप्, speech-doubles open at `अये`, `धैर्यं` opens J13; `मानवशिशुक` depreciative kept, `उग्राक्ष` epithet consistent).
p16:P5 भवतः? मानवाः : clean (continuation closing J13; `सम्मुखीकृतवान्` with accusative `मां`, doubles with `इति + उक्तवान्`).
p16:P6 अनन्तरं महाभवनं : clean (accusative with `पश्यन्`, mdash before speech-doubles, `पृष्टवान् सः राक्षसः` order kept).
p16:P7 "आम्" इति : clean (short `"आम्"` answer-doubles correct; `"अहो हो हो!"` exclamation correct; final speech-doubles open at `एतत् महारण्यं` and unclosed at range end — cross-range pair, see J14; `तातपादाः` ironic honorific kept).

J1 p010:P6 {pb} -> p010:P7 {pc} (continues) : ok (`तौ` no terminal, spaced join `तौ स्वपरिवारतः`).
J2 p010:P10 {pb} -> p011:P2 {pc} (continues) : ok (absolutive `उत्थाय` + `आगतवान्`, single clause across page turn).
J3 p011:P5 {pb} -> p011:P6 {pc} (continues) : ok (verb `ज्ञातवान्` + subject `चित्रसेनः`, mid-sentence column turn).
J4 p011:P10 {pb} -> p012:P2 {pc} (continues) : ok (accusative `अश्वम् अपि` + `एषः दृष्टवान् आसीत्`, object fronted across page turn).
J5 p012:P6 {pb} -> p012:P7 {pc} (continues) : ok (`राक्षसः वा न`, disjunction split across column turn).
J6 p012:P9 {pb} -> p013:P2 {pc} (continues) : ok (locative `हस्ते` + `खड्गं गृहीत्वा`, instrumental phrase across page turn).
J7 p013:P5 {pb} -> p013:P6 {pc} (continues) : ok (`उपविष्टः आसीत् सः`, participle + copula across column turn).
J8 p013:P9 {pb} -> p014:P2 fresh (clean break) : ok (terminal । before edge, fresh scene paragraph, no indent claim needed).
J9 p014:P5 {pb} -> p014:P6 fresh (clean break) : ok (terminal । before edge, fresh paragraph same scene).
J10 p014:P7 {pb} -> p015:P2 {pc} (continues) : ok (nom `चित्रसेनः` + `तीव्रं बुभुक्षाम् अनुभूतवान्` across page turn).
J11 p015:P4 {wb} -> p015:P5 {pc} (continues) : ok (solid mid-word `क्षणद्वया+नन्तरं`, hyphenation dropped).
J12 p015:P7 {wb} -> p016:P2 {pc} (continues) : ok (solid mid-word `अनुभूत+वान्` across page turn, hyphenation dropped).
J13 p016:P4 {pb} -> p016:P5 {pc} (continues) : ok (`धैर्यं भवतः?`, question split across column turn).
J14 p016:P7 {pb} -> END (clean break) : continues to next range (mid-sentence `समुद्रे` + open speech-doubles at `एतत् महारण्यं`; tool labels END but the serial carries `- अनुवर्तते` on p17 — coordinator to pair with p017:P2 `{pc}`).

## Continuation 2026-11-15: orphan scan 17 appended (p017)

Phase A (images open, ONLY `17.jpg`; other scans never reopened): the story file covered scans 10--16 (7 page spans) with scan 17 orphaned mid-sentence (`समुद्रे{pb}{pgb}`). Transcribed scan 17 print-faithfully as one new page span after the last complete `{pgb}`; no existing span altered. Layout `{x-com:layout: 2col, text top, art bottom full-width}` (text block above, full-width signed illustration below; illustrator word stripped). The span opens with `{pc}` (straight continuation of the rakshasa's speech) and closes `(--- अनुवर्तते){pb}{pgb}` (bare `{pgb}`, no folio in print; mdash per the `(--- अनुवर्तते)` precedent). Phase A left two filings in the new span: an x-com on a lone single stroke before `इदानीम्` (verified single at 3x, no mate) and `{sug-del:अर्पयत}{sug-ins:अर्पयतु}`. Images closed after Phase A; the proofread below rules only on p017, old spans untouched.

### Summary (continuation)

Three findings, all in the new span: one stray print quote-mark deleted (F6), one imperative restored (F7), one mismatched thought-close corrected to single (F8); all applied as verdict blocks in p017 only. `scan.py orth` on deblocked full-story text after the verdicts: 0 hits. Proofread gate green (8 pages, 0 error paras, 0 story findings). Story now spans 8 page spans, p10--p17.

### Findings (continued numbering)

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 6 | p17:P2 क्षिपामि इदानीम्। :1 | lone `'` between `क्षिपामि` and `इदानीम्` | delete stray `'` | STY | error | high | 3x crop shows one single stroke; the enclosing speech-doubles (`"एतत् ... भवान्?"`) leave no mate anywhere on the page and no nested-sense role, so the mark crosses the pair; deleted as stray sort, print recorded in the adjacent x-com |
| 7 | p17:P6 "भवान् अस्मिन् :16 | `मह्यम् अर्पयत यदा` | `अर्पयतु` | MOR | error | high | second-person demand (`भवान्`) with `यदा`-future clause requires the imperative; bare `अर्पयत` is ungrammatical here; print lacks the उ-mātrā at 3x (apparent misprint); Phase A filed the pair, promoted to verdict |
| 8 | p17:P7 'का इयं :22 | `कर्तव्यम्" इति` | `कर्तव्यम्' इति` | STY | error | high | thought span (SQ open + `इति + चिन्तितवान्`) takes singles; print's double close is a wrong sort, corrected (same correction as F2) |

Kept print forms in p017 (no blocks): open sandhi (`मया अत्र`, `मम तत्र`, `तदा तं`); `जागरूको` (regular visarga sandhi before `भवतु`); `इतःपूर्वं`; `अनन्तरं` (matches old spans); `अष्टादशवर्षीयः` kept as printed (differs from `अष्टादशवर्षीयः` at p10:P4; number-word print variant, sense identical); `काऽपि` avagraha as seen.

### Coverage (p017 only)

p17:P1 {x-com:layout: : skip x-com-only chunk, no story text.
p17:P2 क्षिपामि इदानीम्। : F6 (closes J14 with `समुद्रे क्षिपामि`; enclosing speech-doubles close at `भवान्?`; `ग्रहीतुम्` infinitive of purpose; stray single deleted).
p17:P3 चित्रसेनः राक्षसतः : clean (mdash before speech-doubles, `पृच्छेयम्` optative, `कदा मिलितवान्` closing question).
p17:P4 "किमपि व्याजं : clean (speech-doubles with `इति + उक्तवान्`, `धिक्कृत्य` kept, gerundive `अङ्गीकरणीयं` + instrumental `भवता`).
p17:P5 "किं तत्?" : clean (short question-doubles with `इति + पृष्टवान्`, terminal ।, opens J15 column turn).
p17:P6 "भवान् अस्मिन् : F7 (demand-doubles with `इति + पृष्टवान्`; `निवसतु` 3rd imperative with `भवान्`; `अर्पयतु` restored by verdict).
p17:P7 'का इयं : F8 (thought mapped mark by mark; SQ open kept, DQ close corrected to single; `अविवाहितः` kept, `प्राणरक्षणं तु प्रथमं कर्तव्यम्` maxim).
p17:P8 अतः सः : clean (counter-offer doubles with `इति`; `उत्पत्स्यमानः ... पुत्रः` fut-participle agreement; `तं नेतुम् अर्हति भवान्` idiom).
p17:P9 एतत् श्रुत्वा : clean (acceptance doubles with `इति`; `विस्मर्तव्यम्`/`करणीयम्` gerundives; `(--- अनुवर्तते)` serial marker; bare `{pgb}`, no folio; opens J16 range end).

J14 p016:P7 {pb} -> p017:P2 {pc} (continues) : ok (`समुद्रे क्षिपामि` locative + 1sg verb across the page turn; supersedes the "continues to next range" line above, now resolved in-file).
J15 p017:P5 {pb} -> p017:P6 fresh (clean break) : ok (terminal । before edge; left-column Q/A closes, right-column demand-doubles open fresh — column turn, no indent claim).
J16 p017:P9 {pb} -> END (clean break) : ok (terminal । before edge; `(--- अनुवर्तते)` marks serial continuation beyond the issue range, not a swallowed continuation).
