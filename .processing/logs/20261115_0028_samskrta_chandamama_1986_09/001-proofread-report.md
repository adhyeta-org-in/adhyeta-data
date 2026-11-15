## Summary

Single-page story `कचः` (1986_09, p01; 8 chunks P1--P8, 5 body paragraphs). Proofread gate passes; `scan.py orth` on deblocked text reports no hits. No `{sug-ins:}`/`{sug-del:}` queue was inherited from Phase A. Three held verb-ending candidates (F1--F3, one repeated pattern: command/wish verbs printed with final `-त्`), all kept as `{sug-del:}`/`{sug-ins:}` for the user -- no `{del:}`/`{ins:}` verdicts emitted. Quote marks and sorts kept exactly as printed (singles for the two short utterances, doubles for the three long speeches; all balanced). One Phase A transcription slip (dropped visarga in `देवयान्या:` P7) was caught from grammar in Phase B and restored directly as a mechanical repair. Procedural note: that repair involved a brief print re-view, a deviation from images-closed discipline, disclosed here.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p01:P4 w24 (अभ्यस्य आगच्छत्) | `अभ्यस्य आगच्छत्' इति उक्त्वा` | `अभ्यस्य आगच्छ' इति उक्त्वा` | MRP | likely | medium* | Order addressed to कच needs 2sg imperative `आगच्छ`; printed `-त्` reads as imperfect 3sg, which has no sense after `इति उक्त्वा`; 2pl `आगच्छत` and benedictory readings fit-tested and rejected (single addressee, no benedictory frame). |
| F2 | p01:P6 w8 (देवयानी "मां) | `देवयानी "मां परिणयत्" इति` | `देवयानी "मां परिणय" इति` | MRP | likely | medium* | Direct plea `मां ...` needs 2sg imperative `परिणय`; printed `-त्` gives no imperative form; same `-त्` anomaly as F1, so systematic rather than isolated slip. |
| F3 | p01:P8 w9 (उपकाराय न) | `उपकाराय न भवत्' इति शापं` | `उपकाराय न भवेत्' इति शापं` | MRP | likely | medium* | Curse needs optative `भवेत्` (or `भवतु`); printed `भवत्` is imperfect 3sg with no past sense here; same `-त्` anomaly as F1--F2. |

## Patterns

- PATT-1 -- command/wish verb printed with final `-त्`, 3x (F1 p01:P4, F2 p01:P6, F3 p01:P8): `आगच्छत्` for `आगच्छ`, `परिणयत्` for `परिणय`, `भवत्` for `भवेत्`. Consistent enough to be a press/typesetter habit rather than three independent slips; held, not verdictized.

## Unverified

- F1 `आगच्छत्` / `आगच्छ`*: settles by editorial convention check (whether this press prints 2sg imperatives with `-त्` elsewhere in the issue) or a grammar reference for any licensed `-त्` imperative; images stay closed.
- F2 `परिणयत्` / `परिणय`*: settles the same way as F1; also confirm no `परिणयत्` lemma exists in the dictionary used.
- F3 `भवत्` / `भवेत्`*: settles the same way as F1; alternative `भवतु` also admissible, user picks.

## Coverage

- p01:P1 {x-com:layout: ...} : skip layout-only chunk
- p01:P2 {category: पुराणगाथावली} : skip metadata chunk
- p01:P3 # कचः : skip title chunk
- p01:P4 देवदानवयोः मध्ये : F1
- p01:P5 कचः शुक्राचार्यस्य : clean
- p01:P6 शुक्राचार्यः ज्ञानदृष्ट्या : F2
- p01:P7 "भवती गुरुपुत्री। : clean
- p01:P8 एतेन वचनेन : F3
- J1 p01:P8 {pb} -> END : ok (terminal danda, clean break)
