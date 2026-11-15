## Summary

Six findings: three errors, two likely, one style. Print doubles every speech closer (transcribed single per the era two-strokes-one-mark rule and documented in page x-coms); open sandhi at word junctions is the consistent house norm, so there are no sandhi findings. Two low-confidence words are held as suggestion pairs with blocks for the user. Transcription was eyes-only with no OCR tool; scan.py orth gave one medium hit, adjudicated as an intentional exclamation. Glyph re-checks are impossible with images closed; J4 carries {pc} after a terminal edge with a speaker change and is kept per the no-strip rule for coordinator re-check.

## Findings

Loc = story page:chunk (lint P numbers) plus anchor words plus word index counted on the deblocked chunk from 1; block spans cite the preceding word. No corrected-text section: corrections travel as verdict blocks in the story file.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p002:P4 कापालिका महाशिलयोः w22 | `पुच्छे निलीनम् आसीत्` | `पुच्छे निलीनः आसीत्` | AGR | likely | medium* | participle must agree with the masculine subject |
| 2 | p008:P2 मम कार्यं span-after-w4 | `भवतो कालनागेन` | `भवती कालनागेन` | MRP | error | high | vocative to the feminine addressee needs भवती |
| 3 | p008:P5 कार्यं तु span-after-w17 | `प्रन्थिम् आकृष्य` | `ग्रन्थिम् आकृष्य` | SPL | error | high | प्रन्थि is no word; the pulled knot is ग्रन्थि |
| 4 | p009:P8 चन्द्रवर्मा रज्जुं span-after-w47 | `उद्धतं मरोवरस्य जलं` | `उद्धतं सरोवरस्य जलं` | OCR | error | high | dropped initial स; सरोवरः stands twice before |
| 5 | p005:P6 अत्रयं युद्धम् w1 | `अत्रयं युद्धम्` | `अत्रस्थं युद्धम्` | SPL | likely | low* | अत्रयं parses as nothing; tried अत्र यत्, अत्र यं, एतत् below |
| 6 | p006:P5 ज्ञातुं शक्यते w13 | `गौरवं सूचितवान्!` | `सूचितवान्! (keep as is)` | STY | style | medium | print exclamation kept as emphatic stop |

## Unverified

F1 निलीनम्/निलीनः: the fix is grammatically certain but the print reading rests on a 2x transcription (म्/ः confusion possible); settled by a 3x re-view of scan 2. F5 अत्रयं: tried segmentations are अत्रस्थं (locational adjective, best sense), अत्र यत् (relative without clean correlative), अत्र यं (doubles the object), एतत् (no glyph similarity); settled by user ruling. Print quirks kept as seen with no block: doubled closers normalized to single (x-com on p003), extra colon after गच्छावः, short stop after आनीता इति, इति inside quotes twice (p004:P6, p007:P5), commas after विशाला/परीक्ष्य/स्म, detached specks omitted (तदा and उक्तवती interpuncts, lone stroke after ज्ञाता, speck after अस्ति एव).

## Coverage

p002:P1 {x-com:layout:} : skip layout-only chunk
p002:P2 # कांस्य-दुर्गम् : skip title
p002:P3 [भेरुण्डपक्षिणः पुच्छे : clean
p002:P4 कापालिका महाशिलयोः : F1
p002:P5 चिन्तितवान् चन्द्रवर्मा। : clean
p003:P1 {x-com:layout:} : skip layout-only chunk
p003:P2 तस्याः शरीरं : clean
p003:P3 तदा कापालिका : clean
p003:P4 चन्द्रवर्मा हस्तसाहाय्येन : clean
p003:P5 स्थितिः केनापि : clean
p003:P6 चन्द्रवर्मा जागरूकतया : clean
p003:P7 गुहायाः द्वारं : clean
p003:P8 कापालिका गुहां : clean
p003:P9 कापालिका मन्दं : clean
p003:P10 "चन्द्रवर्मन्! पर्वतसमीपे : clean
p003:P11 {x-com: print : skip x-com-only plus page marker
p004:P1 {x-com:layout:} : skip layout-only chunk
p004:P2 "एवं वा? : clean
p004:P3 कापालिका चन्द्रवर्मणः : clean
p004:P4 "एवं तर्हि : clean
p004:P5 तदा कापालिका : clean
p004:P6 "कः सः : clean
p004:P7 कापालिकायाः वचनं : clean
p004:P8 "अये! कापालिके! : clean
p005:P1 {x-com:layout:} : skip layout-only chunk
p005:P2 सन्दर्भः" इति : clean
p005:P3 "मास्तु भोः! : clean
p005:P4 "मान्त्रिकस्य भृत्यम् : clean
p005:P5 अत्रान्तरे अग्निपक्षि-कालनागयोः : clean
p005:P6 "अत्रयं युद्धम् : F5
p005:P7 "तथा किमपि : clean
p005:P8 एतावता अग्निपक्षिणः : clean
p006:P1 {x-com:layout:} : skip layout-only chunk
p006:P2 गृहीतवान् आसीत्। : clean
p006:P3 आनन्दातिरेकेण 'जयतु : clean
p006:P4 कालनागः अत्यायासेन : clean
p006:P5 ज्ञातुं शक्यते : F6
p006:P6 चन्द्रवर्मा प्रीत्या : clean
p007:P1 {x-com:layout:} : skip layout-only chunk
p007:P2 भवान् मानवरूपं : clean
p007:P3 मन्त्रगृहशब्दस्य श्रवणेन : clean
p007:P4 कापालिका अपि : clean
p007:P5 "कः सः : clean
p007:P6 "शङ्खमान्त्रिकः प्रतिदिनं : clean
p007:P7 "तं प्रपाते : clean
p007:P8 "वदामि। समीपम् : clean
p007:P9 चन्द्रवर्मा क्षणकालं : clean
p008:P1 {x-com:layout:} : skip layout-only chunk
p008:P2 मम कार्यं : F2
p008:P3 अरण्यमध्यं गत्वा : clean
p008:P4 गुहायाः समीपम् : clean
p008:P5 "कार्यं तु : F3
p008:P6 अधः पतेत् : clean
p008:P7 कापालिका मन्दहासं : clean
p008:P8 चन्द्रवर्मा कापालिकां : clean
p008:P9 अत्रान्तरे सा : clean
p009:P1 {x-com:layout:} : skip layout-only chunk
p009:P2 सूचितवती --- : clean
p009:P3 चन्द्रवर्मा पर्वतशिखरं : clean
p009:P4 'महामान्त्रिकां कापालिकाम् : clean
p009:P5 अग्रे गत्वा : clean
p009:P6 अत्रान्तरे शङ्खमान्त्रिकः : clean
p009:P7 आकृष्य भवान् : clean
p009:P8 चन्द्रवर्मा रज्जुं : F4
p009:P9 अत्रान्तरे प्रपाते : clean
p009:P10 (अनुवर्तते) : clean
J1 column-turn : ok (इति into चिन्तितवान्, spaced join)
J2 page-turn : ok (पृच्छन् into तस्याः, participle plus verb)
J3 column-turn : ok (आवयोः into स्थितिः, genitive phrase)
J4 page-turn : kept-{pc} (terminal edge plus speaker change; marker retained per no-strip rule, coordinator may re-check print indent)
J5 column-turn : ok (clean break)
J6 column-turn : ok (clean break)
J7 page-turn : ok (योग्यः into सन्दर्भः completes the speech)
J8 column-turn : ok (clean break)
J9 page-turn : ok (कण्ठं into गृहीतवान् completes the verb)
J10 column-turn : ok (इति into ज्ञातुं, same clause)
J11 page-turn : ok (चेत् into भवान्, apodosis follows)
J12 column-turn : ok (clean break)
J13 column-turn : ok (clean break)
J14 page-turn : ok (अहं into मम, same sentence)
J15 column-turn : ok (clean break)
J16 column-turn : ok (आकर्षणेव into अधः, spaced join)
J17 page-turn : ok (मन्दस्वरेण into सूचितवती completes the verb)
J18 column-turn : ok (वेगेन into आकृष्य completes the phrase)
J19 intra-page break : ok (clean break before serial marker)
J20 page-end : ok (END clean break)
