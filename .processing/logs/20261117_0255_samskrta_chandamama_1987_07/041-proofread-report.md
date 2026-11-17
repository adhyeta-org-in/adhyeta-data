# Proofread report — 1987_07, pages 41–45 — प्रत्युपकारः (story start p041)

## Summary

Phase B on `.processing/samskrta_chandamama/1987_07/p041.md` (scan pages 41–45, images closed throughout). 10 findings: 7 fixed as `{del:}/{ins:}` verdicts (6 quote-sort/stray-mark rulings F1–F3, F5, F7, F9–F10), 2 held as `{sug-del:}/{sug-ins:}` candidates (F4 `भापयति`, F6 `पूर्वपिक्षया`), 1 kept as printed with reason (F8 `इति.` period). Systematic problem: the print mixes double-open sorts with single closes (3 instances) plus two stray singles in narration and one triple-struck close. `scan.py orth` on deblocked text: 1 low hit (the F8 period — print-faithful, kept). No passage left unchecked; every body chunk read sentence by sentence. This text is human Phase A transcription, not OCR output. Loc below is `pNN:Pm` + word number within the chunk (lint P numbering, Devanagari words counted from 1, blocks not counted); anchor = first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p041:P4 w1 (सीतारामनामकस्य गृहे) | `' सीतारामनामकस्य` | `सीतारामनामकस्य` (drop stray `'`) | STY | error | high | Lone opening single with no mate anywhere; the paragraph is straight narration (theft report, no speaker or thinker), so no quotation exists to open; fixed as lone `{del:'}` |
| 2 | p041:P7 w13 (उपकारस्य प्रतिक्रियारूपेण) | `"सुधाकरः … द्रष्टव्यम्'` | `'सुधाकरः … द्रष्टव्यम्'` | STY | error | high | `इति तस्य विचारः` marks interior thought, which takes singles per house style; print's double open corrected via `{del:"}{ins:'}`, print's single close kept |
| 3 | p041:P10 w4 (सीतारामस्य वचनानि) | `श्रुत्वा 'ज्येष्ठः` | `श्रुत्वा ज्येष्ठः` (drop stray `'`) | STY | error | high | Stray high single inside narration; the speech pair `"एवं … एषः"` is otherwise complete and balanced across the p041→p042 page turn, so the mark has no role; fixed as `{del:'}` |
| 4 | p042:P6 w6 ("भोः कुतश्चित्) | `अस्मान् एव भापयति वा` | `अस्मान् एव त्रापयति वा` (or `तापयति`) | SPL | likely | medium* | `भापयति` has no Sanskrit parse (no root भाप्); the angry retort needs "frighten" (`त्रापयति`) or "torment" (`तापयति`); held as `{sug-del:भापयति}{sug-ins:त्रापयति}`, glyphs settled in Phase A so no verdict |
| 5 | p043:P3 w32 ("सीतारामेण यावती) | `पूरितं भविष्यति'` | `पूरितं भविष्यति"` | STY | error | high | `सूचनां दत्तवान्` introduces spoken instruction, which takes doubles; single close corrected via `{del:'}{ins:"}`, print's double open kept |
| 6 | p043:P7 w12 (एतत् प्रकरणं) | `व्यवहारः पूर्वपिक्षया अपि` | `व्यवहारः पूर्वापेक्षया अपि` | SPL | likely | medium* | `पूर्वपिक्षया` has no parse (पिक्षा is not a word); the comparison "more mysterious than before" needs `पूर्वापेक्षया`; held as `{sug-del:पूर्वपिक्षया}{sug-ins:पूर्वापेक्षया}`, glyphs settled in Phase A so no verdict |
| 7 | p043:P8 w25 (ग्रामज्येष्ठयोः पुत्रौ) | `अपायकरी'` | `अपायकरी"` | STY | error | high | `सूचयतः` introduces the parents' spoken instruction, which takes doubles; single close corrected via `{del:'}{ins:"}` (close pairs across the same-section column turn with p043:P9 `{pc}इति।`) |
| 8 | p044:P8 w15 ("यः स्वार्थचिन्तनं) | `यच्छन्ति" इति. उक्तवान्` | `यच्छन्ति" इति उक्तवान्` (drop period) | STY | style | high | Full stop after `इति` occurs nowhere else in the range (orth scan's only hit); kept as printed — punctuation fidelity outranks normalization, sense unchanged; no block issued |
| 9 | p045:P5 w30 ("यावत् भवन्तौ) | `भविष्यति' "` | `भविष्यति"` (drop stray `'`) | STY | error | high | Triple-struck close after Sudhakara's spoken warning (उक्त्वा → doubles); the `"` pair is complete without it, so the single has no role; inherited `{sug-del:'}` promoted to `{del:'}` |
| 10 | p045:P7 w1 ('दुष्टकार्याणि न) | `'दुष्टकार्याणि … किल?"` | `"दुष्टकार्याणि … किल?"` | STY | error | medium | Direct complaint utterance (1st-pl verbs, `किल?`, `इति` closure) reads as voiced speech rather than inner feeling, so doubles; single open corrected via `{del:'}{ins:"}`, print's double close kept |

## Patterns

1. Double-open with single-close mismatch (F2, F5, F7 — 3 instances): print opens speech with the double sort but closes with a single stroke (`द्रष्टव्यम्'`, `भविष्यति'`, `अपायकरी'`). All three are spoken content (विचारः excepted — F2 folds the other way to thought singles), each corrected to the sense-pinned sort with the surviving print mark kept.
2. Stray singles in narration (F1, F3 — 2 instances): isolated `'` marks with no quotative content (`' सीतारामनामकस्य`, `श्रुत्वा 'ज्येष्ठः`), both deleted; the surrounding quote pairs were already complete without them.

## Unverified

- `त्रापयति` (F4): what would settle it — a Heritage/dictionary check that no root भाप् exists, plus a re-read of the p042 scan akshara at high zoom to exclude `त्रापयति`/`तापयति`/`भाषयति` sorts. Held as `{sug-}` for human review; glyphs (भापयति) stay in text via the del span.
- `पूर्वापेक्षया` (F6): what would settle it — a re-read of the p043 scan word for पे/पि and the presence of ा (पूर्वापेक्षया needs two more signs than पूर्वपिक्षया shows). Held as `{sug-}` for human review.
- `सः अतीव अपायकरी` (p043:P8, no block): theのfile reads short-ि (masc. nominative of अपायकारिन् expects long -कारी, as printed in p041:P3 `अपायकारी`). What would settle it — a 5x re-read of the p043 close for ि/ी length; if long, no action; if short, `{del:अपायकरी}{ins:अपायकारी}` (CNS with p041:P3). Grammar expects long, print (as read) shows short; held without block since Phase A carried no flag on it.

## Dispositions of Phase A carried candidates

- `{sug-del:'}` (p045:P5): **promoted** to `{del:'}` — see F9.
- Removed Phase A `{x-com:}` notes whose rulings landed as verdicts (F1 lone open, F2/F5 sort mismatch, F3 stray mark, F7 trio, F10 sort mismatch): the verdict blocks plus this report carry the record.
- Kept `{x-com:}` notes: period after `इति` (F8, kept print mark), detached dot before `वस्तुतः` omitted as print noise (single mid-line dot, clearly detached; narration needs no bullet — omission sanctioned, no block possible).
- Draft-vs-print corrections settled in Phase A (no action needed, already in text): `उक्तवन्तौ` (draft `उक्तबन्तौ`), `युवतिः` (draft `युर्वातः`), `अवकाशम् अपि न` (draft `अपिन`), `समीपस्थं` for the hill episode; the entire p044 left column (`तत्सन्दर्भे…हस्ते`) had no draft and was transcribed from the scan.
- Footer metadata kept as seen: `{misc: 'श्रीमाता'}` (p041, single-quoted tag as printed), `{misc: (अनुवर्तते)}` (p045, story continues); `चन्दमामा` running feet and folios stripped per furniture rule, folios recorded in `{pgb: ५६/५७/५८}`.

## Coverage appendix

Chunks (lint P numbers include layout/title/footer chunks; anchors are first two Devanagari words):

- p041:P1 (layout x-com) : skip layout-declaration chunk
- p041:P2 (प्रत्युपकारः ५) : skip title
- p041:P3 'नूतनतया ग्रामम् : clean (balanced singles kept: the elders' deliberation reads as inner resolve, house singles cover inner speech)
- p041:P4 सीतारामनामकस्य गृहे : F1
- p041:P5 सुधाकरः एतां : clean
- p041:P6 आभरणग्रन्थिः दृष्टः : clean
- p041:P7 उपकारस्य प्रतिक्रियारूपेण : F2
- p041:P8 तद्दिने रात्रौ : clean
- p041:P9 अनन्तरदिने सीतारामः : clean
- p041:P10 सीतारामस्य वचनानि : F3 (speech pair completed across J2)
- p041:P11 (misc श्रीमाता) : skip footer metadata, contents checked
- p042:P1 (layout x-com) : skip layout-declaration chunk
- p042:P2 भवेत् मया : clean (page-turn "" pair with p041:P10; stray handled in F3)
- p042:P3 एषा वार्ता : clean
- p042:P4 एतां वार्तां : clean
- p042:P5 भवद्भ्यां पूरणीया : clean
- p042:P6 "भोः कुतश्चित् : F4
- p042:P7 "किं भविष्यति : clean
- p042:P8 तद्दिने एव : clean
- p042:P9 एतत् दृष्ट्वा : clean
- p042:P10 "अहं यः : clean
- p043:P1 (layout x-com) : skip layout-declaration chunk
- p043:P2 "एवं तर्हि : clean
- p043:P3 "सीतारामेण यावती : F5
- p043:P4 अन्यम् उपायम् : clean
- p043:P5 सीतारामेण अनुगृहीतान् : clean
- p043:P6 तद्दिने एव : clean
- p043:P7 एतत् प्रकरणं : F6
- p043:P8 ग्रामज्येष्ठयोः पुत्रौ : F7 (vowel-length query noted above, no block)
- p043:P9 इति : clean (continuation of F7 speech)
- p043:P10 एकदा जयः : clean
- p043:P11 "भोः समीपे : clean
- p043:P12 सा तरुणी : clean
- p044:P1 (layout x-com) : skip layout-declaration chunk
- p044:P2 तत्सन्दर्भे सुधाकरः : clean
- p044:P3 "प्रथमम् आम्रफलं : clean
- p044:P4 (x-com dot note) : skip note-only chunk
- p044:P5 वस्तुतः तदानीम् : clean
- p044:P6 दत्तवान् एव : clean
- p044:P7 जयविजयौ आश्चर्येण : clean
- p044:P8 "यः स्वार्थचिन्तनं : F8 (period kept, no block)
- p044:P9 "एवं तर्हि : clean
- p044:P10 "स च : clean
- p044:P11 "न प्रत्यर्पयिष्यावः : clean
- p044:P12 "भगिनि भवती : clean
- p044:P13 सा झटिति : clean
- p045:P1 (layout x-com) : skip layout-declaration chunk
- p045:P2 "भवान् मान्त्रिकः : clean (मान्त्रिकः is valid: mantra-knower/magician)
- p045:P3 "अहं तु : clean
- p045:P4 "आवयोः व्यवहारे : clean
- p045:P5 "यावत् भवन्तौ : F9
- p045:P6 एतदनन्तरं सुधाकरः : clean (balanced 'तस्य…मास्तु' kept: reported advice content, sense does not force doubles)
- p045:P7 'दुष्टकार्याणि न : F10
- p045:P8 सुधाकरस्य विषये : clean
- p045:P9 सुधाकरः जयविजयौ : clean
- p045:P10 जयविजयौ तदानीं : clean
- p045:P11 (misc अनुवर्तते) : skip footer metadata, contents checked

Joints (from in-file `## Joints` index):

- J1 p041:P5 {pb} -> p041:P6 {pc} : ok (column turn; `तस्य अन्तः` → `आभरणग्रन्थिः` one sentence)
- J2 p041:P10 {pb} -> p042:P2 {pc} : ok (page turn; `वा न` → `भवेत्?` completes `न भवेत्?`; speech pair spans the turn)
- J3 p042:P4 {pb} -> p042:P5 {pc} : ok (column turn; `सा` → `भवद्भ्यां` completes `सा भवद्भ्यां पूरणीया`)
- J4 p042:P10 {pb} -> p043:P2 : ok (page turn, clean break; younger elder's question follows Sudhakara's terms)
- J5 p043:P8 {pb} -> p043:P9 {pc} : ok (column turn; `अपायकरी` → `इति।` closes the parents' instruction)
- J6 p043:P12 {pb} -> p044:P2 : ok (page turn, clean break; new scene `तत्सन्दर्भे` follows the stranded girl)
- J7 p044:P5 {pb} -> p044:P6 {pc} : ok (column turn; `हस्ते` → `दत्तवान् एव।` one sentence)
- J8 p044:P13 {pb} -> p045:P2 : ok (page turn, clean break; Jaya's question follows the regained speech)
- J9 p045:P6 {pb} -> p045:P7 : ok (column turn, clean break; the boys' grievance follows the parents' counsel)
- J10 p045:P10 {pb} -> END : ok (clean break into `(अनुवर्तते)` footer; story continues next issue)
