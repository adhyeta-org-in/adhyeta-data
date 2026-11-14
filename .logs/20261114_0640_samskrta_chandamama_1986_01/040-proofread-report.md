# Proofread report: 1986_01 p040 (मूकः तेमियः, उत्तरार्धम्)

## Summary

Eight findings: six STY/style quote-edge repairs (F1--F6, all `{del:}`/`{ins:}` verdicts in file), one SPL/error print slip (F7, dittography plus dropped sign), and one KRK/likely held candidate (F8, `{sug-}` pair in file). The systematic problem is print mixing `"` and `'` at speech/thought edges (6x); every repair follows the surviving mark (speech takes doubles, thought takes singles), per the p01 precedent. Kept as print-faithful without blocks: `भवति किमपि अवलक्षणं नास्ति इति` climax with nested `'अहं...प्रार्थयामि'"` (balanced DQ/SQ/SQ/DQ after 3x check), short public-utterance singles (`'श्वः आरभ्य...`, `'किमिदं विचित्रं वैभवम्!'`, as in p01's kept taunt-singles), and house forms `रुद्रभूमिम्` (glyph 3x-verified; reads as a desolate-ground coinage fitting the pit-digging scene), `व्यामुग्धाः`/`व्यामोहतः` (held separately below), `सडिण्डिमघोषं`, `अङ्गाङ्गचालनार्थम्`, `काशीराजस्य`, `वार्धक्यं`. Every sentence read for continuity across all six spans; no ruptures, no moves proposed. Text was transcribed from print scans (not OCR); `scan.py orth` on deblocked text returns zero hits. Loc below is `pNN:Pm` (scan sequence + lint chunk) with anchor words, and `wN` counts plain words on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p040:P7 (एव तादृशम्) w11 | `वदन्तु' इति उक्तवान्` | `"` (`{del:'}{ins:"}` in file) | STY | style | high | king's direct speech with reporting verb + इति takes doubles; single close is a dropped second stroke |
| F2 | p042:P3 (एतत् वचनं) w17 | `भविष्यामि" इति। सगद्गदं` | `'` (`{del:"}{ins:'}` in file) | STY | style | high | inner resolve with no speech verb (thought) takes singles; print's open `'` decides the sort |
| F3 | p042:P7 ("षोडशवर्षाणाम् अनन्तरम्) w1 | `"षोडशवर्षाणाम्` | `'` (`{del:"}{ins:'}` in file) | STY | style | high | `चिन्तयित्वा`-thought takes singles; print's close `'` decides the sort |
| F4 | p043:P8 ("पूर्वम् अहम्) w10 | `अनुभूतः अपि।` (no close) | `"` (lone `{ins:"}` in file) | STY | style | high | multi-para speech stands alone per para; first-person account answering सुनन्द needs its own close |
| F5 | p043:P9 ('पुनः राज्यपदं) w1 | `'` para-open before `'पुनः` | `"` (lone `{ins:"}` in file) | STY | style | high | speech with `उक्तवान्` + इति takes doubles; speech-open dropped entirely (p01 precedent), nested `'पुनः...'` stays |
| F6 | p043:P9 ('पुनः राज्यपदं) w59 | `अनुभवन्ति" इति` | `'` (lone `{ins:'}` in file) | STY | style | high | nested `'क्षण...जानन्` thought needs its single close before the speech's double close |
| F7 | p040:P8 (प्रभो! एतस्य) w4-6 | `भवतः भवतः पल्याः वा` | `भवतः पत्न्याः वा` (`{del:भवतः भवतः पल्याः}{ins:भवतः पत्न्याः}` in file) | SPL | error | high | dittography plus non-word `पल्याः`; triple `भवतः X वा Y वा` needs yours, wife's, kingdom's |
| F8 | p041:P6 (अतीव सन्तुष्टा) w20 | `वार्तां ... प्रसारिता` | `वार्ता` (`{sug-del:वार्तां}{sug-ins:वार्ता}` in file) | KRK | likely | medium* | accusative object with passive kta participle is mixed; nominative `वार्ता प्रसारिता` is the smaller fix |

## Patterns

- Quote-edge repairs (6x: F1 p040:P7, F2 p042:P3, F3 p042:P7, F4 p043:P8, F5+F6 p043:P9). Print drops or mixes `"`/`'` at speech/thought boundaries; each repaired toward the surviving mark, never inventing a new pairing.
- Single-open-for-speech with dropped stroke (1x: F5 p043:P9), matching the p026 pattern; distinguished from fully dropped opens (p01 precedent, also F5's mate fix).

## Unverified

- `वार्तां` for `वार्ता` (F8, p041:P6, अतीव सन्तुष्टा, w20): passive-`kta` with accusative object looks mixed, but no Phase A glyph note covers the anusvāra, so no verdict block. `{sug-del:वार्तां}{sug-ins:वार्ता}` plus `{x-com:}` on file. Settles with: scan reopen at 5x+ to check the anusvāra, or another copy of 1986_01.
- `व्यामुग्धाः` (p043:P9, 'पुनः राज्यपदं, w56): `मुग्ध` = bewildered is attested, so `व्यामुग्धाः` reads as an intensive variant beside `व्यामोहतः` in the same speech; the alternative is a `मुग्ध`/`मूढ` slip for `व्यामूढाः`. No block; kept as print-faithful. Settles with: dictionary check of `व्यामुग्ध` or another copy.

## Coverage

p040:P1 {x-com:layout: : skip (layout declaration)
p040:P2 मूकः तेमियः : skip (title)
p040:P3 (गतसञ्चिकायाः कथायाः : clean
p040:P4 महाराजः ज्योतिषिकान् : clean
p040:P5 "महाराज! बहोः : clean
p040:P6 "किं वा : clean
p040:P7 {pc}एव तादृशम् : F1
p040:P8 "प्रभो! एतस्य : F7
p040:P9 आगामिष्यमाणेभ्यः अपायेभ्यः : clean
p040:P10 {category: जातककथा} : skip (footer metadata)
p041:P1 {x-com:layout: : skip (layout declaration)
p041:P2 "एवं तर्हि : clean
p041:P3 "एतत् सर्वथा : clean
p041:P4 तदा राज्ञी : clean
p041:P5 तदपि न : clean
p041:P6 अतीव सन्तुष्टा : F8
p041:P7 तद्दिने रात्रौ : clean
p041:P8 {pc}जानामि। मत्कृते : clean
p041:P9 एवम् एव : clean
p041:P10 सप्तमे दिने : clean
p042:P1 {x-com:layout: : skip (layout declaration)
p042:P2 {pc}आलिङ्ग्य --- : clean
p042:P3 एतत् वचनं : F2
p042:P4 अपरस्मिन् दिने : clean
p042:P5 {pc}चन्द्रादेवी पुत्रम् : clean
p042:P6 अश्वाः योजनत्रयपर्यन्तं : clean
p042:P7 "षोडशवर्षाणाम् अनन्तरम् : F3
p042:P8 अनन्तरं गर्तखनने : clean
p042:P9 'कश्चित् पथिकः : clean
p043:P1 {x-com:layout: : skip (layout declaration)
p043:P2 {pc}अस्ति। तदर्थम् : clean
p043:P3 "अये! मां : clean
p043:P4 सारथिः बोधिसत्त्वम् : clean
p043:P5 बोधिसत्त्वः निजवृत्तान्तम् : clean
p043:P6 "मूर्ख! अद्य : clean
p043:P7 "महाराज! एतावत्पर्यन्तम् : clean
p043:P8 "पूर्वम् अहम् : F4
p043:P9 {ins:"}'पुनः राज्यपदं : F5, F6
p043:P10 एतेन उपदेशात्मकवचनेन : clean
p044:P1 {x-com:layout: : skip (layout declaration)
p044:P2 {pc}शृण्वन् अहम् : clean
p044:P3 "एतत् न : clean
p044:P4 तदा सुनन्दः : clean
p044:P5 बोधिसत्त्वः 'भवतः : clean
p044:P6 {pc}तं पुनरपि : clean
p044:P7 कुमाररहितं रिक्तं : clean
p044:P8 "भवती पुत्रविषये : clean
p044:P9 पुत्रस्य वार्तां : clean
p045:P1 {x-com:layout: : skip (layout declaration)
p045:P2 {pc}उपविश्य उक्तवान् : clean
p045:P3 "तात! भवता : clean
p045:P4 "भवतः वचनानि : clean
p045:P5 {pc}अरण्ये तपः : clean
p045:P6 "सर्वसङ्गपरित्यागिनः मम : clean
p045:P7 काशीराजस्य संन्यासवार्तां : clean
J1 p040:P6 {pb} -> p040:P7 {pc} (continues) : ok (column turn, spaced join भाग्यम्|एव)
J2 p040:P9 {pb} -> p041:P2 fresh (clean break) : ok (page turn, new speech)
J3 p041:P7 {pb} -> p041:P8 {pc} (continues) : ok (column turn, nested quote continues)
J4 p041:P10 {pb} -> p042:P2 {pc} (continues) : ok (page turn, पुत्रम्|आलिङ्ग्य)
J5 p042:P4 {pb} -> p042:P5 {pc} (continues) : ok (column turn, morning scene flows to second embrace)
J6 p042:P9 {pb} -> p043:P2 {pc} (continues) : ok (page turn, periphrastic कृतवान्|अस्ति)
J7 p043:P8 {pb} -> p043:P9 fresh (clean break) : ok (column turn, new para of same speech)
J8 p043:P10 {pb} -> p044:P2 {pc} (continues) : ok (page turn, उपदेशं|शृण्वन्)
J9 p044:P5 {pb} -> p044:P6 {pc} (continues) : ok (column turn, सुनन्दः|तं subject-verb split)
J10 p044:P9 {pb} -> p045:P2 {pc} (continues) : ok (page turn, एव|उपविश्य)
J11 p045:P4 {pb} -> p045:P5 {pc} (continues) : ok (column turn, अहं|अरण्ये)
J12 p045:P7 {pb} -> END (clean break) : ok (clean end of range)
