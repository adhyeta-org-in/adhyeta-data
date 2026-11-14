# Proofread report: 1985_03 p038 (pages 38-40, बुद्धिमत्ता)

## Summary

Story `p038` (1985_03, scans 38-40, `बुद्धिमत्ता`) proofread images-closed: 5 findings (2 `STY`/error quote verdicts placed as blocks F1-F2, 3 held grammar observations without blocks F3-F5) and 3 held candidates (= F3-F5, all `*`). Extract gate reached 0 error paras with one print-faithful crossed-quote residual carried forward and ruled here as F1; proofread gate passes with 0 error paras and 0 story findings; `scan.py orth` on deblocked text reports no findings. Loc below is `pNN:Pm:word` (scan-sequence page + chunk matching lint `P` numbers, word counted on the raw chunk from 1) plus the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p040:P4:46 (एतत् उत्तरं) | `अस्ति। अध्यापकस्य` | `अस्ति।' अध्यापकस्य` (lone `{ins:'}`) | STY | error | high | Inner single opened before `अतीव` never closes in print; the sentence boundary pins the only slot that uncrosses the pairs; inherited `{sug-ins:'}` dropped as a true single (crisp one stroke at 3x, SQ is the correct nested sort) |
| 2 | p040:P4:18 (एतत् उत्तरं) | `"एतादृश … शक्येत?"` | `'…'` (sort corrected via `{del:"}{ins:'}` at both ends) | STY | error | high | Interior deliberation (`इति चिन्तयन्`) takes singles; doubles are the wrong sort |
| 3 | p039:P5:10 (बृहस्पतेः कोपमिश्रितवचनेन) and p039:P8:17 (अकस्मात् उपस्थितं) | `क्षाम्यतु माम्` / `क्षाम्यतु भवान्` (2x) | `क्षम्यताम्` | MRP | likely | low* | `क्षाम्यतु` (grow thin) makes no sense as `forgive me`; exact intended imperative uncertain images-closed, so no block |
| 4 | p040:P6:25 (भूस्वामी सहानुभूतिं) | `पर्यवेक्षकं भैरवाचार्य,` | `भैरवाचार्यम्,` | KRK | likely | medium* | `प्रेषयामि` governs accusatives (`पर्यवेक्षकं`, `अश्वपतिं`, `मल्लं`); bare `भैरवाचार्य` breaks government, print-vs-transcription slip undecided images-closed, so no block |
| 5 | p040:P6:35 (भूस्वामी सहानुभूतिं) | `आगच्छतः एते` | `आगच्छन्तः` | AGR | likely | medium* | Participle must agree with nominative plural `एते … शक्नुवन्ति`; `न्तः` vs `तः` undecided images-closed, so no block |

## Patterns

Quote-edge punctuation gaps fixed for readability, 2x (F1 missing inner close, F2 wrong sort on interior thought): both certain from speech-vs-thought sense plus sentence boundary. Print `क्षम्` anomaly, 2x (F3): the same non-form `क्षाम्यतु` in the boy's and the teacher's mouth, suggesting press habit or repeated slip rather than transcription error.

## Unverified

U1 (= F3) `क्षाम्यतु` vs `क्षम्यताम्`: settle by reopening scan 39 left column (`श्रीमन्! क्षाम्यतु माम्` line) and right column (`महानुभाव! क्षाम्यतु भवान्` line) — vowel length `क्षा` vs `क्षा/क्षम्या` decides print-vs-transcription slip, plus dictionary check of the intended forgive-imperative. U2 (= F4) `भैरवाचार्य`: settle by reopening scan 40 right column (`शुनकानां पर्यवेक्षकं भैरवाचार्य,अश्वरक्षणे` line) — missing anusvara decides print slip vs transcription drop. U3 (= F5) `आगच्छतः`: settle by reopening scan 40 right column (`भवता सह आगच्छतः एते अपि` line) — `न्तः` vs `तः` decides transcription slip (then verdict `{del:आगच्छतः}{ins:आगच्छन्तः}`) vs print agreement error.

## Coverage

p038:P1 {x-com:layout: 2col, : skip layout
p038:P2 # बुद्धिमत्ता : skip title
p038:P3 केशवपुरस्य भूस्वामी : clean
p038:P4 कदाचित् एषः : clean
p038:P5 स्वग्रामम् आगत्य : clean
p038:P6 {pc}पाठशालानां व्यवस्था : clean
p038:P7 बृहस्पतिः अपि : clean
p038:P8 बृहस्पतिः एतद्विषये : clean
p038:P9 {author: "श्रीमाता"}{pgb} : skip metadata
p039:P1 {x-com:layout: 2col, : skip layout
p039:P2 एवं क्रमेण : clean
p039:P3 बृहस्पतिः प्रथमं : clean
p039:P4 बृहस्पतिः शालायाः : clean
p039:P5 बृहस्पतेः कोपमिश्रितवचनेन : F3
p039:P6 एतेन उत्तरेण : clean
p039:P7 {pc}एतत्?" इति। : clean
p039:P8 अकस्मात् उपस्थितं : F3
p039:P9 एतेन उत्तरेण : clean
p040:P1 {x-com:layout: art : skip layout
p040:P2 {pc}न। भवान् : clean
p040:P3 प्रधानाध्यापकः भीत्या : clean
p040:P4 एतत् उत्तरं : F1, F2
p040:P5 {pc}प्रधानाध्यापकस्य विद्यार्थिनां : clean
p040:P6 भूस्वामी सहानुभूतिं : F4, F5
p040:P7 भूस्वामिनः वचने : clean
J1 p038:P5 {pb} -> p038:P6 {pc} : ok
J2 p038:P8 {pb} -> p039:P2 fresh : ok
J3 p039:P6 {pb} -> p039:P7 {pc} : ok
J4 p039:P9 {pb} -> p040:P2 {pc} : ok
J5 p040:P4 {pb} -> p040:P5 {pc} : ok
J6 p040:P7 {pb} -> END : ok
