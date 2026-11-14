# Proofread report: 1984_11 p050 (दिव्यौषधम्, pp. 50-52)

## Summary

Story दिव्यौषधम् (p050--p052, 32 chunks, 7 joints): zero findings. No `{sug-ins:}`/`{sug-del:}` inherited from Phase A, no `{del:}`/`{ins:}` verdicts on file, and none created — nothing met the bar for a block from text alone, and Phase B invents no new glyph claims without a Phase A note on file. Proofread gate passes green (`p050/p051/p052: clean`, exit 0, 0 error paras, 0 story findings via `--json`); all five gate notes dispositioned below as checked print-continuations/breaks, none promoted. The `orth` scan on deblocked text (32 lines) returned a single hit (line 3, Latin `!`) which is genuine print exclamation punctuation (`हन्त! ... दन्ताः!`, consistent with `अस्ति!`/`किल?`-style exclamations throughout), dismissed. The text is a fresh print transcription, not OCR output; no passages left unchecked. `Loc` below is story coordinates `pNN:Pm` plus the chunk's first two words as anchor, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | No findings: zero candidate/verdict blocks on file; proofread gate (`--phase proofread --json`) reports an empty findings list |

## Patterns

None. No repeats to fold: the two split speeches (minister's counsel across the column turn, the vaidya's herb-clause speech across the page turn) both pair cleanly via asserted `{pb}`/`{pc}` joints, and every other speech/thought opens and closes inside its own paragraph.

## Unverified

None held. No Phase A residuals existed to route (zero `{sug-}` blocks), and no word was held for the user: clause-level re-segmentation was tested at the two boundary-coincident seams (P10→P2 page edge, P5→P6 fresh break) and both read as clean breaks with new-speaker starts, so holding was not reached. Nothing to settle; no reopen of scans required or performed.

## Coverage

p050:P1 {x-com:layout:} : skip (x-com-only chunk, no story text)
p050:P2 # दिव्यौषधम् : skip (title heading)
p050:P3 कस्मिंश्चित् राज्ये : clean
p050:P4 राज्ञी प्रथमप्रसूत्या : clean
p050:P5 तदा राजा : clean
p050:P6 तदा मन्त्री : clean (open half of column-turn speech; mid-para-imbalance note pairs with P7 per issue lint)
p050:P7 प्रकृतिनियमः। यथा : clean (close half via `{pc}`; paired-continuation verified in issue lint; column-turn exception, no verdict)
p050:P8 "शृणोतु मन्त्रिन्!, : clean
p050:P9 देशस्य प्रसिद्धवैद्याः : clean
p050:P10 "महाराज! एतत् : clean (possible-swallowed-continuation note checked: terminal `"` after `असाध्यम्` closes the cry; next page opens fresh with a new speaker, J2 clean break, no omission proposed from text alone)
p050:P11 {note}/{pgb} : skip (reprint note plus page-close metadata, deblocks empty)
p051:P1 {x-com:layout:} : skip (x-com-only chunk, no story text)
p051:P2 तदा कश्चित् : clean
p051:P3 "बहु समीचीनम्। : clean
p051:P4 वृद्धः वैद्यः : clean
p051:P5 "कालावकाशः किमर्थम्? : clean
p051:P6 इति सर्वे : clean (iti-verb paragraph kept as printed; fresh break both sides, J3)
p051:P7 "रे शृण्वन्तु! : clean
p051:P8 पञ्चषनिमेषेषु प्रत्यागत्य : clean
p051:P9 वैद्याः सर्वे : clean
p051:P10 वैद्यः सावधानेन : clean
p051:P11 राजा सगर्वम् : clean
p051:P12 "महाराज! एतत् : clean (open half of page-turn speech; quotes-open-past-pb note pairs with p052:P2 per issue lint)
p052:P1 {x-com:layout:} : skip (x-com-only chunk, no story text)
p052:P2 चतुर्थवारं यदा : clean (close half via `{pc}`; paired-continuation verified in issue lint; page-turn exception, no verdict)
p052:P3 "एवम् अपि : clean
p052:P4 "सप्ताहाभ्यन्तरे किं, : clean
p052:P5 महाराजः राज्ञीं : clean
p052:P6 राज्ञी किञ्चित् : clean
p052:P7 राजा राज्ञ्याः : clean
p052:P8 इदानीं तस्याः : clean
p052:P9 मातापित्रोः मरणानन्तरं : clean
J1 p050:P6 {pb} -> p050:P7 {pc} (continues) : ok (minister's counsel spans the column turn; open/close pair verified)
J2 p050:P10 {pb} -> p051:P2 fresh (clean break) : ok (cry closes with `"`; new speaker उत्थाय opens next page)
J3 p051:P5 {pb} -> p051:P6 fresh (clean break) : ok (king's question closes with इति; iti-verb paragraph stands alone)
J4 p051:P9 {pb} -> p051:P10 fresh (clean break) : ok (silence tableau ends; new speaker सावधानेन opens)
J5 p051:P12 {pb} -> p052:P2 {pc} (continues) : ok (herb-clause speech spans the page turn; open/close pair verified)
J6 p052:P5 {pb} -> p052:P6 fresh (clean break) : ok (king's question closes with इति; queen's deliberation opens fresh)
J7 p052:P9 {pb} -> END (clean break) : ok (story concludes with the reign summary; terminal danda, clean break)
