# Proofread report: samskrta_chandamama 1985_06, story p039 (विपरीतः परिणामः, scans 39-40)

## Summary

Story विपरीतः परिणामः spans scans 39-40 in two `{pgb}` sections with 16 body chunks; the proofread gate is green (0 errors, 0 story findings) after 4 Phase B verdicts, 0 held. 4 findings: 2 style (F1, F4 quote-sort verdicts, high) and 2 error (F2, F3 press-misprint verdicts, high); Loc is `pNN:Pm:Wn` (scan-sequence page, lint chunk number, raw whitespace-token index on the file chunk) with the chunk's first two words as anchor. Systematic issues: two sort-mismatched print quote pairs plus two single-glyph press misprints. No OCR was used anywhere (manual transcription from the scans with 3-6x glyph crops in Phase A); the orth scanner had zero hits; all four joints walked clean.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p040:P2:W26 [मन्दभाग्यः स्वयं] | `स्थास्यति" इति` | `स्थास्यति' इति` | STY | style | high | '-thought opened with ' closes with two strokes; sort pinned by चिन्तितवान्...इति |
| 2 | p040:P5:W9 [एतत् दृष्ट्वा] | `विषये अवीव कुपितः` | `विषये अतीव कुपितः` | SPL | error | high | अवीव is not a word; अतीव कुपितः is the idiom (press त/व swap, verified at 3x in Phase A) |
| 3 | p040:P8:W17 [अरे दुष्ट!] | `उच्चरितवान्।` | `उच्चारितवान्।` | SPL | error | high | causative kta of चर् is चारित (उत् + चारित); print drops the आ-length |
| 4 | p040:P9:W7 [मन्त्रिणः एतस्य] | `ज्ञातवान्। "सर्वस्य` | `ज्ञातवान्। 'सर्वस्य` | STY | style | high | thought opened with " closes with '; sort pinned by ज्ञातवान्...इति |

## Patterns

Mismatched print quote sorts (2): SQ-open/DQ-close in the 'सर्वे...स्थास्यति" thought (F1) and DQ-open/SQ-close in the "सर्वस्य...कारणम्' realization (F4); both fixed to singles. Footer reprint note `..'द्वाविंशतिवर्षेभ्यः पूर्वं चन्दमामायां प्रकाशिता कथा"` opens single and closes double: kept as seen with no block (read-only note, sense-neutral stock line). Press misprints (2: F2, F3) corrected by verdict from Phase A 3x glyph records. Open word sandhi stands throughout (मन्दभाग्यः नाम, भवति चेत्, पूर्ववत् एव): house mix of open and joined forms, kept as seen; mid-line hyphen in व्यवहारे-एवं kept as seen. Singles mark thought ('राजाज्ञा पालिता भवेत् एव', 'मन्त्री मम...परीक्षणीयम्'), doubles mark speech: re-derived every mark, no sort changes beyond F1/F4. Proper nouns consistent throughout (मन्दभाग्यः, मन्त्री/मन्त्रिणः); डिण्डिमघोषं/सडिण्डिमघोषं both intended.

## Coverage

p039:P1 skip layout-only chunk. p039:P2 skip title heading. p039:P3 पूर्वं मिथिलायां : clean. p039:P4 एकदा मन्दभाग्यः : clean. p039:P5 उपस्थितः अस्मि : clean. p039:P6 राजपथं परिशीलयतु : clean. p039:P7 स्वेच्छाप्रवृत्तिं न : clean. p039:P8 मन्त्री विनयपूर्वकं : clean. p039:P9 द्वित्राणि दिनानि : clean. p039:P10 skip note/footer chunk. p040:P1 skip layout-only chunk. p040:P2 मन्दभाग्यः स्वयं : F1. p040:P3 चतुर्थे दिने : clean. p040:P4 एतदनन्तरं राजा : clean. p040:P5 एतत् दृष्ट्वा : F2. p040:P6 मन्त्री कः : clean. p040:P7 उत्तररूपेण मन्त्री : clean. p040:P8 अरे दुष्ट! : F3. p040:P9 मन्त्रिणः एतस्य : F4. p040:P10 स्वकीयमूर्खताविषये राजा : clean.

J1 p039:P6 {pb} -> p039:P7 {pc} : ok. J2 p039:P9 {pb} -> p040:P2 {pc} : ok. J3 p040:P5 {pb} -> p040:P6 {pc} : ok. J4 p040:P10 {pb} -> END : ok.
