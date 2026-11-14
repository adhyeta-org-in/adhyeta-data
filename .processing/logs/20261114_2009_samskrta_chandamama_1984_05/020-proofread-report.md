# Proofread report: 1984_05 p020 (उत्कोचग्राही, single scan page)

## Summary

Loc below is story-coordinate `pNN:Pm` plus anchor words, words counted on the chunk from 1 (Chandamama delta; `---` tokens counted). One verdict applied for a print quote-sort mismatch (F1, single open `'` against double close `"` in an assembly address, corrected to `"` on era-standard plus matching-close evidence); one print-punctuation keep documented (F2, `?` outside the closing quote). No inherited `{sug-ins:}`/`{sug-del:}` queue existed. The `orth` scanner gave one low hit (terminal `॥` flagged verse-candidate) dismissed as the prose story closer. Nothing held for the user; text is otherwise clean.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p020:P5 'महाराज (w48) | `--- 'महाराज! श्रीपतिः यत् आरोपणं कृतवान् तत् सत्यम् एव"।` | `{del:'}{ins:"}महाराज! ... एव"।` (applied in file) | STY | style | high | Spoken assembly address takes era-standard DQ; reporting verb `उक्तवान् ---` opens it and the print close is DQ, so the single open is a dropped stroke. |
| 2 | p020:P6 बन्धनम्'? (w7) | `'किमर्थं मम बन्धनम्'? इति` | keep print order (no block) | STY | style | high | Print puts `?` outside the closing quote; sense is unambiguous and print marks stand where no mark is missing. |

## Patterns

Open word-junction orthography kept throughout as house style (print mixes `तद्दिने` with `तद् आरोपणं`, keeps visarga/halant before vowels and voiced initials): `तद् आरोपणं`, `माम् एव`, `भवान् एव`, `भवान् मम`, `अस्मिन् व्यवहारे`, `निर्णयः एव`, `देव्याः निर्णयः`, `श्रीपतिः, सहोद्योगिनः` — 8+ instances, no blocks per print-fidelity doctrine. Mixed `तद्दिने`/`तद्` on the same page confirms the house mix is intentional print behavior, not damage.

## Unverified

None held. Every candidate above was decided from text, house style, and story sense; no word-level window required re-segmentation hypotheses.

## Coverage

p020:P3 विदिशा नाम : clean
p020:P4 'अनुग्रहः अपि : clean
p020:P5 तद्दिने रात्रौ : F1
p020:P6 राजा कर्कटशास्त्रिणः : F2
J1 p020:P6 {pb} -> END (clean break) : ok
