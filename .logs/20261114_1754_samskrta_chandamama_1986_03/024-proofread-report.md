# Proofread report — 1986_03 p024 (scans 24–25, story चतुरः भीमराजः)

## Summary

7 findings: 4 verdicts applied as blocks in the story file (F1 extra-उ deletion, F2 stray-anusvara deletion, F3 supplied opening quote, F4 nested-quote sort correction) and 3 held candidates (F5 speaker attribution, F6 अनुद्धोषितः, F7 अर्हस्य), all marked Conf* for user decision. Loc key is `pNN:Pm` plus the first two words of the chunk. Systematic house mark: every long speech closes with a two-stroke `"'`-like cluster in print, transcribed as `"` per the two-strokes-one-mark rule, giving balanced DQ pairs throughout. No passage left unchecked; text was transcribed by eye from scans (not OCR), and the orth scanner reported zero hits on deblocked text.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p24:P5 कुशलप्रश्नानन्तरं | `उजोतिषिकः` | `ज्योतिषिकः` (`{del:उ}` applied) | SPL | error | high | extra initial उ is a press slip; `ज्योतिषिकः` occurs 8 more times identically |
| 2 | p25:P2 इति पुनः | `पृष्टवांन्` | `पृष्टवान्` (`{del:ं}` applied) | OCR | error | high | stray anusvara dot (speck or slip); `वान्` participle cannot carry ं, and `पृष्टवान्` occurs 3 times |
| 3 | p25:P3 इति उक्तवान् | (no opening mark) `अत्र आगमनेन` | `{ins:"}` before `अत्र` (applied) | STY | likely | high | print closes भीमराजः's speech with `"` but never opens it; gate showed dq=3 |
| 4 | p24:P8 भवन्तम् --- | `"एतावद् ददातु"` | `'एतावद् ददातु'` (`{del:"}{ins:'}` pair applied) | STY | likely | high | quoted speech nested inside DQ speech takes SQ by the sort rule |
| 5 | p25:P8 इति उक्तवान् | `इति उक्तवान् ज्योतिषिकः` | `इति उक्तवान् भीमराजः` | LEX | likely | medium* | the 5%-tax demand (`कररूपेण ददातु`) is the clerk भीमराजः speaking; print attributes it to the astrologer; kept verbatim, user to decide |
| 6 | p24:P8 ग्रामस्य | `अनुद्धोषितः` | `अनुद्घोषितः` | SPL | likely | low* | no such word; `अनुद्घोषितः` (proclaimed) fits the flattery, but print reads द्ध and द्ध/द्घ cannot be settled images-closed |
| 7 | p24:P6 अलङ्कर्तुम् | `अर्हस्य हस्तः` | `अर्हः हस्तः` | MRP | likely | low* | genitive `अर्हस्य` does not govern the infinitive; `अर्हः` fits, but the स्य is clearly printed and no Phase A marker covers it |

## Patterns

- Two-stroke quote clusters: all 8 long-speech closings print as `"'`-like clusters (p24:P4? no — P6/P7/P8; p25:P2/P3/P4/P7/P8); each transcribed as one `"` mark, so every speech is a balanced DQ pair and the thought (`'इतोऽपि...आपतेयुः'`, p25:P9) stays SQ. Count 8, e.g. p24:P8 `भावयामि"`, p25:P8 `भविष्यति"`.
- Print spaces before `?`/`!` (e.g. `भवते ?`, `वा ?`, `किम् ?`) removed throughout per the no-space-before-punct rule; wording otherwise untouched.

## Unverified

- F5 (`ज्योतिषिकः` for `भीमराजः`, p25:P8): settled by an editorial decision to emend a speaker name against explicit print, or by accepting the print as a compositor slip; a look at scan 25 cannot change the words, only confirm them.
- F6 (`अनुद्धोषितः`, p24:P8): settled by reopening scan 24 at 3x or tighter on `ग्रामस्य अनुद्धोषितः महाप्रभुः` to read द्ध vs द्घ.
- F7 (`अर्हस्य`, p24:P6): settled the same way on scan 24 (`अलङ्कर्तुम् अर्हस्य हस्तः`), reading स्य vs visarga.

## Coverage

- p24:P1 {x-com:layout...} : skip layout-only chunk
- p24:P2 # चतुरः : skip title chunk
- p24:P3 लिपिकारस्य भीमराजस्य : clean
- p24:P4 एकदा प्रसिद्धः : clean
- p24:P5 "आगच्छतु आगच्छतु : F1
- p24:P6 ज्योतिषिकः --- : F7
- p24:P7 अनन्तरं ज्योतिषिकः : clean
- p24:P8 "तत्र किम्? : F4, F6
- p24:P9 {note: पञ्चविंशतिवर्षेभ्यः...} : skip footer-note chunk
- p25:P1 {x-com:layout...} : skip layout-only chunk
- p25:P2 "भवान् ग्रामस्थान् : F2
- p25:P3 "आम्। अत्र : F3
- p25:P4 "सत्यं, वस्तुतः : clean
- p25:P5 "भवता यत् : clean
- p25:P6 {pc}पृष्टवान् भीमराजः : clean
- p25:P7 "असत्यकथनेन भवन्तं : clean
- p25:P8 "ओह् एवं : F5
- p25:P9 एतेन आघातेन : clean
- J1 p024:P5 {pb} -> p024:P6 fresh (clean break) : ok
- J2 p024:P8 {pb} -> p025:P2 fresh (clean break) : ok
- J3 p025:P5 {pb} -> p025:P6 {pc} (continues) : ok
- J4 p025:P9 {pb} -> END (clean break) : ok (range end; the p25 bottom art appears to illustrate the following page, outside this range)
