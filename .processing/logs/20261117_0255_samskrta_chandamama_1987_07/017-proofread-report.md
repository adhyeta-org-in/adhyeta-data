# Proofread report — 1987_07, पृष्ठ 17–22 — देवतातुल्यः चोरः (story start p017)

## Summary

Phase B on `.processing/samskrta_chandamama/1987_07/p017.md` (scan pages 17–22, images closed throughout). 7 findings: 3 print-misprint verdicts (`आवृश्यः`→`अदृश्यः`, `यच्चा`→`यच्च`, `ता`→`भवता` with supplied speech open), 2 quote-sort verdicts (single opens corrected to doubles), 1 stray-tick deletion, 1 held `{sug-}` candidate (`कीर्तीं`). Systematic problem: this print run's quote sorts are unreliable — dropped opens, single/double swaps, one stray tick (8 spots, each verified at native resolution in Phase A). `scan.py orth` on deblocked text: 1 hit (full stop for danda after `ललितादित्यः`), dispositioned as print-faithful. Quote pass: every paragraph opens and closes its own pair (page-turn `{pb}`/`{pc}` spans excepted); no para ships unbalanced; proofread gate exits 0. All six pages read straight through; joints J1–J11 verified continuous. Text is eyes-verified print transcription, not OCR; no passages unchecked. Loc below is `pNN:Pm` + word number within the chunk (lint P numbering, counting all chunks of the page); anchor = first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p022:P8 w11 (शवसहितम् आवृश्यः) | `शवसहितम् आवृश्यः भूत्वा` | `शवसहितम् अदृश्यः भूत्वा` | SPL | error | high | `आवृश्यः` is not a word; the vetala-vanishing formula admits only `अदृश्यः`; fixed as `{del:आवृश्यः}{ins:अदृश्यः}` per Phase A `{x-com:}` on file |
| 2 | p022:P6 w35 (एव यच्चा) | `वर्धते एव। यच्चा अनिष्टकरम्` | `वर्धते एव। यच्च अनिष्टकरम्` | SPL | error | high | `यच्चा` is ungrammatical; `यत् + च` sandhi forces `यच्च`; fixed as `{del:यच्चा}{ins:यच्च}` per Phase A `{x-com:}` on file |
| 3 | p020:P7 w6 (तदा मन्त्री) | `उक्तवान् ता यत् उच्यते` | `उक्तवान् "भवता यत् उच्यते` | SPL | error | high | Bare `ता` after bare `उक्तवान्` (no dash, no quote in print) is broken; `भवता यत् उच्यते तत्` (whatever is said by you) is the unique grammatical completion; print dropped `— "भव`; fixed as `{del:ता}{ins:"भवता}` per Phase A `{x-com:}` on file |
| 4 | p022:P2 w19 (इति कीर्तीं) | `इति कीर्तीं सम्पादितवान्` | `इति कीर्तिम् सम्पादितवान्` | SPL | likely | medium* | `कीर्तीं` (lengthened vowel + anusvara) is not the accusative of `कीर्तिः`; held as `{sug-del:कीर्तीं}{sug-ins:कीर्तिम्}` — no Phase A `{x-com:}` on file, so no verdict per protocol |
| 5 | p022:P2 w12 (कार्याणि 'अर्थबलानुगुणं) | `'अर्थबलानुगुणं … सम्पादितवान्।` | `(tick removed)` | STY | likely | medium | Lone low single with no quotational role (plain narration, no `इति`-closure or thought boundary anywhere it could mate); supplying a close would invent an unpinned thought-frame; removed as a stray tick via `{del:'}`, documented here |
| 6 | p018:P9 w6 (उक्तवान् 'अविचार्य) | `--- 'अविचार्य … प्रमाणम्"` | `--- "अविचार्य … प्रमाणम्"` | STY | likely | high | Minister's spoken counsel (`उक्तवान्`) closes with a double; era standard and the paired close pin doubles; corrected via `{del:'}{ins:"}` |
| 7 | p019:P10 w6 (कोपेन 'चोराय) | `--- 'चोराय … अभविष्यन्"` | `--- "चोराय … अभविष्यन्"` | STY | likely | high | Lalitaditya's spoken rebuke (`कोपेन`, `उक्तवान्`) closes with a double; corrected via `{del:'}{ins:"}` |

## Patterns

- Unreliable quote sorts across the run (8 spots): single opens where doubles belong (F6, F7 — corrected), lone singles completed into sense-pinned frames (`'गणेशसम्बन्धीनि…शक्यन्ते{ins:'}`, `{ins:'}राजा…लुण्ठयति'`, `{ins:'}यत्…इति'` — embedded-`यत्`/thought/`इति` frames per the quote pass), one stray tick deleted (F5), one dropped speech open restored with its word (F3). All other speech pairs were printed doubles and verified balanced at native resolution.
- Print drops fragments: `— "भव` missing before `ता` (F3, p020:P7); midline speck dots omitted as print noise (2 spots, Phase A `{x-com:}` on file).

## Unverified

- `कीर्तिम्` (F4): what would settle it — the p022 scan line at higher resolution (confirming vowel length and anusvara), or any other `कीर्ति` accusative in the issue. Kept as a held `{sug-}` candidate for human review; not an open task.

## Dispositions of Phase A carried notes

- Full stop after `ललितादित्यः` (p018:P3): **ruled print-faithful, no block.** Orth flags it, but the scan shows visarga plus a low round stop (not a danda); transcribed as seen with Phase A `{x-com:}`; house punctuation quirk, not a defect.
- Detached midline dots (`भवनं · च` p021, `सम्मुखम् · आगतः` p022): **omitted as print noise, no block.** Clearly detached specks mid-sentence; Phase A `{x-com:}` on file for both; sense needs no stop in either place.
- `देवतुल्यं` (p021, short) beside `देवतातुल्यं` (elsewhere): **kept as printed, no block.** Both are valid words; three independent native reads confirm the short form here; house variant, not flagged.
- `क्षाम्यतु` (p020 “क्षाम्यतु महोदय”, p021 “क्षाम्यतु माम्”): **stands as printed, no block.** Consistent twice; house spelling, not normalized.
- `तद न निवेदितवान्` (p021): **stands as printed** (`तद`, not `तदा`); `राज्ञा` for the stub's `राजा`, `श्मशानाभिमुखं` for the stub's `श्मशानभिमुखं`, `प्रार्थ्यमाणस्य`, `कीर्तीं`, `सम्माननीयः`, `यथापूर्वं`, `तदेकदृष्ट्यापश्यन्`, `यच्चा`, `आवृश्यः` — all Phase A native-resolution corrections of draft/stub misreadings, now in text.
- `ता` line (p020:P7): **ruled** — see F3 (word fixed; speech open restored; missing dash left unrestored and documented).
- `'अर्थबल` outer tick (p022:P2): **ruled** — see F5 (stray deleted; inner `'उत्तमः राजा'` pair stands).
- `इति'` tick (p022:P7): **ruled** — mate supplied at `यत्` (embedded-`यत्…इति` single frame, quote-pass sanctioned shape); Trivikrama speech part 2 opens with supplied `"` and closes with print `"`.
- `'गणेशसम्बन्धीनि…शक्यन्ते'` (p020:P3), `'राजा…लुण्ठयति'` (p020:P5): **ruled** — mates supplied at sense-pinned boundaries (thought-content + `इति`; nested clause start + printed close).
- `"महाप्रभो…माम्"` across the p021 column turn (fresh break, no `{pc}`): **ruled per-para** — close supplied at P5 end, open at P6 start; no forcing across `{pb}`/`{pc}` continuations (those mates stand: J3–J7, J10 verified untouched).
- `"क्षाम्यतु…एव"` across p020→p021 (J7 `{pb}`/`{pc}`): **untouched** — open supplied with the F3 word fix, print close stands; pair spans the page turn as the continuation exception requires.
- `"गणेशस्य…इति"` across p022:P5→P7 (J10 `{pb}`/`{pc}` + plain P6/P7 seam): **per-para split at the complete-sentence boundary** — close supplied at P6 end, open at P7 start; each part opens and closes its own pair.

## Coverage appendix

Chunks (lint P numbers include layout/title chunks):

- p017:P1 (layout x-com) : skip layout-declaration chunk
- p017:P2 (देवतातुल्यः चोरः) : skip title
- p017:P3 स्कन्धात् अवतीर्णः : clean
- p017:P4 तदा शवान्तर्गतः : clean (speech pair `"`…`"` verified balanced at native resolution)
- p017:P5 (category वेतालकथा) : skip story-label node
- p018:P1 (layout x-com) : skip layout-declaration chunk
- p018:P2 अनन्तरं वेतालेन : clean
- p018:P3 लक्ष्मणपुरस्य शासकः : clean (full-stop sentence ender kept as print; orth-noted, dispositioned above)
- p018:P4 तद्दिने एव : clean
- p018:P5 बहवः चाराः : clean
- p018:P6 गणेशस्य महाचोरत्वं : clean
- p018:P7 तदा मन्त्री : clean
- p018:P8 "एतस्य कारणम् : clean (double open verified native; closes `भवन्ति"` same para)
- p018:P9 मन्त्री क्षणकालम् : F6
- p019:P1 (layout x-com) : skip layout-declaration chunk
- p019:P2 भवेत् इतः : clean (closes `"अविचार्य` speech via `{pc}` continuation)
- p019:P3 मन्त्रिणः सूचनानुसारं : clean
- p019:P4 तौ उभौ : clean
- p019:P5 किन्तु कोऽपि : clean
- p019:P6 "गणेशस्य वसत्यादिविषये : clean
- p019:P7 एकदा मन्त्री : clean
- p019:P8 तत् श्रुत्वा : clean (open `"` held by `{pc}` continuation into P9)
- p019:P9 {pc}आदरं दृष्ट्वा : clean (closes `"गणेशस्य` via `{pc}`; balanced inner pair)
- p019:P10 एतत् श्रुत्वा : F7
- p019:P11 लोकनाथः महाराजं : clean (cut word held by `{pc}` into p020:P2)
- p020:P1 (layout x-com) : skip layout-declaration chunk
- p020:P2 उक्तवान् भवन्तौ : clean (closes `"भवन्तौ` via `{pc}`; balanced pair)
- p020:P3 एतस्य उत्तररूपेण : clean (lone `'` closed via supplied mate at `शक्यन्ते`)
- p020:P4 सः लोकनाथम् : clean (open `"` held by `{pc}` into P5)
- p020:P5 राजापेक्षया उत्तमः : clean (nested `'...'` pair via supplied open; closes `"क्षाम्यतु` via `{pc}`)
- p020:P6 लोकनाथः क्षणकालस्य : clean
- p020:P7 तदा मन्त्री : F3 (open `"` supplied with word fix; pair spans page turn via J7)
- p021:P1 (layout x-com) : skip layout-declaration chunk
- p021:P2 जनाभिप्रायः तु : clean (closes `"भवता` minister speech via `{pc}`)
- p021:P3 तदा लोकनाथः : clean (speck omission dispositioned above)
- p021:P4 एतत् सर्वं : clean
- p021:P5 अनन्तरं राजा : clean (per-para close supplied at sentence end; column turn is a fresh break)
- p021:P6 तत्समये एतस्य : clean (per-para open supplied; closes print `माम्"`)
- p021:P7 ललितादित्यराजः मन्त्रिणः : clean (balanced `"` pair as printed)
- p021:P8 अनन्तरम् अल्पेषु : clean
- p022:P1 (layout x-com) : skip layout-declaration chunk
- p022:P2 अनन्तरं समर्थानां : F4, F5
- p022:P3 अनन्तरकाले पूर्वं : clean
- p022:P4 वेतालः एवं : clean (speck omission dispositioned above)
- p022:P5 तदा राजा : clean (open `"` held by `{pc}` into P6)
- p022:P6 ज्ञातवान् यत् : F2 (per-para close supplied at sentence end; inner `'...'` pair as printed)
- p022:P7 अतः सः : clean (per-para open supplied; embedded-`यत्…इति'` frame completed via supplied open)
- p022:P8 एवं वदता : F1

Joints (from in-file `## Joints` index):

- J1 p017:P4 {pb} -> p018:P2 fresh (clean break) : ok (vetala's offer ends; frame narration begins the tale)
- J2 p018:P5 {pb} -> p018:P6 fresh (clean break) : ok (story-start block ends `अनुभूतवान् राजा।`; right column opens new background `गणेशस्य…`; order forced: frame opening must precede tale content)
- J3 p018:P9 {pb} -> p019:P2 {pc} : ok (`अवमाननं` → `भवेत्।` one continuous sentence)
- J4 p019:P8 {pb} -> p019:P9 {pc} : ok (`प्रजानाम्` → `आदरं` one continuous sentence)
- J5 p019:P11 {pb} -> p020:P2 {pc} : ok (`पश्यन्` → `उक्तवान्` one continuous sentence)
- J6 p020:P4 {pb} -> p020:P5 {pc} : ok (`इति` → `राजापेक्षया` one continuous sentence; order forced: left column ends the minister's `क्षम्यतु…न इति`, right column continues it — reverse order is ungrammatical)
- J7 p020:P7 {pb} -> p021:P2 {pc} : ok (`विश्वासः?` → `जनाभिप्रायः` one continuous speech; closes `तदा मन्त्री…` on p021)
- J8 p021:P5 {pb} -> p021:P6 fresh (clean break) : ok (minister's report ends `आसीत् सः।`; right column opens fresh `तत्समये…`; per-para quote pairs supplied both sides)
- J9 p021:P8 {pb} -> p022:P2 fresh (clean break) : ok (reforms complete `दण्डितवान्।`; p022 opens fresh `अनन्तरं…` on results)
- J10 p022:P5 {pb} -> p022:P6 {pc} : ok (`राजा` → `ज्ञातवान्` one continuous sentence)
- J11 p022:P8 {pb} -> END (clean break) : ok (tale closes with the vetala-vanishing formula; story ends)
