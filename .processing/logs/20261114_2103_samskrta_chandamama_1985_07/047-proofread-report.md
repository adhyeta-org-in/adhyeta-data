## Summary

Phase A is complete and untouched apart from the Phase B block below: 1 `{pgb}`-terminated span (scan 47) with a 1-joint index; `lint.py --phase extract` passes (exit 0, no residuals) and the page was not re-transcribed. Phase B proofread gate passes clean (`lint.py --phase proofread`: 1 page, 0 error paras, 0 story findings, exit 0); `scan.py orth` on deblocked text reports 0 hits across 8 lines. Findings table: 0 verified verdicts, 1 held candidate (F1 मधावी, OCR/likely, medium*). Print keeps the baseline comma after उत्तीर्णौ and balanced single quotes for the minister's short recommendation to the king; both are kept as seen per the proofread reference's handling of spoken singles. Open sandhi and visarga-before-vowel are house style throughout and never flagged. Loc below is keyed `pNN:Pm:w` (NN = scan sequence 47 + `{pgb}`-span ordinal, Pm = lint chunk number, w = word in chunk from 1) plus the chunk's first two words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p047:P3:5 कस्यचित् महाराजस्य | `कश्चित् मधावी महामन्त्री` | `मेधावी` | OCR | likely | medium* | मधावी is no word; मेधावी ("wise") fits महामन्त्री, missing े-stroke is the smallest glyph change |

## Unverified

F1 `मधावी` (p047:P3:5) is held as `{sug-del:मधावी}{sug-ins:मेधावी}`, not a verdict: the print reads मधावी with no े-stroke at 6x (flagged `{x-com:}` in Phase A), and मेधावी fits the महामन्त्री epithet exactly, but with images closed and no dictionary/tool confirmation the emendation stays a candidate for the user. What would settle it: a dictionary check confirming मधावी is unattested, or user acceptance of मेधावी. U1 `काञ्चित्` (p047:P5, मन्त्री काञ्चित् परीक्षाम्) is report-only with no story block: expected कञ्चित्, but Phase A left no flag on it and images are closed, so no new glyph claim is made; a scan re-check would settle whether the print shows आ or अ.

## Coverage

p047:P1 {x-com:} : skip layout-only chunk
p047:P2 # सर्वज्ञः : skip title
p047:P3 कस्यचित् महाराजस्य : F1
p047:P4 राज्ये एतद्विषये : clean
p047:P5 उत्तीर्णौ, द्वौ : clean
p047:P6 उभौ अपि : clean
p047:P7 तत्क्षणे एव : clean
p047:P8 वृद्धः मन्त्री : clean
J1 p047:P8 {pb} -> END : ok (clean story close on निवेदितवान्।)
