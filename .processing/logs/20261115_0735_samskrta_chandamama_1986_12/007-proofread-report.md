# Proofread report: 1986_12, START=7 (p007)

## Summary

Three-page story `महाश्वकः` (p007–p009, 28 chunks, 22 Devanagari body chunks); extract gate and proofread gate both pass with 0 errors and 0 notes, re-verified after the pass, and the story file is left byte-identical (no `{del:}`/`{ins:}`/`{sug-}` blocks added: no inherited `{sug-}` queue existed, the quote/sort pass needed no supply, and glyph-suspect forms have no Phase A flag on file so Phase B invents no new glyph claim). No systematic problem found; open sandhi throughout and the `अड्ग-` (`अड्गमार्जनं`, `अड्गीकृतवान्` 2×) press/transcription convention are kept as printed, and `scan.py orth` on deblocked text reports zero hits — the text is direct print transcription, not OCR output. Two sub-high-confidence readings (`आस्म्` for `आसम्` in p009:P5, `प्रेषयत्` for `प्रेषयेत्` in p008:P5) were examined against clause context and left untouched as print-faithful per the Phase B rule; no verse and no unchecked passages remain. Loc below would be `pNN:Pm` (lint page tag and chunk) with the chunk's first two words as anchor; there are no findings to locate.

## Findings

No findings — the text is clean.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|

## Patterns

1. Kept-as-printed house conventions (no action): open sandhi throughout (`तस्य अश्वशालायाम्`, `च अपि` — never flagged per doctrine); `अड्ग-` for `अङ्ग-` in 3 places (p007:P5 `अड्गमार्जनं`, p008:P7 and p008:P8 `अड्गीकृतवान्`); `परिणत`/`परिणति` as the standing word for `skilled/skill` (p007:P4, P5, P6); foreign-name spellings `अरब्बी`, `पर्शिया`, `सयां` (p007:P3).

## Unverified

None — nothing held for the user.

## Coverage

- p007:P1 ({x-com:layout}) : skip layout-note, no story text
- p007:P2 (# महाश्वकः) : skip title
- p007:P3 जयसागरदेशस्य राजा : clean
- p007:P4 यथा विविधजातीयाः : clean
- p007:P5 विविधजातीयानाम् अश्वानाम् : clean
- p007:P6 अन्यान्यदेशेषु अश्वसम्बन्धी : clean
- p007:P7 आशां प्रदर्श्य : clean
- p007:P8 एकदा कश्चन : clean
- p007:P9 एतत् वचनं : clean
- p007:P10 ({author: विवेकः}) : skip metadata
- p008:P1 ({x-com:layout}) : skip layout-note, no story text
- p008:P2 प्रकटितवान् सः : clean
- p008:P3 अनन्तरं रत्नदेवः : clean
- p008:P4 तदा मन्त्री : clean
- p008:P5 शतं सुवर्णनाणकानि : clean
- p008:P6 'यावत् कथनेन : clean
- p008:P7 इतः सप्तमे : clean
- p008:P8 वैशालीराजस्य आस्थाने : clean
- p009:P1 ({x-com:layout}) : skip layout-note, no story text
- p009:P2 अतीव सन्तुष्टः : clean
- p009:P3 सः नूतनः : clean
- p009:P4 एतत् श्रुत्वा : clean
- p009:P5 तदा मन्त्री : clean
- p009:P6 इति : clean
- p009:P7 तदा रत्नदेवः : clean
- p009:P8 "युक्तम् उक्तं : clean
- p009:P9 मन्त्रिणः सूचनानुसारं : clean
- p009:P10 एतया घटनया : clean
- J1 p007:P6 {pb} -> p007:P7 {pc} (continues) : ok
- J2 p007:P9 {pb} -> p008:P2 {pc} (continues) : ok
- J3 p008:P4 {pb} -> p008:P5 {pc} (continues) : ok
- J4 p008:P8 {pb} -> p009:P2 {pc} (continues) : ok
- J5 p009:P5 {pb} -> p009:P6 {pc} (continues) : ok
- J6 p009:P10 {pb} -> END (clean break) : ok
