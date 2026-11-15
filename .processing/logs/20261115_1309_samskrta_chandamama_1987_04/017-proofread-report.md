# Proofread report: 1987_04, START=017 (pp. 17--23, story `त्रयः वणिजः`, vetāla-frame + embedded tale)

## Summary

Range p017--p023 (seven scan pages: frame opening on p017, embedded tale of the three merchants through Vetāla's unanswered question on p023) proofread with images closed. Ten verdict findings in the table (12 applied blocks: F1--F10) plus one held candidate (H1); by severity one `error` (F10 spelling) and the rest `style`/`likely` quote-punctuation work. Two systematic issues dominate: unevenly-inked opening double strokes that Phase A kept as singles and Phase B upgrades or completes only where a reporting verb plus `इति` pins the speech boundary, and lone single strokes in narration kept as printed except two stack-forced speck deletions. Glyphs were not rechecked (images closed for Phase B; readings rest on Phase A 3--5x crops, recorded in the per-page `{x-com:}` notes). The text is hand transcription from print, not OCR output; `scan.py orth` on deblocked text returns zero hits. `Loc` below is `pNN:Pm:W` (page span, chunk, word counted on the chunk from 1) plus anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p017:P3:32 `अवदत् भोः` | `'भोः` | `{del:'}{ins:"}भोः` | STY | style | high | speech open after `---` with `अवदत्` plus closing `"` and `इति` pins double sort |
| F2 | p017:P3:1 `श्मशाने इतस्ततः` | stray `'` before `श्मशाने` | `{del:'}` | STY | likely | medium | single with no quotational function at margin edge reads as ink speck and breaks quote nesting |
| F3 | p017:P3:81 `कथां शृण्वतः` | stray `'` before `शृण्वतः` | `{del:'}` | STY | likely | medium | unpaired single inside narration with no reporting verb reads as print tic and breaks quote nesting |
| F4 | p019:P8:3 `शब्दान् उच्चार्य` | `'शब्दान् उच्चार्य` | `'शब्दान्{ins:'} उच्चार्य` | STY | style | medium | lone single needs its mate at the adjacent word end to balance the dying-man passage |
| F5 | p020:P6:1 `प्राणनिर्गमनसमये` | `'प्राणनिर्गमनसमये` | `{del:'}{ins:"}प्राणनिर्गमनसमये` | STY | style | high | outer speech open pinned by `इति उक्तवान् प्रणवः` takes double sort |
| F6 | p020:P6:13 `कासः च अतः` | `च। अतः` | `च।{ins:'} अतः` | STY | style | medium | nested aside `'शब्दाः ... च।` closes at this sentence end inside the outer speech |
| F7 | p022:P3:44 `सन्ति समाप्य` | `सन्ति।{pb}` | `सन्ति।{ins:"}{pb}` | STY | style | high | Jayendra's speech spans the column break so this para closes its own pair per multi-para rule |
| F8 | p022:P4:1 `शिवदासेन तस्मै` | `शिवदासेन` | `{ins:"}शिवदासेन` | STY | style | high | same speech continues after the clean column break so this para opens its own pair |
| F9 | p023:P11:24 `शिवदासपत्न्यै अंत` | `पत्न्यै{pb}` | `पत्न्यै{ins:"}{pb}` | STY | style | low | range ends mid-speech so the gate forces a close; REVIEW at compile and drop this block if p024 opens continuing Vetāla's question |
| F10 | p023:P4:20 `भवान् निश्चन्तः` | `निश्चन्तः` | `{del:निश्चन्तः}{ins:निश्चिन्तः}` | SPL | error | high | `निश्चन्तः` is a nonword and `निश्चिन्तः` fits `भवान् भवतु` exactly |

## Patterns

PAT-1 print singles kept as seen (no block): narration and thought singles that already balance are untouched, viz. p017 `'शवम् 'शवान्तर्गतः 'श्मशाने 'शक्नुयात्`, p018 `'शिवदासः 'यवाद्वीपेषु 'धनं …आगमिष्यामि'`, p019 `'इतःपरं … जीवामि'`, p020 `'मया … अस्ति'`, p021 `'भवान् … वा?'`, p022 `'वाणिज्ये … प्राप्स्यामि' 'अवमान … अपि' 'भगवद्दर्शनेन … भवति' 'शिवदाससम्बन्धि … दातव्यम्'`, plus house spellings kept throughout (`कानिचन` 4x, `कांशचन`, `मः`, `दद्मः`, `काऽपि`, `दृढं`, `शृण्वतः`, `आश्वर्यचकितः`, `दिवङ्गतः`, `साङ्क्रामकरोगैः`, `वणिक्कुतः`, `तावद्गात्रकं`, `शिवदासपत्न्यैः`, `एकापोशनेन` for a single sipping draught, `न्याययतेन` read as justice-effecting conduct). PAT-2 Phase A reading adoptions recorded in per-page `{x-com:}` and kept here: `पूर्ववृत्तः`, `आनेष्यावः`, `शिथिलावस्थायां`, `अपृच्छत्`, `जयेन्द्रकुमार्याः` (faint `ु`), two detached specks dropped (`पुनः ·अपि` dot, `यत'` tick).

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| H1 | p023:P6:19 `समग्रम् लोकरहित` | `लोकरहितकार्यार्थं` | `{sug-del:लोकरहितकार्यार्थं}{sug-ins:लोकहितकार्यार्थं}` | LEX | likely | medium* | print clearly shows `र` at 4x yet `लोकहितकार्य` fits donating the pit-hoard to welfare; needs a sharper look or a parallel-text check to settle |

## Coverage

p017:P1 layout : skip layout declaration
p017:P2 title त्रयः : skip title
p017:P3 श्मशाने इतस्ततः : F1,F2,F3
p017:P4 अनन्तरं वेतालेन : clean
p017:P5 note एकलचिह्नानि : skip note-only chunk
p017:P6 category वेतालकथा : skip metadata page-end
p018:P1 layout : skip layout declaration
p018:P2 पूर्वं प्रतिष्ठान : clean
p018:P3 प्रतिष्ठानपुरस्य वज्रखनी : clean
p018:P4 किन्तु न : clean
p018:P5 आगमनसमनन्तरम् एव : clean
p018:P6 शिवदासः सिंहपुरीयस्य : clean
p018:P7 शिवदासस्य अप्राप्त : clean
p018:P8 जयेन्द्रः सोमेन्द्रः : clean
p018:P9 note एकलचिह्नानि : skip note-only chunk
p018:P10 page-end २८ : skip page-end
p019:P1 layout : skip layout declaration
p019:P2 विशेषमूल्यम् अस्तीति : clean
p019:P3 जयेन्द्रस्य एका : clean
p019:P4 प्रणवः परम्पराप्राप्ते : clean
p019:P5 दिनेषु अतीतेषु : clean
p019:P6 एवम् एव : clean
p019:P7 एकदा सोमेन्द्रः : clean
p019:P8 क्षीणस्वरेण कांशचन : F4
p019:P9 अन्तिमश्वाससन्दर्भे सोमेन्द्रः : clean
p019:P10 भक्त्या श्रद्धया : clean
p019:P11 note कानिचन : skip note-only chunk
p019:P12 page-end २९ : skip page-end
p020:P1 layout : skip layout declaration
p020:P2 भवता दातव्यं : clean
p020:P3 तत् श्रुत्वा : clean
p020:P4 गणयन् मया : clean
p020:P5 किञ्चित्कालानन्तरं पुनः : clean
p020:P6 प्राणनिर्गमनसमये सः : F5,F6
p020:P7 एतद्विषये वार्तालापः : clean
p020:P8 एवम् एव : clean
p020:P9 एतस्मिन् प्रयाणे : clean
p020:P10 अनन्तरवार्तालापेन ज्ञातं : clean
p020:P11 note एकलचिह्नानि : skip note-only chunk
p020:P12 page-end ३० : skip page-end
p021:P1 layout : skip layout declaration
p021:P2 जयेन्द्रः प्रणवः : clean
p021:P3 अनन्तरं तौ : clean
p021:P4 अनन्तरदिने तौ : clean
p021:P5 प्रणवः प्रतिष्ठानपुरीयः : clean
p021:P6 तस्मै राज्ञे : clean
p021:P7 जयेन्द्रः अपि : clean
p021:P8 नैव किल : clean
p021:P9 विशेषः कोऽपि : clean
p021:P10 अनन्तरदिने प्रणवः : clean
p021:P11 note कानिचन : skip note-only chunk
p021:P12 page-end ३१ : skip page-end
p022:P1 layout : skip layout declaration
p022:P2 उक्तवान् श्रीमन् : clean
p022:P3 तदा जयेन्द्रः : F7
p022:P4 शिवदासेन तस्मै : F8
p022:P5 पुनः दशदिनानाम् : clean
p022:P6 अपरेद्युः जयेन्द्रः : clean
p022:P7 प्रणवः एतत् : clean
p022:P8 अग्रे गच्छन् : clean
p022:P9 विकारध्वनिं श्रुत्वा : clean
p022:P10 note एकलचिह्नानि : skip note-only chunk
p022:P11 page-end ३२ : skip page-end
p023:P1 layout : skip layout declaration
p023:P2 जलम् इति : clean
p023:P3 जयेन्द्रः जलम् : clean
p023:P4 प्रणवः जयेन्द्रस्य : F10
p023:P5 एतत् वचनं : clean
p023:P6 प्रणवः आश्रमं : H1
p023:P7 अनन्तरं जयेन्द्रस्य : clean
p023:P8 अर्धं भागं : clean
p023:P9 केषाञ्चित् दिनानाम् : clean
p023:P10 एकवर्षाभ्यन्तरे जयेन्द्रकुमार्याः : clean
p023:P11 एवं कथां : F9
p023:P12 note एकलचिह्नानि : skip note-only chunk
p023:P13 page-end ३३ : skip page-end
J1 p017:P4 {pb} -> p018:P2 fresh (clean break) : ok
J2 p018:P4 {pb} -> p018:P5 fresh (clean break) : ok
J3 p018:P8 {pb} -> p019:P2 {pc} (continues) : ok
J4 p019:P7 {pb} -> p019:P8 {pc} (continues) : F4
J5 p019:P10 {pb} -> p020:P2 {pc} (continues) : ok
J6 p020:P3 {pb} -> p020:P4 {pc} (continues) : ok
J7 p020:P10 {pb} -> p021:P2 fresh (clean break) : ok
J8 p021:P6 {pb} -> p021:P7 {pc} (continues) : ok
J9 p021:P10 {pb} -> p022:P2 {pc} (continues) : ok
J10 p022:P3 {pb} -> p022:P4 fresh (clean break) : F7,F8
J11 p022:P9 {pb} -> p023:P2 {pc} (continues) : ok
J12 p023:P7 {pb} -> p023:P8 {pc} (continues) : ok
J13 p023:P11 {pb} -> END (clean break) : F9

## Continuation (scan 24)

Scan 24 (eighth span, p024, bare `{pgb}` — no folio visible; art bottom full-width) appended after p023. Layout `{x-com:layout: 2col, text top, art bottom full-width}`; reading order left column then right; one mid-span column turn plus final page close. Proofread gate (`--refresh-joints`, then `--phase proofread`) exits 0; `scan.py orth` on deblocked text returns zero findings. House forms kept throughout: none of कानिचन / आश्वर्य / एकापोशनेन / न्याययतेन occur on this scan.

New span (chunks): p024:P1 layout (skip); p024:P2 `{pc}दत्तवान्, ... तावत्" इति।` — Vetāla-question tail, closing print `"` kept, no opening (edge-spanning `{pc}` holds the mate); p024:P3 `तदा त्रिविक्रमः ... न जानाति।{ins:"}` — Trivikrama speech opens with print `--- "`, close supplied (F11); p024:P4 `{ins:"}जयेन्द्रः ... निराकृतवान्{pb}` — same speech, fresh para, open supplied (F12), column turn; p024:P5 `{pc}तथापि ... अपि।{ins:"}` — column continuation (`यद्यपि...तथापि` one sentence), close supplied at para end (F13); inner `'अहं महापापी'` balanced, kept; p024:P6 `{ins:"}एतत्सर्वं ... ज्ञायते" इति।` — same speech, fresh para, open supplied (F14), print close `"` kept; p024:P7 `एवं वदता ... अवलम्बितवान्।{pb}` — frame closing narration, clean; pair `'शवान्तर्गतः / 'शाखाम्` balanced, kept as print tics (cf. PAT-1); page note + bare `{pgb}`.

Joints: J13 revised from `p023:P11 {pb} -> END` to `p023:P11 {pb} -> p024:P2 {pc} (continues) : ok` — spaced join `पत्न्यै दत्तवान्` confirms continuation; J14 `p024:P4 {pb} -> p024:P5 {pc} (continues) : ok` — column turn inside `निराकृतवान् तथापि` (`यद्यपि...तथापि`), valid word/sentence join; J15 `p024:P7 {pb} -> END (clean break) : ok` — story ends terminal `।`, next START=25 is a new story.

Verdicts on new text: F11 p024:P3 close `जानाति।{ins:"}` (STY/style/high — multi-para speech, each fresh para stands alone); F12 p024:P4 open `{ins:"}जयेन्द्रः` (STY/style/high — same speech continues after clean para break); F13 p024:P5 close `अपि।{ins:"}` (STY/style/high — closes the F12 pair at para end; column edge itself unsplit since `{pc}` continuation); F14 p024:P6 open `{ins:"}एतत्सर्वं` (STY/style/high — same speech, fresh para, print close `"` present); F15 p024:P6 `{del:'}शपथ` (STY/likely/medium — lone print single with no quotational function or mate; deleting leaves the para quote-balanced); F16 p024:P4 `{del:'}शक्यते` (STY/likely/medium — three print singles `'मार्गे ... 'शक्यते' इति` are SQ-inside-SQ suspect with no inner reporting verb; deleting the functionless middle open leaves one balanced thought pair `'मार्गे ... शक्यते'`). Print-faithful keeps (no blocks, recorded in page `{x-com:}`): `यवादिद्वीपं`, `शिवदासम्य` (vs `शिवदासस्य` two lines below, both kept as seen), `तर्कितवान् स्मः।`, `धर्मयुतमार्गेण` (line-end hyphen dropped, solid join), `नीतिमार्गेण`, mdash `उक्तवान् --- "`.

F9 resolution: REMOVED the forced close `पत्न्यै{ins:"}{pb}` at p023:P11 — scan 24 opens `{pc}दत्तवान्,` i.e. the speech genuinely continues (`शिवदासपत्न्यै दत्तवान्, एतत् किमर्थम्?`), so the range-level gate close is dropped per the report's own condition; J13 is now a true `{pb}->{pc}` continuation and Vetāla's question closes only on p024:P2 with print `तावत्" इति।`. Flag for compile: `शिवदासपुत्रीं परिणीय` (p024:P6) is clear in print at 2–3x but contradicts the tale (`जयेन्द्रकुमार्याः प्रणवस्य च विवाहः`, p023:P10) — kept as printed, no block (no glyph basis for emendation); compiler/user to decide.
