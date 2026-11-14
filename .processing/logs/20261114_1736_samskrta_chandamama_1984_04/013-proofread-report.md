# Proofread report — 1984_04, START=013 (scan pages 13–18, story `पद्मनाभस्य विवाहः`, Vetala tale spanning the run)

## Summary

4 findings: 2 style (quote-supply verdicts F1–F2 for one speech split across a fresh column break) and 2 likely held unverified (verbatim dittography F3, speaker rupture F4). Systematic sort: frame-level Vetala/Raja dialogue in print singles, inner-story spoken dialogue in print doubles, thoughts and nested quotes in singles. `scan.py orth` on deblocked text reports 0 hits. Text is fresh human transcription from scans (not OCR output). Loc below is `pNN:Pm` (scan span + lint chunk) with the first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p017:P2 `करोति इति` | `अतः प्रतिनिवृत्य नगरं गच्छतु।` | `{ins:"}` after `गच्छतु।` | STY | style | high | one speech split by a fresh column break, so each para opens and closes its own pair; the `"वत्स!` open in this para pins the close at this sentence boundary |
| 2 | p017:P3 `रत्नभद्राय सर्वं` | `रत्नभद्राय सर्वं वृत्तान्तं निवेदयतु।` | `{ins:"}` before `रत्नभद्राय` | STY | style | high | same speech continued in a fresh para; the `अशक्तः"` close later in this para pins the open at the para start |
| 3 | p017:P3 `रत्नभद्रः बहुसन्तुष्टः` | `दृष्ट्वा बहु सन्तुष्टः अभवत्। रत्नभद्रः बहुसन्तुष्टः अभवत्। सः प्रीत्यादरेण` | `{sug-del:रत्नभद्रः बहुसन्तुष्टः अभवत्।}` kept | STY | likely | medium* | sentence repeats the preceding one verbatim with the same subject and predicate; probable dittography, held because sentence deletion needs a scan check |
| 4 | p017:P2 `चोरः उक्तवान्` | `करोति इति" चोरः उक्तवान्। अतः तुलामितं सुवर्णं मम कृते ददातु। यावज्जीवं भवतः उपकारं न विस्मरामि" इति।` | `?` | LEX | likely | low* | the thief speaks inside the ghost's cave and demands gold the penniless hero hasn't got, contradicting the ghost's free gift two sentences on; tried ghost-speaker, thief's-fee, and `करोति`-fix readings and none fits; settle by scan re-check of `चोरः`/`करोति` since images stay closed in this phase |

## Patterns

Pattern A — kept print punctuation (checked print-faithful, no blocks): the `महाशय!...भविष्यति"` speech in p016:P3 opens with `---` and no quote mark, and the stray `"` after `निश्चितवान्` in p018:P3 closes nothing locally; both are genuine print mismatches documented for the compiler, and the proofread gate's only residual (`quotes-open-past-end` on the p017:P3–p018:P3 chain) is this documented stray. Pattern B — house variants kept as seen, no findings: `बान्धवाः`, `वणिक्`, unapplied sandhi (`शिशुः इव`), `समयमानः`, and `तुलापरिमितं` (Ratnabhadra/Kapalika demand) beside `तुलामितं` elsewhere.

## Unverified

F3: settle by scan check whether both `सन्तुष्टः` sentences stand in print (possible proofreader strike on the second is not usable evidence in this images-closed phase); if print is single, drop the candidate. F4: settle by scan re-read of `चोरः` (candidates `घोरः`/`कृष्णभूतः`) and `करोति` (candidate `करोमि`) at 3x or tighter; no block added here because Phase A left no glyph flag on these words.

## Coverage

p013:P1 skip layout-only chunk
p013:P2 skip title chunk
p013:P3 पुनः पुनः : clean
p013:P4 पद्मनाभनामकः : clean
p013:P5 skip category metadata chunk
p014:P1 skip layout-only chunk
p014:P2 वसति स्म : clean
p014:P3 एव' इति : clean
p015:P1 skip layout-only chunk
p015:P2 रविवर्मणः वचने : clean
p015:P3 परिहासपात्रं करोमि : clean
p016:P1 skip layout-only chunk
p016:P2 लोहपरिवर्तनविद्याम् उपदिशामि : clean
p016:P3 गौरमुखः आदरेण : clean
p017:P1 skip layout-only chunk
p017:P2 करोति इति : F1, F4
p017:P3 रत्नभद्राय सर्वं : F2, F3
p018:P1 skip layout-only chunk
p018:P2 अवश्यं भविष्यति : clean
p018:P3 एव कुर्यात् : clean
J1 p013:P4 {pb} -> p014:P2 {pc} : ok (कुमुद्वतीनगरे + वसति spaced join)
J2 p014:P2 {pb} -> p014:P3 {pc} : ok (भवेत् + एव' spaced join, thought-single spans the column)
J3 p014:P3 {pb} -> p015:P2 fresh : ok (दत्तवान्। closes the advice; new scene at Ratnabhadra's house)
J4 p015:P2 {pb} -> p015:P3 {pc} : ok (किञ्चित् + परिहासपात्रं spaced join, thought-doubles span the column)
J5 p015:P3 {pb} -> p016:P2 {pc} : ok (आसीत्। closes the Somnatha scene; Kapalika backstory continues the topic)
J6 p016:P2 {pb} -> p016:P3 {pc} : ok (चोरः + गौरमुखः spaced join)
J7 p016:P3 {pb} -> p017:P2 {pc} : ok (साहाय्यं + करोति spaced join; the speaker word is queried in F4 but the join itself is clean)
J8 p017:P2 {pb} -> p017:P3 fresh : ok (गच्छतु। ends the column; the same speech continues fresh with the supplied marks F1/F2)
J9 p017:P3 {pb} -> p018:P2 {pc} : ok (विवाहः + अवश्यं spaced join)
J10 p018:P2 {pb} -> p018:P3 {pc} : ok (उपकारम् + एव spaced join, the Raja's answer spans the column)
J11 p018:P3 {pb} -> END : ok (clean tale close, frame returns to the tree)
