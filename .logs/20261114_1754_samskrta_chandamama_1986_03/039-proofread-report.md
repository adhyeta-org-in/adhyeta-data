# Proofread report: 1986_03 p039 (चाणक्यकथा, scans 39–44)

## Summary

Range scans 39–44 hold the first instalment of चाणक्यकथा (to be continued). 7 findings: 4 high-confidence verdicts already landed as blocks (2 print-composition spellings, 2 defective quote marks) and 3 held sug candidates for the user. Loc below is `pNN:Pm` (NN = scan number, Pm = lint chunk in that span) plus anchor words. Systematic issues are intrusive/extra print sorts with no grammatical parse and mixed quote sorts that print itself uses inconsistently, kept as seen. No passage was skipped and the text is manual transcription, not OCR. Orth scanner (`scan.py orth`) on deblocked text returned zero hits.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p040:P5 अपि तु | `एकैकस्मिन् आसने` | `एकस्मिन्` | SPL | error | high | ै verified at 3x but एकैकस्मिन् is no word; स्थापयित्वा takes एकस्मिन् आसने |
| F2 | p043:P4 एतेन चाणक्यस्य | `हिमवत्पर्वन्तं गत्वा` | `हिमवत्पर्वतम्` | SPL | error | high | न्त verified at 2x but पर्वन् is no stem here; हिमवत् + पर्वतम् is certain |
| F3 | p041:P7 भवान् महाराजः | `नीतवान्। 'चन्द्रगुप्तस्य` | delete `'` | STY | error | high | single open verified at 2x with no mate in the para; passage is narration, not speech or thought |
| F4 | p042:P7 अत्रान्तरे अन्यः | `'भोः! ... प्रेषितवान्"` | `"` for opening `'` | STY | error | high | single open against double close is mechanically defective; spoken utterance takes doubles |
| F5 | p039:P5 चणी ऐहिकसुखेषु | `एव किञ्च राजपदव्याम्` | `किञ्चन` | SPL | likely | medium* | किञ्च verified at 3x but is no word; किञ्चन or किञ्चित् both fit |
| F6 | p040:P7 'अन्यद्वारा राज्यशासनं | `प्रतिनिधिवेन राज्यपालनं` | `प्रतिनिधिना` | MRP | likely | medium* | वेन is no instrumental ending; deputy sense points to प्रतिनिधिना |
| F7 | p044:P2 आलये स्थितान् | `विग्रहान् निर्गतवान्। निष्कासितवन्तः` | delete `निर्गतवान्।` | AGR | likely | medium* | singular participle with plural मूढाः पौराः plus synonymous plural verb reads as anticipatory doublet |

## Patterns

- Nasal-spelling variation kept as print (3): काञ्चित् (p039:P7), कांश्चन (p041:P3), कञ्चित् (p042:P8).
- Open sandhi kept as house style (5): यत् नन्दराजं (p043:P4), तत् नगरं (p044:P3), तत् अहं (p041:P8), एतत् आक्रमणं (p041:P8), तावत् आक्रमणं (p043:P7).
- Mixed quote sorts kept as print: thought in doubles ("भोगभाग्येषु...करोमि" p039:P5, "एषः विधेयः...व्यवहरिष्यति" p042:P6) and speech in singles ('महाराज! मह्यं किमपि ददातु' p041:P4, 'एवं कथने किं कारणम्' p043:P2); print varies, so sense does not pin a re-sort.
- चन्द्र/चन्द्र spelling kept as print (1): चन्द्रम् (p041:P2) against चन्द्रं/चन्द्ररसः elsewhere.

## Unverified

- F5 किञ्चन vs किञ्चित्: a dictionary or the next instalment's usage would settle it; chosen किञ्चन for "any at all" sense.
- F6 प्रतिनिधिना: no dictionary checked; alternatives such as प्रतिनिधिरूपेण are longer shots against the glyphs.
- F7 निर्गतवान्। deletion: settling needs the editor's eye on whether print really lacks agreement or means निर्गतान्; pure deletion is the minimal hypothesis.

## Coverage

p039:P1 {x-com:layout:} : skip layout chunk
p039:P2 # चाणक्यकथा : skip title
p039:P3 पूर्वं चणकनामके : clean
p039:P4 चाणक्यस्य जन्म : clean
p039:P5 चणी ऐहिकसुखेषु : F5
p039:P6 पुत्रस्य शिशोः : clean
p039:P7 चाणक्यः क्रमशः : clean
p039:P8 कदाचित् चाणक्यस्य : clean
p039:P9 एतेन अपमानिता : clean
p039:P10 {note:} : skip footer note
p040:P1 {x-com:layout:} : skip layout chunk
p040:P2 दुःखस्य कारणं : clean
p040:P3 तदानीं पाटलीपुत्रं : clean
p040:P4 किञ्चित्कालानन्तरं नन्दराजः : clean
p040:P5 अपि तु : F1
p040:P6 तदा चाणक्यः : clean
p040:P7 'अन्यद्वारा राज्यशासनं : F6
p040:P8 आरब्धवान्। एवम् : clean
p040:P9 तद्ग्रामीणाः महाराजस्य : clean
p040:P10 "यदि एतस्याः : clean
p040:P11 चाणक्यः एतदर्थम् : clean
p041:P1 {x-com:layout:} : skip layout chunk
p041:P2 तस्य छदिकायां : clean
p041:P3 एतदनन्तरं चाणक्यः : clean
p041:P4 चाणक्यः बालस्य : clean
p041:P5 "ब्राह्मणोत्तम! तत्र : clean
p041:P6 इतरबालकानां द्वारा : clean
p041:P7 भवान् महाराजः : F3
p041:P8 चाणक्यः आत्मना : clean
p041:P9 चन्द्रगुप्तं चाणक्यं : clean
p042:P1 {x-com:layout:} : skip layout chunk
p042:P2 आश्रितवान्। स्वयं : clean
p042:P3 कश्चन अश्वारोही : clean
p042:P4 सः सैनिकः : clean
p042:P5 अनन्तरं चाणक्यः : clean
p042:P6 इति। "भवतः : clean
p042:P7 अत्रान्तरे अन्यः : F4
p042:P8 बुभुक्षया पीडितौ : clean
p043:P1 {x-com:layout:} : skip layout chunk
p043:P2 तदा सा : clean
p043:P3 "अन्नं यदा : clean
p043:P4 एतेन चाणक्यस्य : F2
p043:P5 एतदनुसारं चाणक्यः : clean
p043:P6 जेतव्यम्?' इति : clean
p043:P7 सः संन्यासिनः : clean
p044:P1 {x-com:layout:} : skip layout chunk
p044:P2 आलये स्थितान् : F7
p044:P3 तद्दिने एव : clean
p044:P4 अनन्तरं चाणक्यः : clean
p044:P5 एतदनुगुणं नन्दः : clean
p044:P6 निर्गतवान्। यदा : clean
p044:P7 पितुः वचनं : clean
p044:P8 {misc:} : skip footer note
J1 p039:P5 {pb} -> p039:P6 {pc} : ok
J2 p039:P9 {pb} -> p040:P2 {pc} : ok
J3 p040:P4 {pb} -> p040:P5 fresh : ok
J4 p040:P7 {pb} -> p040:P8 {pc} : ok
J5 p040:P11 {pb} -> p041:P2 {pc} : ok
J6 p041:P6 {pb} -> p041:P7 {pc} : ok
J7 p041:P9 {pb} -> p042:P2 {pc} : ok
J8 p042:P5 {pb} -> p042:P6 {pc} : ok
J9 p042:P8 {pb} -> p043:P2 fresh : ok
J10 p043:P5 {pb} -> p043:P6 {pc} : ok
J11 p043:P7 {pb} -> p044:P2 {pc} : ok
J12 p044:P5 {pb} -> p044:P6 {pc} : ok
J13 p044:P7 {pb} -> END : ok
