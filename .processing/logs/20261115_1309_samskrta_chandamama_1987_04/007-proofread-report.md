# Proofread report: 1987_04, START=007 (pp. 7--8, story `पिशुनता`)

## Summary

Range p007--p008 (two scan pages, title `पिशुनता`) proofread with images closed. No findings: zero `{del:}`/`{ins:}` verdicts, zero held candidates; the file is byte-identical to the Phase A transcription apart from the tool-generated `## Joints` index. The three linter notes are one legitimate chain (an outer `"` speech opened in p007:P9 and closed in p008:P2 across the page turn, plus the final speech left open past END into the next range) and are recorded as checked print-faithful below. The inherited `{sug-ins:}`/`{sug-del:}` queue was empty. Orth scan (`scan.py orth` on deblocked text) returned zero hits. Proper nouns are consistent throughout (`विक्रमकीर्तिः`, `चिन्मयः`, `अमलवर्मा`). House forms kept as seen (`स्नेहितः`, `सहानुभूतिः`, open sandhi). `Loc` below is keyed on story coordinates `pNN:Pm` plus the first two words as anchor. The text does not appear to be OCR output.

## Findings

No findings. No blocks were added to the story file.

## Patterns

None.

## Unverified

None. No form was flagged below high confidence.

## Coverage

p007:P3 पूर्व विदेहराज्यं : clean
p007:P4 एवं स्थिते : clean
p007:P5 अत्र कारणं : clean
p007:P6 राजा मातुः : clean
p007:P7 चिन्मयः तत्र : clean
p007:P8 सत्यं किल! : clean
p007:P9 विशेषकारणं किम्? : clean
p008:P2 सन्तोषः एव : clean
p008:P3 राजा तु : clean
p008:P4 सः महता : clean
p008:P5 सेवकाः साक्षात् : clean
p008:P6 एतां वार्तां : clean
p008:P7 किम् अन्यत् : clean
p008:P8 क्षाम्यतु माम्। : clean
p008:P9 राजा क्षणकालं : clean
p008:P10 कारागारं गतः : clean
J1 p007:P6 {pb} -> p007:P7 {pc} (continues) : ok
J2 p007:P9 {pb} -> p008:P2 {pc} (continues) : ok (outer " speech opened at विशेषकारणं spans the page turn and closes at एतत्" in P2; never forced closed; lint edge-note checked print-faithful)
J3 p008:P6 {pb} -> p008:P7 fresh (clean break) : ok
J4 p008:P10 {pb} -> END : ok (sentence and outer " speech continue past END into the next range; lint quotes-open-past-end note checked print-faithful)

## Continuation (scan 9)

### Summary
Scan 9 transcribed as a new page span p009 (2-col text over bottom-full-width prison art; no title, no byline, no printed folio, so bare {pgb}; story text only) and proofread from text. The range is now pp. 7--9 and the story `पिशुनता` ends complete at p009:P7. One finding (F1, STY/style/high): a stray lone single-quote stroke before शृङ्खलाम् with no mate and no quotable role, removed via a lone {del:'} in the file. Orth scan (`scan.py orth` on deblocked text) returned zero hits. Proper nouns are consistent (चिन्मयः, विक्रमकीर्तिः; अमलवर्मा does not recur in this span). House spellings are kept as seen (कर्-stem अङ्गीकर्यात्/अङ्गीकरोमि twice, क्षाम्यतु twice matching p008:P8, open न). Loc below is keyed on story coordinates pNN:Pm plus the first two words as anchor. The text is print transcription, not OCR output.

### Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p009:P7 बद्धां शृङ्खलाम् | `बद्धां 'शृङ्खलाम्` | `बद्धां शृङ्खलाम्` (lone {del:'} applied in file) | STY | style | high | lone single stroke has no mate and no role (singles mark thought or nested speech, never a plain noun in narration); detached stroke verified at 3x |

### Checked print-faithful (no blocks)
- p009:P7 अनुभवोक्तव्यम् : वो + क्त verified unambiguous at 3x; sense is strained but no minimal-glyph alternative exists (अनुभवितव्यम् would rewrite two aksharas), and Phase B invents no new glyph claims — kept as printed.
- p009:P3 अङ्गीकर्यात् / p009:P4 अङ्गीकरोमि : कर्-stem in both, a consistent house form — kept.
- p009:P7 मां क्षाम्यतु : matches p008:P8 क्षाम्यतु माम् — kept.
- p009:P3 काञ्चित् (ञ्च), निस्सन्तानः (स्स), तारतम्यभावः, दायित्वम्, तात्कालिकमरण-दुःखापेक्षया (glued compound hyphen); p009:P7 दृढम्, असहमानाः, अपरामृश्य, बन्धनार्थम्; p009:P5 तिरस्कर्तुं : glyphs verified at 2-3x crops, kept as seen.
- Quotes: p009:P2 `खलु?"` closes the p008:P10 outer speech across the page turn (edge-spanning pair, lint notes-only, verified continuous); p009:P3 `"महाराज!` opens and p009:P4 `स्थापितवन्तः"` closes across the P3->P4 column turn (mid-speech continuation, verified); P6 balanced; P7 balanced after F1.

### Joints (updated)
- J4 re-pointed: p008:P10 {pb} -> p009:P2 {pc} (continues) : ok — spaced join "न आगतवान्" (house keeps न open, cf. p007 "न उपस्थितः"); sentence and outer " speech complete at P2 `खलु?" इति।`.
- J5 (new): p009:P3 {pb} -> p009:P4 {pc} (continues) : ok — column turn mid-sentence (भवद्दर्शनं कृत्वा absolutive into the main clause सहानुभूतिः प्रदर्शनीया आसीत्...).
- J6 (new END): p009:P7 {pb} -> END (clean break) : ok — story ends complete "आलिङ्गितवान्।"; this supersedes the old J4 quotes-open-past-END note above; nothing continues past END.

### Coverage (continuation)
p009:P2 आगतवान् राजभवने : clean
p009:P3 तत् श्रुत्वा : clean
p009:P4 सहानुभूतिः प्रदर्शनीया : clean
p009:P5 चिन्मयस्य वचनं : clean
p009:P6 "पिशुनजनानां वचनश्रवणेन : clean
p009:P7 "चिन्मय! वस्तुस्थितिम् : F1
J4 p008:P10 {pb} -> p009:P2 {pc} (continues) : ok
J5 p009:P3 {pb} -> p009:P4 {pc} (continues) : ok
J6 p009:P7 {pb} -> END (clean break) : ok

### Verification
- `python3 .agents/tools/chandamama/lint.py --refresh-joints` → joints refreshed (6: J4 re-pointed, J5/J6 new).
- `python3 .agents/tools/chandamama/lint.py --phase proofread --story .processing/samskrta_chandamama/1987_04/p007.md` → exit 0 (3 pages, 0 error paras, 0 story findings).
- `python3 .agents/tools/sanskrit/scan.py orth` on deblocked story text → 0 findings.

### Corrected end disposition
The story ends, complete and balanced, at p009:P7 with the king removing Chinmaya's fetters himself and embracing him ("...स्वयम् अपसार्य प्रीत्या तं दृढम् आलिङ्गितवान्।"). The earlier end disposition (open speech continuing past END into the next range) was an artifact of the missing scan and is withdrawn.
