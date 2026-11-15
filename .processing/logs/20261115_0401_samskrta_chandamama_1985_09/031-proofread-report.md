# Proofread report: 1985_09 p031 (धनिकस्य दुराशा, pp. 31-32)

## Summary

Story `धनिकस्य दुराशा` (pp. 31-32, 20 body chunks across 2 page spans) proofread with images closed. Three verdicts issued as blocks in the story file: one missing opening quote supplied (F1), one stray single deleted (F2), one case correction दृष्टि to दृष्टिं (F3). No held candidates, no unverified items, no flow ruptures: all four joints show unique grammatical fit and the plot arc (debt, quest, magic conch, greedy condition, self-blinding wager, restoration) reads continuously. Orth scanner (`scan.py orth`) reported zero hits; the text is a manual transcription, not OCR output. Loc below is `pNN:Pm:wk` (page span, chunk, word counted on the chunk from 1, blocks excluded) plus anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p031:P11:w29 (योगी तु) `पृष्टवान्-सहोदर!` | `पृष्टवान्-सहोदर! कुत्र गच्छति"।` | `{ins:"}` before `सहोदर` | STY | likely | high | Opening double quote dropped in print; close present and पृष्टवान् reports direct speech, so position and sort are certain (hugging dash kept as printed) |
| F2 | p032:P10:w16 ('धनिकः केन) `प्रार्थितवान्' "मम` | `प्रार्थितवान्'` | `{del:'}` | STY | likely | high | Lone single has no mate under nesting rules while the rest of the para is balanced with correct sorts (thought in singles, speech in doubles) |
| F3 | p032:P11:w9 (एतेन भीतः) `पुनः दृष्टि प्राप्तवान्` | `दृष्टि` | `दृष्टिं` | OCR | error | high | प्राप् takes the accusative and दृष्टिम् is the unique fit; print verified dotless at 3x-5x against crisp p31 दृष्टिं, so one dropped anusvara |

## Patterns

Avagraha omission in `o + a` junctions is a house variant, not flagged: `इतोडपि` (p031:P11:w9) and `ततोडपि` (p032:P8:w9) print without avagraha while `कोऽपि` (p031:P12) prints it. Sandhi openness mixes throughout (`तत्सर्वं` joined vs `तत् सर्वं`-style spacing elsewhere, `रोटिकां` vs `रोटिकाम्` before a vowel) and stands as seen.

## Unverified

None. No `{sug-}` candidates were emitted or kept; every ruling above is high confidence from text, sort and story sense.

## Coverage

p031:P1 {x-com:layout:} : skip layout declaration, read-only in this phase
p031:P2 धनिकस्य दुराशा : skip title block, single title for the story
p031:P3 कस्मिंश्चित् ग्रामे : clean
p031:P4 एकदा रामनाथः : clean
p031:P5 धनिकः उदासीनभावनया : clean
p031:P6 रामनाथः धनिकस्य : clean
p031:P7 रामनाथः मार्गे : clean
p031:P8 मेलितुं प्रस्थितः : clean
p031:P9 ब्राह्मणः रोटिकां : clean
p031:P10 रामनाथः ततः : clean
p031:P11 योगी तु : F1
p031:P12 रामस्य सकाशात् : clean
p031:P13 reprint note : skip footer metadata, contents proofread as seen
p032:P1 {x-com:layout:} : skip layout declaration, read-only in this phase
p032:P2 पृष्टवान् रामनाथः : clean
p032:P3 निर्धनः मन्दहासं : clean
p032:P4 सः वृद्धः : clean
p032:P5 एवंस्थिते एकदा : clean
p032:P6 शङ्खः प्राप्तः : clean
p032:P7 इति पृष्टवान् : clean
p032:P8 शङ्खम् अहं : clean
p032:P9 अनिवार्यतया रामनाथः : clean
p032:P10 'धनिकः केन : F2
p032:P11 एतेन भीतः : F3
J1 p031:P7 {pb} -> p031:P8 {pc} : ok (रामेण + मेलितुं unique fit, column order confirmed)
J2 p031:P12 {pb} -> p032:P2 {pc} : ok (इति + पृष्टवान् completes the report)
J3 p032:P6 {pb} -> p032:P7 {pc} : ok (ददातु + इति completes the demand)
J4 p032:P11 {pb} -> END : ok (clean break on terminal danda, story ends here)
