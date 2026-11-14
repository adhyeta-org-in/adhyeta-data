## Summary
Four verified findings (F1–F4), all quote-mark punctuation (STY/error/high): two speeches printed without opening marks on p25, one plea closed with a single instead of a double on p26, and one interior thought printed in doubles instead of house singles on p27. Orth scan (`scan.py orth`) on deblocked text reported zero hits. No `{sug-ins:}`/`{sug-del:}` were inherited from Phase A and none were created. No held candidates. All twelve joints verified grammatical with no moves proposed.

## Findings
| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p25:P6 समूहेन प्रथमसमूहस्य | `कृतम्। कुतः इदम् आक्रमणम्? इति` | `कृतम्। {ins:"}कुतः इदम् आक्रमणम्?{ins:"} इति` | STY | error | high | Reporting verb `पृष्टवन्तः` plus `?` plus `इति` pins a spoken question; print carries no marks so supply the certain pair |
| 2 | p25:P6 समूहेन प्रथमसमूहस्य | `पृष्टवन्तः। किम् अन्यत् स्यात्?` | `पृष्टवन्तः। {ins:"}किम् अन्यत् स्यात्?` | STY | error | high | Answer speech closes with print `"` after `गच्छन्तु` (kept) but never opens; `उक्तवन्तः` plus `इति` pins the open so supply it |
| 3 | p26:P6 कदाचित् मन्त्रपठनेन | `दास्यामि' इति` | `दास्यामि{del:'}{ins:"} इति` | STY | error | high | Plea speech opens with `"` in P5 and singles mark thought or nested speech only, so the close sorts to doubles |
| 4 | p27:P2 प्रथमः धनरक्षकः | `मनसि "इदानीं` ... `भविष्यति" इति` | `मनसि {del:"}{ins:'}इदानीं` ... `भविष्यति{del:"}{ins:'} इति` | STY | error | high | `मनसि` plus `इति चिन्तयन्` pins interior thought and the adjacent thought (P3) prints singles, confirming the house sort |

## Patterns
None. Four isolated print punctuation gaps in separate speeches; every other speech and thought in the story opens and closes correctly (page-turn continuations via `{pb}`/`{pc}` excepted).

## Unverified
None. No words held for the user.

## Coverage
p23:P3 पुरा ब्रह्मदत्तः : clean
p23:P4 बोधिसत्त्वः अस्य : clean
p23:P5 मार्गे गच्छति : clean
p23:P6 यदि पिता : clean
p23:P1 layout : skip x-com-only chunk
p23:P2 वक्र बुद्धिः : skip title heading
p23:P7 जातककथा : skip category metadata chunk
p24:P2 मरणम् इति : clean
p24:P3 गमनतः पूर्वं : clean
p24:P4 एतादृशः योगः : clean
p24:P5 किञ्चित्कालानन्तरं सूर्यः : clean
p24:P6 अनन्तरं ब्राह्मणः : clean
p24:P7 आम् सत्यम्। : clean
p24:P8 एतावदेव खलु! : clean
p25:P2 एकैकः अपि : clean
p25:P3 कुतः मया : clean
p25:P4 एतत् सर्वं : clean
p25:P5 गत्यन्तराभावात् ब्राह्मणः : clean
p25:P6 समूहेन प्रथमसमूहस्य : F1, F2
p25:P7 एतावदेव खलु? : clean
p25:P8 एतत्सर्वं सत्यं : clean
p26:P2 किन्तु... इति : clean
p26:P3 किञ्चित् सावधानेन : clean
p26:P4 भोः ब्राह्मण! : clean
p26:P5 निरुपायः ब्राह्मणः : clean
p26:P6 कदाचित् मन्त्रपठनेन : F3
p26:P7 किन्तु तस्य : clean
p26:P8 अनन्तरं सर्वे : clean
p26:P9 इदानीं नूतनतया : clean
p26:P10 तदा तयोः : clean
p27:P2 प्रथमः धनरक्षकः : F4
p27:P3 द्वितीयः नगरं : clean
p27:P4 यदा सः : clean
p27:P5 एवंक्रमेण ब्राह्मणस्य : clean
p27:P6 दिनद्वयानन्तरं शिष्यः : clean
p27:P7 असमर्थः एषः : clean
p27:P8 तस्मात् स्थानात् : clean
p28:P2 हस्य चोराणां : clean
p28:P3 एकत्र गुल्मानां : clean
p28:P4 एतत्सर्वम् आलोचयन् : clean
p28:P5 अपि वचनं : clean
p28:P6 अनन्तरं बोधिसत्त्वः : clean
J1 p023:P4 {wb} -> p023:P5 {pc} : ok
J2 p023:P6 {pb} -> p024:P2 {pc} : ok
J3 p024:P3 {pb} -> p024:P4 {pc} : ok
J4 p024:P8 {pb} -> p025:P2 {pc} : ok
J5 p025:P5 {pb} -> p025:P6 {pc} : ok
J6 p025:P8 {pb} -> p026:P2 {pc} : ok
J7 p026:P5 {pb} -> p026:P6 {pc} : ok
J8 p026:P10 {pb} -> p027:P2 fresh : ok
J9 p027:P6 {pb} -> p027:P7 {pc} : ok
J10 p027:P8 {wb} -> p028:P2 {pc} : ok
J11 p028:P4 {pb} -> p028:P5 {pc} : ok
J12 p028:P6 {pb} -> END : ok
