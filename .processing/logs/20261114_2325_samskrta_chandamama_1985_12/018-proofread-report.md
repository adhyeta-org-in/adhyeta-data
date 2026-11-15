# Proofread report: 1985_12 p018 (योग्यः साहाय्यकः, scans 18–19)

## Summary

Four findings, all applied as verdict blocks in the story file: three print-misprint corrections (F1–F3, severity error, confidence high) and one quote-nesting repair (F4, style/error, confidence high). One form held unverified without touching the file (U1: `क्षाम्यतु`, confidence low*). No systematic bias found; the three misprints are unrelated (wrong word, short vowel, wrong conjunct). Loc below is story coordinates `pNN:Pm:w` (page span, chunk, word counted on the chunk from 1, blocks and `---` skipped) plus anchor words. The text is a print-faithful transcription, not OCR output; the Sanskrit orth scanner reported no hits.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p018:P9:20 (`दोषान् कृत्वा एम`) | `एम` | `एव` | OCR | error | high | `एम` is not a word; `एव` fits (`दोषान् कृत्वा एव`); print `म`/`व` verified at 3x in Phase A |
| 2 | p019:P4:6 (`पृष्टवान् गोराङ्गाय`) | `गोराङ्गाय` | `गौराङ्गाय` | CNS | error | high | name spelled `गौराङ्ग` in three other places; print `गो` verified at 4x in Phase A |
| 3 | p019:P6:1 (`गौराङ्गसट्टशाः सर्वदा`) | `सट्टशाः` | `सदृशाः` | OCR | error | high | `सट्टशाः` is not a word; `सदृशाः` fits (`गौराङ्गसदृशाः`); ट्ट-like conjunct verified at 5x in Phase A |
| 4 | p019:P5:24→P6:19 (`चिन्तयामि` quote) | `"गौराङ्गः … "गौराङ्गसट्टशाः … किल?"` (outer unclosed) | inner `"…"` → `'…'` (thought), supply outer `"` close | STY | error | high | `चिन्तयामि` introduces thought, which takes singles (house precedent); outer speech needs its close before final `इति` |

## Unverified

| # | Loc | Form | Conf | What would settle it |
|---|---|---|---|---|
| U1 | p018:P9:1 (`क्षाम्यतु भवान्`) | `क्षाम्यतु` | low* | `क्षम्` is Ātmanepada (expected `क्षमताम्`), so `क्षाम्यतु` looks like a print misprint, but the glyph was read clearly in Phase A with no flag on file, so no block was issued; re-examining the scan (closed in this phase) or a dictionary check of any sanctioned `क्षाम्यतु` form would settle it |

## Notes (variants kept as seen, not findings)

House spellings and open-sandhi variants stand: `प्रामाणिक` (×2) for `प्रामाणिक`, `यत् पूर्वं`, `एतत् स्थानम्`, `एतत् सत्यं`, and the `साहाय्यकानां`/`साहाय्यकानाम्` anusvāra alternation. The singles in `'एतदर्थं … अस्ति'` (notice text) and the `"भगिनी"` footer misc are kept as printed.

## Coverage

p018:P1 {x-com:layout} : skip layout
p018:P2 योग्यः साहाय्यकः : skip title
p018:P3 लक्ष्मीपुरस्य कस्यचित् : clean
p018:P4 कदाचित् गौराङ्गः : clean
p018:P5 गौराङ्गः धैर्येण : clean
p018:P6 भूस्वामी तानि : clean
p018:P7 तदा गम्भीरः : clean
p018:P8 एवं तर्हि : clean
p018:P9 क्षाम्यतु भवान्। : F1, U1
p019:P1 {x-com:layout} : skip layout
p019:P2 सिध्यति। मम : clean
p019:P3 भवन्तम् अस्मिन् : clean
p019:P4 गम्भीरस्य गमनानन्तरं : F2
p019:P5 तदा भूस्वामी : F4
p019:P6 सर्वदा साहाय्यकानां : F3, F4
p019:P7 भूस्वामिनः वचनेषु : clean
p019:P8 कार्यनिर्वहणसन्दर्भे दोषाः : clean
p019:P9 भूस्वामिनः तर्कः : clean
J1 p018:P5 {pb} -> p018:P6 {pc} (continues) : ok
J2 p018:P9 {pb} -> p019:P2 {pc} (continues) : ok
J3 p019:P5 {wb} -> p019:P6 {pc} (continues) : ok
J4 p019:P9 {pb} -> END (clean break) : ok
