# Proofread report — 1987_07, पृष्ठ 8–9 — वज्रवीक्षाः (story start p008)

## Summary

Phase B on `.processing/samskrta_chandamama/1987_07/p008.md` (scan pages 8–9, images closed). 3 findings: 1 error fixed as a `{del:}/{ins:}` verdict (`वधते`→`वर्धते`), 1 held candidate kept as `{sug-del:}/{sug-ins:}` (`गोवधनागारे`), 1 print inconsistency recorded as a variant and kept (`नागवर्मा`/`नागदत्तः`). `scan.py orth` on deblocked text: 0 hits. Quote pass: all double-quote speech pairs balanced and correctly sorted; the one nested speech uses single quotes as printed; no para ships unbalanced. Both `{pb}`/`{pc}` joints and the `{pgb}` page seam read continuous. Loc below is `pNN:Pm` + word number within the chunk (lint P numbering, counting all chunks of the page); anchor = first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p008:P3 w2 (किशोरवर्ममहाराजः गोवधनागारे) | `गोवधनागारे` | `गोवर्धननगरे` | SPL | likely | medium* | Held as `{sug-del:गोवधनागारे}{sug-ins:गोवर्धननगरे}`; as printed it has no Sanskrit parse (नागार/वधन not words) and "king ruled in the cow-wealth storehouse" fails narratively; `गोवर्धननगरे` is the unique minimal repair (dropped `र्`, garbled `नगरे`) but the intended toponym cannot be recovered from text alone |
| 2 | p009:P2 w13 (चन्द्रचूडः एकं) | `शोभा वधते` | `शोभा वर्धते` | OCR | error | high | `वधते` is not an attested form; print dropped `र्`; "if you accept this diamond, your necklace's beauty will **increase**" admits only `वर्धते`; fixed as `{del:वधते}{ins:वर्धते}` per Phase A `{x-com:}` on file |
| 3 | p009:P4 w2 (अनन्तरं नागवर्मा) | `नागवर्मा` | `नागदत्तः` | CNS | variant | high | Same merchant is `नागदत्तः` in p009:P6–P11; print inconsistency, kept as printed per Phase A `{x-com:}` — no block issued |

## Patterns

None — no defect repeats.

## Unverified

- `गोवर्धननगरे` (F1): what would settle it — the p008 scan line 1 at higher resolution, or any other occurrence of the capital's name in the issue. Kept as a held `{sug-}` candidate for human review; not an open task.

## Dispositions of Phase A carried candidates

- `किशोरवर्ममहाराजः` spacing gap (p008:P3): **accepted Phase A reading, no block.** The gap inside the name (कि शोर…) and after कि in किशोरवर्मा is a typesetting artifact, not a word break; text already carries the single name `किशोरवर्मा` consistently in P3 and P4. Checked print-faithful.
- `गोवधनागारे` (p008:P3): **held** — see F1.
- `वधते` (p009:P2): **ruled** — fixed via `{del:वधते}{ins:वर्धते}`; see F2.
- Standalone `"भगिनी"` (p008:P11): **ruled print-faithful, no block.** One-word vocative address ("Sister!") by चन्द्रचूडः opening the exchange continued on p009:P2 (`चन्द्रचूडः एकं वज्रम् उन्नीय प्रदर्शयन्…`); both quote marks present and balanced in print; the page-turn `{pgb}` seam to p009:P2 is narratively continuous (address → he lifts a diamond and speaks).
- p009:P8 opening quote folded to double (Phase A `{x-com:}`): **re-derived and ratified.** Reporting verb `पृष्टवन्तौ` (dual, the two merchants) pins spoken discourse; house style gives `"`. No further block needed — the mark is already in text.
- `युवराज्ञी` for the राजकुमारी (p009:P4, P5): **stands as printed.** Consistent within the page; she is the yuvarāja's bride (p008:P3: हेमपुरयुवराजाय जयसेनाय), so the anticipatory title fits sense. House-style variant, not flagged.

## Coverage appendix

Chunks (lint P numbers include layout/title chunks):

- p008:P1 (layout x-com) : skip layout-declaration chunk
- p008:P2 (वज्रवीक्षाः) : skip title
- p008:P3 किशोरवर्ममहाराजः गोवधनागारे : F1 (spacing-artifact note dispositioned above, no block)
- p008:P4 विवाहसन्दर्भे राजकुमार्यै : clean
- p008:P5 बहवः प्रसिद्धाः : clean
- p008:P6 प्रथमं धनगुप्तः : clean
- p008:P7 नमस्कृत्य स्वसमीपस्थानि : clean
- p008:P8 तदा धनगुप्तः : clean
- p008:P9 तदा मनोरमा : clean
- p008:P10 अनन्तरं चन्द्रचूडः : clean
- p008:P11 "भगिनी" : clean (dispositioned above)
- p009:P1 (layout x-com) : skip layout-declaration chunk
- p009:P2 चन्द्रचूडः एकं : F2
- p009:P3 मनोरमा कोपेन : clean
- p009:P4 अनन्तरं नागवर्मा : F3
- p009:P5 युवराज्ञी सर्वाणि : clean (युवराज्ञी dispositioned above)
- p009:P6 नागदत्तः वज्रस्य : clean (nested single-quote speech as printed, house style)
- p009:P7 नागदत्तः यदा : clean
- p009:P8 पृष्टवन्तौ : clean (opening quote ratified, dispositioned above)
- p009:P9 "भवन्तः प्रायः : clean
- p009:P10 "भवतः वचन : clean
- p009:P11 "अत्रैव भवतां : clean

Joints (from in-file `## Joints` index):

- J1 p008:P6 {pb} -> p008:P7 {pc} : ok (column turn; `गत्वा` → `नमस्कृत्य` one continuous sentence)
- J2 p009:P7 {pb} -> p009:P8 {pc} : ok (column turn; `च` → `पृष्टवन्तौ` one continuous sentence)
- p008:P11 -> p009:P2 {pgb} page seam : ok-text (address `भगिनी` then चन्द्रचूडः lifts a diamond — narratively continuous; layout unverified, images closed)
