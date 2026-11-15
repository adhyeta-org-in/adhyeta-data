# Proofread report: 1986_12, p017 (वचनभङ्गः / वेतालकथा)

## Summary

Six findings: four `error` (print misprints corrected as verdicts) and two `style` (supplied quote marks for readability, five `{ins:}` blocks). No candidates held. `Loc` below is story coordinates `pNN:Pm` (scan-sequence page plus lint chunk number) with the first two words as anchor. One scan defect limits coverage: folio 33 is absent (23.jpg duplicates folio 31), so the story jumps from folio 32 to the closing page across joint J12. Orth scan (`scan.py orth`) on deblocked text reported no hits.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p019:P4 सुवर्णदेव्या सह | `अनुसूतवन्तः` | `अनुसृतवन्तः` | MRP | error | high | अनु-सृ (follow) governs the accusative escort; सू (impel) does not fit |
| F2 | p020:P2 सुवर्णदिवी | `दिवी` | `देवी` | CNS | error | high | proper noun spelled देवी in ~25 other places in this story |
| F3 | p022:P8 चोराः आयुधानि | `भापितवन्तः` | `भाषितवन्तः` | OCR | error | high | smallest glyph change प→ष; भाष् (address) fits, भाप् is no root |
| F4 | p024:P2 वेतालः एवं | `अङ्गीकृतती` | `अङ्गीकृतवती` | OCR | error | high | feminine agent सा needs -वती; व dropped in print |
| F5 | p024:P4 चोरनायकः सञ्जातः | `सुवर्णदेवी परिणेष्यामि'` | `सुवर्णदेवी {ins:'}परिणेष्यामि'` | STY | style | high | vow verb nested inside speech takes a single; print lost the open |
| F6 | p024:P4 चोरनायकः सञ्जातः / P5 शेखरस्य दृष्ट्या / P6 'चोराणां दण्डनं | bare multi-para speech paras | per-para `"` pairs (`{ins:"}` ×4) | STY | style | high | Trivikrama speaks continuously across three paras; every para opens and closes its pair |

## Patterns

- Print leaves middle paras of a long speech bare (single open at start, single close at end): Trivikrama's verdict needed four supplied `"` (F6, p024:P4 end, P5 open+close, P6 open) plus one supplied `'` (F5).

## Unverified

None held. Every candidate was either promoted with print-plus-context evidence or supplied where speech-vs-thought sense and sentence boundary pin it.

## Coverage

p017:P2 वचनभङ्गः : skip title
p017:P3 असाध्यपदम् अजानन् : clean
p017:P4 अनन्तरं वेतालेन : clean
p017:P5 category : skip metadata
p018:P2 कदाचित् सायङ्कालसमये : clean
p018:P3 राजधानीगमनतः पूर्वं : clean
p018:P4 तावति काले : clean
p018:P5 सः प्रदेशः : clean
p018:P6 तस्मिन् क्षणे : clean
p018:P7 अन्ये चोराः : clean
p018:P8 एतान् नूतनान् : clean
p018:P9 एतत् दृष्ट्वा : clean
p018:P10 राजकुमार्याः सुवर्णदेव्याः : clean
p019:P2 नायकः शेखरः : clean
p019:P3 केभ्यश्चित् दिनेभ्यः : clean
p019:P4 सुवर्णदेव्या सह : F1
p019:P5 "तान् चोरान् : clean
p019:P6 राजधानीं गतवान् : clean
p019:P7 परेद्युः राजा : clean
p019:P8 तदा शेखरः : clean
p019:P9 राजा अनुमतिपूर्वकं : clean
p019:P10 सुवर्णदेवी शेखरं : clean
p019:P11 "अहं यत् : clean
p020:P2 सुवर्णदिवी : F2
p020:P3 "तथा न, : clean
p020:P4 एताम् अपेक्षां : clean
p020:P5 प्रतिप्रश्नं कृतवान् : clean
p020:P6 "यदि अहं : clean
p020:P7 तस्याः वचनेन : clean
p020:P8 राजकुमार्याः वचनेन : clean
p020:P9 एतेन किञ्चित् : clean
p021:P2 पूर्ववचनं किमपि : clean
p021:P3 "पितः, राजकुमारः : clean
p021:P4 "अस्तु, एतस्मिन् : clean
p021:P5 परेद्युः राजा : clean
p021:P6 एतेन खिन्नः : clean
p021:P7 राजकुमारी तं : clean
p021:P8 एतेन वचनेन : clean
p021:P9 एकं वर्षम् : clean
p021:P10 शीघ्रातिशीघ्रं भवत्याः : clean
p021:P11 शेखरविषये पितरं : clean
p021:P12 पुनः एकदा : clean
p021:P13 सुवर्णदेव्याः सहोदरः : clean
p022:P2 राजा हृदयाघातेन : clean
p022:P3 एतेन प्रसङ्गेन : clean
p022:P4 एवमेव बहूनि : clean
p022:P5 किन्तु शेखरः : clean
p022:P6 कदाचित् सा : clean
p022:P7 तस्य प्रान्तस्य : clean
p022:P8 चोराः आयुधानि : F3
p022:P9 एका घण्टा : clean
p023:P1 x-missing : skip no story text, folio 33 absent from scan
p024:P2 वेतालः एवं : F4
p024:P3 तदा त्रिविक्रमः : clean
p024:P4 चोरनायकः सञ्जातः : F5, F6
p024:P5 शेखरस्य दृष्ट्या : F6
p024:P6 'चोराणां दण्डनं : F6
p024:P7 एवं वदता : clean
J1 p017:P4 -> p018:P2 fresh : ok frame to embedded-tale start
J2 p018:P4 -> p018:P5 {pc} : ok सञ्जातः सः प्रदेशः, print order kept
J3 p018:P10 -> p019:P2 {pc} : ok तेषां नायकः शेखरः
J4 p019:P5 -> p019:P6 {pc} : ok सह राजधानीं
J5 p019:P11 -> p020:P2 fresh : ok question to reply, new speaker
J6 p020:P4 -> p020:P5 fresh : ok reply to counter-question
J7 p020:P7 -> p020:P8 fresh : ok question to narrator
J8 p020:P9 -> p021:P2 {pc} : ok इतः पूर्ववचनं, raja speech spans page turn
J9 p021:P9 -> p021:P10 {pc} : ok दृष्ट्वा शीघ्रातिशीघ्रं
J10 p021:P13 -> p022:P2 {pc} : ok व्याधिपीडितः राजा
J11 p022:P5 -> p022:P6 fresh : ok waiting to new episode
J12 p022:P9 -> p024:P2 fresh : rupture, folio 33 absent (23.jpg duplicates folio 31); omission held, no reorder proposed
J13 p024:P3 -> p024:P4 {pc} : ok पीडयन् चोरनायकः, column turn mid-speech
J14 p024:P7 -> END : ok vetala vanishes, story ends
