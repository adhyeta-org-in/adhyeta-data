# Proofread report: 1987_03, story p001 (p. 1, "रजिः")

## Summary

Phase B (images closed) on `.processing/samskrta_chandamama/1987_03/p001.md`. One held unverified candidate (U1: unclear print ligature in the opening epithet `वीरार्गधवीरः`, kept as a `{sug-del:}/{sug-ins:}` pair with best-guess replacement); zero verified verdicts, so the story text is otherwise byte-identical to the Phase A extract. Orth scan (`scan.py orth`) on deblocked text: zero hits. Word/sandhi/morphology/syntax, quote, and joint-flow passes: zero findings. Loc key: story coordinates `pNN:Pm` (chunk numbers per lint) plus first-two-word anchor; word counts counted on the chunk excluding blocks. Text is human transcription, not OCR output; the edition's systematic open visarga across word boundaries (`जयः न`, `उक्तः विषयः`, `राक्षसाः एतत्`) is kept throughout as a Chandamama house-style variant, never flagged.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| (none) | | | | | | | |

No `{del:}`/`{ins:}` verdict blocks were added to the story file. Print quote sorts are kept as seen: doubles for all five spoken exchanges (p001:P5/P6/P7/P8/P10/P11), balanced with no nesting; sense does not force any change, so nothing was supplied or re-sorted. Open accusatives before consonants (`अपेक्षां निवेदितवन्तः`, `युद्धे साहाय्यं`, `महाराजस्थानं दातुम्`) and the honorific genitive `भवतां` for the second person are kept as house-style variants. `पूरूरवसः` (genitive of the s-stem `पूरूरवस्`), `रजेः` (genitive of the i-stem `रजि`), `निवेदितवन्तः`, `तृप्त्या`, and the `तव्य`-predicate `भवता ... स्थातव्यम्` all read as grammatical in context, and correlatives (`यस्मिन् ... तस्यैव`) resolve cleanly — Phase B invents no new glyph claims.

## Patterns

(none)

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| U1 | p001:P4 w5 (चक्रवर्तिनः पूरूरवसः) | `रजिः वीरार्गधवीरः इति` | `वीराधवीरः` ? | LEX | likely | low* | print ligature unclear at 4x with no certain reading; tried clause-level re-segmentation `वीराधवीरः` (hero of heroes) and `वीराग्रवीरः` (foremost hero) against the `तत्समानः वीरः कोऽपि न` context, neither fits with confidence; held for the user, file keeps print span as `{sug-del:वीरार्गधवीरः}{sug-ins:वीराधवीरः}` |

## Coverage

p001:P1 {x-com:layout:} : skip x-com-only chunk
p001:P2 {category: पुराणगाथावली} : skip metadata chunk
p001:P3 # रजिः : skip title
p001:P4 चक्रवर्तिनः पूरूरवसः : U1
p001:P5 कदाचित् देवदानवयुद्धे : clean
p001:P6 "रजिः यस्मिन् : clean
p001:P7 ब्रह्मणा उक्तः : clean
p001:P8 "जयप्राप्तेः अनन्तरं : clean
p001:P9 अनन्तरं देवाः : clean
p001:P10 देवदानवयोः घोरं : clean
p001:P11 "देवाः भवन्तः : clean
J1 p001:P11 {pb} -> END (clean break) : ok (P11 ends terminal ।, story span ends here)
