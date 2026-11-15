# Proofread report: 1985_08 p048 — प्रजाप्रतिनिधिः

## Summary

4 findings: 3 error (F1 held as candidate, F2 and F3 as verdict blocks), 1 style (F4 kept as seen). No systematic problem; three isolated print slips in an otherwise clean single-page story. Every body chunk read sentence by sentence; orth scan clean; no unchecked passages. Text is eye transcription, not OCR output. Loc is `p048:Pm:word` (words counted on the chunk from 1, blocks excluded) with the finding context as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p048:P3:9 `कश्चित् आसीन्` | `आसीन्` | `आसीत्` | OCR | error | medium* | `आसीन्` is not a Sanskrit form; 3sg imperfect of `अस्` is `आसीत्`, which the file prints twice in P4, and `त`/`न` is a documented confusable pair |
| 2 | p048:P7:6 `"आम्, वामतमूर्तिः` | `वामतमूर्तिः` | `वामनमूर्तिः` | CNS | error | high | the same character is `वामनमूर्तिः` five times elsewhere in the story; Phase A verified print shows `त` at 3x, so this is a print slip |
| 3 | p048:P7:21 `इति हढीकृतः` | `हढीकृतः` | `दृढीकृतः` | OCR | error | high | `हढीकृतः` is not a word; the clause needs the past participle `दृढीकृतः` agreeing with `सन्देहः`, and Phase A verified print reads `ह` at 4x, so this is a print slip |
| 4 | p048:P8:12 `प्रजाप्रतिनिधि" राजधानीं` | stray `"` after `प्रजाप्रतिनिधि` | keep as seen | STY | style | high | unbalanced print mark with no mate anywhere in the story; Phase A verified it at 5x, so no pairing is invented and the mark is kept |

## Unverified

- U1 (F1): `आसीन्` vs `आसीत्`. In-file `आसीत्` (P4 ×2) plus the `त`/`न` confusion makes `आसीत्` the strong reading, but the glyph itself was not flagged in Phase A and images stay closed, so it ships as `{sug-del:आसीन्}{sug-ins:आसीत्}`. A user look at the scan settles it.
- U2: `घटनेन` (P7, `गतद्वित्रेषु दिनेषु घटनेन`). If the intended noun is feminine `घटना`, the instrumental should be `घटनया`; a neuter `घटन` would license `घटनेन`. No block emitted. A dictionary check of `घटन` settles it.
- U3 (F4): the sentence wants accusative `प्रजाप्रतिनिधिं` (`ते वामनमूर्तिं प्रजाप्रतिनिधिं राजधानीं प्रेषितवन्तः`, object plus predicative accusative plus destination). Either the stray `"` is print noise and the anusvara dropped, or the mark itself is a damaged anusvara. No block emitted. A user look at the scan settles it.

## Coverage

- p048:P1 `{x-com:layout:` : skip x-com-only chunk
- p048:P2 `# प्रजाप्रतिनिधिः` : skip title
- p048:P3 `नागपल्ली सुसम्पन्नः` : F1
- p048:P4 `एकदा प्रजाप्रतिनिधिः` : clean
- p048:P5 `ग्रामप्रमुखः द्वित्राणि` : clean
- p048:P6 `तदा ग्रामीणाः` : clean (possible extra close stroke after `वा` ruled print noise; single `"` kept, pair balanced)
- p048:P7 `ग्रामप्रमुखः शान्तस्वरेण` : F2, F3
- p048:P8 `ग्रामवासिनः ग्रामप्रमुखस्य` : F4 (kept as seen, documented above)
- J1 p048:P8 {pb} -> END (clean break) : ok (story closes on a completed sentence; single-page span, no continuation)
