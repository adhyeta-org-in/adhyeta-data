# Proofread report: 1986_06 p023 (उत्तमः यजमानः)

## Summary

One layout finding (print columns transposed on p24; file reordered into story order, F1) and two held word candidates (H1 `भवतुः`, H2 `क्षाम्यतु`). The `orth` scan on deblocked text returned zero hits, the proofread lint gate is green (exit 0, 0 error paras, 0 story findings), and all quote pairs balance in story order (DQ speech ×9 with one SQ inner quote, SQ request ×1, SQ short quote ×1, all kept as printed). Open sandhi across words (`तत् वचनं`, `एतत् श्रुत्वा`, `यावत् वेतनम्`) and mixed joined/open forms are the edition's house style and were kept. The text is a human transcription, not OCR output. Loc uses story coordinates `pNN:Pm` plus the first two words as anchor, counting words on the deblocked chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p024:P5→P6 (तस्य वचनं / 'श्वः परश्वः) | print column order: left column (`'श्वः...अहम्'`, `"एवं...`, `"योगिनाथस्य...इदानीं`) before right column (`उक्त्वा...`, `तस्य...भोजः...`, `तस्य...हसन् "भवान्`) | story order right-then-left (applied in file; print order recorded in Moves) | STY | error | high | print columns transposed: grammar ruptures both ways in print order, unique fit swapped; quote pairs balance only swapped |
| H1 | p024:P7 w3 ("एवं तर्हि) | `भवतुः` in `एवं तर्हि भवतुः कश्चित् बन्धुः` | `{sug-del:भवतुः}{sug-ins:भवतः}` (held, see Unverified) | SPL | likely | medium* | `भवतुः` is not a valid genitive of `भवत्`; context needs `भवतः` (your), one-stroke typesetting slip |
| H2 | p025:P8 w42 (कृपया मां) | `क्षाम्यतु` in `कृपया मां क्षाम्यतु` | `{sug-del:क्षाम्यतु}{sug-ins:क्षमस्व}` (held, see Unverified) | SPL | likely | low* | no `क्षम्` imperative `क्षाम्यतु` exists; context needs 2sg "forgive me", best single fix `क्षमस्व` |

## Patterns

None. The two held forms are unrelated singletons; no repeat, no systematic confusion. Open (unjoined) word-boundary sandhi is consistent house style, kept throughout.

## Unverified

H1 `भवतुः` (p024:P7 w3): glyphs verified clear at 3x in Phase A (`तुः` with ु-hook plus visarga), so this is a print typesetting slip, not a transcription misread. Clause-level re-segmentation was tried (`भवतु` imperative + stray visarga, vocative reading) and no segmentation saves `भवतुः`; the sentence needs the genitive `भवतः` ("your relative"). Held because Phase A carried no `{x-com:}`/`{sug-…}` license for a `{del:}` verdict and the image cannot be reopened; settling needs a second print look at `भवतुः` vs `भवतः`. H2 `क्षाम्यतु` (p025:P8 w42): glyphs clear in Phase A. `क्षम्` (forgive) has no `-य-`/`-आ-` imperative (`क्षमस्व`/`क्षमतु` 2sg, `क्षमताम्` passive); the `शाम्यति`-analogy (`शम्` → `शाम्यति` by long-श्यन्) may have produced an authorial `क्षाम्यतु`, or it is a slip for `क्षमस्व` (fits `कृपया मां`, 2nd person, single-word fix) or `क्षम्यताम्` (needs `मयि`, two changes, weaker). Held at low confidence; settling needs a lexicon check for any attested `क्षाम्य-` present stem plus editorial choice among `क्षमस्व`/`क्षमतु`.

## Moves

M1 (applied, user-reversible): p24 print columns transposed. Print order left (`'श्वः...अहम्'`, `"एवं तर्हि...भोजः।`, `"योगिनाथस्य...इदानीं`) then right (`उक्त्वा...पृष्टवान्।`, `तस्य...निवेदयतु...`, `तस्य...हसन् "भवान्`) ruptures at both seams: (a) `...इदानीं` + `उक्त्वा वरदराजः` gives `भवान्...इदानीं उक्त्वा` with the gerund's agent mismatched to the main verb and the marriage inquiry (`"एवं तर्हि...इत्यादिकं सर्वम् असत्यं वा?"`) referring to content not yet spoken; (b) `"भवान्` + `ज्ञातवान् खलु?" इति उक्तवान् वरदराजः` is grammatical but strands `"योगिनाथस्य...इदानीं` without a mate. Swapped order fits uniquely at every seam: `...योगिनाथः।` → `उक्त्वा वरदराजः...` (fresh episode, dismissal follows Yoganatha's speech; the dismissal words `'श्वः परश्वः वा मदीयं निर्णयं वदामि'` are reported later inside Varadaraja's speech to Bhoja, licensing `उक्त्वा` with Varadaraja as agent) → `"भवान्` + `'श्वः...वदामि' इति तु...अहम्"` (perfect DQ(SQ)DQ nesting, `भवान्...श्लाघते` honorific 3sg) → `"एवं तर्हि...` (Bhoja answers the marriage inquiry) → `"योगिनाथस्य...इदानीं` + `ज्ञातवान् खलु?"` (perfect edge pair across the page turn, same speaker वरदराजः). File reorders the p24 chunks into story order with `{pb}`/`{pc}` re-asserted for story adjacency and an `{x-com:}` marker at p024:P2; reverting is deleting that marker and swapping the two column blocks back. No other page is affected.

## Coverage

p023:P1 {x-com:layout:} : skip x-com-only
p023:P2 # उत्तमः : skip title
p023:P3 विरिञ्चपत्तनस्य : clean
p023:P4 वरदराजस्य : clean
p023:P5 एकदा : clean
p023:P6 तदा : clean (DQ opener pairs into P7; SQ request kept as inner speech)
p023:P7 {pc}वेतनं : clean (paired continuation of योगिनाथः speech)
p023:P8 वरदराजः : clean
p023:P9 "आर्य, : clean
p023:P10 {author:} : skip metadata
p024:P1 {x-com:layout:} : skip x-com-only
p024:P2 {x-com: print} : skip x-com-only (reorder marker for M1/F1)
p024:P3 उक्त्वा : clean (fresh episode; उक्त्वा agent वरदराजः, content reported at P6)
p024:P4 तस्य : clean (DQ pair भवतः...वदतु balanced)
p024:P5 तस्य : clean (DQ opener भवान् pairs into P6; F1)
p024:P6 {pc}'श्वः : clean (paired continuation; SQ inner quote kept)
p024:P7 "एवं : H1 (held भवतुः, see Unverified)
p024:P8 "योगिनाथस्य : clean (DQ opener pairs into p025:P2)
p025:P1 {x-com:layout:} : skip x-com-only
p025:P2 {pc}ज्ञातवान् : clean (paired continuation closing वरदराजः speech)
p025:P3 तत् : clean
p025:P4 "भवतः : clean
p025:P5 "अत्र : clean (DQ closes before इति भोजः; tail प्रति...उक्तवान् in P6)
p025:P6 {pc}निन्दाभङ्ग्या : clean (paired continuation)
p025:P7 अनन्तरं वरदराजः : clean
p025:P8 आपणस्य : H2 (held क्षाम्यतु, see Unverified)
p025:P9 अनन्तरं योगिनाथः : clean
p025:P10 अनन्तरं भोजस्य : clean
J1 p023:P6 {pb} -> p023:P7 {pc} (continues) : ok (भोजः यावत् + वेतनं ददाति unique fit)
J2 p023:P9 {pb} -> p024:P3 fresh (clean break) : ok (complete sentence, author footer, new episode)
J3 p024:P5 {pb} -> p024:P6 {pc} (continues) : F1 (transposed column turn; DQ(SQ)DQ nesting verified)
J4 p024:P8 {pb} -> p025:P2 {pc} (continues) : ok (...इदानीं + ज्ञातवान् खलु? unique fit, same speaker)
J5 p025:P5 {pb} -> p025:P6 {pc} (continues) : ok (...वरदराजं प्रति + निन्दाभङ्ग्या उक्तवान् unique fit)
J6 p025:P10 {pb} -> END (clean break) : ok
