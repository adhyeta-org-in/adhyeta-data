# Proofread report: 1984_08 p020 (वैद्यस्य त्वरा)

## Summary

5 findings: 1 error (SPL print slip मविष्यति for भविष्यति) and 4 style (STY quote-sort modernizations, singles to doubles for two reported speeches). Loc is story coordinates pNN:Pm with word counted on the chunk from 1, blocks ignored. The systematic issue is print using single quotes for spoken dialogue where modern readability wants doubles; the nested belief-quote inside P7 correctly stays single. No passages left unchecked; the text is a print transcription, not OCR output (orth scan clean, 0 hits).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p020:P6 [एतत्सर्वं दृष्ट्वा] w7 | `'वैद्याचार्य!` | `"वैद्याचार्य!` | STY | style | high | reported speech takes doubles; singles mark thought or nested speech |
| 2 | p020:P6 [एतत्सर्वं दृष्ट्वा] w19 | `एव' इति` | `एव" इति` | STY | style | high | close must match the opened double; iti-closure pins speech |
| 3 | p020:P7 [वैद्यः शिरः] w6 | `'श्रद्धां` | `"श्रद्धां` | STY | style | high | reported speech takes doubles; reporting verb plus iti pins it |
| 4 | p020:P7 [वैद्यः शिरः] w47 | `किल?' इति` | `किल?" इति` | STY | style | high | close must match the opened double; iti-closure pins speech |
| 5 | p020:P7 [वैद्यः शिरः] w19 | `मुक्तः मविष्यति एव` | `मुक्तः भविष्यति एव` | SPL | error | high | भविष्यति is the भू-future; मविष्यति is not a word (म/भ print slip) |

## Patterns

Print singles-for-speech modernized to doubles: 4 blocks across 2 speeches (P6 villagers' praise F1-F2, P7 vaidya's cynical reply outer F3-F4); inner belief-quote 'मम औषधेन एव रोगात् मुक्तः अहम्' kept single as correct nesting.

## Unverified

None. All findings high confidence; no dictionary check needed (quote sorts pinned by reporting verbs and iti; भविष्यति is elementary morphology).

## Coverage

p020:P1 {x-com:layout} : skip layout
p020:P2 वैद्यस्य त्वरा : skip title
p020:P3 वैद्यः कश्चित् : clean
p020:P4 श्रवणसमनन्तरम् एव : clean
p020:P5 त्वरितगत्या गृहम् : clean
p020:P6 एतत्सर्वं दृष्ट्वा : F1, F2
p020:P7 वैद्यः शिरः : F3, F4, F5
J1 p020:P7 {pb} -> END : ok (clean break)
