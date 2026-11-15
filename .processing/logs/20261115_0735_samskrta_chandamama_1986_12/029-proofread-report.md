# Proofread report: 1986_12, START=29 (p029)

## Summary

Range p029 (8 page spans, 53 body chunks): the `उत्तररामायणम्` instalment from Sumāli's return through the Maṇibhadra battle. Extract gate and proofread gate both pass with 0 errors and 0 notes. Seven findings, all `likely`: four verified quote verdicts applied as in-file `{del:}`/`{ins:}` blocks (F4--F7, `high`), three held word candidates left as `{sug-del:}`/`{sug-ins:}` for the user (F1--F3, `medium*`). Systematic checks: open sandhi (`तत् नगरम्`, `पातालतः प्रस्थाय`) is the edition's house style and was never flagged; `scan.py orth` on deblocked text reports 0 hits, and the text is direct print transcription, not OCR output, so no OCR hypotheses were entertained. Kept as print-faithful with reasons: the `सुमाली`/`सुमालिः` stem variation, the hyphenated `वि-रूपाक्ष`, and the verbless `रावणः स्वीयम् असाधारणबलं।` fragment. Loc words are counted on whitespace-separated tokens excluding `{...}` blocks.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p031:P4 (विश्रवाः कुबेरस्य) w24 | `वराणां प्राप्या इदानीं` | `वराणां प्राप्त्या इदानीं` | SPL | likely | medium* | `प्राप्या` has no agreeing parse beside genitive `वराणां` (tried gerund `प्राप्य` and feminine `प्राप्या`: neither governs the genitive); instrumental `प्राप्त्या` (through obtaining) is the unique clause fit |
| 2 | p032:P5 (लङ्काधिपत्य ---) w17 | `रावणेन प्रप्रथमतया कृतं` | `रावणेन प्रथमतया कृतं` | SPL | likely | medium* | `प्रप्रथम` is not a Sanskrit word (no `प्र`-doubling); `प्रथमतया` (for the first time) is the unique fit for the wedding-celebration clause |
| 3 | p032:P10 (अहं पुलस्त्य) w17 | `इति द्वौ अनुजौः,` | `इति द्वौ अनुजौ,` | MRP | likely | medium* | dual `द्वौ` needs dual `अनुजौ`; the visarga on `अनुजौः` matches no dual ending (tried nominative and accusative dual: neither takes visarga) |
| 4 | p032:P10 (अहं पुलस्त्य) w21 | `च सन्ति' इति` | `च सन्ति" इति` | STY | likely | high | Rāvaṇa's self-introduction is reported speech (`उक्तवान् रावणः`) so doubles are required; the single close is a dropped second stroke per the era quote rule |
| 5 | p033:P2 (अपि तस्य) w23 | `महत् 'शक्त्यायुधं यौतकरूपेण` | `महत् 'शक्त्यायुधं' यौतकरूपेण` | STY | likely | high | the weapon name is term-quoted in print singles; the close belongs at the term boundary after `शक्त्यायुधं`, not around the narrative `यौतकरूपेण दत्तवान्` |
| 6 | p034:P5 (रावणं प्रति) w103 | `मां "पूर्वम् अहम्` | `मां 'पूर्वम् अहम्` | STY | likely | high | Śiva's words are nested inside Kubera's still-open `"अनुज,` message, so the inner open takes single per the nesting rule; `मां` pins the position |
| 7 | p034:P5 (रावणं प्रति) w128 | `नामधेयम् अस्तु" इति` | `नामधेयम् अस्तु' इति` | STY | likely | high | mate of F6: the inner close sits before `इति उक्तवान्`, keeping the `DQ SQ ... SQ DQ` nesting intact |

## Unverified

- F1 `प्राप्या` / `प्राप्त्या` (p031:P4 w24): held as `{sug-del:प्राप्या}{sug-ins:प्राप्त्या}` in-file; what would settle it is a user-side look at whether the print shows a `त्त` conjunct, plus confirming the idiom `वराणां प्राप्त्या`, since Phase B cannot reopen scans and no Phase A note was on file.
- F2 `प्रप्रथमतया` / `प्रथमतया` (p032:P5 w17): held as `{sug-del:प्रप्रथमतया}{sug-ins:प्रथमतया}` in-file; what would settle it is a user-side check for a possible syllable-break hyphen or dittography in print, since the glyphs are certain at 1x but only the user can confirm the press reading.
- F3 `अनुजौः,` / `अनुजौ,` (p032:P10 w17): held as `{sug-del:अनुजौः,}{sug-ins:अनुजौ,}` in-file; what would settle it is a user-side 3x look confirming the visarga stroke, since a dropped-stroke or press-variant reading cannot be excluded from text alone.

## Coverage

- p029:P1 ({x-com:layout}) : skip layout-note, no story text
- p029:P2 (# उत्तररामायणम्) : skip title
- p029:P3 (पाताललोके स्थितः) : clean
- p029:P4 (सः मारीच) : clean
- p029:P5 (सुमालिः रावणम्) : clean
- p029:P6 (भयं नास्ति) : clean
- p029:P7 (तत् सर्वं) : clean
- p029:P8 ({misc: ३.) : skip metadata
- p030:P1 ({x-com:layout}) : skip layout-note, no story text
- p030:P2 (कुबेरः पितृसदृशः) : clean
- p030:P3 (सुमालिः अन्यत्) : clean
- p030:P4 (वत्स, रावण,) : clean
- p030:P5 (कश्यपब्रह्मणः पत्न्यौ) : clean
- p030:P6 (तस्य वचनानि) : clean
- p030:P7 (अनन्तरं वाचोयुक्तिपटुं) : clean
- p030:P8 (अग्रज, इदानीं) : clean
- p031:P1 ({x-com:layout}) : skip layout-note, no story text
- p031:P2 (रावणस्य दूतरूपः) : clean
- p031:P3 (प्रहस्तद्वारा एतं) : clean
- p031:P4 (विश्रवाः कुबेरस्य) : F1
- p031:P5 (इदानीं भवान्) : clean
- p031:P6 (कुबेरः निर्मलचित्तेन) : clean
- p031:P7 (अत्यानन्दम् अनुभवन्) : clean
- p032:P1 ({x-com:layout}) : skip layout-note, no story text
- p032:P2 (करोतु" इति) : clean
- p032:P3 (रावणः अनुजाभ्यां,) : clean
- p032:P4 (एवंरीत्या अत्र) : clean
- p032:P5 (लङ्काधिपत्य ---) : F2
- p032:P6 (आसीत्।) : clean
- p032:P7 (एवंरीत्या काले) : clean
- p032:P8 (भवान् कः?) : clean
- p032:P9 (तदा सः) : clean
- p032:P10 (अहं पुलस्त्य) : F3, F4
- p032:P11 (रावणः महर्षि) : clean
- p033:P1 ({x-com:layout}) : skip layout-note, no story text
- p033:P2 (अपि तस्य) : F5
- p033:P3 (रावणः स्वीय) : clean
- p033:P4 (त्रयः अपि) : clean
- p033:P5 (कदाचित् रावणः) : clean
- p033:P6 (अग्रज, एषा) : clean
- p033:P7 (रावणः प्रिय) : clean
- p033:P8 (कुम्भकर्णः तस्मिन्) : clean
- p033:P9 (यदा कुम्भ) : clean
- p034:P1 ({x-com:layout}) : skip layout-note, no story text
- p034:P2 (असाधारणबलं। प्रति) : clean
- p034:P3 (अनुजस्य एतादृश) : clean
- p034:P4 (आगमनकारणं पृष्ट) : clean
- p034:P5 (रावणं प्रति) : F6, F7
- p035:P1 ({x-com:layout}) : skip layout-note, no story text
- p035:P2 (दुष्कृत्यानां वार्ता) : clean
- p035:P3 (एवं रीत्या) : clean
- p035:P4 (अनन्तरं रावणः) : clean
- p035:P5 (सः प्रप्रथ) : clean
- p035:P6 (शीघ्रं शीघ्रं) : clean
- p035:P7 (सद्यः एव) : clean
- p036:P1 ({x-com:layout}) : skip layout-note, no story text
- p036:P2 (निर्गत्य धावित) : clean
- p036:P3 (एतं वृत्तान्तं) : clean
- p036:P4 (अनन्तरं रावणः) : clean
- p036:P5 (द्वितीयवारं प्रेषिताः) : clean
- p036:P6 (मणिभद्रः चतुस्) : clean
- p036:P7 (कृतवन्तः, तदा) : clean
- p036:P8 (तथापि मणिभद्रः) : clean
- J1 p029:P5 {pb} -> p029:P6 {pc} (continues) : ok
- J2 p029:P7 {pb} -> p030:P2 {pc} (continues) : ok
- J3 p030:P4 {pb} -> p030:P5 {pc} (continues) : ok
- J4 p030:P8 {pb} -> p031:P2 fresh (clean break) : ok
- J5 p031:P4 {pb} -> p031:P5 {pc} (continues) : ok
- J6 p031:P7 {pb} -> p032:P2 {pc} (continues) : ok
- J7 p032:P5 {pb} -> p032:P6 {pc} (continues) : ok
- J8 p032:P11 {pb} -> p033:P2 {pc} (continues) : ok
- J9 p033:P4 {pb} -> p033:P5 fresh (clean break) : ok
- J10 p033:P5 {pb} -> p033:P6 fresh (clean break) : ok
- J11 p033:P9 {pb} -> p034:P2 {pc} (continues) : ok
- J12 p034:P3 {pb} -> p034:P4 {pc} (continues) : ok
- J13 p034:P5 {pb} -> p035:P2 {pc} (continues) : ok
- J14 p035:P5 {pb} -> p035:P6 {pc} (continues) : ok
- J15 p035:P7 {pb} -> p036:P2 {pc} (continues) : ok
- J16 p036:P6 {pb} -> p036:P7 {pc} (continues) : ok
- J17 p036:P8 {pb} -> END (clean break) : ok
