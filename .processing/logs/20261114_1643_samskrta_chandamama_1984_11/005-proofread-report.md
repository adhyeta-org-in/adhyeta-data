# Proofread report: samskrta_chandamama 1984_11, p005 (scans 5-12, story त्रयः मान्त्रिकाः)

## Summary

13 verdict findings applied as file blocks (F1-F13: 2 spelling errors, 11 quote-mark fixes) and 7 held unverified candidates (U1-U7). Systematic problems: the print drops the second stroke of double-quote opens on speech three times (all corrected to `"`), and one Pidgala speech runs over five paragraphs, so per-para pairs were supplied. Orth scan (`scan.py orth`, stdlib) on deblocked story text: 0 hits. Every scan 5-12 was read in Phase A; nothing was left unchecked. The source is letterpress print, not OCR output.
Loc below is `pNN:Pm wK`: page span (p005 = scan 5) plus chunk number matching lint `P` numbers, plus the deblocked word number at the finding (blocks stripped before counting); the anchor is the chunk's first two deblocked words. Findings counted on chunks, not scratch lines.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p005:P6 w3 (अतः सः) | `हसनगोरिं अर्थगर्भर्या दृष्ट्या` | `अर्थगर्भर्या` → `अर्थगर्भया` | SPL | error | high | dittography of र verified at 3x+; instrumental अर्थगर्भया is certain |
| F2 | p005:P8 w6 (अकस्मात् आगतेन) | `किञ्चित् सम्भ्रन्तः इव` | `सम्भ्रन्तः` → `सम्भ्रान्तः` | SPL | error | high | आ-mātrā dropped in print, verified at 3x; सम्भ्रान्त certain |
| F3 | p006:P4 w1 (न, पद्मपाद!) | `'न, पद्मपाद! ... नास्ति"` | open `'` → `"` | STY | style | high | reported speech with इति-closure; single open is a dropped second stroke |
| F4 | p008:P6 w1 (पद्मपाद! भवतः) | `'पद्मपाद! ... अतः` + `"... वैराग्यम्!"` | open `'` → `"` | STY | style | high | reported speech continued and closed with `"` in p009:P2; sorts must match |
| F5 | p009:P7 w7 (पिड्गलः दैन्यं) | `'पद्मपाद! ... एतादृशानां` + `"... भविष्यति।"` | open `'` → `"` | STY | style | high | reported speech closed with `"` in p010:P2; sorts must match |
| F6 | p006:P2 w54 (न ज्ञातवान्) | `भवन्तः --- इति` | `भवन्तः"` (supply close) | STY | style | high | reported clause closed by इति; position pinned after भवन्तः |
| F7 | p006:P2 w59 (न ज्ञातवान्) | `चिन्तयामि। अवकाशे` | supply open `"` before अवकाशे | STY | style | high | sentence boundary after चिन्तयामि।; speech resumes with अवकाशे |
| F8 | p008:P5 w16+w19 (पिड्गलस्य वचनं) | `"पिड्गलः! ... तदा "अहम् ..." इति` | inner `"..."` → `'...'` | STY | style | high | nesting is only DQ SQ ... SQ DQ; inner reported identity is the nested pair |
| F9 | p009:P4 w17 (तयोः वार्तालापः) | `एषः 'ध्वनिः सर्वत्र` | `'ध्वनिः'` (supply close) | STY | style | medium* | lone emphatic open with no mate; close pinned after ध्वनिः |
| F10 | p007:P7 w19 (मान्त्रिकं जेतुम्) | `... भीतिः नास्ति।` + `लक्ष्य...` | supply close `"` | STY | style | high | multi-para speech: each paragraph opens and closes its own pair |
| F11 | p007:P8 w1+w22 (लक्ष्यप्राप्तेः अनन्तरं) | whole paragraph | supply open + close `"` | STY | style | high | middle paragraph of the same multi-para speech |
| F12 | p007:P9 w1+w18 (अतः एव) | whole paragraph | supply open + close `"` | STY | style | high | middle paragraph of the same multi-para speech |
| F13 | p007:P10 w1 (इदानीं तु) | `इदानीं ... लुण्टाकानाम्` + `{pc}` | supply open `"` | STY | style | high | last paragraph of the speech; page-turn `{pb}/{pc}` join needs no close |

## Patterns

- Dropped second stroke on speech opens (3x): F3, F4, F5. All are reported speech with reporting verbs and इति-closures, so the era-standard double open is certain; corrected via blocks, no other singles-upgraded-silently.
- Vocative `पिड्गलः!` with visarga (2x, held U5/U6) against clean vocative `पिड्गल!` (p006:P2, p007:P3, p007:P6, p012:P2). Print habit is inconsistent; held, not verdict.
- `मन्त्रस्यूतः` (2x, p007:P4 and the dative echo two lines later, held U7): spelled consistently, reads as a proper name (giver of the gift with the wealth); kept as seen.
- House spellings and sandhi stood as seen, never normalized: `निश्शङ्कं`, `कुतन्त्रं`, `सञ्चारं`/`सञ्चरन्तः`, `वणिजः`/`वणिग्भिः`/`अन्यवणिग्भिः` (ज्→ग् before voiced), open/joined mix (`तद् दिने`-type openness kept where printed), `भीकरयुद्धं` (भीकर is a word), `व्रणिताः`, `स्थातुम्`, `स्वैः` (valid instr.), `उद्भवति स्म` (colloquial present + स्म kept).
- Transcription joins asserted from both sides in Phase A: soft wrap hyphens dropped (`पर्वतमध्ये`, `एतादृश्यः`, `मरुभूमिचोराणां`, `समीपस्थे`, `हसनमहोदय`, `इतःपरं`, `गर्जनध्वनिः`, `तीक्ष्णप्रकाशतः`, `विद्यमानः`); `यत् वणिजः` spaced (separate words); `ह्यस्तन`-style hard hyphens: none in this range. Detached dot after `पिड्गल!` (p005:P8) omitted as speck with an `{x-com:}` on file.

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| U1 | p008:P3 w39 (तदा आश्चर्यं) | `भवनः वशे` | `भवनः` → `भवतः`? | MRP | likely | medium* | genitive required by वशे; print read at 2x only |
| U2 | p007:P3 w8 ("पिड्गल! अपरिचितायाम्) | `अनिरीक्षितम् व मम` | `व` → `च`? or `एव`? | LEX | likely | low* | व is no word here; च is minimal, एव fits sense; print read at 2x only |
| U3 | p007:P2 w9 (मानः संशयः) | `प्रदर्शितम् दिशम्` | `प्रदर्शितम्` → `प्रदर्शितां`? | AGR | likely | medium* | accusative feminine दिशम् needs agreeing participle; print read at 2x only |
| U4 | p007:P6 w4 ("पिड्गल! अहम्) | `न कश्चिदपि मान्त्रिकं` | `कश्चिदपि` → `कञ्चिदपि`? | KRK | likely | medium* | object of जेतुम् must be accusative; print read at 2x only |
| U5 | p008:P5 w9 (पिड्गलस्य वचनं) | `"पिड्गलः! अहं` | `पिड्गलः!` → `पिड्गल!`? | MRP | likely | medium* | vocative takes no visarga; print inconsistent with clean पिड्गल! elsewhere |
| U6 | p009:P3 w1 ('रे इदानीम्) | `'रे पिड्गलः!` | `पिड्गलः!` → `पिड्गल!`? | MRP | likely | medium* | same as U5; thought-vs-speech sort kept as printed |
| U7 | p007:P4 w8 ("पद्मपाद! मम) | `मन्त्रस्यूतः ... मन्त्रस्यूतः` | `?` (keep) | LEX | variant | low* | consistent 2x spelling; likely a proper name; settle against earlier instalments of this serial |

## Coverage

Skip lines: layout-only chunks (P1 of every page), the title (p005:P2), and the `{note:}` closer (p012:P10).
p005:P3 [हसनगोरिः पिड्गलेन] : clean
p005:P4 ['पद्मपादस्य पुनर्मिलनं] : clean
p005:P5 [पिड्गलस्य मनसि] : clean
p005:P6 [अतः सः] : F1
p005:P7 [सः पिड्गलं] : clean
p005:P8 [अकस्मात् आगतेन] : F2
p005:P9 ["किम् उत्तरं] : clean
p006:P2 [न ज्ञातवान्] : F6, F7
p006:P3 [सूत्रधारस्य भगवतः] : clean
p006:P4 [न, पद्मपाद!] : F3
p006:P5 [एतत् श्रुत्वा] : clean
p006:P6 [इदानीम् अपि] : clean
p006:P7 [पिड्गलस्य वचनेन] : clean
p007:P2 [मानः संशयः] : U3
p007:P3 ["पिड्गल! अपरिचितायाम्] : U2
p007:P4 ["पद्मपाद! मम] : U7
p007:P5 [पिड्गलस्य वचनेन] : clean
p007:P6 ["पिड्गल! अहम्] : U4
p007:P7 [मान्त्रिकं जेतुम्] : F10
p007:P8 [लक्ष्यप्राप्तेः अनन्तरं] : F11
p007:P9 [अतः एव] : F12
p007:P10 [इदानीं तु] : F13
p008:P2 [एकं दलम्] : clean
p008:P3 [तदा आश्चर्यं] : U1
p008:P4 [शक्तयः केनापि] : clean
p008:P5 [पिड्गलस्य वचनं] : F8, U5
p008:P6 [पद्मपाद! भवतः] : F4
p009:P2 [भवतः प्रयासः] : clean
p009:P3 ['रे इदानीम्] : U6
p009:P4 [तयोः वार्तालापः] : F9
p009:P5 [तस्मिन् समये] : clean
p009:P6 [उक्तवान् ---] : clean
p009:P7 [पिड्गलः दैन्यं] : F5
p010:P2 [बन्धनार्थं भवान्] : clean
p010:P3 ["पिड्गल! भवदीयां] : clean
p010:P4 [आरब्धवान्।] : clean
p010:P5 [पद्मपादस्य एतां] : clean
p010:P6 [पद्मपादः मन्दहासं] : clean
p011:P2 [वृकाणां व्याघ्राणां] : clean
p011:P3 [एवम् उक्त्वा] : clean
p011:P4 [पश्यति पिड्गले,] : clean
p011:P5 [एतत् अद्भुतं] : clean
p011:P6 [वृकान् च] : clean
p011:P7 [वणिजः नु] : clean
p012:P2 [हसनः आश्चर्यं] : clean
p012:P3 [पिड्गलः पद्मपादं] : clean
p012:P4 [पद्मपादः शिरश्चालनपूर्वकम्] : clean
p012:P5 [प्रकाशतः समग्रः] : clean
p012:P6 [पिड्गलः तत्र] : clean
p012:P7 [अनन्तरं हसनम्] : clean
p012:P8 [पिड्गलस्य वचनं] : clean
p012:P9 [क्रूरप्राणिनाम् आक्रमणतः] : clean
J1 p005:P6 {pb} -> p005:P7 fresh : ok (clean break after स्म।)
J2 p005:P9 {pb} -> p006:P2 {pc} : ok (पिड्गलः न ज्ञातवान् continues)
J3 p006:P2 {pb} -> p006:P3 {pc} : ok (same Padmapada speech continues; sentence ends नाटकम्। but speech runs on)
J4 p006:P7 {wb} -> p007:P2 {pc} : ok (विद्य-मानः solid join)
J5 p007:P6 {pb} -> p007:P7 {pc} : ok (कश्चिदपि मान्त्रिकं continues)
J6 p007:P10 {pb} -> p008:P2 {pc} : ok (लुण्टाकानाम् एकं दलम् continues)
J7 p008:P3 {pb} -> p008:P4 {pc} : ok (विद्यामानाः शक्तयः spaced join)
J8 p008:P6 {pb} -> p009:P2 {pc} : ok (अतः भवतः प्रयासः continues)
J9 p009:P5 {pb} -> p009:P6 {pc} : ok (सः उक्तवान् continues)
J10 p009:P7 {pb} -> p010:P2 {pc} : ok (एतादृशानां बन्धनार्थं continues)
J11 p010:P3 {pb} -> p010:P4 {pc} : ok (कर्तुम् आरब्धवान् spaced join)
J12 p010:P6 {pb} -> p011:P2 {pc} : ok (अहं वृकाणां continues)
J13 p011:P5 {pb} -> p011:P6 {pc} : ok (व्याघ्रान् वृकान् spaced join)
J14 p011:P7 {pb} -> p012:P2 fresh : ok (clean break after सन्तुष्टाः।)
J15 p012:P4 {wb} -> p012:P5 {pc} : ok (तीक्ष्ण-प्रकाशतः solid join)
J16 p012:P9 {pb} -> END : ok (clean break + {note: अनुवर्तते}; serial continues next issue)
