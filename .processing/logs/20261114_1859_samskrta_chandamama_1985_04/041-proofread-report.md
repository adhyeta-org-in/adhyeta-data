## Summary

7 findings (4 error, 2 likely, 1 style) plus 1 unverified name; every verdict is already applied in the story file and both gates pass. The systematic problem is print quote marks for direct speech: three speeches open with `'` but close with `"`, one speech drops its open entirely, and two spoken questions sit in balanced singles (F1-F6) --- all corrected to era-house doubles. One Phase A omission (the whole p43 right column, `तु सृष्टेः ... सर्पादयः।`) was caught at the flow pass and restored from Phase A notes; images stayed closed throughout Phase B. The text is human transcription from 300 DPI scans, not OCR output; the Sanskrit orth scan reports no hits and no passage was left unchecked.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p042:P4 विष्णुः ध्यानमग्नः | `उक्तवान् --- यः एतस्य` | insert `"` before `यः` (`{ins:"}` applied) | STY | error | high | speech open missing in print; the close `"` is present and उक्तवान्+इति pins direct speech |
| 2 | p043:P6 शिवस्य स्वरूपं | `'कः भवान्?'` | `"कः भवान्?"` (both marks corrected) | STY | error | high | spoken question (पृष्टवान्+इति) takes doubles in era house; 3x-zoom verified print singles |
| 3 | p044:P6 तदा सर्वे | `'भवन्तः ... तिष्ठामि"` | `"भवन्तः ... तिष्ठामि"` (open corrected) | STY | error | high | direct speech opens print-single but closes print-double; sort corrected to doubles |
| 4 | p044:P7 तदा विष्णुब्रह्मादयः | `'एषः ... उचितम्"` | `"एषः ... उचितम्"` (open corrected) | STY | error | high | same mismatch; 3x-zoom verified the print `'` open |
| 5 | p046:P2 पृष्टवन्तः च | `'भवान् ... अनुपस्थितौ'` | `"भवान् ... अनुपस्थितौ"` (both marks corrected) | STY | likely | medium | spoken question in print singles; corrected to house doubles on the zoom-verified F4 pattern |
| 6 | p046:P4 शिवस्य निन्दया | `'एतद्यागार्थं ... अनुभविष्यन्ति"` (spans P4-P5) | `"एतद्यागार्थं ... अनुभविष्यन्ति"` (open corrected) | STY | likely | medium | speech opens single and closes double; corrected on the zoom-verified F4 pattern |
| 7 | p044:P3 शिवं परिणेतुम् | `नन्दिकेश्वरं` vs `नन्दीश्वरा` / `नन्दिकेश्वरा` (p047:P4, p047:P8) | unify the spelling (editor choice) | CNS | style | medium | one attendant's name in two spellings; no glyph claim, editor to decide |

## Patterns

- Print quote-mark gaps for direct speech (6 cases): 3x single-open/double-close (F3, F4, F6), 1x dropped open (F1), 2x balanced singles around spoken questions (F2, F5). All corrected to doubles; kept singles elsewhere are all thoughts, resolves, or desires, where singles are the correct sort.
- House variants kept as seen (no findings): mixed open/joined sandhi (`जगतः सृष्टिकर्ता`, `सः अपवित्रः`), `-ं`/`-म्` finals (`ओङ्कारजपं`/`जपम्`), `याग`/`यज्ञ`, `आमन्त्रण`/`निमन्त्रण`, case-driven `कैलासं`/`कैलासे`.

## Unverified

- U1: p044:P2 `स्वायाः` (कद्रुदेव्याः गर्भतः सर्पादयः। जाताः। स्वायाः गर्भतः यक्षराक्षसादयः) --- a Kashyapa-wife name; print glyphs are clear but the intended referent cannot be settled from text. Settles with an editor check against the Purana source. No block emitted; name kept as printed.

## Coverage

- p041:P1 {x-com:layout} : skip layout-only
- p041:P2 शिवपुराणम् : skip title
- p041:P3 सृष्टेः पूर्वं : clean
- p041:P4 परमेश्वरी परमेश्वरः : clean
- p041:P5 उत्पन्ना। समस्तलोकं : clean
- p041:P6 तदा विष्णुः : clean
- p041:P7 category दक्षयज्ञः : skip metadata
- p042:P1 {x-com:layout} : skip layout-only
- p042:P2 अहं विष्णुः : clean
- p042:P3 तदा ब्रह्मणः : clean
- p042:P4 विष्णुः ध्यानमग्नः : F1
- p042:P5 माणस्य विश्वस्य : clean (joins to निर्मीयमाणस्य, the only grammatical fit)
- p042:P6 ब्रह्मा परमेश्वरं : clean
- p042:P7 ब्रह्मणः वचनं : clean
- p042:P8 तदा परमेश्वरः : clean
- p042:P9 एतदनन्तरं ब्रह्मा : clean
- p042:P10 तदा जले : clean
- p042:P11 folio ५२ : skip page furniture
- p043:P1 {x-com:layout} : skip layout-only
- p043:P2 पूर्वकं तत् : clean
- p043:P3 एतत् दृष्ट्वा : clean
- p043:P4 तदा तदीयानि : clean
- p043:P5 शिवस्य स्वरूपं : clean
- p043:P6 अहं शिवः : F2
- p043:P7 तदा विष्णुः : clean
- p043:P8 तु सृष्टेः : clean
- p043:P9 एतदनन्तरं ब्रह्मा : clean
- p043:P10 तेषु दक्षब्रह्मणः : clean
- p043:P11 folio ५३ : skip page furniture
- p044:P1 {x-com:layout} : skip layout-only
- p044:P2 जाताः। स्वायाः : U1
- p044:P3 शिवं परिणेतुम् : F7 (also clean text; flagged only for the name spelling)
- p044:P4 किञ्चित् कालानन्तरं : clean
- p044:P5 यागार्थम् आगतानां : clean
- p044:P6 तदा सर्वे : F3
- p044:P7 तदा विष्णुब्रह्मादयः : F4
- p044:P8 अत्रान्तरे ईश्वरनिन्दनेन : clean
- p044:P9 folio ५४ : skip page furniture
- p045:P1 {x-com:layout} : skip layout-only
- p045:P2 आहुतिरूपेण पततु : clean
- p045:P3 एतेन क्रुद्धः : clean
- p045:P4 एतदनन्तरं रुद्रः : clean
- p045:P5 दक्षः अपि : clean
- p045:P6 एतेन अपि : clean
- p045:P7 अस्मिन् यज्ञे : clean
- p045:P8 एतद्यज्ञार्थं विश्वेदेवाः : clean
- p045:P9 स्थिताः। एतेषां : clean
- p045:P10 यज्ञदीक्षादीक्षितः दक्षः : clean
- p045:P11 शिवस्य निमन्त्रणम् : clean
- p045:P12 देवताभिः महर्षिभिः : clean
- p045:P13 folio ५५ : skip page furniture
- p046:P1 {x-com:layout} : skip layout-only
- p046:P2 पृष्टवन्तः च : F5
- p046:P3 तदा दक्षः : clean
- p046:P4 शिवस्य निन्दया : F6
- p046:P5 अपि अल्पे : clean
- p046:P6 तदा दक्षः : clean
- p046:P7 कैलासे शिवेन : clean
- p046:P8 सख्यः सर्वत्र : clean
- p046:P9 एतत् श्रुतवत्याः : clean
- p046:P10 सा शिवसमीपं : clean
- p046:P11 folio ५६ : skip page furniture
- p047:P1 {x-com:layout} : skip layout-only
- p047:P2 रुद्रगणैः सह : clean
- p047:P3 तदा शिवः : clean
- p047:P4 तर्हि भवान् : clean
- p047:P5 दिभिः सह : clean
- p047:P6 वती। : clean
- p047:P7 सतीदेवि! भवतीं : clean
- p047:P8 किन्तु पितृगृहं : clean
- p047:P9 शिवः चिन्तितवान् : clean
- J1 p041:P4 {pb} -> p041:P5 {pc} : ok (सरस्वती अपि उत्पन्ना, spaced)
- J2 p041:P6 {pb} -> p042:P2 {pc} : ok (speech continues, new sentence)
- J3 p042:P4 {wb} -> p042:P5 {pc} : ok (निर्मीयमाणस्य, unique fit)
- J4 p042:P10 {wb} -> p043:P2 {pc} : ok (विस्मयपूर्वकं, solid adverb)
- J5 p043:P7 {pb} -> p043:P8 {pc} : ok (अहं तु, spaced)
- J6 p043:P10 {pb} -> p044:P2 {pc} : ok (सर्पादयः जाताः, spaced)
- J7 p044:P4 {pb} -> p044:P5 fresh : ok (indented new paragraph)
- J8 p044:P8 {pb} -> p045:P2 {pc} : ok (यज्ञकुण्डे आहुतिरूपेण, spaced)
- J9 p045:P8 {wb} -> p045:P9 {pc} : ok (उपस्थिताः)
- J10 p045:P12 {pb} -> p046:P2 {pc} : ok (ते दक्षं पृष्टवन्तः, spaced)
- J11 p046:P4 {pb} -> p046:P5 {pc} : ok (जनाः अपि, spaced)
- J12 p046:P10 {pb} -> p047:P2 {pc} : ok (वयम् अपि रुद्रगणैः, spaced)
- J13 p047:P4 {wb} -> p047:P5 {pc} : ok (नन्दीश्वरादिभिः)
- J14 p047:P5 {wb} -> p047:P6 {pc} : ok (उक्तवती)
- J15 p047:P9 {pb} -> END : ok (clean break)
