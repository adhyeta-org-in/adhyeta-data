## Summary

Phase B proofread of `p019.md` (1984_09, scan 19, new story "स्पर्धा"). Proofread gate passes with 0 errors and 0 story findings; `scan.py orth` reports 0 hits. 9 findings, all `STY` quote-punctuation verdicts (severity `likely`, confidence `high`): the print sets speech opens as lone singles (once as `'`+`"` with a stray single) and closes as doubles, with one speech missing its open entirely. All 9 land as `{ins:}`/`{del:}` blocks pinned by reporting verbs (`उक्तवान्`, `उक्तवती`, `पृष्टवान्`, `इति`-closures). No `{sug-…}` queue was inherited from Phase A; no held candidates. Text is manual transcription, not OCR; nothing was left unchecked. `Loc` is `pNN:Pm:word` (word index within the chunk) plus anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p019:P3:21 (उक्तवान् मोः) | `उक्तवान् --- मोः!` | `{ins:"}मोः!` | STY | likely | high | speech after reporting verb has no open mark; `इति` closes it |
| 2 | p019:P3:35 (आगच्छामि एव) | `एव' इति।` | `एव{del:'}{ins:"} इति।` | STY | likely | high | speech close must be double like every other speech close; lone stroke is a dropped second stroke |
| 3 | p019:P4:14 (उक्तवती किमर्थं) | `--- 'किमर्थं` | `--- {del:'}{ins:"}किमर्थं` | STY | likely | high | wife's speech opens single but closes double; sort corrected to house double |
| 4 | p019:P5:18 (आगच्छामि एव) | `एव', इति` | `एव{del:'}{ins:"}, इति` | STY | likely | high | speech close must be double; comma stays outside the close |
| 5 | p019:P6:1 (इदानीं किमर्थं) | `'इदानीं` | `{del:'}{ins:"}इदानीं` | STY | likely | high | wife's speech opens single but closes double; sort corrected to house double |
| 6 | p019:P8:17 (पृष्टवान् जगन्नाथः) | `--- '"जगन्नाथः` | `--- {del:'}"जगन्नाथः` | STY | likely | high | stray single before the double open has no possible mate; single speech span takes one double pair |
| 7 | p019:P9:1 (आम् अहं) | `'"आम्,` | `{del:'}"आम्,` | STY | likely | high | stray single before the double open has no possible mate |
| 8 | p019:P9:10 (महोपाध्यायस्य गृहं) | `'"महोपाध्यायस्य` | `{del:'}"महोपाध्यायस्य` | STY | likely | high | stray single before the double open has no possible mate |
| 9 | p019:P10:1 (एवं वा) | `'"एवं` | `{del:'}"एवं` | STY | likely | high | stray single before the double open has no possible mate |

## Patterns

1. Asymmetric print quote setting (9 spans): opens set as lone `'` (F3, F5) or `'`+`"` with a stray single (F6-F9), closes as `"` (F2-F5), one open missing entirely (F1). All ruled as speech doubles per reporting-verb + `इति` pinning.

## Unverified

None.

## Coverage

p019:P1 {x-com:layout:} : skip layout declaration
p019:P2 # स्पर्धा : skip title
p019:P3 एकः ग्रामः : F1, F2
p019:P4 परन्तु रात्रौ : F3
p019:P5 "भवती मां : F4
p019:P6 'इदानीं किमर्थं : F5
p019:P7 पतिपत्न्योः मध्ये : clean
p019:P8 सः ग्रामतः : F6
p019:P9 '"आम् अहं : F7, F8
p019:P10 '"एवं वा : F9
p019:P11 {misc:} : skip footer metadata
J1 p019:P6 {pb} -> p019:P7 fresh (clean break) : ok
J2 p019:P10 {pb} -> END (clean break) : ok
