# Proofread report: 1986_04 p026 (`विचित्रा पत्नी`, scans 26–29)

## Summary

Three findings, all quote-punctuation (STY/style, high confidence), each fixed as a verdict block in the story file; the proofread gate is green (4 pages, 0 error paras, 0 findings). One pattern: print mixes double and single marks for spoken lines, kept as seen. Five held notes below (no blocks): one hapax name, two odd instrumentals, two odd words, plus a recurring press-dot omitted in transcription. Orth scanner (`scan.py orth`) on deblocked text: no hits. Text is a print transcription, not OCR output. Loc below is `pNN:Pm:word` (word counted on the chunk from 1, blocks excluded).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p026:P9:1 | `'एषा 'रात्रौ` | `'एषा रात्रौ` | STY | style | high | inner open has no role; one clause takes one thought-quote pair; stray mark deleted via `{del:'}` |
| 2 | p027:P4:23 | `कल्पयित्वा{pb}` | `कल्पयित्वा'{pb}` | STY | style | high | thought (`'पिशाचेन...`) ends at the column edge and narration resumes after it; close supplied via `{ins:'}` |
| 3 | p028:P7:13 | `अपि। आपणिकस्य सङ्केतादिकं` | `अपि। "आपणिकस्य सङ्केतादिकं` | STY | style | high | amazement quote closes at `किल?" इति`; the genitive binds `आपणिकस्य` to `सङ्केतादिकं`, so the open sits at the sentence boundary; supplied via `{ins:"}` |

## Patterns

- Spoken lines in singles vs doubles: most speech uses doubles (`"भवती यादृशम्...`, `"मया सह आगच्छतु"`), but the shopkeeper's boast uses singles (`'मम शुनकः नाणकपरीक्षायां निपुणः' इति`, p028:P8). Print inconsistency kept as seen; no block.

## Unverified

- U1 `निद्रीसुमान्` (p026:P3:3): hapax merchant name (hero called `सुमानः` thereafter); glyph verified at 3x in Phase A (`नि` + `द्री` conjunct); no emendation proposed. Would settle: another issue printing the name.
- U2 `तया` as quasi-subject twice (p027:P2:1 `तया तस्याः अनुसरणं कृतवान्`; p028:P2:3 `किन्तु तया आगमनसमये`): odd instrumental, kept as print; no block (a fix would be normalisation). Would settle: print collation.
- U3 `भापयित्वा` (p028:P3:26, `मार्गशुनकान् भापयित्वा`): odd causative kept as print; no block. Would settle: dictionary/parallel-text check.
- U4 `निर्दुष्टं` (p028:P7:20, `नाणकपरीक्षां निर्दुष्टं करोति`): odd for the sense, kept as print since Phase A flagged no glyph doubt; no block. Would settle: another edition.
- U5 recurring subscript dot under `व`/`स` sorts (`एव`, `एवम्`, `सा`): omitted in transcription as a press defect, not a character; documented here, no block.

## Coverage

- p026:P1 `{x-com:layout:` : skip layout-only chunk
- p026:P2 `# विचित्रा` : skip title chunk
- p026:P3 `बाग्दादनगरे निद्रीसुमान्` : clean (U1 noted above, no block)
- p026:P4 `एतद्विषये ज्येष्ठानां` : clean
- p026:P5 `विवाहानन्तरं सुमानः` : clean
- p026:P6 `अनन्तरं तस्याः` : clean
- p026:P7 `एवम् एव` : clean
- p026:P8 `तेषु दिनेषु` : clean
- p026:P9 `'एषा रात्रौ` : F1
- p026:P10 `मध्यरात्रे सा` : clean
- p026:P11 `{category: अरेबिया` : skip metadata chunk
- p027:P1 `{x-com:layout:` : skip layout-only chunk
- p027:P2 `तया तस्याः` : clean (U2 noted above, no block)
- p027:P3 `अन्धकारे एव` : clean
- p027:P4 `एतत् दृश्यं` : F2
- p027:P5 `एव सः` : clean
- p027:P6 `अनन्तरदिने सुमानः` : clean
- p027:P7 `एतत् श्रुतवत्याः` : clean
- p027:P8 `आत्मानं रक्षितुम्` : clean
- p028:P1 `{x-com:layout:` : skip layout-only chunk
- p028:P2 `आगतवान्। किन्तु` : clean (U2 noted above, no block)
- p028:P3 `छिन्नपुच्छं नूतनशुनकं` : clean (U3 noted above, no block)
- p028:P4 `एकदा वस्तूनि` : clean
- p028:P5 `एतत् नाणकं` : clean
- p028:P6 `एवं वा?` : clean
- p028:P7 `शुनकेन पादसाहाय्येन` : F3 (U4 noted above, no block)
- p028:P8 `मम शुनकः` : clean
- p028:P9 `एकदा काचित्` : clean
- p029:P1 `{x-com:layout:` : skip layout-only chunk
- p029:P2 `आसीत्। सा` : clean
- p029:P3 `वृद्धा ततः` : clean
- p029:P4 `विंशतिवर्षीया सा` : clean
- p029:P5 `तत्क्षणं शुनकः` : clean
- p029:P6 `सा युवतिः` : clean
- p029:P7 `सुमानः ततः` : clean
- p029:P8 `किञ्चित्कालानन्तरम् आगता` : clean
- p029:P9 `तत्क्षण एव` : clean
- J1 p026:P7 {pb} -> p026:P8 {pc} : ok (`पत्नी तेषु दिनेषु...` continuous)
- J2 p026:P10 {wb} -> p027:P2 {pc} : ok (`जागरूकतया तस्याः अनुसरणं...` solid)
- J3 p027:P4 {pb} -> p027:P5 {pc} : ok (`...कल्पयित्वा' एव सः भीत्या...` spaced; close supplied F2)
- J4 p027:P8 {pb} -> p028:P2 {pc} : ok (`गृहात् बहिः आगतवान्` spaced)
- J5 p028:P6 {pb} -> p028:P7 fresh : ok (clean break after `पातितवती।`)
- J6 p028:P9 {pb} -> p029:P2 {pc} : ok (`व्यग्रः आसीत्` spaced)
- J7 p029:P5 {pb} -> p029:P6 fresh : ok (clean break after `निवेदितवान्।`)
- J8 p029:P9 {pb} -> END : ok (range ends mid-story with `गतवती च।`; continuation lies outside scans 26–29)
