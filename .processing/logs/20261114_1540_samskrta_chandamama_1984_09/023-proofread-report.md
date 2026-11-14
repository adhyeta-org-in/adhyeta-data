## Summary

Phase B proofread of `p023.md` (1984_09, scan 23, story "एकम् एव दुर्व्यसनम्"). Proofread gate passes with 0 errors; `scan.py orth` reports 0 hits. Two held sense-level candidates, both in p023:P5, kept as `{sug-…}` for the user: a voice-agreement mismatch (F1) and a speaker attribution that contradicts the dialogue logic (F2). No Phase A `{sug-…}` queue existed, so nothing inherited needed routing. Quotes balance (all doubles for speech, one pair per paragraph); sandhi openness and house spellings kept as seen. `Loc` is story coordinates `pNN:Pm` plus anchor words, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p023:P5 वार्तां श्रुता (w22-23) | `इति वार्तां श्रुता` | `इति वार्ता श्रुता` or `इति वार्तां श्रुतवान्` | KRK | error | medium* | accusative object with a passive nominative-feminine participle; held because print attribution is unverified (images closed, no Phase A note) |
| 2 | p023:P5 इति आनन्दः (w32) | `इति आनन्दः पृष्टवान्` | `इति गोविन्दः पृष्टवान्` | LEX | likely | medium* | the father would not ask why no girl is given to his own son, and P6 answers the question as Govinda's; held as sense conjecture, print reads आनन्दः as transcribed |

## Patterns

None.

## Unverified

F1: grammar judgment is certain but the print reading cannot be rechecked (images closed) and Phase A left no note, so the minimal fix (drop the anusvāra) vs the active rephrasing (श्रुतवान्) is undecided; settling needs the scan line or an editor's call. F2: गोविन्दः fits the dialogue uniquely, but authorial intention cannot be proven from text alone; settling needs the series editor.

## Coverage

p023:P1 {x-com:layout:} : skip layout declaration
p023:P2 # एकम् : skip title
p023:P3 एकस्मिन् ग्रामे : clean
p023:P4 बहोः कालात् : clean
p023:P5 तदा गोविन्दः : F1, F2
p023:P6 "भवान् एव : clean
p023:P7 सायङ्काले गोविन्दः : clean
p023:P8 "नैव, दुर्व्यसनं : clean
p023:P9 गोविन्दः एतं : clean
J1 p023:P9 {pb} -> END : ok
