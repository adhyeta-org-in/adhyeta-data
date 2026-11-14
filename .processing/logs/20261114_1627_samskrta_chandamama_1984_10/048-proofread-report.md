# Proofread report — 1984_10 p048 (RUN 20261114_1627_samskrta_chandamama_1984_10)

## Summary

7 findings: 3 quote-mark corrections (STY / style / high, F1–F3), 2 print-slip corrections (OCR / error / high, F4–F5), 1 stray-mark deletion (ENC / error / high, F6), and 1 held spelling candidate (OCR / likely / medium*, F7). The systematic problems are the print's dropped quote opens (2 supplied) with one single-spoken pair promoted to doubles, plus dropped vowel signs in print (ु in F4, आ in F7, ह/ह in F5). `scan.py orth` on deblocked story text gave 1 hit (F6's full stop), otherwise clean; word, sandhi, quote, and flow passes found nothing else; no passages were left unchecked. The text was transcribed by eye from scans (not OCR), with uncertain glyphs verified under enlarged crops in Phase A. Loc below is `pNN:Pm` (NN = scan sequence from filename `p048` plus `{pgb}`-span order; Pm = chunk number in that span, matching lint `P` numbers) plus the chunk's first two words as anchor; corrections travel only as blocks in the story file, never as silent edits. Print forms kept as seen with no block: open-sandhi spellings (`यत् चोरितवस्तुभिः`, `एतत् न`, `तत् उद्यानम्`, `एतत् सर्वं`), house spellings (`अजागरूकाः`, `अनुकम्पं`), and the odd name-form `रहमत्मामकः` (possibly fused `रहमत्-नामकः`, but no confident segmentation, so left untouched).

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p049:P8 «अतः सः» | `प्रार्थितवान् --- अहं चोरः` | `प्रार्थितवान् --- {ins:"}अहं चोरः` | STY | style | high | spoken plea (`प्रार्थितवान्` … `इति`) takes doubles; open dropped in print, pinned after `---` |
| F2 | p050:P3 «एतेन उत्साहितः» | `उक्तवान् --- मां किमर्थम्` | `उक्तवान् --- {ins:"}मां किमर्थम्` | STY | style | high | spoken challenge (`उक्तवान्` … `इति`) takes doubles; open dropped in print, pinned after `---` |
| F3 | p050:P4 «एतेन वचनेन» | `'माम् एव न्यायनियमान् शिक्षयति वा?'` | `{del:'}{ins:"}माम् एव न्यायनियमान् शिक्षयति वा?{del:'}{ins:"}` | STY | style | high | spoken (`इति वदन्`) takes doubles per issue house style; both singles promoted |
| F4 | p050:P6 «अनन्तरं भिक्षुकवेषधारी» | `भिक्षकवेषधारिणः` | `{del:भिक्षक}{ins:भिक्षुक}वेषधारिणः` | OCR | error | high | dropped ु matra in print; `भिक्षुक` spelled with ु four times elsewhere in this story |
| F5 | p051:P8 «रहमतः उद्यानरक्षकं» | `मध्याह्ने पिपासितं` | `{del:मध्याह्ने}{ins:मध्याह्ने}` | OCR | error | high | ह/ह slip in print; `मध्याह्नपर्यन्तं` (p049:P3) and `मध्याह्ने` (p051:P9) pin `मध्याह्न` |
| F6 | p049:P8 «अतः सः» | `शान्तः. भवतु` | `शान्तः{del:.} भवतु` | ENC | error | high | ASCII full stop after Devanagari (orth `fullstop-for-danda` hit); sentence continues, so the stop is print noise |
| F7 | p051:P4 «दशवर्षीयः पुत्रः» | `तनि अहं प्रदर्शयामि` | `{sug-del:तनि}{sug-ins:तानि} अहं प्रदर्शयामि` | OCR | likely | medium* | dropped आ matra (`तानि वस्तूनि`, cf. `तानि वस्तूनि` in p051:P6); glyph re-check closed so held for the user |

## Patterns

PAT-1 print quote sorts: doubles for all reported speech (verified two-stroke opens/closes, e.g. p048:P5, p048:P8, p049:P6, p049:P9, p051:P4, p051:P6, p051:P8–P9), with one embedded single-inside-double kept as seen (`'चोरम् अन्विष्यतु'` inside the king's speech, p048:P6). 2 dropped opens supplied (F1, F2) and 1 single-spoken pair promoted to doubles (F3); spoken takes doubles and thought takes singles with no thought-quotes in this range.
PAT-2 dropped vowel signs in print: ु (F4, corrected), आ (F7, held), and ह for ह (F5, corrected) — 3 spots, each pinned by a repeated correct form in the same story.

## Unverified

F7 `तनि` → `तानि` (OCR, medium*): agreement with neuter plural `वस्तूनि` and the parallel `तानि वस्तूनि` (p051:P6) make `तानि` near-certain, but the print's त/ता glyph cannot be re-checked with images closed (read `तनि` at display size in Phase A); a print re-check at 3x of `तनि अहं प्रदर्श-यामि` would settle it. The candidate travels as `{sug-del:तनि}{sug-ins:तानि}` in the story file.

## Coverage

p048:P1 «{x-com:layout:» : skip layout
p048:P2 «# राजाज्ञा» : skip title
p048:P3 «कदाचित् बस्ताराज्यस्य» : clean
p048:P4 «एषा वार्ता» : clean
p048:P5 «राजा तु» : clean
p048:P6 «सर्वान् रक्षाधिकारिणः» : clean
p048:P7 «कुर्वन्ति इति» : clean
p048:P8 «महाराजस्य आज्ञां» : clean
p048:P9 «रक्षणप्रमुखः सर्वान्» : clean
p048:P10 «"सायङ्काले नगरस्य» : clean
p048:P11 «{category: अरेबिया» : skip metadata
p049:P1 «{x-com:layout:» : skip layout
p049:P2 «सूचना आसीत्।» : clean
p049:P3 «रहमत्मामकः कश्चित्» : clean
p049:P4 «तत्र एकम्» : clean
p049:P5 «जलपानम् अर्धं» : clean
p049:P6 «कवेषं धृत्वा» : clean
p049:P7 «रहमतः यद्यपि» : clean
p049:P8 «अतः सः» : F1, F6
p049:P9 «"अहो! एवं» : clean
p050:P1 «{x-com:layout:» : skip layout
p050:P2 «गृहीतवान्। रक्षणाधिकारी» : clean
p050:P3 «एतेन उत्साहितः» : F2
p050:P4 «एतेन वचनेन» : F3
p050:P5 «इति वदन्» : clean
p050:P6 «अनन्तरं भिक्षुकवेषधारी» : F4
p050:P7 «रहमतः यदा» : clean
p050:P8 «उद्यानपालकः दशवर्षीयेण» : clean
p051:P1 «{x-com:layout:» : skip layout
p051:P2 «किमपि रहस्यवार्तालापं» : clean
p051:P3 «अकस्मात् प्रवृत्तेन» : clean
p051:P4 «दशवर्षीयः पुत्रः» : F7
p051:P5 «बालकस्य एतत्» : clean
p051:P6 «"कुत्र सन्ति» : clean
p051:P7 «रुदन् बालकः» : clean
p051:P8 «रहमतः उद्यानरक्षकं» : F5
p051:P9 «एतेन वचनेन» : clean
p051:P10 «अधिकारिणः चोरितवस्तुभिः» : clean
J1 p048:P6 {pb} -> p048:P7 {pc} (continues) : ok (किं + कुर्वन्ति, spaced column joint mid-speech; embedded 'चोरम्' pair balanced inside)
J2 p048:P10 {pb} -> p049:P2 {pc} (continues) : ok (इति + सूचना, spaced page turn completing the सूचना sentence)
J3 p049:P5 {wb} -> p049:P6 {pc} (continues) : ok (भिक्षु + कवेषं = भिक्षुकवेषं, solid column joint)
J4 p049:P9 {wb} -> p050:P2 {pc} (continues) : ok (अनु + गृहीतवान् = अनुगृहीतवान्, solid page turn)
J5 p050:P4 {pb} -> p050:P5 {pc} (continues) : ok (?' + इति वदन्, spaced column joint; quote plus इति continues one sentence)
J6 p050:P8 {pb} -> p051:P2 {pc} (continues) : ok (सह + किमपि, spaced page turn)
J7 p051:P6 {pb} -> p051:P7 fresh (clean break) : ok (column turn to fresh paragraph रुदन् बालकः)
J8 p051:P10 {pb} -> END (clean break) : ok (story ends नियोजितवान्।; no dangling pair)
