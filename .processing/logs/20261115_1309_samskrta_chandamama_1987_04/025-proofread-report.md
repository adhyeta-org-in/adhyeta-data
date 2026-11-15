# Proofread report: 025 (1987_04, RUN 20261115_1309)

## Summary
Story `p025.md` (वधूस्वीकारः, scans 25-28, 4 page spans) reviewed print-faithfully in Phase B with images closed. Findings: 2 spelling errors (print misprints, corrected via verdicts), 2 punctuation insertions (unbalanced print quote marks, supplied), 1 held morphology candidate. No systematic corruption; the file is a manual transcription, not OCR output, and the orth scanner reported zero hits. All joints and sentence continuity check out; both gates pass.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p025:P9 किञ्चित्कालानन्तरं-तैः w6 | `कन्यासम्बन्धिनीं रंहस्यवार्तां` | `रहस्यवार्तां` | SPL | error | high | `रंहस्य` is not a Sanskrit word; print shows an intrusive anusvara on रहस्य, verified at 3x in Phase A |
| 2 | p026:P2 यदा-महाराजः w25 | `सादरसक्कारं कृतवती` | `सादरसत्कारं` | SPL | error | high | `सक्कारं` is not a word; welcome context needs सत्कारं, verified at 3x in Phase A |
| 3 | p028:P6 भवान्-यदा w36-end | `इति तर्कितवती।` (no closing mark) | `{ins:"}` after danda | STY | style | high | opening `"` before भवान् never closes; final इति pins the close at paragraph end |
| 4 | p028:P7 किन्तु-अन्ते w0-start | `किन्तु अन्ते..."` (no opening mark) | `{ins:"}` before किन्तु | STY | style | high | closing `"` after अन्ते... with इति वदन्ती pins a trailing-speech open at paragraph start |
| 5 | p028:P9 महाराज!-इदानीम् w9 | `मां क्षाम्यतु` | `क्षम्यताम्` | MRP | likely | medium* | 3rd-sg active imperative with मां needs a passive; print's long आ unconfirmed, held for the user |

## Unverified

- U1 (= F5): `क्षाम्यतु` vs `क्षम्यताम्`. Tried window: `तदर्थं मां क्षाम्यतु` addressed to the king asks forgiveness for the coming words, which needs 2nd person (क्षमस्व) or passive (क्षम्यताम्); a 3rd-sg active form fits neither. Settled by: dictionary/grammar check of क्षम् imperative paradigms or acceptance of a house form.

## Coverage

- p025:P1 {x-com:layout} : skip x-com-only chunk
- p025:P2 # वधूस्वीकारः : skip title
- p025:P3 पूर्वं विजयसेनः : clean
- p025:P4 विजयसेनराजस्य एकः : clean
- p025:P5 एकस्मिन् दिने : clean
- p025:P6 तस्य सचिवाः : clean
- p025:P7 अस्माभिः काचन : clean
- p025:P8 मन्त्रिणां सूचना : clean
- p025:P9 किञ्चित्कालानन्तरं तैः : F1
- p025:P10 {author} : skip metadata
- p026:P1 {x-com:layout} : skip x-com-only chunk
- p026:P2 यदा महाराजः : F2
- p026:P3 रात्रौ भोजनवेलायां : clean
- p026:P4 भूमौ स्थापिते : clean
- p026:P5 कष्टम् अनुभोक्तव्यम् : clean
- p026:P6 महाराजः तस्याः : clean
- p026:P7 तदा सुमती : clean
- p026:P8 तत् किम् : clean
- p026:P9 सर्वापेक्षया किंवदन्ती : clean
- p026:P10 किंवदन्ती वा : clean
- p026:P11 मम वचनं : clean
- p026:P12 साधारणकुटुम्बे जन्म : clean
- p027:P1 {x-com:layout} : skip x-com-only chunk
- p027:P2 सुमत्याः यादृशी : clean
- p027:P3 घृतं परिवेषयन्ती : clean
- p027:P4 तस्याः वचनस्य : clean
- p027:P5 मनुष्येषु अर्धसङ्ख्याकजनानां : clean
- p027:P6 दृष्ट्वा जनाः : clean
- p027:P7 अनन्तरं महाराजः : clean
- p027:P8 सुमती महाराजाय : clean
- p027:P9 विजयसेनराजस्य तस्याः : clean
- p028:P1 {x-com:layout} : skip x-com-only chunk
- p028:P2 उक्तवती : clean
- p028:P3 अहं वेषान्तरं : clean
- p028:P4 भवान् काशीं : clean
- p028:P5 समीचीनम् अहं : clean
- p028:P6 भवान् यदा : F3
- p028:P7 किन्तु अन्ते : F4
- p028:P8 विजयसेनराजः हसन् : clean
- p028:P9 महाराज! इदानीम् : F5
- p028:P10 सुमत्याः बुद्धिशक्त्या : clean
- p028:P11 तस्याः मातापितरौ : clean
- J1 p25:P6 {pb} -> p25:P7 {pc} : ok
- J2 p25:P9 {pb} -> p26:P2 fresh : ok
- J3 p26:P4 {pb} -> p26:P5 {pc} : ok
- J4 p26:P12 {pb} -> p27:P2 {pc} : ok
- J5 p27:P5 {pb} -> p27:P6 {pc} : ok
- J6 p27:P9 {pb} -> p28:P2 {pc} : ok
- J7 p28:P11 {pb} -> END : ok
