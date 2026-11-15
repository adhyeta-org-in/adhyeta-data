# Proofread report: 1986_08 p025 (सहनशक्तिः)

## Summary

One finding (severity style): a single-stroke opening quote in direct speech where the era standard expects a double, corrected via verdict block. No repeats, so no Patterns section. Every body chunk read sentence by sentence for continuity; deblocked `scan.py orth` run clean (0 hits). The file is a manual transcription, not OCR output. Nothing held for the user.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p026:P10 मल्लिनाथः शान्तस्वरेण (w4) | `एव ' नारायण!` | `एव " नारायण!` | STY | style | high | Direct speech takes doubles in this era; single stroke is a dropped second stroke, closed by `"` at p027:P2 |

## Unverified

None. The single Phase A candidate was promoted to a verified verdict (F1); no item is held.

## Coverage

p025:P1 {x-com:layout: : skip layout
p025:P2 # सहनशक्तिः : skip title
p025:P3 कश्चन ग्रामः : clean
p025:P4 तस्य एतादृशं : clean
p025:P5 किन्तु नारायणस्य : clean
p025:P6 "मां क्रुद्धं : clean
p025:P7 एतावदेव न : clean
p025:P8 एवं चिन्तयन् : clean
p025:P9 {author: सुभद्रा} : skip metadata
p026:P1 {x-com:layout: : skip layout
p026:P2 {pc}"पश्यतु भोः : clean
p026:P3 तस्य वचनं : clean
p026:P4 दिनद्वयानन्तरं नारायणः : clean
p026:P5 {pc}वर्धमाना आस्त : clean
p026:P6 तदा मल्लिनाथः : clean
p026:P7 नारायणः तद्वचनम् : clean
p026:P8 "तत्र किमस्ति : clean
p026:P9 "भवान् सर्वदा : clean
p026:P10 मल्लिनाथः शान्तस्वरेण : F1
p027:P1 {x-com:layout: : skip layout
p027:P2 {pc}भवतु तत् : clean
p027:P3 "एवं वयं : clean
p027:P4 "वयं तु : clean
p027:P5 नारायणः किञ्चित्कालं : clean
p027:P6 {pc}इति उक्तवान् : clean
p027:P7 "तत्तु कथं : clean
p027:P8 "किं किम्? : clean
p027:P9 "सत्यम् सोमनाथस्य : clean
p028:P1 {x-com:layout: : skip layout
p028:P2 {pc}तथैव निश्चयं : clean
p028:P3 "तदर्थं किं : clean
p028:P4 "पूर्वापेक्षया अहम् : clean
p028:P5 तस्य वचनं : clean
p028:P6 सा अपि : clean
p028:P7 {pc}सीवनकार्यं जानामि : clean
p028:P8 काले गच्छति : clean
p028:P9 अल्पानि प्रातिवेशिकगृहाणि : clean
p028:P10 "मम कारणातः : clean
J1 p025:P5 -> p025:P6 fresh : ok
J2 p025:P8 -> p026:P2 {pc} : ok
J3 p026:P4 -> p026:P5 {pc} : ok
J4 p026:P10 -> p027:P2 {pc} : F1
J5 p027:P5 -> p027:P6 {pc} : ok
J6 p027:P9 -> p028:P2 {pc} : ok
J7 p028:P6 -> p028:P7 {pc} : ok
J8 p028:P10 -> END : ok
