# Proofread report — 1986_01 p018 (scan pages 18–23, `नटेशस्य सेवकः`)

## Summary

Story file (6 page spans, 44 chunks) passes `lint --phase proofread` with 0 errors. Four verified verdicts landed as blocks: three print-misprint corrections promoted from Phase A candidates (F1–F3) and one quote-sort correction of a dictated message from singles to doubles (F4). One form is held as a `{sug-…}` candidate for the user (F5). The edge-spanning Vetala-frame quote (open p018, close p019) and the three `{pb}`/`{pc}`-spanning speeches (J5, J8, J11) are kept as print pairings with no blocks. Print spelling/sandhi variants (`हृद्गतं`, `निश्शङ्कम्`, `इदंप्रथमतया`, open sandhi like `तस्य कथां`, `बेतालकथा` beside narrative `वेतालः`) are kept as seen. `Loc` is keyed on story coordinates `pNN:Pm` plus the chunk's first two words, with the word counted on whitespace-separated tokens (blocks excluded) from 1. Text was transcribed directly from scans, not OCR output; no passages unchecked.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p018:P3 (राजा त्रिविक्रमः) :1 | `दृढाप्रहवान् राजा` | `{del:दृढाप्रहवान्}{ins:दृढाग्रहवान्}` | OCR | error | high | प्र/ग्र type confusion at 3x; `दृढाप्रहवान्` is no word, `दृढाग्रहवान्` (resolute) is the only fit for the frame opening |
| F2 | p020:P5 (तत् दृष्ट्वा) :4 | `"कि भोः` | `किम् भोः ({ins:म्})` | OCR | error | high | bare `कि` is no word here; the `किम् भोः` vocative formula opens the question, and `किमर्थं` follows in the same sentence |
| F3 | p022:P4 (अपि नटेशः) :1 | `परेघुः अपि` | `{del:परेघुः}{ins:परेद्युः}` | OCR | error | high | `परेघुः` is no word; `परेद्युः` (next day) fits the day-by-day sequence after the pacification |
| F4 | p022:P4 (अपि नटेशः) :16 | `तथा 'अद्यापि आगन्तुं न शक्नोमि' इति` | `{del:'}{ins:"} … {del:'}{ins:"}` (doubles both ends) | STY | error | high | dictated message with reporting verb `सूचितवान्` plus `इति` closure is spoken conversation, which takes doubles; singles are thought or nested speech |
| F5 | p022:P10 (तदा नटेशः) :36 | `मां क्षाम्यतु` | `क्षम्यतु` (held) | MRP | likely | low* | `क्षाम्यतु` is no standard imperative of `क्षम्`; sense is "forgive me" but the exact replacement is not pinned |

## Patterns

बेताल/वेताल house pair (2 shapes): the story label prints `बेतालकथा` (p018:P3 `{category:}`) while the narrative prints `वेतालः`/`वेतालेन` throughout (p019:P3, p023:P2, p023:P5). Both kept as seen; no blocks.

## Unverified

F5 held: `क्षम्यतु` is the minimal fix already on file from Phase A, but `क्षमस्व` or `क्षम्यताम्` (cf. the parallel `क्षाम्यतु माम्` held in the p002 report, F5) cannot be excluded from text alone; an editor ruling or another copy of the issue would settle it.

## Coverage

p018:P1 : skip layout
p018:P2 : skip title
p018:P3 राजा त्रिविक्रमः : F1
p019:P1 : skip layout
p019:P2 किल?" इति। : clean
p019:P3 अनन्तरं वेतालेन : clean
p019:P4 नटेशस्य एतत् : clean
p019:P5 केशवः नटेशस्य : clean
p019:P6 सेवकवृत्तिं करोति : clean
p019:P7 एवं क्रमेण : clean
p019:P8 कदाचित् केनापि : clean
p019:P9 चकोरः सर्वदा : clean
p020:P1 : skip layout
p020:P2 कालं यापयति। : clean
p020:P3 सः महाराजस्य : clean
p020:P4 केशवः नटेशस्य : clean
p020:P5 तत् दृष्ट्वा : F2
p020:P6 "भवतः अभिप्रायं : clean
p020:P7 तस्य उत्तरं : clean
p020:P8 कार्यं कुर्वाणः : clean
p020:P9 तदा केशवः : clean
p021:P1 : skip layout
p021:P2 "न्यायरीत्या भवान् : clean
p021:P3 राजशब्दस्य चन्द्रः : clean
p021:P4 सन्तुष्टः महाराजः : clean
p021:P5 तस्य वचनं : clean
p021:P6 "इदानीम् उभयोः : clean
p021:P7 तस्य अभिप्रायं : clean
p021:P8 केशवः नटेशस्य : clean
p022:P1 : skip layout
p022:P2 कुत्रापि अहं : clean
p022:P3 किञ्चित्कालानन्तरं नटेशः : clean
p022:P4 अपि नटेशः : F3, F4
p022:P5 एवंरीत्या चत्वारि : clean
p022:P6 तदा नटेशः : clean
p022:P7 अत्र नटेशः : clean
p022:P8 दत्त्वा, केशवः : clean
p022:P9 नटेशस्य वचनं : clean
p022:P10 तदा नटेशः : F5
p023:P1 : skip layout
p023:P2 वेतालः एवं : clean
p023:P3 भवतः शिरः : clean
p023:P4 तदा त्रिविक्रमः : clean
p023:P5 एवंरीत्या यदा : clean
J1 p018:P3 -> p019:P2 {pc} (continues) : ok
J2 p019:P5 -> p019:P6 {pc} (continues) : ok
J3 p019:P9 -> p020:P2 {pc} (continues) : ok
J4 p020:P4 -> p020:P5 fresh (clean break) : ok
J5 p020:P7 -> p020:P8 {pc} (continues) : ok
J6 p020:P9 -> p021:P2 fresh (clean break) : ok
J7 p021:P4 -> p021:P5 fresh (clean break) : ok
J8 p021:P8 -> p022:P2 {pc} (continues) : ok
J9 p022:P7 -> p022:P8 {pc} (continues) : ok
J10 p022:P10 -> p023:P2 fresh (clean break) : ok
J11 p023:P2 -> p023:P3 {pc} (continues) : ok
J12 p023:P5 -> END (clean break) : ok
