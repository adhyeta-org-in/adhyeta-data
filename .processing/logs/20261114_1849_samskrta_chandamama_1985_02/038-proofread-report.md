## Summary

5 findings, all severity style (quote punctuation for modern readability; no story text changed silently). Systematic problem: two spoken passages printed with single quotes where doubles are required (वदन्/उक्तवान् + इति closures), and one multi-chunk speech whose opening mark the print dropped. One word held for the user (असहनयाः). Scanner orth run clean; story read sentence by sentence for continuity with all six joints fit-tested; proper nouns कमला/नारायण spelled consistently throughout. Loc below is story coordinates pNN:Pm plus anchor words, word counted on the chunk from 1. Text is a print-faithful transcription, not OCR output.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p038:P6 w1 (यदि वयम्) | `यदि वयम् ... किल?" इति उक्तवती कमला` | `{ins:"}यदि वयम्` | STY | style | high | इति उक्तवती कमला closes a speech (वयम्/क्रेष्यामः first-person) whose opening the print dropped; supplied at the certain sentence start |
| F2 | p038:P9 w9 (महता कष्टेन) | `'मया` | `"मया` | STY | style | high | इति वदन् pins speech, which takes doubles |
| F3 | p038:P9 w11 (महता कष्टेन) | `शक्यते'` | `शक्यते"` | STY | style | high | closing sort must match the speech opening in F2 |
| F4 | p040:P7 w7 (वैद्यः रूप्यकद्वयं) | `'प्रतिदिनं` | `"प्रतिदिनं` | STY | style | high | इति उक्तवान् pins speech, which takes doubles |
| F5 | p040:P7 w12 (वैद्यः रूप्यकद्वयं) | `स्वीकरणीया'` | `स्वीकरणीया"` | STY | style | high | closing sort must match the speech opening in F4 |

## Patterns

Quote-sort inconsistency: 2 passages / 4 marks. Print uses singles for aloud speech closed by इति वदन्/उक्तवान् (F2--F5) where the era standard and the rest of this story use doubles for speech; corrected per mark with {del:}/{ins:} verdicts. All other quote pairs already match their roles and nesting and are kept as seen. Print-faithful variants kept without blocks: दूरङ्गता (दूरम् + गता, valid anusvāra sandhi), निश्शुल्कं (for निःशुल्कम्), गुलिका (pill, verified गुलिका with ल at 4x), क्रेष्यामः (correct क्री-future 1pl), असह्यया, एकरूप्यकात्मकेन, सायं-त्रिवारम्.

## Unverified

| # | Loc | Question | Conf | What would settle it |
|---|---|---|---|---|
| U1 | p039:P5 w9 (कदलीफलानि खादन्) | `असहनयाः` is not a valid form in `अतः सः असहनयाः उक्तवान्`. Emitted `{sug-del:असहनयाः}{sug-ins:असहनतया}` (he spoke out of impatience, instr. of manner); alternative `असहनः` (impatient, nom. sg. adj. on सः). | low* | User decision on the intended word |

## Coverage

p038:P1 {x-com: layout} : skip layout-only chunk
p038:P2 # सञ्चयप्रवृत्तिः : skip title chunk
p038:P3 कमलायाः नारायणस्य : clean
p038:P4 सा पतिम् : clean
p038:P5 "सम्पूर्णं महागुच्छं : clean
p038:P6 यदि वयम् : F1
p038:P7 काणि। तस्यैव : clean
p038:P8 नारायणः तस्याः : clean
p038:P9 महता कष्टेन : F2, F3
p038:P10 अर्धमार्गपर्यन्तं नारायणः : clean
p038:P11 भारवाहद्वारा महागुच्छः : clean
p038:P12 {author: सुभद्रा}{pgb} : skip metadata chunk
p039:P1 {x-com: layout} : skip layout-only chunk
p039:P2 सन्तुष्टा। : clean
p039:P3 अनन्तरदिनात् आरभ्य : clean
p039:P4 तदा कमला : clean
p039:P5 कदलीफलानि खादन् : U1
p039:P6 शिष्टानि सन्ति : clean
p039:P7 किन्तु कमला : clean
p039:P8 द्वित्रेषु दिनेषु : clean
p039:P9 वस्तुतः कमला : clean
p040:P1 {x-com: layout} : skip layout-only chunk
p040:P2 खादितवन्तौ। एतावता : clean
p040:P3 किन्तु एतस्य : clean
p040:P4 नारायणः पत्नीं : clean
p040:P5 "अस्तु नाम। : clean
p040:P6 "उपवासकारणतः पुनः : clean
p040:P7 वैद्यः रूप्यकद्वयं : F4, F5
p040:P8 गुलिकायाः स्वीकारणेन : clean
p040:P9 अन्ते नारायणः : clean
p040:P10 बहिः आगत्य : clean
J1 p038:P6 {wb} -> p038:P7 {pc} (continues) : ok
J2 p038:P11 {pb} -> p039:P2 {pc} (continues) : ok
J3 p039:P5 {wb} -> p039:P6 {pc} (continues) : ok
J4 p039:P9 {pb} -> p040:P2 {pc} (continues) : ok
J5 p040:P6 {pb} -> p040:P7 fresh (clean break) : ok
J6 p040:P10 {pb} -> END (clean break) : ok
