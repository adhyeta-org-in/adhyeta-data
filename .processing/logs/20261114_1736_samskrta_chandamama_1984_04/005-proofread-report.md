# Proofread report — 1984_04, START=005 (scan pages 5–12, story `त्रयः मान्त्रिकाः`, serial continues with `(अनुवर्तते)`)

## Summary

0 findings: no high-confidence error met the bar for a story-file block, so the story file is byte-identical to its extract-gate state (no `{del:}`/`{ins:}`/`{sug-…}` added). No systematic problem found; proper nouns are consistent in the body (`पद्मपाद`, `पिङ्गल`, `भल्लूककेतु`) with one recap-bracket spelling variant noted but kept as print (U3). `scan.py orth` on deblocked text reports 2 hits, both dispositioned as print-faithful (double `॥` after `इति` is the printer's close; `!` in `उत्सवः!` is a genuine exclamation). Text is fresh human transcription from scans (not OCR output). Loc below is `pNN:Pm` (scan span + lint chunk) with the first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
(none — every sub-threshold item is held in Unverified without a file block)

## Patterns

Variants kept as seen, no findings: recap-bracket `भल्लूकेकेतुम्` beside body `भल्लूककेतुम्` (proper-noun openness in a summary reprint); prohibitive `मास्तु` for `मा + अस्तु` throughout; interjection `हं हो` kept as printed; five-dot run `.....।` in p012:P5 kept as the print ellipsis; `इति ॥` double-danda closes kept (p006:P8); exclamation `!` and question `?` attached without preceding space per house lint.

## Unverified

U1 p006:P6 `आर्य, पद्मपादमहोदय`: `आर्य` (vocative of `आर्य`, respected one) is the expected address, but the file reads `आर्य`; rेफ placement is a glyph question and the images stay closed in this phase, so no block is filed — settle from house usage of `आर्य` elsewhere in the issue.
U2 p005:P4 `कूर्दमानाः नृत्यन्तः`: root `कूर्द्` (to leap) fits leaping-dancing pisachas, but no dictionary check was run; if `कूर्दमान` is unlexical, the print may read `कुर्दमान` or similar — settle from the lexicon, not from a re-read.
U3 p005:P3 `भल्लूकेकेतुम् आनेतुं`: recap bracket spells the name with `-के-` (`भल्लूकेकेतुम्`, twice) against body `भल्लूककेतुम्`; kept as a print variant, but a compiler normalizing names should pick the body form.

## Coverage

p005:P1 skip layout-only chunk
p005:P2 skip title chunk
p005:P3 [महामायस्य अद्भुतशक्तयः : clean
p005:P4 "इतः परं : clean
p005:P5 जुगुप्सितः भल्लूककेतुः, : clean
p006:P1 skip layout-only chunk
p006:P2 पिशाचान् नियमयन् : clean
p006:P3 पिङ्गलः निरुत्तरः : clean
p006:P4 अनेन भवतः : clean
p006:P5 "हं हो! : clean
p006:P6 तावति काले, : U1
p006:P7 "किं तत्?" : clean
p006:P8 "भल्लूकेकेतोः तु : clean
p006:P9 एतत् वचनं : clean
p007:P1 skip layout-only chunk
p007:P2 अन्ये केचन : clean
p007:P3 "एवं वा? : clean
p007:P4 "मनुष्येषु इव : clean
p007:P5 "एषः क्रमः : clean
p007:P6 केचन गजरूपं : clean
p007:P7 एवं किञ्चित्कालम् : clean
p008:P1 skip layout-only chunk
p008:P2 उक्तवान् --- : clean
p008:P3 मृत्युभयात् विमोचिताः : clean
p008:P4 गतवन्तः। : clean
p008:P5 पद्मपादः प्रसन्नवदनः : clean
p009:P1 skip layout-only chunk
p009:P2 पिङ्गलः "तथैव : clean
p009:P3 पद्मपादः एकं : clean
p009:P4 पिङ्गलः समयमानः : clean
p009:P5 गर्दभः तौ : clean
p009:P6 अरण्यानि, पर्वताः, : clean
p009:P7 पद्मपादस्य वाहनभूतः : clean
p010:P1 skip layout-only chunk
p010:P2 उन्नमय्य --- : clean
p010:P3 प्रथमं पद्मपादः : clean
p010:P4 पिङ्गलः अपि : clean
p010:P5 सूक्ष्मं परिशील्य : clean
p010:P6 "आम्, एषः : clean
p010:P7 पद्मपादः मुखतः : clean
p011:P1 skip layout-only chunk
p011:P2 प्रबलविरोधी। तम् : clean
p011:P3 वृद्धवचनं श्रुत्वा : clean
p011:P4 पद्मपादे एवं : clean
p011:P5 पिङ्गलः कृतज्ञतापूर्वकं : clean
p011:P6 एतावदेव न, : clean
p011:P7 पिङ्गलः तत् : clean
p011:P8 उक्तवान् --- : clean
p011:P9 पद्मपादः उक्तवान् : clean
p011:P10 "भवतः समीपे : clean
p012:P1 skip layout-only chunk
p012:P2 "तत् वा? : clean
p012:P3 सान्द्रैः मेघैः : clean
p012:P4 भल्लूककेतुः पिङ्गलेन : clean
p012:P5 पिङ्गलः भल्लूकेकेतोः : clean
p012:P6 पिङ्गलस्य मनःस्थितिं : clean
p012:P7 पिङ्गलः पद्मपादेन : clean
p012:P8 हस्तं प्रसार्य : clean
J1 p005:P3 {pb} -> p005:P4 fresh (clean break) : ok
J2 p005:P4 {pb} -> p005:P5 {pc} (continues) : ok
J3 p005:P5 {pb} -> p006:P2 {pc} (continues) : ok
J4 p006:P3 {pb} -> p006:P4 {pc} (continues) : ok
J5 p006:P9 {pb} -> p007:P2 fresh (clean break) : ok
J6 p007:P5 {pb} -> p007:P6 {pc} (continues) : ok
J7 p007:P7 {pb} -> p008:P2 fresh (clean break) : ok
J8 p008:P3 {pb} -> p008:P4 {pc} (continues) : ok
J9 p008:P5 {pb} -> p009:P2 fresh (clean break) : ok
J10 p009:P4 {pb} -> p009:P5 {pc} (continues) : ok
J11 p009:P7 {pb} -> p010:P2 {pc} (continues) : ok
J12 p010:P4 {pb} -> p010:P5 {pc} (continues) : ok
J13 p010:P7 {pb} -> p011:P2 {pc} (continues) : ok
J14 p011:P7 {pb} -> p011:P8 {pc} (continues) : ok
J15 p011:P10 {pb} -> p012:P2 fresh (clean break) : ok
J16 p012:P5 {pb} -> p012:P6 fresh (clean break) : ok
J17 p012:P8 {pb} -> END (clean break) : ok
