# Proofread report: 1985_05, story START=33 (p. 33, `p033.md`)

## Summary

One finding (severity error, confidence high): a single print misprint (कृषिकः for कृषकः, extra ि-stroke). No held candidates. The orth scanner ran on deblocked text with zero hits, quote pairs are balanced (doubles for the two direct speeches, singles for the 'किं क्रियते' thought), and open-sandhi spellings (सः वस्तुतः, विश्वासः एव) are kept as the edition's house convention. All work is from the Phase A transcription with images closed throughout Phase B; every chunk was read sentence by sentence for continuity. The text is hand-transcribed from print, not OCR output. Loc is `pNN:Pm` (scan sequence + chunk, matching lint P numbers) with the anchor's first two words and word number counting space-separated tokens on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p033:P3 (पूर्वं कस्मिंश्चित्) w6 | `नाम कृषिकः आसीत्` | `नाम कृषकः आसीत्` | SPL | error | high | कृषिकः is not a word; the farmer Balabhadra needs कृषकः; extra ि-stroke in print |

## Unverified

None.

## Coverage

p033:P1 {x-com:layout:} : skip layout
p033:P2 # शीघ्रकोपी : skip title
p033:P3 पूर्वं कस्मिंश्चित् : F1
p033:P4 किन्तु सहनायाः : clean (print singles on 'किं क्रियते' kept as thought; mdash before the wife's speech kept)
p033:P5 पत्न्याः वचनैः : clean
p033:P6 सः क्रोधेन : clean (direct speech quotes balanced)
p033:P7 पत्युः एतानि : clean
p033:P8 तद्दिनपूर्णं बलभद्रः : clean (तद्दिनपूर्णं kept as print; सः/विश्वासः open sandhi kept as house variant; चिन्तितवान् thought left without quotes as indirect)
p033:P9 शान्तायाः बाल्ये : clean (दिवङ्गतौ ङ/ं variation kept; sentence runs on past the page turn; {misc: "माणवकः"} footer closed with page)
J1 p033:P5 {pb} -> p033:P6 fresh (clean break) : ok
J2 p033:P9 {pb} -> END (clean break) : ok (mid-sentence page turn; continues to p34 outside this range)
