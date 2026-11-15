## Summary

Story 1985_10 pp. 30-34 (आशाः अनन्ताः): 2 findings — 1 punctuation verdict (F1, missing opening double-quote, high) and 1 spelling candidate (F2, स्थगतन्/स्थगयन्, medium* held). One additional form held without a new block (U1, भक्तः/भवतः?, low* via Phase A x-com; linter forbids adjacent ins+del so the certain quote and the uncertain word cannot sit side by side). No systematic defect; proper nouns (श्रीनाथः, प्रमीला, विमाता, पिशाचः) consistent, open/joined sandhi and homorganic ङ्ग/ङ्क kept as print-faithful house style, 3rd-person imperatives (मुञ्चतु, जानातु, उत्तिष्ठतु, पृच्छतु, क्षिपतु) consistent polite address. Orth scanner (sanskrit/scan.py orth on deblocked text, 49 lines): 0 hits; text reads as clean print, not OCR output. Extract gate and proofread gate both pass (exit 0); 6 para-level notes dispositioned as legitimate column/page-turn continuations. Loc below is story coordinates pNN:Pm plus the first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p032:P2 {ins:"}भक्तः?" इति | `भक्तः?" इति` | `"भक्तः?" इति` | STY | error | high | direct speech pinned by पृष्टवती + इति; opening double-quote missing in print, supplied via {ins:"} |
| 2 | p034:P3 श्रीनाथः तां | `स्थगतन्` | `स्थगयन्` | SPL | likely | medium* | स्थगतन् is no word; त→य yields pres. part stopping her, masc. agreeing with श्रीनाथः; same root attested in-story as स्थगयितुम् |

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf* | What would settle it |
|---|---|---|---|---|---|---|---|
| U1 | p032:P2 भक्तः? इति | `भक्तः` | `भवतः?` | LEX | likely | low* | Single-word angry question by the stepmother; भक्तः (devotee) has no context, repeated भवतः? (cf. previous chunk ending भवतः?) fits no better; tried joining with previous speech and reading as standalone — neither fits at clause level. Held via Phase A {x-com:} (3x: भक्तः as printed); needs glyph re-check of क्त vs वत ligature plus sense review — images closed, so left for the user. No new {sug-} block added: the certain opening quote (F1) already occupies the left edge and the linter forbids ins→del adjacency, so the uncertain word rides on the existing x-com. |

## Coverage

p030:P1 {x-com:layout: 2col, : skip layout chunk
p030:P2 # आशाः : skip title
p030:P3 कश्चित् ग्रामः। : clean
p030:P4 एवं स्थिते : clean
p030:P5 पितामहस्य लघुपेटिकायां : clean
p030:P6 {pc}जनाः "अलसः : clean
p030:P7 एतादृशवचनानि श्रुत्वा : clean
p030:P8 हस्तस्थितस्य धनस्य : clean
p030:P9 तादृशी एका : clean
p030:P10 {author: "श्रीमाता" : skip footer metadata
p031:P1 {x-com:layout: 2col, : skip layout chunk
p031:P2 {pc}तीर्वा कूपसमीपं : clean
p031:P3 प्रमीला रोदनं : clean
p031:P4 "तादृशवृद्धेन सह : clean
p031:P5 {pc}मां मुञ्चतु" : clean
p031:P6 "कष्टानां परिहारार्थं : clean
p031:P7 प्रमीला किञ्चित्कालपर्यन्तं : clean
p031:P8 तस्मिन् समये : clean
p031:P9 परेद्युः प्रातः : clean
p031:P10 "इच्छा कथं : clean
p032:P1 {x-com:layout: 2col, : skip layout chunk
p032:P2 {ins:"}भक्तः?" इति : F1
p032:P3 श्रीनाथः अवमानेन : clean
p032:P4 मध्यरात्रसमये पार्श्वे : clean
p032:P5 "एतस्यां भयङ्कररात्रौ : clean
p032:P6 श्रीनाथः पिशाचं : clean
p032:P7 वृद्धपिशाचः तं : clean
p032:P8 श्रीनाथः स्वीयं : clean
p032:P9 तस्य वचनं : clean
p033:P1 {x-com:layout: 2col, : skip layout chunk
p033:P2 {pc}सम्यक् स्मरतु : clean
p033:P3 श्रीनाथः अङ्गुलीयकम् : clean
p033:P4 पूर्वं सः : clean
p033:P5 श्रीनाथः तत्र : clean
p033:P6 {pc}कार्यं कृत्वा : clean
p033:P7 "महान् प्रमोदः : clean
p033:P8 दशद्वादशदिनानि अतीतानि। : clean
p033:P9 श्रीनाथः प्रवृत्तं : clean
p033:P10 प्राचीनस्य ताम्राङ्गुलीयकस्य : clean
p033:P11 "एतावदेव खलु? : clean
p033:P12 तस्य वचनं : clean
p034:P1 {x-com:layout: 2col, : skip layout chunk
p034:P2 {pc}महिमयुक्तम् अङ्गुलीयकं : clean
p034:P3 श्रीनाथः तां : F2
p034:P4 एतत् किमपि : clean
p034:P5 सा तत् : clean
p034:P6 "अस्तु, पृच्छतु" : clean
p034:P7 अङ्गुलीयकस्य महत्त्वं : clean
p034:P8 पत्युः वचनस्य : clean
J1 p030:P5 {pb} -> p030:P6 {pc} (continues) : ok
J2 p030:P9 {pb} -> p031:P2 {pc} (continues) : ok
J3 p031:P4 {pb} -> p031:P5 {pc} (continues) : ok
J4 p031:P10 {pb} -> p032:P2 fresh (clean break) : ok
J5 p032:P9 {pb} -> p033:P2 {pc} (continues) : ok
J6 p033:P5 {pb} -> p033:P6 {pc} (continues) : ok
J7 p033:P12 {wb} -> p034:P2 {pc} (continues) : ok
J8 p034:P8 {pb} -> END (clean break) : ok
