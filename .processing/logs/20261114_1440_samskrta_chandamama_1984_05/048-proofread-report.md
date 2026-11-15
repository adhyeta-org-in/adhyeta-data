# Proofread report: 1984_05 story range 048 (pages 48-52, `प्रतीकारः`)

## Summary

21 findings, all `STY`/error: every one normalizes a print quote mark for modern readability (speech to `"..."`, thought to `'...'`); no word, sandhi, morphology, agreement, or case finding survived the text pass, and `scan.py orth` reported zero hits on the deblocked text, so the transcription itself is clean and the story reads as hand-set print, not OCR output. The systematic issue is the printer's mixed quote sorts: speech opens are mostly a single stroke while closes are doubles (`'...''`), with a few double opens (`"बलात्कारेण`, `"तात`, `"भवत्या`, `"एषः`), so 17 logical paragraphs gated unbalanced and each was pinned by sense (reporting verb or `इति`/`चिन्तयित्वा`). Nothing was left unchecked in-text: every sentence was read for continuity and every joint walked, but 14 print-reading observations below are held as unverified because images stay closed in this phase and settling them needs either a rescan look or an editorial call.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p048:P4 महासचिवस्य एका | `'सचिववर्य!` opens king's order | `{del:'}{ins:"}सचिववर्य!` | STY | error | high | speech confirmed by `इति ... उक्तवान्`; open sorts to `"` (close verified double at 3x) |
| F2 | p048:P7 भवतः पुत्र्याः | `{pc}भवतः` quote opens with no mark | `{pc}{ins:"}भवतः` | STY | error | high | second imperative of the same royal order, closed by print `"`; lone open supplied |
| F3 | p048:P10 इतः परम् | `वरम्"` closes minister's musing | `वरम्{del:"}{ins:'}` | STY | error | high | `इति चिन्तयित्वा` pins interior thought, which takes `'...'` (close verified double at 3x) |
| F4 | p049:P3 अहो कियान् | `रक्षति'?` closes king's outburst | `रक्षति?{del:'}{ins:"}` | STY | error | medium | angry speech to the captive (`कोपेन पृष्टवान्`); open verified double in print |
| F5 | p049:P4 इदानीं स्वयं | `'इदानीं` opens her reply | `{del:'}{ins:"}इदानीं` | STY | error | medium | spoken reply closing with print `"` across the page turn; pair forced by `{pb}`/`{pc}` |
| F6 | p049:P9 एतत् श्रुत्वा | `'एतस्यां` opens her refusal | `{del:'}{ins:"}एतस्यां` | STY | error | medium | outer speech (`उक्तवती`) must be `"` to nest the quoted message |
| F7 | p049:P9 एतत् श्रुत्वा | `वदतु 'इतः` nested message | `वदतु{ins:"} 'इतः` | STY | error | high | lone close supplied so outer `"` closes before inner `'...'`; only legal nesting is `DQ SQ ... SQ DQ` |
| F8 | p050:P5 उपसचिवः किमपि | `'प्रभो! एतादृशव्यक्तेः` opens old man's plea | `{del:'}{ins:"}प्रभो! एतादृशव्यक्तेः` | STY | error | high | spoken plea (`निवेदितवान्`), close verified single in print |
| F9 | p050:P6 प्राणधारणं वा | `सूचना'` closes old man's plea | `सूचना{del:'}{ins:"}` | STY | error | high | pair with F8 across the column joint; close verified single at 3x |
| F10 | p051:P2 अहम् अत्र | `'अहम्` opens her reply to the camel-driver | `{del:'}{ins:"}अहम्` | STY | error | medium | spoken reply chaining from `'आर्य!` across the page turn; close verified single in print |
| F11 | p051:P2 अहम् अत्र | `भवामि'` closes her reply | `भवामि{del:'}{ins:"}` | STY | error | medium | pair with F10; spoken `"` required by the balance |
| F12 | p051:P5 युवराजः स्वस्य | `'भवति!` opens prince's invitation | `{del:'}{ins:"}भवति!` | STY | error | medium | spoken invitation (`आमन्त्रितवान्`), close verified double in print |
| F13 | p051:P7 युवराजः नगरं | `निवारयेत्"?` closes prince's musing | `निवारयेत्{del:"}{ins:'}?` | STY | error | medium | `चिन्तितवान्` pins interior thought, which takes `'...'` |
| F14 | p051:P8 अनन्तरदिने रात्रौ | `'युवराज!` opens her rebuke | `{del:'}{ins:"}युवराज!` | STY | error | medium | spoken rebuke, close verified double in print |
| F15 | p051:P9 भवत्या युक्तम् | `'माम्` opens her resolve | `{del:'}{ins:"}माम्` | STY | error | medium | spoken resolve closing with print `"`; pair forced by the sentence |
| F16 | p052:P3 युवराजः शीघ्रम् | `'भवान्` opens order to march | `{del:'}{ins:"}भवान्` | STY | error | high | spoken order (`आज्ञापितवान्`), open verified single at 3x, close double |
| F17 | p052:P4 युवराजः कबरिस्थानस्य | `'पूर्वं` opens her request | `{del:'}{ins:"}पूर्वं` | STY | error | medium | spoken request (`प्रार्थितवती`), close verified double in print |
| F18 | p052:P6 तस्यां सभायां | `'पूर्वं` opens her accusation | `{del:'}{ins:"}पूर्वं` | STY | error | medium | spoken in assembly (`उक्तवती`), close verified double in print |
| F19 | p052:P7 सः उपसचिवः | `'मम` opens his confession | `{del:'}{ins:"}मम` | STY | error | medium | spoken confession (`उक्तवान्`), close verified double in print |
| F20 | p052:P8 युवराजः सैनिकान् | `'एतं` opens desert order | `{del:'}{ins:"}एतं` | STY | error | medium | spoken order, close verified double in print |
| F21 | p052:P9 अनन्तरम् एषः | `'एषः` opens execution speech | `{del:'}{ins:"}एषः` | STY | error | high | spoken verdict, open verified single and close double in print |

## Patterns

Print mixes single-stroke speech opens with double-stroke closes (`'...''`) at 17 unbalanced sites: 15 speech pairs normalized to `"..."` (F1, F2, F4-F12, F14-F21: 20 blocks) and 2 thought pairs normalized to `'...'` (F3, F13: 2 blocks). Balanced pairs of either sort were kept exactly as printed (e.g. p048:P5, p048:P8, p050:P2, p051:P6), following the p01.proofread.md precedent of preserving print sorts where sense does not force a change. House spellings kept as printed throughout: `वृत्तान्तं` for `वृत्तान्त` (7 occurrences, consistent), `ज्योतिर्षिकं` (3x-verified), open sandhi (`तत्`, `एतत्` uncombined), and print commas (`सन्तुष्टा,`, `प्रस्थितवान्,`).

## Unverified

Forms flagged below high confidence without a second check; each states what would settle it. No `{sug-...}` block was added to the file for these (glyphs read clear in Phase A, so they are editorial holds, not reading candidates).

- U1 `महाराजेन` (p049:P3): kept sic; nominative `महाराजः` expected for the king's self-reference. Settle with a 3x re-exam of 49.jpg bottom-left.
- U2 `व्याकुलेन` (p049:P9): kept sic; feminine `व्याकुला`/`व्याकुलया` expected with `पुत्री उक्तवती`. Settle with a 3x re-exam of 49.jpg bottom-right.
- U3 `विद्यावत्याः` + `भवतः` (p048:P6->P7): possible dittography (appositional genitives, "of Vidyavati, of your daughter"). Both kept since both impressions read clear. Editorial call, not a glyph question.
- U4 `शीघ्रं गत्वा चर्चां करोतु। ... सा आनन्दतुन्दिला भवति` (p048:P6): speaker of the order and antecedent of `सा` unclear (minister's assurance vs king's order vs narration). Kept as one narration chunk. Editorial call.
- U5 `मम राज्ञे` (p052:P7): dangling `मम` before the dative. Kept sic. Settle with a 3x re-exam of 52.jpg right column.
- U6 `बहोः कालात्` (p052:P10): `बहुकालात्` expected ("after a long time"). Kept sic. Settle with a re-exam of 52.jpg left column.
- U7 `स्वयमाना` (p052:P10): sense unclear (`स्वयंवरा`? `स्वयमेव`?). Kept sic. Settle with lexicon plus re-exam.
- U8 `एकषण्टात्मकः` (p049:P2): obscure time-word, glyphs certain at 5x (`एक-षण्ट-ात्मकः`, possibly "about an hour" if `षण्ट` stands for `घण्टा`). Kept. Settle with lexicon or parallel-issue usage.
- U9 `श्रुत्वा देवः प्रमाणम्` (p050:P3): odd sense inside the उपसचिव's speech; paired as its closing stretch (no block beyond F-pairing). Alternative is a stray mark. Editorial call.
- U10 `भवत्या` (p051:P9): instrumental "by you" kept; vocative `भव्या` ("O noble lady") also grammatical. Settle with a 3x re-exam of 51.jpg bottom-right.
- U11 `सद्यः` (p050:P6): kept ("at once"); `अद्य` ("today") not excluded at scan resolution for the first word of the camel-driver's invitation. Settle with a re-exam of 50.jpg right column.
- U12 `समीपस्थ-राज्यस्य` hyphen (p051:P3): kept as a mid-line compound hyphen per the `ह्यस्तन-अपेक्षया` precedent; a wrap hyphen would drop. Settle with a re-exam of 51.jpg bottom-left.
- U13 `सौन्दर्यनिधिं` with feminine adjectives (`अदृष्टपूर्वां ... तादृशीं सुन्दरीं`, p051:P4): gender mismatch inside the phrase kept sic. Settle with a re-exam.
- U14 `रक्षति'?` close and seven other scan-resolution-only marks behind F4, F5, F6, F10-F12, F14, F15, F17-F20: the verdict sort (speech `"` / thought `'`) is sense-pinned at high confidence, but the replaced print stroke was verified at scan resolution only. A 3x re-exam would raise these to high.

## Coverage

Skip lines: layout and title chunks carry no story text.

p048:P1 layout : skip x-com layout declaration
p048:P2 title : skip story heading
p048:P3 पुरा पर्शियादेशे : clean
p048:P4 महासचिवस्य एका : F1
p048:P5 एतत् श्रुत्वा : clean
p048:P6 शीघ्रं गत्वा : clean
p048:P7 भवतः पुत्र्याः : F2
p048:P8 महासचिवः एतं : clean
p048:P9 महासचिवः राज्ञः : clean
p048:P10 इतः परम् : F3
p049:P1 layout : skip x-com layout declaration
p049:P2 प्रवृत्तः गुप्तचराणां : clean
p049:P3 अहो कियान् : F4
p049:P4 इदानीं स्वयं : F5 + chain-note checked (genuine page-turn quote continuation via J4)
p049:P5 परमात्मा एव : clean
p049:P6 परस्मिन् दिने : clean
p049:P7 अन्तःपुरस्य प्रकोष्ठे : clean
p049:P8 सा दासी : clean
p049:P9 एतत् श्रुत्वा : F6, F7
p050:P1 layout : skip x-com layout declaration
p050:P2 दासी प्रतिनिवृत्य : clean
p050:P3 राजविरोधिकृत्यस्य समूलम् : clean
p050:P4 अरे दुष्टे : clean
p050:P5 उपसचिवः किमपि : F8 + chain-note checked (speech opens here, closes in P6 via J7)
p050:P6 प्राणधारणं वा : F9 + chain-note checked (genuine column-turn continuation via J7)
p051:P1 layout : skip x-com layout declaration
p051:P2 अहम् अत्र : F10, F11 + chain-note checked (genuine page-turn continuation via J8)
p051:P3 उष्ट्रवाहकः जलेन : clean
p051:P4 युवराजः अनुक्षणम् : clean
p051:P5 युवराजः स्वस्य : F12
p051:P6 सा तस्य : clean
p051:P7 युवराजः नगरं : F13
p051:P8 अनन्तरदिने रात्रौ : F14
p051:P9 भवत्या युक्तम् : F15
p052:P1 layout : skip x-com layout declaration
p052:P2 अनन्तरं च : clean
p052:P3 युवराजः शीघ्रम् : F16
p052:P4 युवराजः कबरिस्थानस्य : F17
p052:P5 अनन्तरं तैः : clean
p052:P6 तस्यां सभायां : F18
p052:P7 सः उपसचिवः : F19
p052:P8 युवराजः सैनिकान् : F20
p052:P9 अनन्तरम् एषः : F21
p052:P10 प्रतीकारः कृतः : clean

J1 p048:P4 {pb} -> p048:P5 fresh : ok (minister hears the order, stalls)
J2 p048:P6 {pb} -> p048:P7 {pc} : ok (same royal order continues across the column)
J3 p048:P10 {pb} -> p049:P2 {pc} : ok (set out to flee: धावितुं प्रवृत्तः)
J4 p049:P4 {pb} -> p049:P5 {pc} : ok (her reply completes across the column: शक्नोमि। परमात्मा...)
J5 p049:P6 {pb} -> p049:P7 fresh : ok (guard posted, then sees her in the harem)
J6 p049:P9 {pb} -> p050:P2 fresh : ok (message refused, slave-girl returns)
J7 p050:P5 {pb} -> p050:P6 {pc} : ok (death-or-survival: मरणं प्राणधारणं वा)
J8 p050:P6 {pb} -> p051:P2 {pc} : ok (desert sentence reported, her desert reply follows)
J9 p051:P4 {pb} -> p051:P5 fresh : ok (prince arrives astonished, then introduces himself)
J10 p051:P7 {pb} -> p051:P8 fresh : ok (night musing, then next night's visit)
J11 p051:P9 {pb} -> p052:P2 fresh : ok (her resolve, then she narrates everything)
J12 p052:P5 {pb} -> p052:P6 fresh : ok (assembly gathers, then she speaks)
J13 p052:P10 {pb} -> END : ok (story ends on the marriage-hint smile; last range of the issue)
