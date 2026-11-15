# Proofread report — 1986_11 p006 (START 6, scans 6.jpg–8.jpg)

## Summary
Phase B (images closed) on `.processing/samskrta_chandamama/1986_11/p006.md`, three page spans p006–p008. Proofread gate passes with 0 errors and 0 story findings. Orth scan (`scan.py orth` on deblocked text) reports 0 findings. No `{sug-ins:}`/`{sug-del:}` were inherited from Phase A, so there was no candidate queue to route. One form is held as unverified without touching the file (`कर्तयत्`, p008:P10); everything else reads as print-faithful. Loc below is `pNN:Pm` (NN = scan sequence from filename plus `{pgb}`-span ordinal, Pm = chunk number within that span matching lint `P` numbers) plus the first two words of the chunk as anchor, with word counts on whitespace-separated tokens of the chunk. The text does not look like OCR output.

## Findings
| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
(none — no verified finding met the bar for a file block)

## Patterns
(none — no repeats to fold)

## Unverified
- U1 — Loc `p008:P10 एतत् दृष्ट्वा · w16`: chunk reads `... एतस्य नासिकां दंशनेन कर्तयत्" इति सेवकम् आदिष्टवान्।`. `कर्तयत्` (final `त्`) is unexpected in a quoted command to the servant, where causative imperative `कर्तयतु` (or 2nd singular `कर्तय`) would be expected. Held, file unchanged: Phase B invents no new glyph claim without a Phase A `{x-com:}`/`{sug-…}` on file, and the `तु`/`त्` distinction (u-mātrā vs halant) cannot be settled from text alone. What would settle it: a 3x glyph check of that akṣara on the scan (u-hook vs halant slash) in a future images-open pass; do not change on grammar alone.

## Coverage
- p006:P1 `{x-com:layout:` : skip layout-only chunk
- p006:P2 `# नूतनः` : skip title
- p006:P3 पूर्वं विन्ध्यारण्यस्य : clean
- p006:P4 भूस्वामिनः सेवायां : clean
- p006:P5 एतादृशेषु भूस्वामिषु : clean
- p006:P6 `{pc}न्यायाधिकारित्वं` : clean
- p006:P7 तस्मिन् राज्ये : clean
- p006:P8 नागचूडामणिः यदा : clean
- p006:P9 ग्रामम् आगतः : clean
- p006:P10 वादिनः नासिका : clean
- p006:P11 `{author:` : skip metadata/footer chunk
- p007:P1 `{x-com:layout:` : skip layout-only chunk
- p007:P2 नागचूडामणिः कम्पमानस्वरेण : clean
- p007:P3 तदा सः : clean
- p007:P4 `"भवान् किमर्थं` : clean
- p007:P5 `"श्रीमन्! सः` : clean
- p007:P6 `"तत् कथं` : clean
- p007:P7 तदा द्वितीयः : clean
- p007:P8 `{pc}आसन्दम् आरुह्य` : clean
- p007:P9 अत्रान्तरे नागचूडामणिः : clean
- p007:P10 `'इतोऽपि कालहरणं` : clean
- p007:P11 अनन्तरं महाराजम् : clean
- p007:P12 भोजनानन्तरं नागचूडामणिः : clean
- p007:P13 तदा पत्नी : clean
- p007:P14 नागचूडामणिः तथैव : clean
- p008:P1 `{x-com:layout:` : skip layout-only chunk
- p008:P2 `{pc}बुद्धिमत्ताविषये किं` : clean
- p008:P3 `"पुनः एकवारं` : clean
- p008:P4 महाराजस्य अनुमतिं : clean
- p008:P5 नागचूडामणिः निर्णयं : clean
- p008:P6 अत्रान्तरे जवनिकायाः : clean
- p008:P7 एतत् दृष्ट्वा : clean
- p008:P8 नागचूडामणेः पत्न्याः : clean
- p008:P9 `'पतिः पुनः` : clean
- p008:P10 एतत् दृष्ट्वा : clean (U1 noted above, file unchanged)
- p008:P11 नागचूडामणेः पत्नी : clean
- p008:P12 एतत् सर्वं : clean
- J1 p006:P5 {pb} -> p006:P6 {pc} (continues) : ok (`आत्मनः` + `न्यायाधिकारित्वं` forms a valid genitive phrase)
- J2 p006:P10 {pb} -> p007:P2 fresh (clean break) : ok (terminal `।` then fresh interrogation scene)
- J3 p007:P7 {pb} -> p007:P8 {pc} (continues) : ok (`एषः` + `आसन्दम् आरुह्य` completes the quoted sentence across the column turn)
- J4 p007:P14 {pb} -> p008:P2 {pc} (continues) : ok (`मम` + `बुद्धिमत्ताविषये` completes `मम बुद्धिमत्ताविषये किं वा चिन्तयेत्?` across the page turn)
- J5 p008:P7 {pb} -> p008:P8 fresh (clean break) : ok (terminal `।` then verbless `नागचूडामणेः पत्न्याः ... असमाधानम्` as a fresh observation)
- J6 p008:P12 {pb} -> END (clean break) : ok (ends with terminal `।`, story pauses at the king's exit line; continuation, if any, is outside this range)
