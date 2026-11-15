# Proofread report: 1987_02 p041 (चतुरः तन्तुवायः, scans 41-42)

## Summary

No findings, no verdict blocks, no held `{sug-}` candidates: the file is byte-identical to the extract gate pass except one inline `{x-com:}` commentary flag. Both lint gates pass with 0 story findings, the orth scanner reports 0 hits, and all four joints verify clean. One sub-high-confidence grammar observation (व्यवस्थम् for expected व्यवस्थाम्, p41:P10) is flagged via `{x-com:}` only, with no block, since Phase A left no glyph anchor on file. Loc below is keyed on story coordinates `pNN:Pm` plus the first two words as anchor, words counted on the chunk from 1.

## Findings

No findings.

## Patterns

None.

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| U1 | p41:P10 ("तस्य सर्वस्य", w3) | `व्यवस्थम्` | `व्यवस्थाम्` (?) | MRP | likely | medium | व्यवस्था is feminine, so the accusative should be व्यवस्थाम्; needs dictionary/tool check to exclude author license, and no verdict block is emitted since Phase A left no glyph anchor on file |

## Coverage

p41:P1 {x-com:layout:} : skip layout-only chunk
p41:P2 चतुरः तन्तुवायः : skip title
p41:P3 पूर्वं कश्चन : clean
p41:P4 राजा मन्त्रिणः : clean
p41:P5 मन्त्रिणः एतस्य : clean
p41:P6 एतेन भीताः : clean
p41:P7 {pc}प्रतीक्षमाणाः आसन् : clean
p41:P8 मन्त्रिणः अन्यं : clean
p41:P9 "किं भोः : clean
p41:P10 "तस्य सर्वस्य : x-com note (see U1), no block
p41:P11 "आश्चर्यकरम् एतत् : clean
p41:P12 {note:} : skip metadata
p42:P1 {x-com:layout:} : skip layout-only chunk
p42:P2 {pc}शक्नोति वा : clean
p42:P3 "का सा : clean
p42:P4 तन्तुवायः किञ्चित्कालं : clean
p42:P5 तन्तुवायः महाराजं : clean
p42:P6 दूतः स्वकीयकोशात् : clean
p42:P7 तन्तुवायः मन्दहासपूर्वकम् : clean
p42:P8 "एतत् सर्वं : clean
p42:P9 "अत्र कोऽपि : clean
p42:P10 "साधु! साधु : clean
p42:P11 "हन्त! एवं : clean
J1 p041:P6 {pb} -> p041:P7 {pc} : ok (पक्षिणः प्रतीक्षमाणाः आसन्, spaced join)
J2 p041:P11 {pb} -> p042:P2 {pc} : ok (वक्तुं शक्नोति वा, page-turn speech continuation, mate held on {pc} side per Phase A rule)
J3 p042:P8 {pb} -> p042:P9 fresh : ok (clean column break, new speech)
J4 p042:P11 {pb} -> END : ok (story end, clean break)
