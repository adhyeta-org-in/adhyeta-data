## Summary

Two findings, both style: two direct-speech passages were printed with single strokes where era house style uses doubles, and both are corrected to doubles via verdict blocks since reporting verbs plus इति pin speech sense. Open sandhi at word junctions is the consistent house norm, so there are no sandhi findings; proper names are consistent throughout. Transcription was eyes-only with no OCR tool; scan.py orth gave two medium hits, both adjudicated as intentional exclamations (भोः!, महोदय!). Glyph re-checks are impossible with images closed; no words are held.

## Findings

Loc = story page:chunk (lint P numbers) plus anchor words plus word index counted on the deblocked chunk from 1. No corrected-text section: corrections travel as verdict blocks in the story file.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p004:P7 पार्श्वग्रामे देवीदासः w21-w22 | `'एतं पाठयतु'` | `"एतं पाठयतु"` | STY | style | high | direct speech with प्रार्थितवान् plus इति takes doubles; print singles corrected for readability |
| 2 | p006:P6 कस्यचित् सज्जनस्य w10-w15 | `'मार्गे गच्छतः सर्वान् गृहम् आनयति किल।'` | `"मार्गे गच्छतः सर्वान् गृहम् आनयति किल।"` | STY | style | high | scolding speech with तर्जितवती plus इति takes doubles; print singles corrected for readability |

## Patterns

One recurring pattern with two instances: single strokes printed for direct speech, corrected to doubles where speech sense plus इति pins the sort (F1, F2).

## Unverified

None held. Print quirks kept as seen with no block: thought singles ('अग्रे', 'विशारदस्य पुरतः', 'तथैव अस्तु' as mental acceptance via अङ्गीकृत्य), nested inner singles ('महापण्डितैः', 'भवतः गुरुः कः?', 'यः मां', 'तथा न', 'गुरुदक्षिणारूपेण'), open sandhi variants, house spellings with ञ/ङ, and both print exclamations.

## Coverage

p002:P1 {x-com:layout:} : skip layout-only chunk
p002:P2 # पण्डितः : skip title
p002:P3 पूर्वं चण्डीपुरे : clean
p002:P4 विशारदस्य रोदनं, : clean
p002:P5 इदानीं विशारदस्य : clean
p002:P6 चिन्ता। भोजनम्, : clean
p002:P7 एवं स्थिते : clean
p002:P8 तत् श्रुत्वा : clean
p002:P9 संन्यासी तद्दिने : clean
p002:P10 {category: माणवकः} : skip metadata plus page marker
p003:P1 {x-com:layout:} : skip layout-only chunk
p003:P2 जगन्नाथः संन्यासिने : clean
p003:P3 संन्यासी विशारदं : clean
p003:P4 "एतस्य तु : clean
p003:P5 "भवतः वचनं : clean
p003:P6 "अक्षराभ्यासः एव : clean
p003:P7 विशारदः एतत्सर्वं : clean
p003:P8 "पश्यतु। इदानीम् : clean
p004:P1 {x-com:layout:} : skip layout-only chunk
p004:P2 कालः प्राप्तः : clean
p004:P3 जगन्नाथः संस्कृतभाषां : clean
p004:P4 एतेन तीव्रं : clean
p004:P5 "भो! भवान् : clean
p004:P6 "पत्न्याः वचनेषु : clean
p004:P7 पार्श्वग्रामे देवीदासः : F1
p004:P8 प्रार्थितवान्। : clean
p004:P9 तदा देवीदासः : clean
p004:P10 "श्रीमन्! मम : clean
p005:P1 {x-com:layout:} : skip layout-only chunk
p005:P2 "पुत्रस्य अध्ययनविषये : clean
p005:P3 देवीदासस्य वचनैः : clean
p005:P4 अङ्गीकृतं चेत् : clean
p005:P5 अतः देवीदासः : clean
p005:P6 विशारदः आचार्यं : clean
p005:P7 "इतःपरं कोऽपि : clean
p005:P8 विशारदः एतत् : clean
p006:P1 {x-com:layout:} : skip layout-only chunk
p006:P2 सामान्यतः जानाति : clean
p006:P3 तदा विशारदः : clean
p006:P4 तदा सन्तुष्टः : clean
p006:P5 मार्गे विशारदः : clean
p006:P6 कस्यचित् सज्जनस्य : F2
p006:P7 तदा विशारदः : clean
p006:P8 तदा सा : clean
p006:P9 तदा विशारदः : clean
p007:P1 {x-com:layout:} : skip layout-only chunk
p007:P2 तर्कशैल्या वक्तुम् : clean
p007:P3 एतत् श्रुत्वा : clean
p007:P4 'विशारदस्य पुरतः : clean
p007:P5 स्वर्णपुर्यां कवितानन्दः : clean
p007:P6 "एतत् एव : clean
p007:P7 दौर्भाग्यवशात् कवितानन्दः : clean
p007:P8 सः नम्रस्वरेण : clean
p007:P9 'तथैव अस्तु' : clean
p008:P1 {x-com:layout:} : skip layout-only chunk
p008:P2 राजधान्यां तेन : clean
p008:P3 चतुरपादः विशारदम् : clean
p008:P4 विशारदः चतुरपादस्य : clean
p008:P5 चतुरपादः तु : clean
p008:P6 "राजदर्शनं यदि : clean
p008:P7 निश्चयेन राजाश्रयं : clean
p008:P8 तद्दिने एव : clean
p008:P9 "मम नाम : clean
p008:P10 "भवान् तु : clean
p009:P1 {x-com:layout:} : skip layout-only chunk
p009:P2 "गुरोः अनुग्रहेण : clean
p009:P3 यद्यपि महाराजः : clean
p009:P4 "एतत् तु : clean
p009:P5 राजा एतेन : clean
p009:P6 अनन्तरदिने आगतः : clean
p009:P7 एकदिनाभ्यन्तरे एव : clean
p009:P8 "मनः एव : clean
p009:P9 विशारदः राजाश्रयं : clean
p009:P10 यदा विशारदस्य : clean
J1 column-turn : ok (न काऽपि into चिन्ता।, spaced join completes the clause)
J2 page-turn : ok (परिहरिष्यामि इति into जगन्नाथः, clean break with new speaker)
J3 column-turn : ok (जीवतु इति into एतस्य, clean break with speaker change)
J4 page-turn : ok (युक्तः into कालः completes the sannyasi speech)
J5 column-turn : ok (देवीदासं into प्रार्थितवान् completes the verb)
J6 page-turn : ok (जगन्नाथः इति into पुत्रस्य, clean break with speaker change)
J7 column-turn : ok (तथा into अङ्गीकृतं completes the conditional clause)
J8 page-turn : ok (संस्कृतं into सामान्यतः completes the clause)
J9 column-turn : ok (प्राप्तवान् इति into कस्यचित्, clean break scene change)
J10 page-turn : ok (कुर्मः इति into तर्कशैल्या, clean break action follows challenge)
J11 column-turn : ok (महोदय into स्वर्णपुर्यां completes the speech)
J12 page-turn : ok (प्राप्तवान् इति into राजधान्यां, clean break scene change)
J13 column-turn : ok (अहं into निश्चयेन completes the oath sentence)
J14 page-turn : ok (राजा इति into गुरोः, clean break question answered)
J15 column-turn : ok (महाराज into एकदिनाभ्यन्तरे completes the speech)
J16 page-end : ok (END clean break)
