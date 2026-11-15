# Proofread report: 1986_07 p009 (आधिक्यम्), RUN 20261115_0027_samskrta_chandamama_1986_07

## Summary

Single-page complete story, 6 body paras (P3--P8); extract gate and proofread gate both pass (exit 0). Two findings, both `likely` / `medium*` (unverified): the 1pl verbs `आयोजयाम` and `सङ्गृह्णीम` in the same speech lack the expected `-मः` visarga, held as `{sug-ins:ः}` candidates since Phase A left no glyph flag. No inherited Phase A candidates existed (queue was empty) and the orth scanner reports zero hits. Loc below is word-level `pNN:Pm:w` (NN = scan sequence, Pm = lint chunk number, w = whitespace-token index on the chunk) plus a two-word anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p09:P4:10 (`एतत् ज्ञात्वा`) | `सङ्गीतगोष्ठीम् आयोजयाम।` | `आयोजयामः` (`{sug-ins:ः}` in file) | MRP | likely | medium* | 1pl verb with `वयं` subject needs `-मः`; no clause re-segmentation fits another subject. |
| F2 | p09:P4:16 (`एतत् ज्ञात्वा`) | `धनं सङ्गृह्णीम"` | `सङ्गृह्णीमः` (`{sug-ins:ः}` in file) | MRP | likely | medium* | Same 1pl `-मः` ending missing in the same speech; `गृह्णीमः` is the expected 1pl form. |

## Patterns

- 1pl `-मः` printed as bare `-म` (×2, F1--F2, both in the ग्रामज्येष्ठ speech at p09:P4): either a compositor slip repeated in one speech or an author habit; visargas are otherwise printed correctly throughout the story, so this is not a house style.

## Unverified

- F1 `आयोजयाम` vs `आयोजयामः`: glyph absence verified at 3x in Phase A with no flag, but no verified correction without a Phase A note, so held. Settles by: comparing 1pl verb printings in other 1986_07 stories, or a second-reader check of the scan at higher magnification.
- F2 `सङ्गृह्णीम` vs `सङ्गृह्णीमः`: same as F1; additionally confirm the root reading (`ग्रह्` 1pl `गृह्णीमः`) against a dictionary/Heritage check.
- Quote pass (text-only, images closed): all six quote pairs balance; outer `"` marks reported speech (`उक्तवान् --- "..." इति`), inner `'` marks the thought/resolve in P3 and the quoted undertaking inside the long speech in P7 (`'देवकार्यम् ... अपेक्षितम्'`), nesting `DQ SQ ... SQ DQ` valid; no blocks needed.
- Sandhi openness (`तेभ्यः धनं`, `ये आगच्छन्ति`, `तदर्थं धनं`) read as Chandamama house variants per doctrine, never flagged; proper nouns (गोविन्दार्यः, चक्रपाणिः, सोमदत्तः) spell consistently (CNS clean).

## Coverage

p09:P1 {x-com:layout: 1col, : skip x-com-only
p09:P2 # आधिक्यम् : skip title
p09:P3 'स्वग्रामस्य रामदेवालयस्य : clean
p09:P4 एतत् ज्ञात्वा : F1, F2
p09:P5 तस्मिन् ग्रामे : clean
p09:P6 सोमदत्तः तु : clean
p09:P7 सप्ताहानन्तरं सङ्गीतगोष्ठी : clean
p09:P8 सोमदत्तः लज्जया : clean
J1 p009:P8 {pb} -> END (clean break) : ok
