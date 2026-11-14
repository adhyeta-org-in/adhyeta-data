# Proofread report: 1986_01 p046 (राजसत्कारः, scans 46-48)

## Summary

Three findings on this three-page span: two high-confidence verdicts (SPL स/ष correction, OCR dropped-इ insertion) and one held SPL candidate for the non-word odd cluster. No systematic repeats, so no Patterns section. Quote sorts are print-correct throughout (doubles for speech, singles for the भावना thought); sandhi openness variants and folio ६१ on p047 kept as house style. Text was transcribed by eye from print (not OCR); `scan.py orth` on deblocked text returns zero hits. Loc below is `pNN:Pm` (scan sequence + lint chunk) with `wN` counting plain words on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p047:P8 w17 (प्रभो! सत्यनिष्ठस्य) `उद्योगतः निस्कासयति` | `उद्योगतः निष्कासयति` | SPL | error | high | षत्व after निस् before क requires ष; निष्कासयति (expel) is the verb, स is mis-set |
| F2 | p047:P14 w4 (महाराज! अत्र) `सभायाम् उपस्थताः` | `सभायाम् उपस्थिताः` | OCR | error | high | उपस्थिताः (present) agrees with सर्वे महिषाः; उपस्थताः is a non-word with dropped ि |
| F3 | p048:P6 w24 (भोजनविषये अपि) `वज्झनादिकं करणीयम्` | `वर्जनादिकं करणीयम्` | SPL | error | low* | वज्झनादिकं is a non-word with odd ज्झ cluster; tongue-restraint sense needs avoidance वर्जनादिकं, but fasting लङ्घनादिकं also fits, so held |

Filed as blocks in the story file: `{del:निस्कासयति}{ins:निष्कासयति}`, `{del:उपस्थताः}{ins:उपस्थिताः}`, `{sug-del:वज्झनादिकं}{sug-ins:वर्जनादिकं}{x-com: ...}`. Kept as print-faithful without blocks: open-sandhi variants (`अग्रजः भ्रातृजाया`, `गोविन्दः निवसति`, `तदनन्तरं` beside `तद्दिने`), final-म्/ं spellings (`पत्नीं`, `पदव्यां`), hyphenated compounds (`शारीरिक-श्रमस्य`, `अग्रज-भ्रातृजाययोः`, `द्वितीयप्रश्नं`, `दशजनाः`), consistent `सुवर्णनाणकं`, folio `{pgb: ६१}` on p047, and all quote sorts (doubles speech incl. short `भीत्या`/`स्वजीविकायै`, singles thought `'किमर्थं...करणीया?'`).

## Unverified

- F3 (`वज्झनादिकं`, p048:P6, भोजनविषये अपि, w24): held spelling candidate; widened window tested वर्जनादिकं (avoidance etc. for tongue-restraint) against लङ्घनादिकं (fasting etc. for sweets-habit), neither fits uniquely at word level. Settles with: scan reopen at 5x+ to check र्ज vs ज्झ glyphs, or another copy of 1986_01.

## Coverage

p046:P1 {x-com:layout:} : skip (layout chunk)
p046:P2 राजसत्कारः : skip (title)
p046:P3 रामपुरे गोविन्दः : clean
p046:P4 गोविन्दः स्वमत्यानुगुणं : clean
p046:P5 ग्रामीणैः क्रियमाणां : clean
p046:P6 {pc}गच्छेत्? इति। : clean
p046:P7 तदा गोविन्दस्य : clean
p046:P8 अग्रज-भ्रातृजाययोः सम्भाषणं : clean
p046:P9 युगादिमहोत्सवः समीपम् : clean
p046:P10 युगादेः पूर्वदिने : clean
p046:P11 {note:} : skip (footer metadata)
p047:P1 {x-com:layout:} : skip (layout chunk)
p047:P2 {pc}भागग्रहीतारः एकत्र : clean
p047:P3 राजा विजयपालः : clean
p047:P4 "लक्षजनाः स्युः" : clean
p047:P5 अन्यः उक्तवान् : clean
p047:P6 तदा गोविन्दः : clean
p047:P7 "कथम् एवं : clean
p047:P8 "प्रभो! सत्यनिष्ठस्य : F1
p047:P9 "पत्नी किमर्थं : clean
p047:P10 "भीत्या" इति : clean
p047:P11 एतेन उत्तरेण : clean
p047:P12 {pc}"अस्तु, इदानीं : clean
p047:P13 "अहम् आकाशे : clean
p047:P14 "महाराज! अत्र : F2
p047:P15 एवं किञ्चित्कालपर्यन्तं : clean
p047:P16 विजयपालः पूर्वपरम्परानुगुणं : clean
p048:P1 {x-com:layout:} : skip (layout chunk)
p048:P2 {pc}अपि व्यवस्थां : clean
p048:P3 सभाविसर्जनानन्तरं पुरस्कारत्वेन : clean
p048:P4 गोविन्दस्य एषः : clean
p048:P5 तदा गोविन्दः : clean
p048:P6 {pc}भोजनविषये अपि : F3
p048:P7 "मया यत् : clean
p048:P8 "न, महाप्रभो! : clean
p048:P9 गोविन्दस्य सद्बुद्धिं : clean
J1 p046:P5 {pb} -> p046:P6 {pc} (continues) : ok (न गच्छेत्? split, speech balanced DQ=2 across logical para)
J2 p046:P10 {pb} -> p047:P2 {pc} (continues) : ok (कार्यक्रमे भागग्रहीतारः, locative + subject)
J3 p047:P11 {pb} -> p047:P12 {pc} (continues) : ok (उक्तवान् --- "अस्तु, reporting verb + speech)
J4 p047:P16 {wb} -> p048:P2 {pc} (continues) : ok (भोजनकूटस्य अपि व्यवस्थां, genitive + particle; {wb} kept as printed, read spaced)
J5 p048:P5 {pb} -> p048:P6 {pc} (continues) : ok (दत्तवान्। भोजनविषये, same speech next sentence, single logical para DQ=2)
J6 p048:P9 {pb} -> END (clean break) : ok (story conclusive नियोजितवान्।)
