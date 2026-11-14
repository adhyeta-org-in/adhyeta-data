## Summary

Range p026 (scans 26-28, story `कः श्रेष्ठः?`, जातककथा) proofread images-closed: 10 findings — 5 `style` (quote supplies/sorts, high confidence, emitted as verdict blocks) and 5 held candidates `likely/low*` (1 garbled speaker ID, 1 Pali-verse form, 3 काशीगज- spellings, emitted as `{sug-}` blocks). Systematic issues: print uses single quotes for two spoken exchanges and leaves the king's deliberation unopened (all ruled by speech-vs-thought sense); proper-noun spellings wobble on p28 (काशीगज- 3x against काशीराज- elsewhere, कोमलराजमाधिः for the Kosala charioteer). `scan.py orth` on deblocked text: 0 hits; sandhi-openness mix and Pali gāthā forms kept as print variants. `Loc` uses story coordinates `pNN:Pm` (scan file + chunk ordinal) with first-two-word anchors. This is human transcription, not OCR output.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p026:P5 जनानां मध्ये | `अभवत्। स्वीयशासनक्रमे` (no opening mark; closes `करोमि?"`) | `{ins:'}` before `स्वीयशासनक्रमे` | STY | style | high | interior monologue (first-person deliberation closed by `चिन्तयन्`) takes singles; print leaves it unopened |
| 2 | p026:P5 जनानां मध्ये | `किं करोमि?"` | `किं करोमि?'` | STY | style | high | same thought pair as F1; print closes with a double |
| 3 | p026:P6 एवं रीत्या | `'मम शासनक्रमे ... अस्ति वा?' इति पृष्टवान्` | `"मम शासनक्रमे ... अस्ति वा?"` | STY | style | high | spoken question put to people (`पृष्टवान्`) takes doubles; print uses singles |
| 4 | p027:P6 भोः रथचालक | `'भोः रथचालक ... नयामि।` continuing `{pc}तावत्पर्यन्तं ... स्थापयतु"` | `"भोः` | STY | style | high | charioteer's spoken demand (`उक्तवान्`, vocative + imperatives) takes doubles; print opens single against its double close |
| 5 | p027:P8 माम् आज्ञापयितुं | `'माम् आज्ञापयितुं ... अस्ति"` | `"माम्` | STY | style | high | spoken retort (`शान्तस्वरेण ... उक्तवान्`) takes doubles; print opens single against its double close |
| 6 | p028:P4 तदा मधः | `कोमलराजमाधिः` | `कोसलराजसारथिः` | OCR | likely | low* | responder must be the Kosala king's charioteer (answers the Kashi charioteer); print form is garbled |
| 7 | p028:P5 दलहं दलहस्य | `खिपनि` | `खिपति` | OCR | likely | low* | fixed Pali gāthā reads `khipati` (3sg); `खिपनि` is not a Pali form (त/न confusion) |
| 8 | p028:P7 तत् वचनं | `काशीगजस्य सारथिः` | `काशीराजस्य सारथिः` | CNS | likely | low* | same office spelled काशीराज- elsewhere (p026, p028:P10); an elephant needs no charioteer here |
| 9 | p028:P10 काशीराजस्य सारथेः | `काशीगजं प्रणम्य` | `काशीराजं प्रणम्य` | CNS | likely | low* | same as F8; the Kosala king bows to the Kashi king, not an elephant |
| 10 | p028:P11 अनन्तरं काशीगजः | `काशीगजः ... स्वीयां राजधानीं` | `काशीराजः` | CNS | likely | low* | same as F8; the returning ruler is the Kashi king |

## Patterns

- काशीगज- for काशीराज- (3x: F8 p028:P7, F9 p028:P10, F10 p028:P11), held as `{sug-}`; print is consistent within p28 but contradicts p026 and p028:P10's own `काशीराजस्य सारथेः`.
- Speech opened single but closed double (2x: F4 p027:P6, F5 p027:P8), both corrected to doubles.
- Pali gāthā transliteration kept as print throughout (दलहं, साधुम्पि, जेति, एतादिसो, मग्गा, उय्याहि, अक्कोधेन, कदरियं, सच्चेन, अलिकवादिनम्): valid dialect forms, never flagged; only खिपनि (F7) and the मह्लिक- spelling (see Unverified) looked accidental.

## Unverified

- F6 (`कोमलराजमाधिः` → `कोसलराजसारथिः`): role is certain from dialogue order, exact glyph path is not; needs a scan check of the akṣaras.
- `मधः` (p028:P4 `तदा मधः एव ...`): kept as a possible proper name (the Kosala charioteer's name); alternative `मल्लः` is a guess only — no block emitted, needs scan/type check.
- `मह्लिकः` / `मह्लिको` / `मह्लिकमहाराजः` (p027:P10, p028:P5, P6, P10): kept as the print's consistent spelling; Pali parallel suggests `मल्लिक-`, but normalizing would break in-story consistency — needs scan check before any verdict.
- F7 (`खिपनि` → `खिपति`): Pali-parallel certainty is high for the word, but the file keeps print plus a held candidate since the glyph was not re-examined.
- F8-F10 (काशीगज- → काशीराज-): sense is certain, press mechanism (रा/ग) unexplained — held, needs scan check.
- `अनिशयरूपेण` (p028:P10 `इतोऽपि अनिशयरूपेण धर्मेण`): possibly `अतिशयरूपेण`; Phase A left no flag on it so no block was emitted — noted here only, needs scan check.
- Pali verses were not meter-checked (`verse.md` pass skipped: forms are Pali, not Sanskrit ślokas); translations in parentheses read clean.

## Coverage

p026:P1 : skip layout
p026:P2 : skip title
p026:P3 काशीराज्ये ब्रह्मदत्तस्य : clean
p026:P4 तस्य शासनकाले : clean
p026:P5 जनानां मध्ये : F1, F2
p026:P6 एवं रीत्या : F3
p026:P7 एवं क्रमेण : clean
p026:P8 : skip metadata
p027:P1 : skip layout
p027:P2 स्मः अस्माभिः : clean
p027:P3 एतावता महाराजः : clean
p027:P4 अन्ते रथेन : clean
p027:P5 द्वौ अपि : clean
p027:P6 भोः रथचालक : F4
p027:P7 तावत्पर्यन्तं भवतः : clean
p027:P8 माम् आज्ञापयितुं : F5
p027:P9 मम रथे : clean
p027:P10 काशीराज्यं यावत् : clean
p028:P1 : skip layout
p028:P2 वेषपरिवर्तनं कृत्वा : clean
p028:P3 भवतः महाराजे : clean
p028:P4 तदा मधः : F6
p028:P5 दलहं दलहस्य : F7
p028:P6 अस्माकं मह्लिकमहाराजः : clean
p028:P7 तत् वचनं : F8
p028:P8 जिने कदरियं : clean
p028:P9 अस्माकं महाराजः : clean
p028:P10 काशीराजस्य सारथेः : F9
p028:P11 अनन्तरं काशीगजः : F10
p028:P12 एषः स्वयं : clean
J1 p026:P4 -> p026:P5 fresh : ok
J2 p026:P7 -> p027:P2 : ok
J3 p027:P6 -> p027:P7 : ok
J4 p027:P10 -> p028:P2 : ok
J5 p028:P7 -> p028:P8 : ok
J6 p028:P12 -> END : ok
