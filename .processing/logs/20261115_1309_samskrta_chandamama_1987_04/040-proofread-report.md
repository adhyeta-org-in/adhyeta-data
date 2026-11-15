# Proofread report: 1987_04 p040 (START=40 END=41, प्रतिवचनम्)

## Summary

Phase A transcribed one page (40.jpg, story opening with title) and the extract gate passed clean; Phase B ran with images closed and the proofread gate passes clean. 2 findings, both held low-confidence candidates (SPL/error/medium*), no verified verdicts, story text otherwise byte-identical to Phase A. Systematic observation, not flagged: this print leaves visarga sandhi open before voiced consonants and vowels (house-style variant, see Patterns). Whole page checked sentence by sentence with nothing left unverified in passage terms; the only unchecked items are two glyph shapes (ख/क, ध्य/ध) that need the physical print to settle. Text is a print transcription, not OCR output; orth scanner reported zero hits.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p40:P4 (राजकुमारीं परिणेतुम्), w21 | `तप्तायःशलाखारेखया` | `तप्तायःशलाकारेखया` | SPL | error | medium* | `शलाखा` is not a Sanskrit word; तप्त-अयः-शलाका-रेखा (red-hot iron-rod mark) fits the branding punishment, smallest glyph change ख→क |
| F2 | p40:P10 (राजभवनस्य प्राप्तेः), ~w15 | `औषध्यम्` | `औषधम्` | SPL | error | medium* | `औषध्यम्` is unattested; `औषधम्` (medicine) fits `अनुभूयते`, smallest change drops ्य |

## Patterns

Ptn1 (house variant, no blocks): open visarga sandhi kept throughout the page --- `अतः राजा`, `यः मम`, `बहवः असमर्थाः`, `सहोदराः अपि`, `एकः दण्डः`, `ज्येष्ठः राजकुमार्या`, plus unjoined `-म्` before vowels (`राजभवनम् आगतवन्तः`). Vowel sandhi is applied where joined (`तप्तायः`), so the openness is the edition's mixed house style; per fidelity doctrine recorded as variant, never flagged.

## Unverified

F1 (`शलाखा` vs `शलाका`): sense strongly favours `शलाका`, but the glyph read (ख at 3x in Phase A) has no `{x-com:}`/`{sug-…}` on file, so no verified verdict was issued; a look at the physical print (ख vs क in `तप्तायःशलाखारेखया`) plus a dictionary check of `अयःशलाका` would settle it. F2 (`औषध्यम्` vs `औषधम्`): same position --- sense favours `औषधम्`, but ध्य vs ध needs the physical print to settle; a dictionary check confirming no `औषध्य` stem would close it. Also noted for the audit: four tiny detached specks before श (`शूरा`, `शक्नोति`, `शक्यते`, `शृङ्गद्वयं`), verified at 4x in Phase A as clearly detached print noise with no mates and no quotable sense, were omitted without blocks.

## Coverage

p40:P1 {x-com:layout: : skip layout note
p40:P2 प्रतिवचनम् : skip title
p40:P3 पूर्वं कस्यचित् : clean
p40:P4 राजकुमारीं परिणेतुम् : F1
p40:P5 राजकुमारीविवाहवार्तां श्रुत्वा : clean
p40:P6 मार्गे तैः : clean
p40:P7 इति सन्तोषेण : clean
p40:P8 किञ्चद्दूरं गमनानन्तरं : clean
p40:P9 एवं मार्गे : clean
p40:P10 राजभवनस्य प्राप्तेः : F2
p40:P11 {category: "नार्वेदेशस्य : skip category metadata
J1 p040:P6 {pb} -> p040:P7 {pc} (column turn, continues: `पश्यन्तु" इति सन्तोषेण उक्तवान्।`) : ok
J2 p040:P10 {pb} -> END (page turn, continues: `चुल्लीं` awaits its verb on p41) : ok

## Continuation (scan 41)

Scan 41.jpg was untranscribed and belongs to this range (story runs to the page before next start 42). Appended one new page span after the existing `{pgb}`: `{x-com:layout: 2col, art bottom full-width}`, 16 body chunks in reading order left then right, closed `{pb}{pgb}` (bare, no folio in print). Seam pairs continuously: p040:P10 `चुल्लीं{pb}` + p041:P2 `{pc}प्रदर्शितवती।` gives `चुल्लीं प्रदर्शितवती।`. Column turn inside p41 is a clean break: p041:P8 `"दण्डान्ते उत्तोलयामि किल?"{pb}` -> p041:P9 fresh. Proofread gate passes clean (`--refresh-joints`, then `--phase proofread --story` exit 0); orth scanner on deblocked full text reports zero hits. F1 and F2 stay held as instructed and are not re-ruled. Notably p41 prints `तप्तायःशलाकारेखया` and `अयःशलाकाद्वय` with क, supporting the F1 sense, but F1 is left held per instruction.

### New verdict

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F3 | p41:P9 (तदा दग्धात्), w1 | `'` single open before `तदा` | `"` double open | STY | error | high | Era house standard is doubles for reported speech and every neighbouring speech on this page opens/closes `"`; single open with double close leaves dq=2/sq=1 unbalanced, so the missing second stroke is supplied; smallest change restores the double open (`{del:'}{ins:"}` in file) |

Print-noise note (no block, consistent with the four specks in the base report): a tiny detached tick before `शक्नुमः` in p41:P5 (`पक्तुं 'शक्नुमः`) has no mate and no quotable sense inside an already-open `"..."` span, so it was omitted as a speck like the `श`-specks on p40. `मोदोजलम्`, `सङ्गृहणामि`, `पादारक्षायाः`, open visarga sandhi and `-म्` openness are kept as printed (no Phase-A `{sug-}` on file, so no Phase-B glyph claim); orth clean.

### New coverage (p41 span only; p40 coverage above unchanged)

p41:P1 {x-com:layout: : skip layout note
p41:P2 {pc}प्रदर्शितवती। : clean (seam `चुल्लीं प्रदर्शितवती।`)
p41:P3 तृतीयः अपि : clean
p41:P4 राजकुमारी चुल्लीं : clean
p41:P5 युक्तम् एव। : clean (speck before `शक्नुमः` omitted as noise, see note)
p41:P6 पक्षी तत्र : clean
p41:P7 तापयुक्तं तत् : clean
p41:P8 दण्डान्ते उत्तोलयामि : clean
p41:P9 तदा दग्धात् : F3
p41:P10 यथा भूमौ : clean
p41:P11 प्रतिवचनं वक्रतां : clean
p41:P12 वक्रता न : clean
p41:P13 एतादृशम् अन्यत् : clean
p41:P14 तर्हि अत्र : clean
p41:P15 मां पराजेतुम् : clean
p41:P16 आयुषः व्ययः : clean
p41:P17 अग्रे किमपि : clean
J2 p040:P10 {pb} -> p041:P2 {pc} (page turn, continues: `चुल्लीं प्रदर्शितवती।`) : ok (supersedes base J2)
J3 p041:P8 {pb} -> p041:P9 fresh (column turn, clean break) : ok
J4 p041:P17 {pb} -> END (clean break) : ok
