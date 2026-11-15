# Proofread report: 1985_10 p035 (नारिकेलचोरः, scans 35–37)

## Summary

Two findings, both held candidates (CNS, likely, low*): the fellow-cheat's name reads अलीमः once against अलमः/अलमम् five times elsewhere, and the agreement to सलीमः's own proposal is attributed to सलीमः himself. No systematic defects; quotes balance, all six joints form valid words or sentences, and the orth scanner reports zero hits. Loc is pNN:Pm:word (3-digit scan tag per lint, chunk within span, word counted on the deblocked chunk from 1); chunk anchors use the first two words. The text is hand transcription, not OCR; nothing was left unchecked.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p035:P4:6 [सिन्धानगरे सलीमः] | `अलीमः तस्य स्नेहितः` | `अलमः तस्य स्नेहितः` | CNS | likely | low* | same name spelled अलमः/अलमम् five times elsewhere (p036:P4, p036:P9, p037:P2, p037:P3) |
| F2 | p036:P10:5 ["समीचीना आलोचना"] | `उक्तवान् सलीमः` | `उक्तवान् अलमः` | CNS | likely | low* | सलीमः proposed the plan to अलमः, so the agreer should be अलमः, not सलीमः himself |

## Patterns

None (no repeats).

## Unverified

F1: print re-check of scan 35 (ली vs ल at अलीमः/अलमः) and of the अलमः occurrences would settle the intended name; onomastics favours अलीमः (pairs with सलीमः) while the 5:1 majority favours अलमः. F2: print re-check of scan 36 (स vs अ at the agreer) would settle whether the print misattributes the agreement or the transcription misread it.

## Coverage

p035:P1 {x-com:layout:} : skip x-com-only chunk
p035:P2 # नारिकेलचोरः : skip title chunk
p035:P3 सिन्धानगरे दावूदः : clean
p035:P4 सिन्धानगरे सलीमः : F1
p035:P5 दावूदस्य स्वभावम् : clean
p035:P6 नीयं च' : clean
p035:P7 एकदा दावूदः : clean
p035:P8 मध्याह्ने दावूदः : clean
p035:P9 सरलः दावूदः : clean
p035:P10 {category:} : skip metadata chunk
p036:P1 {x-com:layout:} : skip x-com-only chunk
p036:P2 वान् एव। : clean
p036:P3 ततः प्रस्थाय : clean
p036:P4 दावूदः धर्मशालायाः : clean
p036:P5 धर्मशालातः भोजनालयं : clean
p036:P6 तदा दावूदः : clean
p036:P7 दावूदस्य वचनेन : clean
p036:P8 चिन्तयित्वा तौ : clean
p036:P9 तदा सलीमः : clean
p036:P10 "समीचीना आलोचना" : F2
p036:P11 "किम् आनीतवान् : clean
p037:P1 {x-com:layout:} : skip x-com-only chunk
p037:P2 "रोटिकां क्षीरं : clean
p037:P3 तदा अलमः : clean
p037:P4 'समीचीना सूचना। : clean
p037:P5 अनन्तरं तौ : clean
p037:P6 वस्तुतः तयोः : clean
p037:P7 आसीत्। आहारार्थं : clean
p037:P8 सहप्रवासिनोः मरणेन : clean
p037:P9 तदा तत्रत्याः : clean
p037:P10 तेषां वचनेन : clean
J1 p035:P5 {wb} -> p035:P6 {pc} : ok (सम्पादनीयं joins solid)
J2 p035:P9 {wb} -> p036:P2 {pc} : ok (ज्ञातवान् joins solid)
J3 p036:P7 {pb} -> p036:P8 {pc} : ok (इति चिन्तयित्वा joins spaced)
J4 p036:P11 {pb} -> p037:P2 fresh : ok (complete sentence, new paragraph)
J5 p037:P6 {pb} -> p037:P7 {pc} : ok (समानम् आसीत् joins spaced)
J6 p037:P10 {pb} -> END : ok (story ends on complete sentence)
