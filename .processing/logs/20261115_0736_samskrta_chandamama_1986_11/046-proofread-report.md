# Proofread report: 1986_11 p046 (कूष्माण्डचोरः, scans 46–49)

## Summary

Loc convention: `pNN:Pm` (NN = scan sequence 46–49, Pm = lint chunk number) plus the chunk's first two words as anchor; `w<n>` counts deblocked words on that chunk from 1. Two findings, both STY/punctuation with verdict blocks in the file: F1 supplies a missing inner quote pair pinned by a reporting verb plus इति, F2 corrects a quote sort (SQ to DQ) for top-level spoken report. One held candidate (U1, unverified participle agreement) stays as `{sug-del:}/{sug-ins:}`. The orth scanner found 0 hits on deblocked text; this is a clean eye transcription (images verified with PIL crops in Phase A), not OCR output. No passage was left unchecked; every sentence was read for continuity and every joint fit-tested.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p049:P2 (अधिकारी अपि) w9, w11 | `वदति --- एतानि फलानि मदीयानि इति` | `वदति --- 'एतानि फलानि मदीयानि' इति` | STY | style | high | reporting verb वदति plus इति-closure pins a directly quoted claim, so the inner pair is supplied |
| F2 | p048:P6 (कारिणः समीपं) w4, w10 | `'गौरीशः ... विक्रीतवान्' इति निवेदितवान्` | `"गौरीशः ... विक्रीतवान्" इति निवेदितवान्` | STY | style | medium | top-level spoken report (निवेदितवान् plus इति) takes doubles; singles mark thought or nested speech |

## Patterns

PAT-A (variant, no blocks): print keeps open sandhi where joining is possible (तत् श्रुत्वा, तत् पुस्तकम्, एतत् उचितम्, यत् तादृशानि); recorded as Chandamama house-style openness, never flagged. PAT-B (kept sort, no blocks): singles mark cited name-labels ('ऐरावतम्', 'महालक्ष्मीः', 'अग्रजा', 'महाराज्ञी', 'सुवर्णा', 'कूष्माण्डचोरः') and interior thought ('विक्रयणयोग्यानि कानि', पुत्रवत्- and चोरितानि-passages); kept as seen.

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| U1 | p047:P4 (प्रातः वृषभेन्द्रः) w10 | `समीपं गतं तदा` | `गतं` or `गतः`? | AGR | likely | low* | यदा-clause subject is masc वृषभेन्द्रः, so the motion-verb क्त should read गतः; impersonal and locative-absolute re-segmentations were tested and fit nothing, so the final sign (ं vs ः) needs a 3x scan re-read to settle |

## Coverage

p046:P1 ({x-com:layout...}) : skip layout-only chunk
p046:P2 (# कूष्माण्डचोरः) : skip title chunk
p046:P3 (तोरणपुरे वृषभेन्द्रः) : clean
p046:P4 (आत्मना वर्धितानां) : clean
p046:P5 (तस्मिन् एव) : clean
p046:P6 (भवन्ति स्म) : clean
p046:P7 (एकस्मिन् वर्षे) : clean
p046:P8 (नगरे सोमवासरे) : clean
p046:note (पञ्चविंशतिवर्षेभ्यः पूर्वं) : skip reprint-note metadata chunk
p047:P1 ({x-com:layout...}) : skip layout-only chunk
p047:P2 (शकटनिश्चयम् अपि) : clean
p047:P3 (तद्दिने रात्रौ) : clean
p047:P4 (प्रातः वृषभेन्द्रः) : U1
p047:P5 (वृषभेन्द्रः मतिभ्रष्टः) : clean
p047:P6 (अत्रान्तरे वृषभेन्द्रस्य) : clean
p047:P7 (तत्क्षणे एव) : clean
p047:P8 (कस्मिंश्चित् आपणे) : clean
p048:P1 ({x-com:layout...}) : skip layout-only chunk
p048:P2 (वृषभेन्द्रः आपणिकस्य) : clean
p048:P3 (तदा आपणिकः) : clean
p048:P4 ("गौरीशः इतोऽपि) : clean
p048:P5 (वृषभेन्द्रः तत्क्षणे) : clean
p048:P6 (कारिणः समीपं) : F2
p048:P7 (भटाः गत्वा) : clean
p048:P8 ("एतानि सर्वाणि) : clean
p048:P9 ("मया वर्धितानि) : clean
p048:P10 (परितः स्थिताः) : clean
p049:P1 ({x-com:layout...}) : skip layout-only chunk
p049:P2 (अधिकारी अपि) : F1
p049:P3 (वृषभेन्द्रः किमपि) : clean
p049:P4 ("एषः कश्चन) : clean
p049:P5 (तदा वृषभेन्द्रः) : clean
p049:P6 (तत् श्रुत्वा) : clean
p049:P7 (किञ्चित्कालानन्तरम् उभौ) : clean
p049:P8 (गतवन्तौ। गौरीशः) : clean
p049:P9 (अधिकारिणः पुरतः) : clean
p049:P10 (गौरीशस्य पुस्तके) : clean
p049:P11 ("भवतः साक्ष्यं) : clean
p049:P12 (वृषभेन्द्रः ग्रन्थिम्) : clean
p049:P13 (अधिकारी सर्वेषां) : clean
J1 p046:P5 {pb} -> p046:P6 {pc} (continues) : ok
J2 p046:P8 {pb} -> p047:P2 {pc} (continues) : ok
J3 p047:P5 {pb} -> p047:P6 fresh (clean break) : ok
J4 p047:P8 {pb} -> p048:P2 fresh (clean break) : ok
J5 p048:P5 {wb} -> p048:P6 {pc} (continues) : ok
J6 p048:P10 {pb} -> p049:P2 fresh (clean break) : ok
J7 p049:P7 {wb} -> p049:P8 {pc} (continues) : ok
J8 p049:P8 {pb} -> p049:P9 {pc} (continues) : ok
J9 p049:P13 {pb} -> END (clean break) : ok
