# Proofread report — samskrta_chandamama 1986_05, story p002 (pages 2–6, `बुद्धिमान् जामाता`)

## Summary

5 findings (F1–F5), all punctuation/sort verdicts on print quote marks; 4 sub-high-confidence kept-as-seen readings in Unverified (U1–U4). Systematic issues: two printer's dittograph quote marks demoted via `{del:}` (F1, F2), and one thought passage printed in dialogue sorts corrected to singles (F5). Passages not re-checkable: all glyph verification was Phase A (images closed for Phase B); U1–U4 rest on partial-zoom or full-page reads only. Not OCR output — direct print transcription; orth scan (`scan.py orth`) clean; extract gate exited 0 before Phase B edits and the proofread gate exits 0 after them. Loc below is `pNN:Pm` (lint chunk numbers) plus anchor words, counting words on the deblocked chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p004:P2 ज्ञायेत तथा : w3 | `तथा गन्तव्यम्’ इति` | `{del:'}` (delete dittographic close) | STY | error | high | third SQ stroke inside one DQ span; p003 `‘मार्गः…गन्तव्यम्’` pair already closed and the explanation needs no quotes |
| F2 | p006:P2 एवम् एव : w10 | `सत्यं वदतु" इति` | `{del:"}` (delete opener-less close) | STY | error | high | double close verified 4x with no opener in print; p006 opens clean and every p005 speech is closed |
| F3 | p005:P3 सुबुद्धिः पात्राणि : w45 and p005:P4 एतदर्थं कञ्चन : w1 | `किल?{pb}` / `एतदर्थं…’’` | `{ins:"}` closes P3, `{ins:"}` opens P4 | STY | error | high | one speech split by a clean column-break; each paragraph carries its own pair |
| F4 | p004:P6 तदा सुप्रिया : w53 | `पृष्टवती। एषः{pb}` | `{ins:"}` closes the hanging speech | STY | error | high | Supriya’s `"तात` speech is cut by the page turn with no continuation; supplied for readability while the sentence stays incomplete as in print |
| F5 | p005:P2 मनसि मार्गे : w5 and w47 | `"सुप्रिया…परीक्षणीयम्?"` | `{del:"}{ins:'}` at both ends | STY | likely | high | `मनसि` plus `इति चिन्तितवान्` pin interior thought; house sort for thought is SQ |

## Patterns

- Press `उद्युक्-` spelling kept as seen (2×): `उद्युक्तौ` (p003:P4 एकदा भूस्वामी), `उद्युक्तस्य` (p004:P3 अन्यस्मिन् दिने); classical `उद्यत` not substituted.
- `तत्सन्दर्भे` (p003:P5) vs `तस्सन्दर्भे` (p005:P3) kept each as seen (1+1); both verified at 3x+, treated as press variants, not normalized.

## Unverified

- U1 `सम्यक्` (p002:P3 पूर्वं वीरभद्रः : w60, Conf medium*): tail cut at the column edge; kept from visible `स` plus grammar and the parallel `सम्यक्` at p003:P2; a re-image of the line end would settle it.
- U2 `लिपिकारः` (p004:P4 पुत्र्याः वचनं : w70, Conf medium*): tail cut at crop edge (`लिपिक` + आ-stroke stub); standard word fits context; a re-image of the word would settle it.
- U3 `लाल` (p005:P2 मनसि मार्गे : w63, Conf low*): full-page read only (`तस्य मुखे लाल उत्पन्ना`); classical `लाला` expected; a 3x zoom would settle it.
- U4 `बद्ध्वा` (p005:P2 मनसि मार्गे : w77, Conf medium*): read at 2x (`पात्राणि बद्ध्वा केदारं`); a tighter zoom would exclude `बद्ध्वा`.

## Coverage

- p002:P1 : skip layout-only chunk.
- p002:P2 `# बुद्धिमान्` : skip title.
- p002:P3 पूर्वं वीरभद्रः : clean (see U1).
- p002:P4 सुप्रिया प्राप्तवयस्का : clean.
- p002:P5 तेषु बहवः : clean.
- p002:P6 : skip footer metadata chunk.
- p003:P1 : skip layout-only chunk.
- p003:P2 आगच्छति तम् : clean.
- p003:P3 वीरभद्रस्य कार्यालये : clean.
- p003:P4 एकदा भूस्वामी : clean.
- p003:P5 "प्रस्थानसमये पाथेयं : clean.
- p003:P6 तदा सुबुद्धिः : clean.
- p004:P1 : skip layout-only chunk.
- p004:P2 ज्ञायेत तथा : F1.
- p004:P3 अन्यस्मिन् दिने : clean.
- p004:P4 पुत्र्याः वचनं : clean (see U2).
- p004:P5 कारितवान्। विवाहार्थं : clean.
- p004:P6 तदा सुप्रिया : F4.
- p005:P1 : skip layout-only chunk.
- p005:P2 मनसि मार्गे : F5 (see U3, U4).
- p005:P3 सुबुद्धिः पात्राणि : F3.
- p005:P4 एतदर्थं कञ्चन : F3.
- p005:P5 एकसप्ताहानन्तरं धान्यसङ्ग्रहणकार्यम् : clean.
- p005:P6 मध्याह्ने भोजनसमये : clean.
- p006:P1 : skip layout-only chunk.
- p006:P2 एवम् एव : F2.
- p006:P3 मोचयन् --- : clean (print SQ-open/DQ-close mismatch `‘श्रीमन्…क्षाम्यतु"` kept as seen; no certain locus for correction).
- J1 p002:P4 {pb} -> p002:P5 {pc} (continues) : ok (mid-sentence column turn `किन्तु तेषु`, continuation per Sanskrit rule).
- J2 p002:P5 {pb} -> p003:P2 {pc} (continues) : ok (`परिणयेच्छया आगच्छति` joins across the page turn).
- J3 p003:P2 {pb} -> p003:P3 fresh (clean break) : ok (episode shift to the office/Suketu thread).
- J4 p003:P6 {pb} -> p004:P2 {pc} (continues) : ok (`यथा न ज्ञायेत` joins across the page turn).
- J5 p004:P4 {pb} -> p004:P5 {pc} (continues) : ok (`महता वैभवेन कारितवान्` joins across the column turn).
- J6 p004:P6 {pb} -> p005:P2 fresh (clean break) : checked scene-cut (Supriya’s hanging `एषः` has no continuation; narrative jumps to Suketu’s suspicion; `{ins:"}` supplied per F4).
- J7 p005:P3 {pb} -> p005:P4 fresh (clean break) : F3 (one speech spans the clean `?`-edge column break; supplied pair keeps each paragraph balanced).
- J8 p005:P6 {pb} -> p006:P2 {pc} (continues) : ok (`प्रस्थितस्य सुकेतोः एवम् एव` joins across the page turn).
- J9 p006:P2 {pb} -> p006:P3 {pc} (continues) : ok (`अश्रूणि मोचयन्` joins across the column turn).
- J10 p006:P3 {pb} -> END (clean break) : ok (story ends `सम्पन्नः।`).
