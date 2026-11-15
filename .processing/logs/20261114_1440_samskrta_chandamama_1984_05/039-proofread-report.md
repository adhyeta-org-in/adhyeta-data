# Proofread report: 1984_05 story START=039 (यथा तथा)

## Summary

Five findings: four errors (two quote-sort corrections, one print-dropped double-close supplied, one spurious anusvara) and one held likely (dual-subject agreement anomaly). The systematic issue is quote sort: print puts one interior thought in doubles and one spoken reply in singles, against the story's own otherwise consistent sort. The missing double-close after अपेक्षिता। and both sort deviations were verified mark-by-mark at 3x in Phase A. The Sanskrit orth scanner reports zero hits on deblocked text; the text is manual transcription, not OCR output, and every body chunk was read sentence by sentence with no unchecked passages. Two Phase A uncertainty notes (ससंभ्रमम् glyph blur, रमणीयानि frame-clipped initial) were ruled print-faithful from context and removed, recorded here.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p039:P3 [चन्दनपुरे भास्करः] w18 | `सानन्दं निर्वहति स्म` | `सानन्दं निर्वहतः स्म` | AGR | likely | medium* | Dual subject पतिः पत्नी च needs a dual verb, and the same story uses dual अनुभूतवन्तौ; held because the printed form is authorial grammar, not a glyph question. |
| 2 | p039:P6 [{pc}चिन्तितवती] w3, w36 | `"सङ्गीतं ... गायति"` | `'सङ्गीतं ... गायति'` | STY | error | high | Interior thought after मनसि चिन्तितवती takes singles; the story's closing thought uses singles. |
| 3 | p040:P5 [{pc}भास्करः] after w38 | `अपेक्षिता। "इदानीं` | `अपेक्षिता।" "इदानीं` | STY | error | high | भवत्यै proves the तद्दिने speech is Bhaskara's and इति अम्बिका proves the इदानीं speech is hers, so print dropped Bhaskara's close (verified absent at 3x). |
| 4 | p040:P5 [{pc}भास्करः] w57 | `गातुं नं शक्नोमि` | `गातुं न शक्नोमि` | SPL | error | high | Spurious anusvara on the negative particle; तथा अहमपि गातुं न शक्नोमि is the forced reading. |
| 5 | p040:P5 [{pc}भास्करः] w62, w77 | `'किन्तु ... प्रकटनीयः'` | `"किन्तु ... प्रकटनीयः"` | STY | error | high | Spoken reply (प्रत्युत्तरं दत्तवान्) takes doubles; all seven other speeches use doubles. |

## Unverified

F1 (`निर्वहति` / `निर्वहतः`): held for a policy decision on authorial agreement slips rather than a reading doubt. Would settle it: the user's standing rule for classical-vs-print grammar, plus a corpus check whether singular verbs with dual subjects recur in this magazine's Sanskrit (a single search over neighbouring issues' story files).

## Coverage

p039:P1 x-com-layout : skip layout chunk
p039:P2 यथा तथा : skip title
p039:P3 चन्दनपुरे भास्करः : F1
p039:P4 भास्करस्य मित्रं : clean
p039:P5 सप्ताहानन्तरं मुकुन्दः : clean
p039:P6 {pc}चिन्तितवती --- : F2
p039:P7 author भामहः : skip metadata
p040:P1 x-com-layout : skip layout chunk
p040:P2 {pc}रमणीयानि आसन् : clean
p040:P3 तानि चित्राणि : clean
p040:P4 चित्रलेखनं सुलभम् : clean
p040:P5 {pc}भास्करः स्मृतवान् : F3, F4, F5
J1 p039:P5 {pb} -> p039:P6 {pc} : ok
J2 p039:P6 {pb} -> p040:P2 {pc} : ok
J3 p040:P4 {pb} -> p040:P5 {pc} : ok
J4 p040:P5 {pb} -> END : ok
