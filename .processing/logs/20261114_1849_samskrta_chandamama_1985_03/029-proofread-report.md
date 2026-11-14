## Summary

Story `p029` (1985_03, scan 29, `प्रामाणिकता`) proofread images-closed: 5 verdicts applied as blocks (all `STY`/error/high — single-opened long speeches promoted to era-standard doubles and three role-less stray singles deleted), 4 held `SPL`/likely/medium* print-suspect words kept as `{sug-…}` candidates. Both gates pass with 0 error paras; `scan.py orth` on deblocked text reports no findings. Loc below is keyed `pNN:Pm` (scan-sequence page + chunk number matching lint `P` numbers) plus the first two words as anchor, counting words on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p29:P4 'तथा अस्तु w11 | `'{sug-ins:'}यः` | `{del:'}{ins:"}यः` | STY | error | high | long minister-speech opens single where era standard and readability require `"` (reporting verb + `इति`-closure pin the sort) |
| F2 | p29:P4 'तथा अस्तु w37 | `कथम्?{sug-del:'}"` | `कथम्?{del:'}"` | STY | error | high | stray single beside a complete `"` close has no open and no role; double pair stands |
| F3 | p29:P5 "तत् तु w30 | `आगच्छन्तु{sug-del:'}"` | `आगच्छन्तु{del:'}"` | STY | error | high | stray single beside a complete `"` close has no open and no role; double pair stands |
| F4 | p29:P8 तदा सचिवः w3 | `'{sug-ins:'}कोशाधिकारिद्वारा` | `{del:'}{ins:"}कोशाधिकारिद्वारा` | STY | error | high | long secretary-speech opens single where era standard and readability require `"` (reporting verb + `इति`-closure pin the sort) |
| F5 | p29:P8 तदा सचिवः w36 | `नास्ति {sug-del:'}"` | `नास्ति {del:'}"` | STY | error | high | stray single beside a complete `"` close has no open and no role; double pair stands |

## Patterns

Quote-sort drift at speech boundaries (4x: F1/F2 open-single vs double-close, F4/F5 same shape): the compositor opens two long speeches with a single stroke where the era standard prints doubles; corrected once per speech, close counted with its open.

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why | Settles by |
|---|---|---|---|---|---|---|---|---|
| H1 | p29:P3 केतकी-कासारः इति w13 | `{sug-del:पञ्चिवर्षपर्यन्तम्}{sug-ins:पञ्चवर्षपर्यन्तम्}` | `पञ्चवर्षपर्यन्तम्` | SPL | likely | medium* | extra `ि` on `पञ्च` yields no valid word; classical form drops it | user accept/reject at compile |
| H2 | p29:P3 केतकी-कासारः इति w40 | `{sug-del:तत्सहशम्}{sug-ins:तत्सदृशम्}` | `तत्सदृशम्` | SPL | likely | medium* | `सहश` is no word for "like him"; `सदृश` fits sense exactly | user accept/reject at compile |
| H3 | p29:P5 "तत् तु w8 | `{sug-del:केतकीकासरग्रामं}{sug-ins:केतकीकासारग्रामं}` | `केतकीकासारग्रामं` | SPL | likely | medium* | short `कासर` against three in-story `कासार` forms (title line, P5 w13, P7) breaks proper-noun consistency | user accept/reject at compile |
| H4 | p29:P6 एकसप्ताहानन्तरं दश w29 | `{sug-del:परेयुः}{sug-ins:परेद्युः}` | `परेद्युः` | SPL | likely | medium* | `परेयुः` is no word for "next day"; dropped `द्` is the smallest fix | user accept/reject at compile |

No Phase A `{x-com:}`/`{sug-…}` marked these four words, so per Phase B doctrine no verdict block issues on bare text evidence; all four ship held. Short-directive singles `'तथा अस्तु'` (P4) kept as seen per house style (cf. 021 short directives), no block.

## Coverage

p29:P3 केतकी-कासारः इति : H1, H2
p29:P4 'तथा अस्तु : F1, F2
p29:P5 "तत् तु : F3, H3
p29:P6 एकसप्ताहानन्तरं दश : H4
p29:P7 तेषु अभ्यर्थिषु : clean
p29:P8 तदा सचिवः : F4, F5
J1 p029:P8 {pb} -> END (clean break) : ok
