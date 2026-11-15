# Proofread report — 1986_03 p002 (scans 2–6, समस्यापरिहारः)

## Summary

Loc below is `pNN:Pm` (scan-sequence page + lint chunk) with the first two words as anchor and the word counted from 1 on the chunk. Severity / confidence follow `error-taxonomy.md`; `*` marks unverified. Four verdict findings (F1–F4, all landed as blocks in the story file) and three held word-level holds (F5–F7, no file change). The systematic issue is print punctuation: one mismatched quote pair and one stray stroke, both resolved for readability. Balanced single-quote spans kept print-faithful throughout (`'ऋणभारः'`, `'सा पेटिका मम न'`, `'एषा समस्या कथं परिहरणीया'`, `'गिरिबालः पेटिकां नीतवान्'`, `'कथञ्चित् सः अन्वेष्टव्यः'`, `'अत्रत्यानि आभरणानि मदीयानि न'`, `'कुञ्चिकां ददातु'` twice): sense does not force doubles there. No verse in range; orth scanner run once with one hit (F3). Images stayed closed all phase.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p004:P6 तदा रक्षकभटाः w5 | `'{sug-ins:'}भवत्सु ... निर्णेष्यति"` | `{del:'}{ins:"}भवत्सु` | STY | error | high | single open with double close cannot pair; direct speech with उक्तवन्तः and iti-close takes the house double sort |
| 2 | p003:P8 "वयं क्षणमात्रेण w11 | `इति' उक्त्वा` | `इति{del:'} उक्त्वा` | STY | likely | high | stray single stroke between इति and उक्त्वा serves no grammatical role; Phase A verified the stroke at 3x and flagged it on file |
| 3 | p006:P2 समीपे एव w8 | `गिरिबाळः` | `{del:गिरिबाळः}{ins:गिरिबालः}` | CNS | error | high | ळ once against ल five times; orth scanner flags the non-classical letter; proper nouns stay consistent |
| 4 | p006:P7 गिरिबालः तृप्त्या w11 | `निन्दोषित्वम्` | `{del:निन्दोषित्वम्}{ins:निर्दोषित्वम्}` | SPL | error | high | न्द/र्द ligature slip; निर्दोषित्वं in the next speech confirms र्द; print षित्व kept in both |
| 5 | p002:P3 पूर्वं कस्मिंश्चित् w19 | `बहुत्र ऋणं` | `?` | LEX | likely | low* | बहुत्र is not a standard word where sense wants बहु or बहुशः |
| 6 | p003:P4 यदा शाकटिकः w12 | `उपवेशितवान्` | `?` | MRP | likely | low* | causative stem of विश् expects वेशय (उपवेशयितवान्); possibly a dropped य or an analogical stem |
| 7 | p005:P9 गिरिबालस्य गमनानन्तरं w12 | `क्षाम्यतु` | `?` | MRP | likely | low* | क्षम् imperative expects क्षमताम्; क्षाम्य-formation possibly Epic |

## Unverified

- F5 `बहुत्र`: glyphs certain (no block), lexicon uncertain. Settles by collating another print of this story or a pandit ruling on बहुत्र.
- F6 `उपवेशितवान्`: stem uncertain. Settles by a grammar check of the causative stem (वेशय vs वेशित) against a dictionary.
- F7 `क्षाम्यतु`: form uncertain. Settles by a dictionary check for Epic क्षाम्यति attestation.

## Coverage

- p002:P1 {x-com:layout} : skip layout-only chunk
- p002:P2 # समस्यापरिहारः : skip title chunk
- p002:P3 पूर्वं कस्मिंश्चित् : F5
- p002:P4 ग्रामात् किञ्चिद्दूरे : clean
- p002:P5 अस्मि। कृपया : clean
- p002:P6 गिरिबालः अपि : clean
- p002:P7 तस्य मौनं : clean
- p002:P8 "उपचारवचनानि किमर्थम्? : clean
- p002:P9 {author: भामहः} : skip metadata chunk
- p003:P1 {x-com:layout} : skip layout-only chunk
- p003:P2 पेटिकां कृपया : clean
- p003:P3 तत्समये शाकटिकः : clean
- p003:P4 यदा शाकटिकः : F6
- p003:P5 यदा शकटेन : clean
- p003:P6 तत् वचनं : clean
- p003:P7 वान् --- : clean
- p003:P8 "वयं क्षणमात्रेण : F2
- p003:P9 तदा झटिति : clean
- p003:P10 "अहं किं : clean
- p003:P11 "भवतः पेटिकायाः : clean
- p003:P12 तदा शाकटिकः : clean
- p003:P13 किङ्कर्तव्यतामूढः गिरिबालः : clean
- p004:P1 {x-com:layout} : skip layout-only chunk
- p004:P2 उक्त्वा रक्षकभटाः : clean
- p004:P3 रक्षकभटाः गिरिबालस्य : clean
- p004:P4 गिरिबालः कम्पमानस्वरेण : clean
- p004:P5 तदा वृद्धः : clean
- p004:P6 तदा रक्षकभटाः : F1
- p004:P7 भटप्रमुखः शाकटिकं : clean
- p004:P8 "एतौ अद्य : clean
- p004:P9 गृहं गतस्य : clean
- p005:P1 {x-com:layout} : skip layout-only chunk
- p005:P2 तस्य पत्नी : clean
- p005:P3 भटप्रमुखः प्रवृत्तं : clean
- p005:P4 तस्य पत्नी : clean
- p005:P5 अनन्तरदिने भटप्रमुखः : clean
- p005:P6 लब्धानि। अतः : clean
- p005:P7 "निरपराधित्वे सिद्धे : clean
- p005:P8 "प्रथमम् इतः : clean
- p005:P9 गिरिबालस्य गमनानन्तरं : F7
- p005:P10 'गिरिबालः पेटिकां : clean
- p006:P1 {x-com:layout} : skip layout-only chunk
- p006:P2 समीपे एव : F3
- p006:P3 {x-com: गिरिबाळः} : skip note-only chunk
- p006:P4 "अये महाशय! : clean
- p006:P5 तदा भटप्रमुखः : clean
- p006:P6 "एषः एव : clean
- p006:P7 गिरिबालः तृप्त्या : F4
- p006:P8 {x-com: निन्दोषित्वम्} : skip note-only chunk
- p006:P9 भटप्रमुखः गिरिबालस्य : clean
- p006:P10 "उद्योगान्वेषणार्थं प्रस्थितस्य : clean
- J1 p002:P3 {pb} -> p002:P4 fresh : ok
- J2 p002:P4 {pb} -> p002:P5 {pc} : ok
- J3 p002:P8 {pb} -> p003:P2 {pc} : ok
- J4 p003:P6 {wb} -> p003:P7 {pc} : ok
- J5 p003:P13 {pb} -> p004:P2 fresh : ok
- J6 p004:P9 {pb} -> p005:P2 {pc} : ok
- J7 p005:P5 {pb} -> p005:P6 {pc} : ok
- J8 p005:P10 {pb} -> p006:P2 fresh : ok
- J9 p006:P10 {pb} -> END : ok
