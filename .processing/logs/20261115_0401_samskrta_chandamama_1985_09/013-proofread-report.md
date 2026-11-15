# Proofread report: 1985_09, story starting p13 (`p013.md`), RUN 20261115_0401_samskrta_chandamama_1985_09

## Summary

Story `शापरहस्यम्` (वेतालकथा frame: Vikrama carries the corpse, Vetala narrates the Ratnapala tale, pp. 13–16). Three findings, all `STY`/`error`/`high`: two print defects where a speech-open double quote lost one stroke (single open, double close), and one tale-frame open left unclosed by the print, closed here with a supplied mark at the pinned story-end position. One systematic pattern: dropped open-quote strokes (2x). No passage left unchecked; every Phase A residual routed, orth scan clean, no new glyph claims invented (no Phase A `{x-com:}`/`{sug-}` on file for any word, so no word-form verdicts). Text is hand transcription from print, not OCR. Assumption recorded: the tale and story end together at p16 (coordinator boundary); if p17 opens mid-frame (Vetala questioning Vikrama), drop F3 at compile time.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p014:P9 `रत्नपालः गोपालं` | `'अये बालक! ... वा?"` (open single, close double) | `"अये बालक! ... वा?"` via `{del:'}{ins:"}` | STY | error | high | doubles mark spoken speech; close prints double, open dropped a stroke (single verified at 3x with stray dot) |
| 2 | p016:P7 `'भवान् स्वभावेन` | `'भवान् ... रक्षति"` (open single, close double) | `"भवान् ... रक्षति"` via `{del:'}{ins:"}` | STY | error | high | comforting speech takes doubles; close prints double, open dropped a stroke (single verified at 3x with stray dot) |
| 3 | p016:P7 `नास्ति एव` (pairs p014:P2 `पूर्वं रत्नपालः`) | tale-frame open `‘‘पूर्वं` never closed in print | supplied `{ins:"}` after final `इति।` | STY | error | high | frame tale ends where the story ends; close position and double sort pinned by the boundary |

## Patterns

- Print drops one stroke of a speech-open double quote (single-open/double-close pair), 2x: F1 (p014:P9 `अये बालक`), F2 (p016:P7 `भवान् स्वभावेन`). Closes print double in both; opens verified single at 3x, each with a stray dot that was omitted as print noise.

## Unverified

None. No word was held: both inherited `{sug-ins:'}` flags promoted (F1, F2), orth scan reported no hits, and grammar/sense review found no other defect (house spellings `वणिक्`, `कनिष्ठ`, `कोटीश्वर`, open sandhi and Epic forms kept as print).

## Coverage

p013:P1 `{x-com:layout: 2col,` : skip layout-only chunk
p013:P2 `# शापरहस्यम्` : skip title
p013:P3 `वेतालवहनेन अभ्यस्तः` : clean
p013:P4 `अनन्तरं वेतालेन` : clean
p013:P5 `{category: वेतालकथा}{pgb}` : skip metadata
p014:P1 `{x-com:layout: 2col,` : skip layout-only chunk
p014:P2 `"पूर्वं रत्नपालः` : F3
p014:P3 `एवं स्थिते` : clean
p014:P4 `सप्ताश्वयुते रथे` : clean
p014:P5 `महाधनिकः कश्चित्` : clean
p014:P6 `{pc}वसतिव्यवस्थाम् उपकल्पितवन्तः।` : clean
p014:P7 `रत्नपालः वृद्धस्य` : clean
p014:P8 `तत्समये गोपालः` : clean
p014:P9 `रत्नपालः गोपालं` : F1
p014:P10 `"निश्चयेन करोमि।` : clean
p014:P11 `'कश्चित् कर्मकरः` : clean
p015:P1 `{x-com:layout: 2col,` : skip layout-only chunk
p015:P2 `{pc}तारतम्यम् एव` : clean
p015:P3 `"भवतः एकः` : clean
p015:P4 `एतेन रत्नपालस्य` : clean
p015:P5 `तदा गोपालः` : clean
p015:P6 `रत्नपालः गोपालस्य` : clean
p015:P7 `तत्समये भुवनेन्द्रमहर्षिः` : clean
p015:P8 `{pc}निवेदितवान्। 'महत्कष्टम्` : clean
p015:P9 `भुवनेन्द्रमहर्षेः दयागुणं` : clean
p015:P10 `तदा महर्षिः` : clean
p016:P1 `{x-com:layout: 2col,` : skip layout-only chunk
p016:P2 `{pc}गोपालस्य शापानुसारं` : clean
p016:P3 `रत्नपालः आतङ्कं` : clean
p016:P4 `"गोपालेन अनुचितं` : clean
p016:P5 `{pc}तिरस्कुर्वन् धनमदेन` : clean
p016:P6 `एतत् निराकर्तुम्` : clean
p016:P7 `'भवान् स्वभावेन` : F2, F3
J1 p013:P4 {pb} -> p014:P2 fresh (clean break) : ok
J2 p014:P5 {pb} -> p014:P6 {pc} (continues) : ok
J3 p014:P11 {wb} -> p015:P2 {pc} (continues) : ok
J4 p015:P7 {pb} -> p015:P8 {pc} (continues) : ok
J5 p015:P10 {pb} -> p016:P2 {pc} (continues) : ok
J6 p016:P4 {pb} -> p016:P5 {pc} (continues) : ok
J7 p016:P7 {pb} -> END (clean break) : ok
