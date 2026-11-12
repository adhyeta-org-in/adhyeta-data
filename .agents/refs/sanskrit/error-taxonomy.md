# Error taxonomy

Every finding gets exactly one category code from the table below, a severity, and a confidence. Pick the category that describes the *cause*, not the symptom: a wrong case ending produced by an OCR slip is `OCR`, not `MRP`.

## Categories

| Code | Name | What it covers | Typical example |
|---|---|---|---|
| `ENC` | Encoding / glyph | Wrong Unicode characters that render almost right: pipe for danda, colon for visarga, Latin look-alikes, ZWJ/ZWNJ problems, non-NFC | `राम:` for `रामः` |
| `OCR` | OCR substitution | A letter or sign misread as another, a dropped halant / anusvāra / matra, a split or merged glyph | `वनं` read as `बनं`; `तत` for `तत्`, `प्रमो` for `प्रभो` |
| `SPL` | Spelling | Misspelling that is not a scanner artifact: wrong sibilant, wrong nasal, ण/न, श/ष/स, रि/ऋ, क्ष/ज्ञ conjuncts, wrong vowel length, wrong sequence of consonants | `पुरुश` for `पुरुष`; `महारजः` for `महाराजः`; `द्ध` vs `ध्द` confusion; `न्ह` vs `ह्न` confusion |
| `SND` | Sandhi | Missing, wrong or over-applied सन्धि at a word or compound boundary | `रामः गच्छति` in an edition that otherwise applies सन्धि (expected `रामो गच्छति`) |
| `MRP` | Morphology | Wrong case ending, verb ending, stem, gender of a noun, participle formation, क्त्वा / ल्यप् choice | `राजाः` for `राजानः` |
| `AGR` | Agreement | Subject-verb, adjective-noun, participle-agent, number or gender mismatch | `बालिका गतः` (expected `गता`) |
| `KRK` | Kāraka / syntax | Wrong case for the role, voice confusion (कर्तरि / कर्मणि / भावे), missing `इति`, misplaced relative-correlative, क्त्वा with different subjects | `रामः ग्रामे गच्छति` with locative for the destination (expected accusative `ग्रामम्`) |
| `CMP` | Compound | Malformed समास, wrong internal सन्धि, wrong gender of the final member | `राजपुत्रः` split as `राज पुत्रः` by a stray space |
| `LEX` | Word choice | A real word that does not fit: calque from Hindi / Marathi / English, wrong lexical item, OCR that produced a valid but wrong word | Hindi/Marathi word left in the text, or an OCR slip that produced a valid but wrong word (`धनम्` read as `वनम्`) |
| `CNS` | Consistency | The same name, term or spelling convention rendered differently within the text | `विक्रमः` / `विक्रम्` / `विक्रमा` for the same character |
| `STY` | Style / punctuation | Sentence punctuation, word-spacing conventions, over-long sentences, register slips. Never counts as an error in the strict sense | missing danda at paragraph end |
| `MTR` | Meter | Verse line with the wrong syllable count or a पद that breaks its meter's pattern | 15 syllables in a पद of an अनुष्टुभ |

## Severity

- **error**: wrong by any reasonable standard of the classical language, or a clear encoding defect.
- **likely**: probably wrong; a competent editor would fix it, but a variant reading is conceivable.
- **variant**: valid but uncommon (Epic, Vedic, regional); mention only if it looks accidental.
- **style**: not wrong; editorial preference.

This is the editorial verdict in the report, not the scanner's triage level. The scanner emits `high` / `medium` / `low` by pattern confidence: re-judge every confirmed hit into one of the four categories above. Confirmed `high` hits are usually `error`; `medium` hits are usually `likely`; `low` hits are often `style` or `variant`.

## Confidence

- **high**: you can state the rule and the correct form, and you are sure.
- **medium**: you are fairly sure but a variant reading or an unusual word cannot be excluded.
- **low**: a hunch. Say what would settle it.

Add the flag **unverified** to any finding about morphology, sandhi or lexicon that you did not check against a tool or dictionary, whenever your confidence is below high.

## Judging severity for OCR'd stories

A printed Chandamama text rarely contains grammatical errors that the editors left in. If a word looks ungrammatical, the first hypothesis is OCR damage (`OCR`), the second is a typesetting slip, and only the third is that the author erred. Prefer the explanation that requires the smallest change to the glyphs.
