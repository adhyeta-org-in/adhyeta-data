## Summary

Phase B proofread of `p013.md` (1984_09, scans 13-17, vetala-frame story "कनकसुन्दरी", to be continued in the next range). Proofread gate passes with 0 errors and 0 story findings; `scan.py orth` reports only the 2 print periods kept as seen. 10 findings (5 `OCR`/`SPL` severity `error`, 5 `STY` quote-punctuation severity `likely`, all confidence `high`): five print mis-settings promoted from Phase A `{sug-…}` pairs, one supplied nested-quote open, two sort corrections, one sort correction keeping the print comma, and four supplied marks pairing one four-para speech. No held candidates. Text is manual transcription, not OCR; nothing was left unchecked. `Loc` is `pNN:Pm:word` (word index within the chunk) plus anchor words. Extract gate note: one para (p016:P3) carries a genuine print sort error (double-open, single-inner, double-close, each mark verified at 6-8x); kept as seen in Phase A and resolved here as F6.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p013:P3:14 (विघ्नशतैः बाधितः) | `ग्रहीतुं पुतः वृक्षस्य` | `ग्रहीतुं पुनः वृक्षस्य` | OCR | error | high | `पुतः` is not a word; the frame needs `पुनः` (the king goes to the tree again) |
| 2 | p013:P3:21 (विघ्नशतैः बाधितः) | `शवं अंग्रे आरोप्य` | `शवं अंसे आरोप्य` | OCR | error | high | `अंग्रे` is meaningless here; the art shows the corpse slung over the shoulder (`अंसे`) |
| 3 | p013:P3:35 (विघ्नशतैः बाधितः) | `कुर्वन् एतादृश रात्रौ` | `कुर्वन् एतादृशे रात्रौ` | OCR | error | high | locative `रात्रौ` requires `एतादृशे`; the `े`-mātrā dropped in print |
| 4 | p015:P2:5 (वदति? कारणं) | `चेत् समीर्चानम्" इति` | `चेत् समीचीनम्" इति` | SPL | error | high | `समीर्चानम्` is not a word; the idiom takes `समीचीनम्` (proper, fitting) |
| 5 | p016:P4:39 ("मम अभिप्रायः) | `जयपालः नाड्गीकरोति चेत्` | `जयपालः नाङ्गीकरोति चेत्` | SPL | error | high | `न` + `अङ्गीकरोति` gives `नाङ्गीकरोति` (if he does not accept); `ड` set for `ङ` |
| 6 | p016:P3:5 (तदा मणिदीपः) | `सुकीर्तिं "तर्हि युद्धं` | `सुकीर्तिं "{ins:'}तर्हि युद्धं` | STY | likely | high | nested voiced objection needs its own single pair; print dropped the inner open (inner close `'` present) |
| 7 | p016:P6:13 (तत् श्रुत्वा) | `उक्त्वा 'भवत्याः` | `उक्त्वा {del:'}{ins:"}भवत्याः` | STY | likely | high | speech opens single but closes double; sort corrected to house double |
| 8 | p016:P7:4 (कनकसुन्दरी किञ्चित्) | `आलोच्य 'तात!` | `आलोच्य {del:'}{ins:"}तात!` | STY | likely | high | speech opens single but closes double; sort corrected to house double |
| 9 | p015:P8:26 (मणिदीपः सन्देहनिवारणार्थम्) | `एव अस्ति', इति` | `एव अस्ति{del:'}{ins:"}, इति` | STY | likely | high | the भटाः report opens double but closes single; comma stays outside the close |
| 10 | p017:P7:2 (सूचनां तिरस्करोमि।) | `भवतः{pb} {pc}सूचनां तिरस्करोमि। वस्तुतः … एव। एतावत्पर्यन्तम् … वदतु"` | `तिरस्करोमि।{ins:"} {ins:"}वस्तुतः … एव।{ins:"} {ins:"}एतावत्पर्यन्तम् … वदतु"` | STY | likely | high | one मणिदीपः speech spans P6-P9; every para opens and closes its own pair (page-turn `{pb}`/`{pc}` is the only exception) |

## Patterns

1. Print conjunct/mātrā slips (F1-F5): `त` for `न`, `ग्र` for `स`, dropped `े`, intrusive `र` with wrong mātrā, `ड्ग` for `ङ्ग`; all pinned by sense and Sanskrit form.
2. Print quote-sort lapses (F6-F9): dropped inner open, single-for-double opens and closes at speech edges; all pinned by reporting verbs and `इति`-closures.
3. Kept as seen and documented for the compiler: self-consistent single pairs for `'राजन्! … गच्छतु'` (p014:P11) and the वार्ता report (p016:P5); periods for dandas in `पुत्री.` and `रूपवती.` (p016:P5, orth hits verified in print); proper-name openness variants `जस्वन्तराज्ये` (p013) vs `जसवन्तराज्यं` (p016) and `अनुसारेण`/`अनुसारं`; three print specks omitted in Phase A (stray comma before `करोति` p014:P2, dot after `दृष्ट्वा` p015:P8, dot after `जयपालः` p016:P4).

## Unverified

None.

## Coverage

p013:P1 {x-com:layout:} : skip layout declaration
p013:P2 # कनकसुन्दरी : skip title
p013:P3 विघ्नशतैः बाधितः : F1, F2, F3
p013:P4 जस्वन्तराज्ये कुलदीपः : clean
p013:P5 {category:} : skip footer metadata
p014:P1 {x-com:layout:} : skip layout declaration
p014:P2 करोति स्म। : clean
p014:P3 गच्छति काले, : clean
p014:P4 मणिदीपः पितुः : clean
p014:P5 एकदा प्रतिवेशिराज्यस्य : clean
p014:P6 विषये मणिदीपस्य : clean
p014:P7 सुकीर्तिः किञ्चित् : clean
p014:P8 "भवान् राज्याकाङ्क्षया : clean
p014:P9 मणिदीपाय एषा : clean
p014:P10 ततः कतिपय-दिनानन्तरम् : clean
p014:P11 सुकीर्तिः तत् : clean
p014:P12 तत् श्रुत्वा : clean
p015:P1 {x-com:layout:} : skip layout declaration
p015:P2 वदति? कारणं : F4
p015:P3 "अद्य वृष्ट्याः : clean
p015:P4 मणिदीपस्य बहु : clean
p015:P5 तद्दिने वृष्टिः : clean
p015:P6 मणिदीपः सुकीर्तिम् : clean
p015:P7 सुकीर्तिः विहस्य : clean
p015:P8 मणिदीपः सन्देहनिवारणार्थम् : F9
p015:P9 मासद्वयम् अतीतम्। : clean
p015:P10 सुकीर्तिः मणिदीपस्य : clean
p015:P11 एतत् वचनं : clean
p015:P12 सुकीर्तिः शान्तस्वरेण : clean
p016:P1 {x-com:layout:} : skip layout declaration
p016:P2 वाक्यं स्थगितवान्। : clean
p016:P3 तदा मणिदीपः : F6
p016:P4 "मम अभिप्रायः : F5
p016:P5 'जयपालस्य कनकसुन्दरी : clean
p016:P6 तत् श्रुत्वा : F7
p016:P7 कनकसुन्दरी किञ्चित् : F8
p016:P8 "तरुणः मणिदीपः : clean
p016:P9 "भवान् युद्धार्थम् : clean
p016:P10 जयपालः किञ्चित् : clean
p017:P1 {x-com:layout:} : skip layout declaration
p017:P2 राज्यविषये तत्समानः : clean
p017:P3 कनकसुन्दरी --- : clean
p017:P4 जयपालः तथैव : clean
p017:P5 सुकीर्तिः शान्तस्वरेण : clean
p017:P6 "नैव, भवन्तं : clean
p017:P7 सूचनां तिरस्करोमि। : F10
p017:P8 वस्तुतः पूर्वम् : F10
p017:P9 एतावत्पर्यन्तम् अहं : F10
p017:P10 कतिपयदिनानन्तरं मणिदीपः : clean
J1 p013:P4 {pb} -> p014:P2 {pc} (continues) : ok
J2 p014:P5 {pb} -> p014:P6 {pc} (continues) : ok
J3 p014:P12 {pb} -> p015:P2 {pc} (continues) : ok
J4 p015:P9 {pb} -> p015:P10 {pc} (continues) : ok
J5 p015:P12 {pb} -> p016:P2 {pc} (continues) : ok
J6 p016:P4 {pb} -> p016:P5 fresh (clean break) : ok
J7 p016:P10 {pb} -> p017:P2 {pc} (continues) : ok
J8 p017:P6 {pb} -> p017:P7 {pc} (continues) : ok
J9 p017:P10 {pb} -> END (clean break) : ok
