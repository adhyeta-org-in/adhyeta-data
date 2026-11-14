# Proofread report — 1986_05, START 030 (pages 30–34, `शिवपुराणम्`)

## Summary

2 findings, both error/high in one pattern: a dropped second stroke on a speech open (single open against a double close), fixed via `{del:'}{ins:"}` at p030:P8 and p033:P10. Extract gate and proofread gate both pass with 0 error paras and 0 residual notes; the `orth` scanner on deblocked text reports 0 hits. Loc below is `pNN:Pm` (NN = scan-sequence page, Pm = chunk number within that span) plus the first two words as anchor. No inherited `{sug-ins:}`/`{sug-del:}` queue existed and no `{del:}`/`{ins:}` contamination was present, so the only file amendments are the two quote verdicts; story text is otherwise byte-identical to the Phase A transcription. Images stayed closed for the whole phase; every ruling below is from text, house style, and story sense. Print-faithful items checked and kept as seen: balanced single-quote utterances (`'भिक्षां देहि'`, `'अनन्तरम् आगच्छतु'`, `'किमपि न लब्धम्'`, nested `'बुभुक्षितः किं न करोति पापम्'`), open/join sandhi mix (`तद् दिने` nowhere here; kept `तद्दिने`-style joins only where print joins), correct `कोऽपि` avagraha, dual `वसतः` for the divine couple, and house spellings below. Phase A transcription residuals carried as checked (no blocks): mid-word speck dot dropped in `तत्रत्यराजपुरोहितेषु` (p030:P6), detached speck dropped after `इति` before `चिन्तयन्तः` (p034:P4) and under `खलु` (p033:P2), spacing normalized before `?`/`!` per house Unicode rules, wrap hyphens dropped silently inside columns, footer quotes dropped around the `{note: १५. काशीक्षेत्रे व्यासः}` episode label (p030:P10), and `दृष्टम्` (p032:P4) settled from grammar since only neuter `दृष्टम्` parses with `मुखं`.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p030:P8 राजन्, किञ्चित्कालं | `'राजन्,` opening Dhundhi's speech | `"` open (`{del:'}{ins:"}` applied in file) | OCR | error | high | Print drops one stroke of the doubled open; the close mate `दास्यति"` is double and `इति उक्तवान्` marks spoken speech, so the era sort is double. |
| 2 | p033:P10 तदा वृद्धा | `'भोः आर्याः,` opening the hostess's speech | `"` open (`{del:'}{ins:"}` applied in file) | OCR | error | high | Same defect; the close mate `कुर्वन्तु"` on p034:P2 is double and `इति उक्तवती` marks spoken speech, so the era sort is double. |

## Patterns

Dropped open-quote stroke upgraded to double (`{del:'}{ins:"}`), count 2: p030:P8 (close mate `दास्यति"` same page) and p033:P10 (close mate `कुर्वन्तु"` across the page turn on p034:P2). Balanced single-quote utterances elsewhere are kept as seen per the p01 proofread precedent and are not part of this pattern.

## Unverified

No file blocks were issued for these (Phase B invents no new glyph claims without a Phase A flag on file); each is kept as transcribed, with what would settle it. U1. p032:P7 `पञ्चाशद्वर्षीया` — print ambiguous at 3x between `पञ्चा` and `पद्मा`; `पञ्चाशद्वर्षीया` (fifty-year-old) is the only sensible numeral-plus-`वर्षीया` reading and fits later `वृद्धा`, but `पद्माशद्वर्षीया` is a non-word either way; settles with scan re-examination (out of scope in Phase B). U2. p034:P9 `बहि गच्छन्तु` — print lacks the visarga where `बहिः` is expected after `सीमतः`; kept as seen; settles with scan re-examination. U3. p031:P6 `सुमन्तः` — classical form is `सुमन्तुः`; kept as house spelling; settles with a dictionary or authorial-intent check. U4. p031:P5 `समरज्ञपस्य` — unusual stem (`समरज्ञप` as battle-herald name is defensible but unattested to me); kept as seen; settles with a lexicon check. U5. p033:P2 `धीरत्वरहितः` — well-formed (`धीर` + `त्व` + `रहित`) but unusual against expected `धैर्यरहितः`; kept as seen; settles with a lexicon or print check. U6. p032:P6 `भक्त्याः` — kept as archaic/Epic genitive of `भक्ति` against classical `भक्तेः`; settles with a dictionary check. U7. p032:P6 `परम्परात्रयं` — unusual compound (`परम्परा` + `त्रय` for three generations) kept as seen; settles with a lexicon check.

## Coverage

p030:P1 {x-com:layout: : skip x-com layout note
p030:P2 # शिवपुराणम् : skip title
p030:P3 दिवोदासस्य समीपं : clean
p030:P4 काश्यां यत् : clean
p030:P5 विनायकः काशीनगरं : clean
p030:P6 {pc}चितानि उत्तराणि : clean
p030:P7 एकदा महाराजः : clean
p030:P8 राजन्, किञ्चित्कालं : F1
p030:P9 अनन्तरं शिवः : clean
p030:P10 {note: १५. : skip metadata
p031:P1 {x-com:layout: : skip x-com layout note
p031:P2 {pc}जैनधर्मं च : clean
p031:P3 दिवोदासः तं : clean
p031:P4 "राजन्! काशीनगरे : clean
p031:P5 {pc}वचनम् अनुसृत्य : clean
p031:P6 विश्वनाथः विशालाक्षी : clean
p031:P7 ते सर्वे : clean
p031:P8 तस्मिन् समये : clean
p031:P9 तदा विशालाक्ष्याः : clean
p032:P1 {x-com:layout: : skip x-com layout note
p032:P2 {pc}न समाप्तः : clean
p032:P3 व्यासस्य या : clean
p032:P4 "अद्य प्रातः : clean
p032:P5 यद्यपि बुभुक्षां : clean
p032:P6 यथापूर्वं व्यासः : clean
p032:P7 {pc}हस्तः तथैव : clean
p032:P8 व्यासः महता : clean
p033:P1 {x-com:layout: : skip x-com layout note
p033:P2 {pc}अन्नपूर्णादेवी सुवर्णदर्वीं : clean
p033:P3 तस्याः वचनं : clean
p033:P4 तत् वचनं : clean
p033:P5 व्यासः ततः : clean
p033:P6 {pc}गृहीत्वा सावकाशं : clean
p033:P7 व्यासः, तस्य : clean
p033:P8 "एषा कुत्सिता : clean
p033:P9 ते एवं : clean
p033:P10 तदा वृद्धा : F2
p034:P1 {x-com:layout: : skip x-com layout note
p034:P2 {pc}महान् विलम्बः : F2
p034:P3 तेषाम् आपोशनतीर्थपानसमनन्तरम् : clean
p034:P4 "सा वृद्धा : clean
p034:P5 सर्वे भोजनं : clean
p034:P6 किञ्चित्कालानन्तरं पार्वतीसहितः : clean
p034:P7 किन्तु शिवस्य : clean
p034:P8 {pc}पार्वतीं च : clean
p034:P9 पार्वतीसहितः शिवः : clean
p034:P10 तदा तेन : clean
p034:P11 तस्याः वचनानुसारेण : clean
J1 p030:P5 -> p030:P6 : ok (`प्रश्नानाम् उ` / `चितानि`, solid word joint across column turn)
J2 p030:P9 -> p031:P2 : ok (`बौद्धधर्मं,` / `जैनधर्मं च`, list across page turn)
J3 p031:P4 -> p031:P5 : ok (`तस्य` / `वचनम् अनुसृत्य`, genitive phrase across column turn)
J4 p031:P9 -> p032:P2 : ok (`पाकः` / `न समाप्तः`, quote pair across page turn)
J5 p032:P4 -> p032:P5 : ok (`प्राचलन्।` / `यद्यपि`, clean break; seven days' wandering → eighth-day attempt confirms order)
J6 p032:P6 -> p032:P7 : ok (`कम्पमानः` / `हस्तः`, participle-noun across column turn)
J7 p032:P8 -> p033:P2 : ok (`प्रतीक्षमाणा` / `अन्नपूर्णादेवी`, participle-subject across page turn)
J8 p033:P5 -> p033:P6 : ok (`आपोशनं` / `गृहीत्वा`, object-gerund across column turn)
J9 p033:P10 -> p034:P2 : ok (`भोः आर्याः,` / `महान्`, speech pair across page turn; open upgraded F2)
J10 p034:P7 -> p034:P8 : ok (`शिवं` / `पार्वतीं च`, accusatives across column turn)
J11 p034:P11 -> END : ok (clean break, episode ends; next story starts p35)
