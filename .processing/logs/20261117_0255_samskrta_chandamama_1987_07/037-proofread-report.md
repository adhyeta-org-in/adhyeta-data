# Proofread report — 1987_07, पृष्ठ 37–40 — युक्तिमान् सैनिकः (story start p037)

## Summary

Phase B on `.processing/samskrta_chandamama/1987_07/p037.md` (scan pages 37–40, images closed). 3 findings: 2 style verdicts fixed as `{del:}/{ins:}` blocks (a stray single quote with no mate, and single-stroke speech quotes folded to house doubles), 1 likely held candidate kept as `{sug-del:}/{sug-ins:}` (`सम्मिलेयः`). `scan.py orth` on deblocked text: 0 hits. Quote pass: every speech pair is now balanced doubles, every thought pair balanced singles; the one column-split speech (p040:P5→P6) stands on its `{pc}` continuation and was never forced closed. All 8 `{pb}`/`{pc}`/`{pgb}` joints read continuous. Loc below is `pNN:Pm` + word number within the chunk (lint P numbering, counting all chunks of the page); anchor = first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p037:P10 w3 ("मम समीपे) | `समीपे 'धनं` | `समीपे धनं` | STY | style | medium | Single stroke mid-speech with no mate and no nesting semantics while every other speech uses clean doubles (stray sorts); fixed as `{del:'}` with print preserved in the block |
| 2 | p039:P6 w5 ({pc}सैनिकाः आयुधसहिताः) | `राजाङ्गणे सम्मिलेयः` | `राजाङ्गणे सम्मिलेयुः` | AGR | likely | medium* | यत्-clause over plural सर्वे सैनिकाः needs 3pl optative; print reads लेयः in two independent Phase A reads so held as `{sug-del:}/{sug-ins:}` for human review |
| 3 | p039:P7 w1 ('कोऽपि खड्गं) | `'कोऽपि खड्गं दद्यात् वा?'` | `"कोऽपि खड्गं दद्यात् वा?"` | STY | style | high | Reporting verb प्रार्थितवान् pins spoken discourse and house doubles mark speech; folded via `{del:'}{ins:"}` at both marks |

## Patterns

None — no defect repeats.

## Unverified

- `सम्मिलेयुः` (F2): what would settle it — a tighter re-read of the यः/युः akṣara on the scan, or another occurrence of the form in the issue. Kept as a held `{sug-}` candidate for human review; not an open task.

## Dispositions of Phase A carried candidates

- p037 singles `एतेन अल्पेन...शक्नुवन्ति?` and `कथमपि...एव` (p037:P3): **ruled print-faithful, no block.** Both are the king's wondering/resolving thought (कुतूहलः उत्पन्नः मनसि, निश्चितवान्); singles correctly sort as thought.
- p037 nested stray `'` (p037:P10→p038:P2): **ruled** — deleted via `{del:'}`; see F1. The pair is now balanced doubles across the page seam.
- p038 reading order (left column below art, then right column): **confirmed by narrative.** `निधनः` completes `अहं` (J2), and the shopkeeper's refusal answers Yoshka's credit plea across J3; both seams read continuous.
- p038 bold `उक्तवान् सः प्राचीनः सैनिकः।`: **kept as printed emphasis, no block.**
- p039 thought `एते सैनिकाः...दण्डनीयः` (p039:P3): **ruled print-faithful, no block.** King's sleepless thought (चिन्तितवान्); singles correct.
- p039 `कोऽपि खड्गं दद्यात् वा?` (p039:P7): **ruled** — folded to doubles; see F3.
- p039 `सम्मिलेयः` (p039:P6): **held** — see F2. Crop-verified neighbours `आयुधसहिताः`, `स्वपरतः`, `कटिप्रदेशे`, `त्सरुः`, `दृष्ट्या` all kept as printed, no blocks.
- Print variants kept as seen, no blocks: `मदिरापणिकः`/`आपणिकः`, `मात्यासु-महाराजः` hyphen vs `मात्यासुमहाराजेन`, body `हङ्गरी` vs footer `हंगरी`, historic-present `जानाति`.
- p040 thought `एतस्य...निरूपणीयः` (p040:P2): **ruled print-faithful, no block.** King's thought (चिन्तितवान्); singles correct.
- p040 `विना....` four-dot ellipsis and the P5→P6 column-split speech: **kept as printed.** One paragraph split by layout (`{pc}` continuation); the pair stands and was never forced closed.
- Footer `{note: "हंगरीदेशस्य जानपदकथा"}` and folio `{pgb: ५२}` (p038 only; other pages bare): **kept as printed.**

## Coverage appendix

Chunks (lint P numbers include layout/title chunks):

- p037:P1 (layout x-com) : skip layout-declaration chunk
- p037:P2 (युक्तिमान् सैनिकः) : skip title
- p037:P3 पूर्वं कदाचित् : clean
- p037:P4 मात्यासुराजः कदाचित् : clean
- p037:P5 यदा सः : clean
- p037:P6 कोलाहलः च : clean
- p037:P7 अन्तः चत्वारः : clean
- p037:P8 एकः सप्ताहः : clean
- p037:P9 तदा प्राचीनसैनिकः : clean
- p037:P10 मम समीपे : F1
- p038:P1 (layout x-com) : skip layout-declaration chunk
- p038:P2 निधनः इति : clean
- p038:P3 किं भोः : clean
- p038:P4 राजा तस्य : clean
- p038:P5 एतावता अपि : clean
- p038:P6 सैनिकाय कदापि : clean
- p038:P7 योष्का कुपितः : clean
- p038:P8 आपणिकः खड्गं : clean
- p038:P9 तदा रात्रौ : clean
- p038:P10 इदानीं बुभुक्षा : clean
- p038:P11 महाराजः झटिति : clean
- p038:P12 मात्यासुमहाराजेन आनीतानि : clean
- p039:P1 (layout x-com) : skip layout-declaration chunk
- p039:P2 प्राचीनसैनिकानां शयनार्थं : clean
- p039:P3 महाराजः यद्यपि : clean
- p039:P4 एवं चिन्तयित्वा : clean
- p039:P5 प्रातःकाले राजाज्ञा : clean
- p039:P6 सैनिकाः आयुधसहिताः : F2
- p039:P7 कोऽपि खड्गं : F3
- p039:P8 स्वपरतः स्थितेषु : clean
- p040:P1 (layout x-com) : skip layout-declaration chunk
- p040:P2 दृश्यते एतस्य : clean
- p040:P3 महापराधं कृतवन्तं : clean
- p040:P4 मात्यासुराजः योष्कानामकम् : clean
- p040:P5 योष्कासैनिकस्य पादयोः : clean
- p040:P6 इति विनयेन : clean
- p040:P7 अहं राजा : clean
- p040:P8 महाप्रभो शिरच्छेदं : clean
- p040:P9 तदा योष्का : clean
- p040:P10 योष्कासैनिकस्य युक्तिं : clean

Joints:

- J1 p037:P5 {pb} -> p037:P6 {pc} (continues) : ok
- J2 p037:P10 {pb} -> p038:P2 {pc} (continues) : ok (F1 verdict at this edge; अहं + निधनः continuous)
- J3 p038:P5 {pb} -> p038:P6 fresh (clean break) : ok
- J4 p038:P12 {pb} -> p039:P2 fresh (clean break) : ok
- J5 p039:P5 {pb} -> p039:P6 {pc} (continues) : ok
- J6 p039:P8 {pb} -> p040:P2 {pc} (continues) : ok
- J7 p040:P5 {pb} -> p040:P6 {pc} (continues) : ok
- J8 p040:P10 {pb} -> END (clean break) : ok
