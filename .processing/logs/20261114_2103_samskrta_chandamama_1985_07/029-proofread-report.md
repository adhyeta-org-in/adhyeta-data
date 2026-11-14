## Summary

Phase A is complete and untouched: 3 `{pgb}`-terminated spans (scans 29, 30, 31) with a 6-joint index; `lint.py --phase extract` passes (exit 0, residual carried) and no page was re-transcribed. Phase B proofread gate now passes clean (`lint.py --phase proofread`: 3 pages, 0 error paras, 0 story findings, exit 0); `scan.py orth` on deblocked text reports 0 hits across 24 lines. Findings table: 1 verified verdict (F1 quote-sort correction, STY/style, high) plus 1 held candidate (F2 क्षाम्यतु, MRP/likely, low*). Print keeps visarga before vowels and open sandhi throughout (सहृदयाः इति, वेषः अत्यद्भुतः); these are house variants, never flagged. Proper nouns (मह्लिनाथः, उदयभट्टः, वीरसेनः) spell consistently. Loc below is keyed `pNN:Pm[:w]` (NN = scan sequence 29 + `{pgb}`-span ordinal, Pm = lint chunk number, w = word in chunk from 1) plus the first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p030:P2:1 आये, मम | `'आये ... न कृतवान्"` (single open, double close) | `"आये ... न कृतवान्"` via `{del:'}{ins:"}` at open | STY | style | high | direct speech closed by इति उक्तवान् takes doubles; Phase A x-com records the dropped second stroke |
| 2 | p030:P2:4 आये, मम | `मम अपराधं क्षाम्यतु` | `क्षम्यताम्` | MRP | likely | low* | क्षाम् gives no transitive "forgive" sense here; passive imperative क्षम्यताम् governs accusative अपराधं, but unconfirmed without tool check |

## Unverified

F2 `क्षाम्यतु` (p030:P2:4) is held as `{sug-del:क्षाम्यतु}{sug-ins:क्षम्यताम्}`, not a verdict: क्षम् in the passive imperative (क्षम्यताम्, "let the offence be forgiven") fits `मम अपराधं`, while क्षाम्यतु (from क्षाम्/क्षै, "waste away") gives no sensible "forgive my offence" reading in an apology for wearing the commander's disguise; but with images closed and no dictionary/tool confirmation, the emendation stays a candidate for the user (print read was flagged `{x-com: क्षा as seen}` in Phase A). What would settle it: a Heritage Platform / dictionary check of क्षाम्यतु as an attested form, or user acceptance of क्षम्यताम्.

## Coverage

p029:P1 {x-com:} : skip layout-only chunk
p029:P2 # वेषधारी : skip title
p029:P3 अनेकवर्षेभ्यः पूर्वं : clean
p029:P4 एकदा नवरात्रमहोत्सवसन्दर्भे : clean
p029:P5 हस्तद्वारा बहुमानानि : clean
p029:P6 तस्य वचनं : clean
p029:P7 मह्लिनाथः सेनापतिवेषम् : clean
p029:P8 {author:} : skip metadata + x-com-only chunk (byline read as seen, held without confident reading)
p030:P1 {x-com:} : skip layout-only chunk
p030:P2 आये, मम : F1, F2
p030:P3 उदयभट्टः हसन् : clean
p030:P4 मम वेषधारणकौशलं : clean
p030:P5 किमर्थं तथा : clean
p030:P6 कलाकाराणां सत्कारं : clean
p030:P7 तस्य वचनानुसारं : clean
p030:P8 प्रथमदिने मह्लिनाथः : clean
p031:P1 {x-com:} : skip layout-only chunk
p031:P2 च अतीव : clean
p031:P3 परद्युः मह्लिनाथः : clean
p031:P4 मह्लिनाथः विनयपूर्वकं : clean
p031:P5 अनुरूपं बहुमानम् : clean
p031:P6 महाराजः तस्य : clean
p031:P7 तदा मह्लिनाथः : clean
p031:P8 महाराजः तस्य : clean
J1 p029:P4 {pb} -> p029:P5 {pc} : ok (मह्लिनाथस्य / हस्तद्वारा spaced join, sentence continues)
J2 p029:P7 {pb} -> p030:P2 {pc} : ok (विनयेन / आये continuity holds; quote pair corrected by F1, now dq=2 balanced)
J3 p030:P5 {pb} -> p030:P6 {pc} : ok (समर्थानां / कलाकाराणां spaced join; print doublet confirmed as seen, merged speech balanced)
J4 p030:P8 {pb} -> p031:P2 {pc} : ok (महाराजः पौराः / च spaced join with च, single subject list)
J5 p031:P4 {pb} -> p031:P5 {pc} : ok (विद्यायाः / अनुरूपं genitive phrase, merged speech balanced)
J6 p031:P8 {pb} -> END : ok (clean story close on दत्तवान्।)
