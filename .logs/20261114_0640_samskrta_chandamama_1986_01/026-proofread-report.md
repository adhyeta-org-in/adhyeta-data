# Proofread report: 1986_01 p026 (परिवर्तनम्)

## Summary

Three findings, all STY/style: the print opens three speeches with a single stroke where era house standard and sense demand doubles, corrected in-file via `{del:'}{ins:"}`. The systematic problem is single-open-for-speech (3x: husband twice, neighbour wife once), with matching double closes kept as seen. No passages left unchecked; every sentence read for continuity across all four spans. Text was transcribed from print scans (not OCR); `scan.py orth` on deblocked text returns zero hits.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p027:P2 (अतः इदानीम्) w6 | `आनन्देन 'बहुकालानन्तरम्` | `"` (`{del:'}{ins:"}` in file) | STY | style | high | speech with reporting verb + इति takes doubles; single open is a dropped second stroke |
| F2 | p027:P8 (ताम् अनुसृत्य) w5 | `गृहिणी 'ततः अपि` | `"` (`{del:'}{ins:"}` in file) | STY | style | high | neighbour-wife speech closed with `"` on p028 takes double open; page-turn continuation never forced closed |
| F3 | p029:P5 (तस्याः वचनानि) w5 | `गोविन्दनाथः 'भवत्याः` | `"` (`{del:'}{ins:"}` in file) | STY | style | high | husband's reply closed with `"` in same chunk takes double open; sense certain from reporting verb + इति |

## Patterns

- Single-open for double-speech (3x: F1 p027:P2, F2 p027:P8, F3 p029:P5). Print shows one stroke where doubles are expected; closes are all doubles. Corrected sorts only; closes and all balanced thought-singles left as seen.

## Unverified

- `प्रप्रथमं` (p027:P5, तदा स्वीयविषये, w12): printed doubling of `प्र` reads as dittography for `प्रथमं`, but no Phase A glyph note is on file and both shapes live at print resolution. No block. Settles with: scan reopen at 5x+ or another copy of 1986_01.
- `यवागूः पतिताः` (p027:P7, इदानींतनदिनेषु sentence): feminine singular subject with plural-looking `पतिताः` where `पतिता` is expected; no Phase A glyph note, and sandhi/visarga speckle cannot be ruled from text. No block. Settles with: scan reopen at 5x+ or dictionary/usage check of `पतिताः` as variant.

## Coverage

p026:P1 {x-com:layout: : skip (layout declaration)
p026:P2 परिवर्तनम् : skip (title)
p026:P3 सोदरीपुरम् इति : clean
p026:P4 गच्छति काले : clean
p026:P5 आनन्दवती जानाति : clean
p026:P6 गोविन्दनाथः ग्रामे : clean
p026:P7 एवं पर्यालोच्य : clean
p026:P8 एतेन गोविन्दनाथस्य : clean
p026:P9 {author: भामहः} : skip (footer metadata)
p027:P1 {x-com:layout: : skip (layout declaration)
p027:P2 अतः इदानीम् : F1
p027:P3 पति व्यवहारज्ञः : clean
p027:P4 एवंरीत्या कानिचन : clean
p027:P5 तदा स्वीयविषये : clean
p027:P6 आनन्दवत्याः गृहस्य : clean
p027:P7 इदानींतनदिनेषु एतस्याः : clean
p027:P8 ताम् अनुसृत्य : F2
p028:P1 {x-com:layout: : skip (layout declaration)
p028:P2 महान्तं कोलाहलं : F2
p028:P3 एवंरीत्या किञ्चित्कालं : clean
p028:P4 एतत्सर्वं श्रुत्वा : clean
p028:P5 एवंरीत्या प्रातिवेशिकानाम् : clean
p028:P6 काकतालीयन्यायेन तस्मिन् : clean
p028:P7 विचारः एव : clean
p028:P8 कर्मकरी गङ्गा : clean
p028:P9 रङ्गः किञ्चित् : clean
p029:P1 {x-com:layout: : skip (layout declaration)
p029:P2 कस्मिन् क्षणे : clean
p029:P3 आनन्दवती स्वपुत्राणां : clean
p029:P4 सत्कीर्तिं सम्पादयितुम् : clean
p029:P5 तस्याः वचनानि : F3
p029:P6 पत्युः वचनं : clean
p029:P7 अनन्तरं शीघ्रम् : clean
J1 p026:P5 {pb} -> p026:P6 {pc} : ok (column turn, spaced join स्वीयपतिः गोविन्दनाथः)
J2 p026:P8 {pb} -> p027:P2 fresh : ok (clean break, page turn, new episode)
J3 p027:P4 {pb} -> p027:P5 fresh : ok (clean break, column turn, several days pass then curiosity)
J4 p027:P8 {pb} -> p028:P2 {pc} : F2 (page turn, speech continues क्रीडन्तः महान्तं, open sort corrected)
J5 p028:P6 {wb} -> p028:P7 {pc} : ok (column turn, solid join आनन्दवतीविचारः)
J6 p028:P9 {pb} -> p029:P2 {pc} : ok (page turn, Ranga speech continues, balanced doubles across)
J7 p029:P4 {pb} -> p029:P5 {pc} : ok (column turn, wife reports then husband replies, text-continuous)
J8 p029:P7 {pb} -> END : ok (clean break, story conclusive with marriage)
