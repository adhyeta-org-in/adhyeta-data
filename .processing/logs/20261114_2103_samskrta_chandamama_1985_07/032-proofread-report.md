## Summary

Phase A is complete and untouched: 6 `{pgb}`-terminated spans (scans 32–37) with a 12-joint index; `lint.py --phase extract` passes (exit 0, 4 notes-only residuals carried in) and no page was re-transcribed. Phase B proofread gate now passes clean (`lint.py --phase proofread`: 6 pages, 0 error paras, 0 story findings, exit 0); `scan.py orth` on deblocked text reports 0 hits across 57 lines. Findings table: 5 verified verdicts (F1–F5, all quote supply/sort/relocation, STY/style, high) plus 3 held candidates (F6 स्याम् F7 दुरदष्टवशात् F8 क्षम्यतु, MRP/SPL, likely, low*). One Patterns entry (stray `'"` opens ×2 on p036). Print keeps open sandhi and visarga before vowels throughout (मम एव, दुःखिता अभवत्, वासन्ती तु); these are house variants, never flagged. Proper nouns (वज्रगुप्तः, वासन्ती, पद्मावती, चन्द्रकान्तः, रामपुरम्) spell consistently; no verse in this range. Loc below is keyed `pNN:Pm[:w]` (NN = scan sequence 32 + `{pgb}`-span ordinal, Pm = lint chunk number, w = word in chunk from 1) plus the first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p034:P6:18 एतत् श्रुतवत्याः | `इच्छामि' इति एतत् सामान्य` | insert `"` before एतत् via `{ins:"}` | STY | style | high | spoken questions closed by `?"` need a double open; speech verb plus sentence boundary pins it |
| 2 | p035:P4:12 एतत् ज्ञात्वा | `वा? इति।"` | close relocated before इति via `{ins:"}` + `{del:"}` | STY | style | high | इति unambiguously closes the speech; marks after it are misplaced |
| 3 | p036:P4:13 वज्रगुप्तः रामपुरस्य | `'"आचार्य! ... दोषः"` (single+double open) | `"आचार्य! ... दोषः"` via `{del:'}` | STY | style | high | direct speech closed by इति उक्तवान् takes doubles; Phase A verified the stray single at 2x |
| 4 | p036:P5:6 तदा गुरुः | `'"चन्द्रकान्तः ... अर्हति"` (single+double open) | `"चन्द्रकान्तः ... अर्हति"` via `{del:'}` | STY | style | high | same as F3, same page, same quirk |
| 5 | p037:P3:1 'किमर्थम् एवं | `'किमर्थम् एवं कृतवान्?"` (single open, double close) | `"किमर्थम् एवं कृतवान्?"` via `{del:'}{ins:"}` | STY | style | high | spoken in anger (कोपेन पृष्टवान्) takes doubles; sort corrected |
| 6 | p034:P4:9 वासन्ती चन्द्रकान्तं | `भवान् कलाकारः स्याम्` | `{sug-del:स्याम्}{sug-ins:स्यात्}` (held) | MRP | likely | low* | second-person भवान् cannot govern first-person स्याम्; honorific third स्यात् fits, स्याः possible |
| 7 | p035:P3:14 कानिचन दिनानि | `परन्तु दुरदष्टवशात्` | `{sug-del:दुरदष्टवशात्}{sug-ins:दुरदृष्टवशात्}` or दुर्दैववशात् (held) | SPL | likely | low* | दुरदष्ट is no word; one dropped ृ gives दुरदृष्ट (ill luck), दुर्दैववशात् needs more changes |
| 8 | p037:P4:65 "स्वभगिन्याः पद्मावत्याः | `मां क्षम्यतु` | `{sug-del:क्षम्यतु}{sug-ins:क्षम्यताम्}` (held) | MRP | likely | low* | passive imperative क्षम्यताम् governs accusative मां; क्षम्यतु gives no transitive "forgive" sense |

## Patterns

Print opens two p036 speeches with a stray single before the double (`'"आचार्य!` F3, `'"चन्द्रकान्तः` F4) while closing both with plain doubles; both corrected the same way.

## Unverified

F6 `स्याम्` (p034:P4:9) is held as `{sug-del:स्याम्}{sug-ins:स्यात्}`, not a verdict: person agreement rules out the print form with भवान्, but स्यात् versus स्याः cannot be settled from text alone. What would settle it: a Heritage Platform / dictionary check of attested optative use, or user choice between the two replacements.
F7 `दुरदष्टवशात्` (p035:P3:14) is held as `{sug-del:दुरदष्टवशात्}{sug-ins:दुरदृष्टवशात्}`, not a verdict: no grammatical parse of the print form exists, but neither replacement is confirmed. What would settle it: a dictionary attestation of दुरदृष्ट-वशात्, or user acceptance of दुर्दैववशात्.
F8 `क्षम्यतु` (p037:P4:65) is held as `{sug-del:क्षम्यतु}{sug-ins:क्षम्यताम्}`, not a verdict: क्षम् in the passive imperative (क्षम्यताम्, "let me be forgiven") governs accusative मां, while क्षम्यतु gives no sensible "forgive my offence" reading in the plea at the teacher's feet; but with images closed and no tool confirmation, the emendation stays a candidate for the user. What would settle it: a Heritage Platform / dictionary check of क्षम्यतु as an attested form, or user acceptance of क्षम्यताम्.

## Coverage

p032:P1 {x-com:} : skip layout-only chunk
p032:P2 # पाषाण-प्रतिमा : skip title
p032:P3 इन्द्रपुरे वज्रगुप्तः : clean
p032:P4 ज्येष्ठपुत्र्याः नाम : clean
p032:P5 सा स्वगृहे : clean
p032:P6 उभयोः स्वभावः : clean
p032:P7 समानम्। तयोः : clean
p032:P8 वासन्ती स्वार्थपरा : clean
p032:P9 किन्तु तदा : clean
p032:P10 एतद्विषये पद्मावती : clean
p032:P11 {author:} : skip metadata + x-com-only chunk (byline read as seen, no confident reading issue)
p033:P1 {x-com:} : skip layout-only chunk
p033:P2 इति। : clean
p033:P3 "अन्येषां स्तुतिप्राप्तिः : clean
p033:P4 किन्तु पद्मावती : clean
p033:P5 एवं स्थिते : clean
p033:P6 च इति। : clean
p033:P7 चन्द्रकान्तः नवयुवकः : clean
p033:P8 चन्द्रकान्तस्य व्यवहारेण : clean
p033:P9 एकदा वार्तालापमध्ये : clean
p034:P1 {x-com:} : skip layout-only chunk
p034:P2 अतः सा : clean
p034:P3 "असत्यम् उक्त्वा : clean
p034:P4 वासन्ती चन्द्रकान्तं : F6
p034:P5 चन्द्रकान्तः सावधानपूर्वकम् : clean
p034:P6 एतत् श्रुतवत्याः : F1
p034:P7 णयेत्?" इति। : clean
p034:P8 "अहं तत् : clean
p034:P9 वासन्त्याः मनसि : clean
p034:P10 वासन्त्याः एतादृशव्यवहारेण : clean
p035:P1 {x-com:} : skip layout-only chunk
p035:P2 "दरिद्राः धनिकान् : clean
p035:P3 कानिचन दिनानि : F7
p035:P4 एतत् ज्ञात्वा : F2
p035:P5 "सर्वं कृतम्। : clean
p035:P6 अत्रान्तरे एकदा : clean
p035:P7 इदानीं जनानां : clean
p035:P8 ग्रामीणाः सर्वे : clean
p035:P9 प्रसन्नः वज्रगुप्तः : clean
p036:P1 {x-com:} : skip layout-only chunk
p036:P2 एतत् सर्वं : clean
p036:P3 तेषु दुष्टेषु : clean
p036:P4 वज्रगुप्तः रामपुरस्य : F3
p036:P5 तदा गुरुः : F4
p036:P6 अनन्तरं सः : clean
p036:P7 वान्, उक्तवान् : clean
p036:P8 तत्क्षणे एव : clean
p036:P9 चन्द्रकान्तः गुरुं : clean
p037:P1 {x-com:} : skip layout-only chunk
p037:P2 निर्मिता" इति। : clean
p037:P3 'किमर्थम् एवं : F5
p037:P4 "स्वभगिन्याः पद्मावत्याः : F8
p037:P5 प्रवृत्तं सर्वं : clean
p037:P6 कम्पते। यदि : clean
p037:P7 वासन्त्यां जातं : clean
p037:P8 विवाहानन्तरं वासन्ती : clean
p037:P9 'वासन्त्यां यत् : clean
J1 p032:P6 {pb} -> p032:P7 {pc} : ok (रूपं / समानम् spaced join, sentence continues)
J2 p032:P10 {pb} -> p033:P2 {pc} : ok (करिष्यन्ति" / इति। print closes the quote before the turn, stranding च in p033:P6; kept print-faithful with no verdict since relocation would unbalance the merged logical paras)
J3 p033:P5 {pb} -> p033:P6 {pc} : ok (प्रतिष्ठापनीयः / च unique grammatical fit closing चिन्तितवान् यत्, confirming left-column-below-art reads before right column)
J4 p033:P9 {pb} -> p034:P2 fresh : ok (नास्ति। / अतः clean break, speech pair closed)
J5 p034:P6 {wb} -> p034:P7 {pc} : ok (परि / णयेत् solid join to परिणयेत्; question pair completed by supplied open F1)
J6 p034:P10 {pb} -> p035:P2 fresh : ok (इति। / "दरिद्राः clean break, new speaker)
J7 p035:P4 {pb} -> p035:P5 fresh : ok (इति।" / "सर्वं clean break; relocated close F2 balanced in-chunk)
J8 p035:P9 {pb} -> p036:P2 fresh : ok (च। / एतत् clean break)
J9 p036:P6 {wb} -> p036:P7 {pc} : ok (परिशीलित / वान् solid join to परिशीलितवान्)
J10 p036:P9 {pb} -> p037:P2 {pc} : ok (अत्र / निर्मिता DQ pair completed across the page turn, the allowed exception)
J11 p037:P5 {pb} -> p037:P6 {pc} : ok (भयेन / कम्पते spaced join; DQ pair completed across columns)
J12 p037:P9 {pb} -> END : ok (clean story close on इति।)
