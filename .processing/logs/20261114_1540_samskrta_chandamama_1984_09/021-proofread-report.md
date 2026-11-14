# Proofread report: 1984_09 p021 (विवेकः, page 1 of story)

## Summary

Five findings on one page (7 body chunks): three verified print-misprint verdicts (F1--F3, all single-occurrence deviations against consistent forms on the same page), one supplied closing quote at the page edge (F4, style), and one held word candidate (F5, unverified). Checked-correct and kept as seen: `ऐकमत्येन` (instrumental of ऐकमत्यम् `unanimity', grammatical, not a misprint), uniform print double-quote sorts throughout (kept per the p01.proofread kept-sorts precedent; the P4 thought-quote is not re-sorted alone), and the print comma after `प्राप्तुवन्तः` (kept as print punctuation; a speck-dot after it was omitted as noise in Phase A). Scanner (`scan.py orth`) reported no hits. `Loc` is `p021:Pm:Wn`: page span `p021`, lint chunk `Pm`, word `Wn` counting print words on the chunk from 1 (a `{del:}/{ins:}`/`{sug-:}` pair counts at its span's position).

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p021:P4:10 `ज्ञानवान् वीवेकी च` | `{del:वीवेकी}` | `{ins:विवेकी}` | SPL | error | high | `*वीवेक` is no word; `विवेकी` x3 plus `विवेकः`/`विवेकिनः` on the same page, long-`ी` on first syllable is a single-glyph slip |
| F2 | p021:P3:18 `ये प्राप्तुवन्तः,` | `{del:प्राप्तुवन्तः}` | `{ins:प्राप्नुवन्तः}` | MRP | error | high | `kta` stem `प्राप्त` cannot take a `शतृ` ending; relative `ये` needs present participle `प्राप्नुवन्तः` |
| F3 | p021:P8:10 `बुद्धिमत्तायाः परिक्षां` | `{del:परिक्षां}` | `{ins:परीक्षां}` | SPL | error | high | `परि + ईक्षा` is lexically `परीक्षा`; page prints long `ी` twice (`परीक्षाः`, `परीक्षा`) against this once-short form |
| F4 | p021:P9:21 `ददामि।` | `{ins:"}` (close after `।`, before `{pb}`) | `"` | STY | style | high | house pair-per-para convention: sentence complete at page end, each para closes its own pair (p01.proofread supplied-`{ins:"}` precedent); tale speech continues on p022, whose range supplies its own open |
| F5 | p021:P3:11 `आहूय काञ्चन` | `{sug-del:काञ्चन}` | `{sug-ins:काश्चन}` | SPL | likely | medium* | `काञ्चन` (`gold') cannot agree with feminine `परीक्षाः`; feminine indefinite `काश्चन` fits; glyph (`ञ` vs `श`) not 3x-verified in Phase A so held, not verdict |

## Patterns

Vowel-length misprints (x2: F1, F3) — each a single deviant length against consistent forms on the same page (`वीवेकी` vs `विवेकी` x3; `परिक्षां` vs `परीक्षा` x2).

## Unverified

F5 `काञ्चन`/`काश्चन`: grammar and agreement point to `काश्चन`, but the print glyph (`ञ` vs `श`) was not enlarged and verified in Phase A, so no verified verdict is issued; a 3x scan look at P3 word 11 would settle it.

## Coverage

p021:P3 `चित्रपुरग्रामस्य ग्रामाधिकारी` : F2, F5
p021:P4 `एकदा तस्य` : F1
p021:P5 `प्रभाकरश्रेष्ठी बहून्` : clean
p021:P6 `तदा सर्वे` : clean
p021:P7 `एकस्मिन् दिने` : clean
p021:P8 `ग्रामाधिकारिणः वचनं` : F3
p021:P9 `तदा ग्रामाधिकारी` : F4
p021:P1 `{x-com:layout` : skip layout declaration
p021:P2 `# विवेकः` : skip title
p021:P10 `{misc: "भगिनी"}` : skip footer metadata (node `भगिनी` proofread clean)
J1 p021:P6 {pb} -> p021:P7 fresh (clean break) : ok
J2 p021:P9 {pb} -> END (clean break) : F4 (close supplied; tale speech continues on p022, next range opens the pair)
