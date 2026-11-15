# Proofread report: 1985_08 p030 (आस्थानकविः, pp. 30–32)

## Summary
Six findings: five error verdicts (F1, F3, F4, F5, F6) and one held low-confidence candidate (F2). The systematic issue is isolated single-akṣara typesetting slips (a dropped mātrā/akṣara, one dittography, one intrusive akṣara); no recurring confusion pair. All Devanagari body chunks were read sentence by sentence; quote marks re-derived (all spoken-voice doubles, balanced, including three pairs spanning a column/page joint); all six joints walked with no rupture. Loc below is `pNN:Pm` (scan span + lint chunk) plus anchor words, word counted from 1. Text is hand transcription, not OCR output; orth scanner clean. One mechanical fix applied directly (Cyrillic lookalikes `Вет` typed for `वेत्` in `अनुभवेत्`, p031:P8) — not a print finding. Extract gate and proofread gate both pass (exit 0).

## Findings
| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p030:P4 राजा तु:7 | `बहुभ्यः प्रदेशभ्यः` | `प्रदेशेभ्यः` | OCR | error | high | अ-stem dative/ablative plural needs `-ेभ्यः`; ए-mātrā dropped in print |
| 2 | p030:P3 पूर्वं चन्द्रचूडः:37 | `पूर्णकुम्भः इव` | `पूर्णकुम्भः` | SPL | likely | low* | classical form is `पूर्णकुम्भ` (full pot, "like a full vessel"); print read with short-u at 3x |
| 3 | p030:P9 कानिचन दिनानि:28 | `मम प्रप्रथमं काव्यम्` | `प्रथमं` | OCR | error | high | `प्रप्रथमं` is not a word; dittography of `प्र` |
| 4 | p031:P4 महाकवेः गौराङ्गस्य:13 | `"एस्तत् पठित्वा` | `एतत्` | OCR | error | high | intrusive `स`; the sense needs the demonstrative `एतत्` |
| 5 | p031:P7 अनन्तरं राजा:26 | `योग्यव्यस्थाम् उपकल्पयतु` | `योग्यव्यवस्थाम्` | OCR | error | high | the stem is `व्यवस्था`; `व` dropped in print |
| 6 | p032:P8 तदनुसारं गम्भीरः:14 | `गम्भीरः उदारी विवेकी` | `उदारः` | SPL | error | high | masculine nominative singular of `उदार` is `उदारः`; house style keeps visarga open (`सः एव`, `ततः गतवान्`) |

## Patterns
Single-akṣara typesetting slips: 4 instances (F1 dropped ए-mātrā, F3 duplicated `प्र`, F4 intrusive `स`, F5 dropped `व`). Each is a one-off at a different word; no confusion pair repeats, so no global rule is proposed.

## Unverified
F2 `पूर्णकुम्भः` → `पूर्णकुम्भः` (SPL, likely, low*): print was read with short-u at 3x in Phase A and recorded as seen; images are closed so the glyph cannot be re-checked. Settled by a look at the scan line `ज्ञानेन सः अपि पूर्णकुम्भः इव आस्थाने` — long-ū confirms the verdict, short-u confirms the candidate should be dropped.

## Coverage
p030:P1 {x-com:layout: : skip layout-only chunk
p030:P2 # आस्थानकविः : skip title
p030:P3 पूर्वं चन्द्रचूडः : F2
p030:P4 राजा तु : F1
p030:P5 चन्द्रचूडः स्वकीयं : clean
p030:P6 महाराजस्य वचनं : clean
p030:P7 {pc}"महाराज, आस्थाने : clean
p030:P8 राजा सचिवस्य : clean
p030:P9 कानिचन दिनानि : F3
p030:P10 चन्द्रचूडः काव्यं : clean
p030:P11 {author: सुभद्रा} : skip metadata
p031:P1 {x-com:layout: : skip layout-only chunk
p031:P2 {pc}सूचयतु" इति। : clean
p031:P3 परेद्युः गौराङ्गः : clean
p031:P4 महाकवेः गौराङ्गस्य : F4
p031:P5 दिनद्वयानन्तरं गम्भीरः : clean
p031:P6 महाराजस्य अनुमतिं : clean
p031:P7 अनन्तरं राजा : F5
p031:P8 मन्त्री मिहिरवर्मा : clean
p032:P1 {x-com:layout: : skip layout-only chunk
p032:P2 {pc}किम्?" इति : clean
p032:P3 "मन्त्रिवर्य! महाकवेः : clean
p032:P4 मन्त्री पुनः : clean
p032:P5 तदा राजा : clean
p032:P6 {pc}गौराङ्गः भूषणस्य : clean
p032:P7 मन्त्री शिरसा : clean
p032:P8 तदनुसारं गम्भीरः : F6
J1 p030:P6 {pb} -> p030:P7 {pc} (continues) : ok
J2 p030:P10 {pb} -> p031:P2 {pc} (continues) : ok
J3 p031:P5 {pb} -> p031:P6 fresh (clean break) : ok
J4 p031:P8 {pb} -> p032:P2 {pc} (continues) : ok
J5 p032:P5 {pb} -> p032:P6 {pc} (continues) : ok
J6 p032:P8 {pb} -> END (clean break) : ok
