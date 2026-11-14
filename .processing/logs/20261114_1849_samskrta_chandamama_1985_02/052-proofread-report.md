## Summary

3 findings, all severity error with high confidence (F1 case government, F2 vowel length in ल्यप्, F3 dropped anusvāra), each a single-word verdict on P9-P10 with no wording otherwise changed. No systematic repeats, no held candidates, no flow rupture; quotes are balanced doubles throughout and need no verdicts. Scanner orth run clean; the story was read sentence by sentence for continuity; proper nouns (भूपालः, वरप्रसादः, राघवः, नारायणः) are consistent. Text is a print-faithful manual transcription, not OCR output. Loc below is story coordinates p052:Pm plus word number counted on the chunk from 1 (whitespace split, blocks attached), with the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p052:P9 w3 (मार्गे राघवः) | `भूपाल पृष्टवान्` | `भूपालम् पृष्टवान्` | KRK | error | high | प्रच्छ् takes the person asked in the accusative, so the object of पृष्टवान् needs भूपालम् |
| F2 | p052:P9 w9 (मार्गे राघवः) | `उत्थय` | `उत्थाय` | SPL | error | high | ल्यप् of उद्-स्था is उत्थाय with long आ, not short अ |
| F3 | p052:P10 w9 (स्वगृहस्य कन्यायाः) | `इव तूष्णी स्थितवन्तः` | `इव तूष्णीं स्थितवन्तः` | OCR | error | high | adverbial तूष्णीम् needs the anusvāra; bare तूष्णी cannot stand with सर्वे |

## Unverified

None. No word was held: भूपतिः beside भूपालः is a common-noun synonym rather than a proper-name inconsistency, निषिध्यमानः reads as the passive participle agreeing with भूपालः, and the locative absolute अपमाने प्रवृत्ते plus the या-तस्याः correlative are grammatical as printed.

## Coverage

p052:P1 {x-com: layout} : skip layout-only chunk
p052:P2 # अवमानः : skip title chunk
p052:P3 कमलपुरस्य निवासी : clean
p052:P4 अनन्तरं सः : clean
p052:P5 वरप्रसादः पुत्रीं : clean
p052:P6 स च : clean
p052:P7 मया बहुवार : clean
p052:P8 तदा वरप्रसादमहोदय! : clean
p052:P9 मार्गे राघवः : F1, F2
p052:P10 स्वगृहस्य कन्यायाः : F3
J1 p052:P10 {pb} -> END (clean break) : ok
