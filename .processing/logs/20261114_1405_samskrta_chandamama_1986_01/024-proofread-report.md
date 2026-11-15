# Proofread report: 1986_01 p024 (scan pages 24-25, story शापविमुक्तिः)

## Summary

Two findings, both quote-mark verdicts in the second page span: one genuine print mismatch (single open with double close on a thought clause, closed to single) and one sort correction (balanced single pair on reported speech corrected to double). No inherited Phase A candidates were on file, the orth scanner raised zero hits on deblocked text, and every joint and sentence reads continuously with no rupture, so no moves and nothing held. The edition prints visarga open before voiced sounds throughout (चन्द्रमुखः नाम, मुनिः कोपेन), which is consistent house style and was never flagged. The text is a direct print transcription, not OCR output.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p025:P3 'इतःपरम् एतत्:7 | `गन्तव्यं भविष्यति" इति चिन्तयन्` | `गन्तव्यं भविष्यति' इति चिन्तयन्` | STY | error | high | Print opens with single and closes with double; चिन्तयन् marks interior thought, so the close takes single to match the open |
| 2 | p025:P6 प्रवृत्तं सर्वं:4 | `निवेद्य 'किमपि साहाय्यं पृच्छतु' इति उक्तवान्` | `निवेद्य "किमपि साहाय्यं पृच्छतु" इति उक्तवान्` | STY | likely | high | उक्तवान् with इति-closure pins reported speech, which takes double under the era sort; both marks corrected as a pair |

## Patterns

None (two isolated quote-mark rulings, no repeats).

## Unverified

None (no held candidates; both findings ruled high-confidence from speech-vs-thought sense and the era quote sort).

## Coverage

p024:P1 {x-com:layout: : skip x-com-only chunk
p024:P2 # शापविमुक्तिः : skip title chunk
p024:P3 प्राचीनकाले चन्द्रमुखः : clean
p024:P4 एतेन भयङ्करशापेन : clean
p024:P5 श्रुत्वा अपि : clean
p024:P6 अनन्तरक्षणे चन्द्रमुखः : clean
p024:P7 दिनद्वयम् अतीतम् : clean
p024:P8 किन्तु एतदनन्तरं : clean
p024:P9 {author: "विवेक"} : skip metadata chunk, node kept as seen
p025:P1 {x-com:layout: : skip x-com-only chunk
p025:P2 अत्रापि आहारत्वेन : clean
p025:P3 'इतःपरम् एतत् : F1
p025:P4 ब्रह्मराक्षसः आनन्देन : clean
p025:P5 मुनेः वचनानुसारं : clean
p025:P6 प्रवृत्तं सर्वं : F2
p025:P7 तदा सः : clean
p025:P8 'महतः आक्रोशनस्य : clean
p025:P9 सः पथिकः : clean
p025:P10 'आम् इति : clean
J1 p024:P4 {pb} -> p024:P5 {pc} (continues) : ok
J2 p024:P8 {pb} -> p025:P2 fresh (clean break) : ok
J3 p025:P5 {pb} -> p025:P6 {pc} (continues) : ok
J4 p025:P10 {pb} -> END (clean break) : ok
