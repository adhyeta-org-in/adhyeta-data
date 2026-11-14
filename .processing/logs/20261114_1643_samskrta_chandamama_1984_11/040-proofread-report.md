# Proofread report: 1984_11 p040 (वाणिज्यरहस्यम्)

## Summary

Single-page story `वाणिज्यरहस्यम्` (p040, chunks P3–P8): 6 findings — 4 error/high (one SPL, three dropped/confused-sign print slips), 1 likely/medium* held candidate (F5 `-तः` with `पूर्वम्`), 1 style/high spacing fix (F6 hyphen for space). The systematic problem is small-sign press damage (dropped repha, dropped आ-mātrā, घ/ध and त्/न् swaps). No passages were left unchecked; the file is a fresh print transcription, not OCR output. Loc below is `pNN:Pm` (lint chunk number) `:wN` (word number on the deblocked chunk from 1) with the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p040:P3:w1 (एकस्मित् ग्रामे) | `एकस्मित् ग्रामे` | `एकस्मिन्` | SPL | error | high | locative singular of एक is एकस्मिन्; त् for न् is a press slip |
| 2 | p040:P5:w3 (किञ्चित्कालानन्तरं राहुलः) | `अवश्यकायर्थं नगरं` | `अवश्यकार्यार्थं` | OCR | error | high | कायर्थं is not a word here; repha dropped from कार्यार्थं (for necessary business) |
| 3 | p040:P6:w5 (एवंरीत्या तस्य) | `मघ्ये एव` | `मध्ये` | OCR | error | high | मघ्ये is not a word; घ/ध is a listed confusable pair |
| 4 | p040:P8:w13 (एतां वार्तां) | `वाणिज्यव्यवहरस्तं भवान्` | `वाणिज्यव्यवहारस्तं` | OCR | error | high | हरस्तं is not a word; आ-mātrā dropped; व्यवहारः + तं gives regular स्त sandhi |
| 5 | p040:P4:w32 (एकदा भूषणस्य) | `एकसप्ताहतः पूर्वमेव` | `एकसप्ताहात्` | MRP | likely | medium* | -तः after a time noun with पूर्वम् is doubtful; ablative -ात् is the expected case |
| 6 | p040:P8:w17 (एतां वार्तां) | `अश्वशकटेन-भवतः मम` | `अश्वशकटेन भवतः` | STY | style | high | mid-line hyphen joins an instrumental and a genitive that cannot compound |

## Patterns

Small-sign press damage (F1–F4, 4 instances): dropped repha (F2 p040:P5), dropped आ-mātrā (F4 p040:P8), घ/ध swap (F3 p040:P6), त्/न् swap (F1 p040:P3). Each is the smallest glyph change to a fully grammatical form, so they are ruled as print slips rather than authorial variants.

## Unverified

F5 `एकसप्ताहतः` → `एकसप्ताहात्` (medium*): clause-level re-segmentation was tested and no other parse fits ("even before a week [elapsed]" remains the sense), but -तः with पूर्वम् after a time noun cannot be confirmed without a grammar or dictionary attestation; held in-file as `{sug-del:एकसप्ताहतः}{sug-ins:एकसप्ताहात्}` for the user. What would settle it: a cited attestation of time-noun + -तः with पूर्वम्, or acceptance of -तः as a house variant.

## Coverage

p040:P1 {x-com:layout: 1col, : skip (x-com layout declaration, no story text).
p040:P2 # वाणिज्यरहस्यम् : skip (title heading).
p040:P3 एकस्मित् ग्रामे : F1.
p040:P4 एकदा भूषणस्य : F5.
p040:P5 किञ्चित्कालानन्तरं राहुलः : F2.
p040:P6 एवंरीत्या तस्य : F3.
p040:P7 यदा तस्य : clean.
p040:P8 एतां वार्तां : F4, F6.
J1 p040:P8 {pb} -> END (clean break) : ok.
