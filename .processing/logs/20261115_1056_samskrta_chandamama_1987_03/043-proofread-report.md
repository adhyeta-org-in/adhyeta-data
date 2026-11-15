# Proofread report: 1987_03 p043 (pp. 43–47) — प्रत्युपकारः

## Summary

Range 43–47 holds one complete story opening, प्रत्युपकारः (to be continued — p047 ends
with (अनुवर्तते)). Extract gate passed with one unbalanced-quote residual; proofread gate
is now green (0 error paras, 0 story findings). Three findings landed as verdict blocks
(F1 quote, F2–F3 non-word corrections); zero candidates held. One orth-scanner hit
(घोरः सर्पः!) was examined and kept as a print-faithful exclamation. A suspected
agreement error (अस्थास्यन्) resolved clean on wider-window re-analysis (3pl
conditional). No moves proposed; all ten joints read grammatical in asserted order.

## Findings

| ID | Loc | Text | Category | Conf | Ruling |
|----|-----|------|----------|------|--------|
| F1 | p043:P7 प्रियंवदा दिने | 'उत्तमाय राजकुमाराय एव प्रियंवदा दातव्या इति इच्छति स्म। | quote-close-missing | high | Supplied close: दातव्या{ins:'} इति. Single-quote thought opened in print but never closed; इति-closure pins the position. Sort kept (thought = singles). |
| F2 | p044:P4 भयकम्पितां प्रियंवदां | पलायनं कर्तुम् अपि अशक्ना। | non-word | high | {del:अशक्ना}{ins:अशक्ता}. अशक्ना is no Sanskrit word; feminine subject प्रियंवदा demands अशक्ता. No other candidate fits the slot. |
| F3 | p047:P9 सायङ्काले प्रियंवदा | प्रष्टुं विस्मृतवती आस्म्। | non-word | high | {del:आस्म्}{ins:अस्मि}. आस्म् is no word; 1sg speaker + विस्मृतवती periphrastic perfect demands अस्मि. |
| — | p044:P3 प्रियंवदया क्षिप्तं | पश्यति --- घोरः सर्पः! | orth-hit | — | No block. scan.py orth flagged `!` as latin-for-danda; in context (चकिता … पार्श्वे पश्यति) the exclamation is intentional print punctuation. Checked print-faithful. |

Why-notes: F2 — word-level ruling only; no clause re-segmentation saves अशक्ना (no feminine
aorist/injunctive of शक् exists). F3 — आस्म (1pl imperfect "we were") tried and rejected:
speaker is singular throughout ("अहं भवतः नाम प्रष्टुम्"). अस्थास्यन् (p045:P9 राजकुमारी
खेदेन) was suspected of number mismatch with प्राणाः but re-derived as 3pl conditional
(अ-स्थास्य-न्, past-counterfactual with न स्यात्) — agreement correct, no block.

## Patterns

- Visarga/sibilant openness is house spelling, never flagged: निःसङ्कोचं (p044:P11)
  vs निस्सङ्कोचं (p045:P2) for the same phrase; तद्दिने / तस्मिन् दिने / तस्मिन् समये
  free variation. Variants logged, print kept.
- प्र-चल् causative/non-causative mixing is stylistic, both forms valid: प्रचालनीयः
  (gerundive, p047:P6) beside प्रचलेत् / प्रचलत् (p047:P6, p046:P10). No block.
- Print quote sorts kept throughout (1984_04/p01.proofread precedent): doubles for
  speech, singles for thought ('उत्तमाय…', 'मम आगमनम्…', 'एतं विषयम्…), nested
  SQ-in-DQ maxim ('मनोरथानाम्…') intact. Only the genuinely missing close (F1) supplied.

## Unverified

None — no {sug-del:}/{sug-ins:} candidates held; every queue item was promotable from text.

## Coverage

- p043:P1 : skip (x-com layout only)
- p043:P2 : skip (title)
- p043:P3 कीर्तिसेनः कस्यचित् : clean
- p043:P4 तस्याः जन्मसमनन्तरम् : clean (अनुभवतः correct dual for राजा राज्ञी च)
- p043:P5 आस्थानज्योतिषिकः ज्योतिःशास्त्रे : clean
- p043:P6 राजकुमारीम् अपायात् : clean
- p043:P7 प्रियंवदा दिने : F1
- p043:P8 एकदा प्रियंवदा : clean
- p043:P9 : skip (author + pgb only)
- p044:P1 : skip (x-com layout only)
- p044:P2 तदा तत्र : clean (आघ्राय, गन्धाघ्राणनं, फूत्कारम् all valid)
- p044:P3 प्रियंवदया क्षिप्तं : clean (orth `!` kept as print exclamation; --- travel verified)
- p044:P4 भयकम्पितां प्रियंवदां : F2 (भयभ्रान्ता kept: valid भय+भ्रान्ता compound)
- p044:P5 तत्क्षणे एव : clean (निर्भयेन instrumental adverb, valid)
- p044:P6 सचेतनतां प्राप्ता : clean (दृढकायः as seen)
- p044:P7 एतत्सन्दर्भे सः : clean (अनन्यदृष्ट्या valid)
- p044:P8 "भवान् कः?" : clean
- p044:P9 "अहं भवतां : clean
- p044:P10 राजकुमारी इतःपूर्वं : clean (साहसी = साहसिन् nom.sg, correct)
- p044:P11 "सुसमये आगत्य : clean (वदतु-किम् hyphen hugging, kept)
- p044:P12 "मम काऽपि : clean
- p044:P13 "निरपेक्षः इति : clean (edge-spanning open; mate in p045:P2)
- p045:P1 : skip (x-com layout only)
- p045:P2 निस्सङ्कोचं वदतु। : clean (edge-spanning close; mate in p044:P13)
- p045:P3 तदा भटः : clean (आभाणकम् = maxim, valid; शक्नुयात् optative correct)
- p045:P4 "मया पूरयितुं : clean (शक्या agrees with इच्छा)
- p045:P5 "सामर्थ्यबाह्या न : clean (बाह्य = beyond; consistent with p047:P12 बाह्यम्)
- p045:P6 "का सा : clean
- p045:P7 "राजकुमारि! अहं : clean
- p045:P8 भटस्य वचनं : clean
- p045:P9 --- "भटेन : clean (अस्थास्यन् = 3pl conditional, agrees with प्राणाः)
- p045:P10 राजकुमारी खेदेन : clean (mid-word edge उपकाराय|प्रत्युपकारं verified spaced)
- p046:P1 : skip (x-com layout only)
- p046:P2 प्रत्युपकारं कर्तुम् : clean (क्षाम्यतु imperative of क्षम्, valid)
- p046:P3 "किमर्थं क्षमायाचनम्? : clean
- p046:P4 चिन्ताक्रान्ता राजकुमारी : clean
- p046:P5 तत्समये तत्र : clean
- p046:P6 'मम आगमनम् : clean (ज्ञातवन्तौ correct dual)
- p046:P7 राजा पत्नीम् : clean
- p046:P8 "जन्मकुण्डली कथयति : clean (कान्तिमती spelling consistent)
- p046:P9 एतस्य श्रवणेन : clean
- p046:P10 "इदानीं तु : clean
- p046:P11 प्रियंवदा तद्दिने : clean
- p046:P12 महता चिन्तनेन : clean (mid-sentence edge दृढः|जातः verified spaced)
- p047:P1 : skip (x-com layout only)
- p047:P2 जातः। : clean (single-word {pc} completion of दृढः जातः)
- p047:P3 'एतं विषयं : clean
- p047:P4 एवं प्रियंवदा : clean
- p047:P5 कीर्तिसेनः कान्तिमती : clean (आरब्धवन्तौ correct dual)
- p047:P6 ते चिन्तयन्तः : clean (gerundives आनेतव्यः/प्रचालनीयः/मारणीयः/निर्वर्तनीयः all regular)
- p047:P7 एतत्सर्वं श्रुतवत्याः : clean (mid-sentence edge यदि अहम्|इदानीं verified)
- p047:P8 इदानीं भटस्य : clean (अङ्गीकुरुतः/मारयतः/वदतः correct duals)
- p047:P9 सायङ्काले प्रियंवदा : F3
- p047:P10 "जयः इति : clean
- p047:P11 "आवां विवाहितौ : clean (भवाव = 1du lot, correct)
- p047:P12 "राजकुमारि! एतत् : clean (कम्पमानेन middle participle, valid)
- p047:P13 "भीतिः मास्तु। : clean (मास्तु = मा+अस्तु; ends (अनुवर्तते), range ends clean)
- J1 p043:P5 {pb} -> p043:P6 fresh : ok (column turn, new scene)
- J2 p043:P8 {pb} -> p044:P2 fresh : ok (page turn, तदा picks up garden stroll)
- J3 p044:P4 {pb} -> p044:P5 fresh : ok (column turn, क्रन्दनं → तत्क्षणे rescue)
- J4 p044:P13 {pb} -> p045:P2 {pc} : ok (mid-speech नास्ति।|निस्सङ्कोचं, same utterance)
- J5 p045:P8 {pb} -> p045:P9 {pc} : ok (column turn, विचारकोलाहलः --- thought continues)
- J6 p045:P10 {pb} -> p046:P2 {pc} : ok (page turn, उपकाराय|प्रत्युपकारं spaced join)
- J7 p046:P6 {pb} -> p046:P7 fresh : ok (column turn, eavesdrop setup → parents' dialogue)
- J8 p046:P12 {pb} -> p047:P2 {pc} : ok (page turn, दृढः|जातः spaced join)
- J9 p047:P7 {pb} -> p047:P8 {pc} : ok (column turn, यदि अहम्|इदानीं optative construction whole)
- J10 p047:P13 {pb} -> END : ok (range ends; story marked (अनुवर्तते))
