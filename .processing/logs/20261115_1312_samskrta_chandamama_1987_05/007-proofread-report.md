## Summary

Three findings in story p007 (1987_05, scans 7–9): two mismatched quote pairs (single open, double close) on direct speech corrected to doubles, and one dropped-`र` typo (`धमसङ्कटं` for `धर्मसङ्कटं`) corrected against eight parallel tokens plus the title. Sanskrit orth scanner reported zero hits on the deblocked text, and no inherited `{sug-ins:}`/`{sug-del:}` queue existed. No candidates held; every note is dispositioned and the proofread gate is green.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p08:P6 w1 (`'किं तत्`) | `'किं तत् धर्मसङ्कटम्?"` | `"{del:'}{ins:"}` at open, i.e. `"किं तत् धर्मसङ्कटम्?"` | STY | likely | high | mismatched pair on direct speech; reporting verb plus iti-closure pins era-standard doubles |
| 2 | p09:P4 w6 (`गौरवेशं दृष्ट्वा`) | `--- 'पश्यतु भोः, ... भवन्तः?"` | `"{del:'}{ins:"}` at open, i.e. `--- "पश्यतु भोः, ... भवन्तः?"` | STY | likely | high | mismatched pair on direct speech; reporting verb plus iti-closure pins era-standard doubles |
| 3 | p09:P7 w36 (`"भवान् एतत्क्षणे`) | `भवतः धमसङ्कटं परिहृतं` | `{del:धमसङ्कटं}{ins:धर्मसङ्कटं}` | SPL | error | high | `र` absent in print even at 4x; title and eight body tokens read `धर्मसङ्कट`, and story sense needs it |

## Patterns

- Single-open / double-close quote mismatch on direct speech: 2 instances (F1 at p08:P6, F2 at p09:P4). Both opens verified single at 3–5x in Phase A; both closings double. All other speech sorts re-derived: outer doubles with inner singles intact (p08:P7–P8 Ananta's tale, p09:P7 Gauravesha's instruction), thought in singles kept (p09:P3 Gauravesha's `चिन्तयन्`), maxim in singles kept (p07:P6 `यस्यां कस्यां` doctrinal citation where speech sense does not decide).

## Unverified

None. No held candidates; nothing below high confidence.

## Coverage

- p07:P1 `{x-com:layout:` : skip layout-only chunk
- p07:P2 `धर्मसङ्कटम्` : skip title
- p07:P3 `इन्द्रपादग्रामं पूर्वं` : clean
- p07:P4 `एतत्कार्यक्रमार्थं बहवः` : clean
- p07:P5 `अनन्तरदिने तस्यां` : clean
- p07:P6 `उपन्यासं कुर्वन्` : clean
- p07:P7 `एवं धर्मबोधनं` : clean
- p07:P8 `तस्य वचनानि` : clean
- p08:P1 `{x-com:layout:` : skip layout-only chunk
- p08:P2 `लोकस्थितिः। एवं` : clean
- p08:P3 `तदा गौरवेशः` : clean
- p08:P4 `विश्वम्भरः क्षणकालानन्तरम्` : clean
- p08:P5 `अनन्तरदिने विश्वम्भरः` : clean
- p08:P6 `'किं तत्` : F1
- p08:P7 `"अद्य प्रातःकाले` : clean
- p08:P8 `साहाय्यम् आचरन्ति` : clean
- p08:P9 `विश्वम्भरः मृदु` : clean
- p08:P10 `तदा अनन्तः` : clean
- p09:P1 `{x-com:layout:` : skip layout-only chunk
- p09:P2 `मदिरापणं प्रति` : clean
- p09:P3 `गृहस्य अन्तः` : clean
- p09:P4 `गौरवेशं दृष्ट्वा` : F2
- p09:P5 `तदा गौरवेशः` : clean
- p09:P6 `"तत् कथम्?` : clean
- p09:P7 `"भवान् एतत्क्षणे` : F3
- p09:P8 `तत्र सम्मिलिताः` : clean
- p09:P9 `अनन्तस्य गमनानन्तरं` : clean
- p09:P10 `"मम सुदीर्घलोकज्ञानेन` : clean
- J1 p007:P5 `{pb}` -> p007:P6 `{pc}` : ok
- J2 p007:P8 `{pb}` -> p008:P2 `{pc}` : ok
- J3 p008:P7 `{pb}` -> p008:P8 `{pc}` : ok
- J4 p008:P10 `{pb}` -> p009:P2 `{pc}` : ok
- J5 p009:P4 `{pb}` -> p009:P5 fresh : ok
- J6 p009:P10 `{pb}` -> END : ok
