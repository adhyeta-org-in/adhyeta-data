# Proofread report — samskrta_chandamama 1985_04, story p048 (pp. 48–51, issue end)

RUN `20261114_1859_samskrta_chandamama_1985_04`. Loc keyed on story coordinates `pNN:Pm:word` (NN = scan sequence, Pm = chunk number within that span matching lint P numbers, word counted on the chunk from 1, blocks counting as their word); chunk anchor in brackets. Story file `.processing/samskrta_chandamama/1985_04/p048.md`. Images stayed closed for the whole phase; all rulings from text, house style, and story sense.

## Summary

Seven findings: three quote-balance verdicts (one stray single open, two doubled closes, all fixed with `{del:}` blocks), one suspected omitted verb held for the user (dangling accusative at a column edge, no block — nothing to pin), two held spelling candidates (`दृढया`/`दृढया`, `शकट`/`शकट` ×2, `{sug-}` blocks), and one kept print quirk (spaced syllables as sound effect). The edition mixes open and joined sandhi (`यत् श्वः`, `बहिः आनीतवान्`, `वणिक् भैरवः` beside `तद्दिने`, `एतदनन्तरं`) and keeps house variants (`ग्रामीनः` ×2, consistent); per doctrine these stand as seen and are not findings. `scan.py orth` on deblocked text reports zero hits; the text is a manual transcription, not OCR output. Extract gate and proofread gate both pass (exit 0); every inherited `{sug-}` is routed below.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p49:P5:1 (एवं वा?) | `' + "एवं वा?` (stray `'` before the `"` open) | `{del:'}` (adopted; file now `{del:'}"एवं`) | STY | error | high | extra single open has no mate anywhere in the span; mocking speech takes DQ by era standard |
| F2 | p49:P4:16 (तदा उद्विग्नः) | `शक्नोमि""` (doubled close) | `{del:"}` (promoted; file now `शक्नोमि"{del:"}`) | STY | error | high | close carries a doubled mark verified at 3x in Phase A; single close balances the single open |
| F3 | p49:P5:15 (एवं वा?) | `पश्यामः""` (doubled close) | `{del:"}` (promoted; file now `पश्यामः"{del:"}`) | STY | error | high | same as F2; after F1+F3 the span reads `"एवं … पश्यामः"` balanced DQ |
| F4 | p48:P5:44 (महादेवशास्त्रिणां गृहस्य) | `वृषभः तेषां ग्रन्थानां दर्शनेन्छाम्` (accusative, no verb; next span opens fresh `कदाचित्`) | `?` (no block — no verb recoverable) | KRK | error | medium* | accusative object with no governing verb in this or the next span; full-width re-segmentation tested and rejected (breaks the `दृष्टवान् आसीत्`/`स्थापयित्वा` rows); suspected print omission held for the user |
| F5 | p49:P6:4-8 (अत्रान्तरे समीपे) | `व्या घ्र ग र्ज नं` (syllables spaced in print) | keep spacing as printed | STY | style | high | print spaces the syllables as a sound effect; fidelity keeps it, no block |
| F6 | p51:P2:6 (एतं वृषभं) | `दृढया` | `{sug-del:दृढया}{sug-ins:दृढया}` (held) | SPL | likely | medium* | `दृढया` is not a word; `दृढया` fits `गोष्ठे … रज्ज्वा बद्धवान्`; rescan at 3x+ settles ढ/ढ |
| F7 | p51:P4:6,22 (अनन्तरदिने भैरवः) | `शकटकर्षणार्थं`, `शकटकर्षणं` (×2) | `{sug-del:…}{sug-ins:शकट…}` on both (held) | SPL | likely | medium* | `शकट` is not a word; `शकट` (cart) fits both compounds; rescan at 3x+ settles ट/ट |

## Patterns

- Doubled high close strokes (`""`) for a single `"` close: 2 instances (F2, F3), both on p49, both verified at 3x in Phase A and removed by verdict. No other page shows it.
- Retroflex-for-dental suspicion ट/ट in `शकट` for `शकट`: 2 instances in one chunk (F7). Single pattern, single story; no wider claim.

## Unverified

- F4 (p48:P5:44 `दर्शनेन्छाम्`): suspected omitted verb (e.g. a lost `धृतवान्`-class predicate). Tried and rejected: joining with the `कदाचित्` span (no verb there), full-width row reading (breaks neighbouring rows), elided verb (none recoverable). Settles only with editorial judgment or a reprint check; no order change proposed.
- F6 (p51:P2:6): `दृढया` vs `दृढया`. Settles with a 3x+ rescan (out of scope — images closed).
- F7 (p51:P4:6,22): `शकट` vs `शकट` (×2). Settles with a 3x+ rescan.
- U1 (p48:P3:5 `एकं`, anchor महादेवशास्त्री इति): object of `निरोद्धुं` reads `एकं` ("a certain [thing]") — grammatical but thematically orphaned, no small-change glyph rival found (`वेगं`/`क्रोधं` do not fit the strokes). No block. Settles with print recheck or editor's sense; kept as seen.
- U2 (p51:P11:5 `तन्त्रशास्त्रस्य`, anchor एतदनन्तरं वृषभः): alternation `मन्त्रशास्त्र` (p48, the books) vs `तन्त्रशास्त्र` (p51, the renounced talk). Both are real words with distinct senses; kept as seen, no block, no action proposed.
- U3 (p50:P8:6 `ताडनम्`, anchor भैरवः जागरूकतया): `कदाचित् ताडनम् कदाचित् लालयन् च` mixes accusative noun with participle; readable as adverbial accusative ("by way of beating"), so kept as seen with no block. A stricter editor could normalise to `ताडयन्`; not proposed here.

## Coverage

- p48:P1 {x-com:layout} : skip layout-only chunk
- p48:P2 मन्त्रसिद्धिः : skip title chunk
- p48:P3 महादेवशास्त्री इति : clean
- p48:P4 वृषभः इच्छापूरणार्थं : clean
- p48:P5 महादेवशास्त्रिणां गृहस्य : F4
- p48:P6 कदाचित् आचार्येण : clean
- p48:P7 एषः एव : clean
- p48:P8 तद्दिने रात्रौ : clean
- p48:P9 author सुभद्रा : skip metadata chunk
- p49:P1 {x-com:layout} : skip layout-only chunk
- p49:P2 अन्येषां सहपाठिनाम् : clean
- p49:P3 अनन्तरदिने प्रातःकाले : clean
- p49:P4 तदा उद्विग्नः : F2
- p49:P5 एवं वा? : F1, F3
- p49:P6 अत्रान्तरे समीपे : F5
- p49:P7 वृषभः इदानीं : clean
- p49:P8 तदानीं तु : clean
- p50:P1 {x-com:layout} : skip layout-only chunk
- p50:P2 अतः कथं : clean
- p50:P3 अनिच्छन् अपि : clean
- p50:P4 वृषभस्य कष्टम् : clean
- p50:P5 तदा वृषभः : clean
- p50:P6 हृष्टवृषभतः रक्षणार्थं : clean
- p50:P7 अनन्तरं सः : clean
- p50:P8 भैरवः जागरूकतया : clean
- p51:P1 {x-com:layout} : skip layout-only chunk
- p51:P2 एतं वृषभं : F6
- p51:P3 तद्दिने रात्रौ : clean
- p51:P4 अनन्तरदिने भैरवः : F7
- p51:P5 यः वृषभं : clean
- p51:P6 नासारज्जुविषयं श्रुत्वा : clean
- p51:P7 कम्पितः यतः : clean
- p51:P8 तद्दिने रात्रौ : clean
- p51:P9 गुरुकुलस्य आचार्यः : clean
- p51:P10 मानवरूपं प्राप्तः : clean
- p51:P11 एतदनन्तरं वृषभः : clean
- J1 p048:P5 {pb} -> p048:P6 fresh : F4 (edge rupture — P5 ends mid-sentence, P6 opens fresh; suspected omitted verb, no reorder proposed; joint assertion stands as printed)
- J2 p048:P8 {pb} -> p049:P2 fresh : ok (clean break, thought opens new page)
- J3 p049:P4 {pb} -> p049:P5 fresh : ok (boast answered by mocking speech)
- J4 p049:P8 {pb} -> p050:P2 fresh : ok (`?` break into new episode)
- J5 p050:P4 {pb} -> p050:P5 {pc} : ok (attack continues into renewed flight)
- J6 p050:P8 {pb} -> p051:P2 {pc} : ok (caressing continues into leading home)
- J7 p051:P6 {pb} -> p051:P7 {pc} : ok (`भयेन कम्पितः` solid sense)
- J8 p051:P11 {pb} -> END : ok (clean story end, issue end)
