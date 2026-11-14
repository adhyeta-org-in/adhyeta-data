# Proofread report: samskrta_chandamama 1984_12, story p050 (scans 50–51, last pages of issue)

Loc keyed on story coordinates `pNN:Pm:wN` (NN = scan sequence from 50; Pm = chunk number within the span matching lint `P` numbers; wN = word index on the chunk counting whitespace-separated Devanagari tokens from 1, blocks and `---` excluded). Anchors are the chunk's first two words (plus context where needed).

## Summary

7 findings: 6 high-confidence verdicts already landed as `{del:}`/`{ins:}` blocks in `p050.md` (F1–F6, all print slips fixed minimally), plus 1 held candidate (F7, category `अरेत्रियाकथा`, low*). Two systematic problems: quote-sort mixing in spoken speeches, with a stray single turning up before the double-close in four speeches (F2–F5), and single-sign print slips (dropped `ण`, stray `्र`; F1, F6). No passage was left unchecked; every sentence was read for continuity against the Phase A transcription, and all four `J` joints were walked in order. The text is hand-transcribed print, not OCR output, so the `OCR` category below means print/typesetting slips, not scanner damage. Orth-scanner hits were all dismissed in context: `ळ` twice is the print's own spelling (`सम्मिळिताः`, verified at 3x on both pages), and `!` is the print's exclamation (`घटना!`, `अगौरवम्!`).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p050:P4:1 (`महाराजः जागरितः`) | `कोलाहलकारततः महाराजः` | `कोलाहलकारणतः महाराजः` | SPL | error | high | `करततः` is not a word; waking because of the tumult wants `कारणतः` |
| F2 | p050:P9:11 (`उक्तवान् --- 'भो` … `इच्छामि'"`) | `'भो` … `इच्छामि'"` | `"भो` … `इच्छामि"` | OCR | error | high | reported speech opens single and closes single-plus-double; both marks corrected to doubles |
| F3 | p051:P4:17 (`उद्युक्ताः सन्ति'"`) | `सन्ति'"` | `सन्ति"` | OCR | error | high | open is double with no inner single opened; the `'` before the close is a stray sort |
| F4 | p051:P8:43 (`दृष्ट्या प्रधानम्` … `इति उक्तवान्`) | `प्रधानम् '"` | `प्रधानम् "` | OCR | error | high | same stray-`'` close as F3 in the same long speech |
| F5 | p051:P9:1 (`' भवतः वचनं` … `सत्यम् '"`) | `' भवतः` … `सत्यम् '"` | `" भवतः` … `सत्यम् "` | OCR | error | high | king's reply opens single and closes single-plus-double; both marks corrected to doubles |
| F6 | p051:P9:15 (`शृङ्खलया ब्रन्धितवान्`) | `ब्रन्धितवान्` | `बन्धितवान्` | OCR | error | high | `ब्रन्धित-` is no word; the extra `्र` stroke is a print slip and `बन्धित-` stands as the house causative (cf. `बन्धितः` p050:P10) |
| F7 | p051:P14:1 (`अरेत्रियाकथा`) | `अरेत्रियाकथा` | `अरेबियाकथा` | SPL | error | low* | Mosul-tale category sense wants `अरेबिया`, but print shows `त्रि` clearly at 4x; held for the user |

## Patterns

Stray single before the double-close in spoken speeches (4x): the `'"` close in F2, F3, F4, F5, each fixed by deleting the stray `'` (F2 and F5 additionally raise the single open to `"`). Single-sign print slips (2x): F1 (dropped `ण`), F6 (intrusive `्र`). Kept print variants (not findings): `सम्मिळिताः` with `ळ` twice (p050:P6, p051:P6, consistent across the column turn), `बन्धितः`/`बन्धितवान्` causatives for `बद्ध-`, visarga kept before vowels throughout, `महाराजवसतितः` (tas-ablative, stands as printed), `निमेषणमात्रेण`, `तद्दिने`, exclamatory `!` (`घटना!`, `अगौरवम्!`), four-dot trailer `?"....इति`, and loose spaces inside quotes (`" प्रभो!`, `सत्यम् "`, `' चोरः`, `अभविष्यत् '`). Kept quote sorts: balanced thought-singles for the king's reflection `' चोरः … अभविष्यत् '` (p051:P10, `चिन्तितवान्` frame) and the two-word interjection `'अग्रे वदतु'` (p051:P7).

## Unverified

F7 `अरेत्रियाकथा` (p051:P14:1, category colophon `"अरेत्रियाकथा"`): the `त्रि` akshara is clear at 4x with its repha hook, so a `बि` misreading at transcription time is unlikely; yet sense (a Mosul-king tale, i.e. an Arabian story) strongly suggests `अरेबियाकथा`. Settle with another 1984 issue's Arabian-tale colophon or the issue index; candidates are `अरेबियाकथा` ("Arabian story") or a genuinely unknown label kept as printed. Held with the Phase A note kept on file; no verdict landed.

## Coverage

p050:P1 `{x-com:layout:` : skip layout-only chunk
p050:P2 `# चोरस्य` : skip title chunk
p050:P3 `मौसुलदेशस्य महाराजः` : clean
p050:P4 `महाराजः जागरितः` : F1
p050:P5 `अधिकारिणः शिबिरस्य` : clean
p050:P6 `नगरवासिनः तत्र` : clean
p050:P7 `महाराजः इदानीं` : clean
p050:P8 `एतन्मध्ये अकस्मात्` : clean
p050:P9 `अधिकारिणः तं` : F2
p050:P10 `एकः सेनाधिकारी` : clean
p051:P1 `{x-com:layout:` : skip layout-only chunk
p051:P2 `दयितुम् इच्छति।"` : clean
p051:P3 `"चोरः मम` : clean
p051:P4 `चोरः महाराजं` : F3
p051:P5 `"भवतः सम्माननं` : clean
p051:P6 `"राजन्! भवतः` : clean
p051:P7 `'अग्रे वदतु'` : clean
p051:P8 `अन्तः एव` : F4
p051:P9 `" भवतः वचनं` : F5, F6
p051:P10 `तद्दिने एव` : clean
p051:P11 `किञ्चिद्दूरगमनानन्तरं महाराजः` : clean
p051:P12 `{x-com: print` : skip x-com note chunk
p051:P13 `{x-com: category` : skip x-com note chunk
p051:P14 `अरेत्रियाकथा` : F7
J1 p050:P5->p050:P6 : ok (बहवः नगरवासिनः, spaced join)
J2 p050:P10->p051:P2 : ok (निवेदयितुम्, solid word join)
J3 p051:P7->p051:P8 : ok (गतवान्। अन्तः, sentence-boundary spaced join, same print para)
J4 p051:P11->END : ok (clean break; story ends, category colophon follows)
