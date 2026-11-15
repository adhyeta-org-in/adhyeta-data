# Proofread report: 1987_06 p002 (pages 2-6, उपकारी वामनः)

## Summary

4 findings (3 error, 1 style) plus 1 unverified hold; systematic problem is mis-set akṣaras in print (dropped anusvara F2, wrong vowel F3). One word (माग्यता, U1) could not be settled from text alone and is held with hypotheses; scans stayed closed throughout Phase B. Text is human transcription from scans, not OCR output; `scan.py orth` on deblocked text reports zero hits. Loc uses story coordinates `pNN:Pm` (NN = scan sequence, Pm = chunk number matching lint `P` numbers) with the chunk's first two words as anchor and the finding's word index counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p002:P9 (कृषकं दृष्ट्वा) w13 | सञ्जातः। " चलितुं | delete the re-opened `"` | STY | style | high | one speech carries one pair; print re-opens doubles on the continued line with no closing mark before it |
| 2 | p004:P7 (कृषकः कुतूहलेन) w4 | तत् कास्यपात्रं | `तत् कांस्यपात्रं` | OCR | error | high | कास्य is not a word; कांस्यपात्र is the story's vessel term everywhere else |
| 3 | p005:P9 (कृषकस्य समीपम्) w7 | किं भोः कृषिकमहोदय | `कृषकमहोदय` | OCR | error | high | कृषिक is not a word; the dwarf addresses the farmer कृषक throughout |
| 4 | p005:P3 (अनन्तरक्षणे तस्मात्) w19 | रजतमयानि च नाणकानिः | `नाणकानि` | MRP | error | high | नाणकानिः is no valid form; the twin adjectives सुवर्णमयानि रजतमयानि pin neuter plural |

## Patterns

Print mis-set akṣaras (2 instances): dropped anusvara (F2, कास्य for कांस्य) and wrong vowel (F3, कृषिक for कृषक); both corrected via `{del:}`/`{ins:}` verdicts since story context pins the form and the print reading was verified in Phase A.

## Unverified

| # | Loc | Original | Candidates | What would settle it |
|---|---|---|---|---|
| U1 | p002:P4 (किन्तु एतस्य) w6 | भूमिः न माग्यता | माग्यत (passive of माग्, land found no taker)? or a fuller misprint? | a sharper scan look (out of scope: images closed) or another edition; माग्यता is no Sanskrit word but no single fix is certain |

## Kept as printed (no block)

मत्पत्नीपुत्रैः (valid instrumental मत् + पत्नी + पुत्राः, agent of पूरणीयम्); अन्तर्भागतः (parses as adjective agreeing with सङ्गीतध्वनिः); singles for thought and hearsay ('प्रयत्नेन...शक्येत', 'कृषकस्य...अस्ति', 'एतत्...वशीकरणीयम्') and the nested 'कांस्यपात्र!...करोतु' inside its " span, all valid sort usage; onomatopoeia खड्गु खड्गु and हूँकुर्वन्तौ; open sandhi and house spellings throughout; `{category: माणवकः}` kept with print's quotation marks dropped from the node.

## Coverage

p002:P1 {x-com: : skip layout-only chunk; p002:P2 # उपकारी : skip title chunk; p002:P3 पूर्वं कस्मिंश्चित् : clean; p002:P4 किन्तु एतस्य : U1; p002:P5 एवं स्थिते : clean; p002:P6 यावत् वा : clean; p002:P7 वृषभम् अपि : clean; p002:P8 यदा सः : clean; p002:P9 कृषकं दृष्ट्वा : F1; p002:P10 कृषकः वामनस्य : clean; p002:P11 एतत् श्रुत्वा : clean; p002:P12 {category: : skip metadata chunk.
p003:P1 {x-com: : skip layout-only chunk; p003:P2 शोचनीयतां प्राप्नुयात्। : clean; p003:P3 एतत् वचनं : clean; p003:P4 एवं प्रयाणं : clean; p003:P5 कृषकः वामनस्य : clean; p003:P6 कांस्यनिर्मितं जलपात्रम्। : clean; p003:P7 कृषकाय तत् : clean; p003:P8 एतत् श्रुत्वा : clean; p003:P9 वामनः उच्चैः : clean.
p004:P1 {x-com: : skip layout-only chunk; p004:P2 वदन् तस्य : clean; p004:P3 अनन्तरक्षणे तस्य : clean; p004:P4 तन्नाम सङ्गीतश्रवणेन : clean; p004:P5 तदा सः : clean; p004:P6 गृहं गत्वा : clean; p004:P7 कृषकः कुतूहलेन : F2; p004:P8 सः वञ्चकः : clean.
p005:P1 {x-com: : skip layout-only chunk; p005:P2 कांस्यपात्रस्य आवरणम्। : clean; p005:P3 अनन्तरक्षणे तस्मात् : F4; p005:P4 कृषकगृहसदस्याः अद्यावधि : clean; p005:P5 सर्वथा न : clean; p005:P6 निर्धनेन कृषकेण : clean; p005:P7 एकदा सः : clean; p005:P8 एवं कृषकः : clean; p005:P9 कृषकस्य समीपम् : F3; p005:P10 कृषकः प्रवृत्तं : clean.
p006:P1 {x-com: : skip layout-only chunk; p006:P2 वृक्षकोटरतः एकं : clean; p006:P3 कृषकस्य चलनवलनं : clean; p006:P4 एतत् पात्रम् : clean; p006:P5 कृषकः यदा : clean; p006:P6 कृषकः स्ववेषेण : clean; p006:P7 सर्वेषां पुरतः : clean; p006:P8 तदा कुरूपिणौ : clean; p006:P9 वेदनाम् असहमानः : clean; p006:P10 कृषकः तु : clean; p006:P11 धनिकः धावन् : clean; p006:P12 अनन्तरं केषुचित् : clean.
J1 p002:P6->P7 {pb}/{pc} एकं+वृषभम् : ok; J2 p002:P11->p003:P2 {pb}/{pc} परिस्थितिः+शोचनीयतां : ok; J3 p003:P5->P6 {pb}/{pc} तत्+कांस्यनिर्मितं : ok; J4 p003:P9->p004:P2 {pb}/{pc} इति+वदन् : ok; J5 p004:P5->P6 {pb}/{pc} भवान्+गृहं : ok; J6 p004:P8->p005:P2 {pb}/{pc} च+कांस्यपात्रस्य : ok; J7 p005:P4->P5 {pb}/{pc} दारिद्र्यं+सर्वथा : ok; J8 p005:P10->p006:P2 {pb}/{pc} गत्वा+वृक्षकोटरतः : ok; J9 p006:P6->P7 {pb}/{pc} रजतपात्रं+सर्वेषां : ok; J10 p006:P12->END {pb} : ok (range end on a clean break; the story continues in the next range).
