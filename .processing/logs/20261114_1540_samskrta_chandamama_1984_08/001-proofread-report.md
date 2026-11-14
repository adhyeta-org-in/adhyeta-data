# Proofread report: 1984_08 p001 (scans 1-4)

## Summary

3 findings tabled (F1-F2 quote-sort verdicts, F3 spelling verdict) plus 1 systematic pattern (Pat-A: simple-ष printed as प, 18 verdicts applied) plus 1 unverified held candidate (U1); `scan.py orth` on deblocked text reported zero hits; text was manually transcribed from scans (not OCR), so no OCR-merge step applies.

Systematic defect: body type substitutes प for simple ष throughout (कृपिक/कृपि/मूपिक for कृषि-/मूषिक-) while the title (कृषिः), body conjunct-ष (तूष्णीं, वर्षे) and the author byline use ष correctly, so the body-ष sorts were misfiled; ruled minimal-change प→ष only (ि kept), yielding कृषिक (कृषि+क) rather than classical कृषक.

Print kept as seen except where verdicts apply: two reported speeches open with single but close with double (opens corrected to double per era speech convention and their इति closures); title is trimmed at the scan edge after च; held: प्रचलत् missing augment (single instance, print intent unknown, images closed).

Flow: all 8 joints grammatically continuous with the asserted scan-2 left-column-first order (the unique grammatical fit: एकस्मिन्+एव, तस्य+ग्रामस्य, अस्मिन्+ग्रामे); straight read shows no rupture at any seam, so no Moves proposed.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p04:P4 w6 `उक्तवान् --- ' भवतः` | `--- ' भवतः ... अस्माभिः" इति` | open `'` → `"` (`{del:'}{ins:"}`) | STY | style | high | Era doubles mark reported speech; इति plus उक्तवान् pins this span as speech, and the print close is double. |
| F2 | p04:P2 w29 `हसितवान्। 'द्रष्टुं` | `'द्रष्टुं ... करोति वा?" इति` | open `'` → `"` (`{del:'}{ins:"}`) | STY | style | high | Speech closed by a double plus इति plus पृष्टवती pins the sort; the single open is a dropped second stroke. |
| F3 | p04:P5 w32 `एव भीजस्य एव` | `भीजस्य` | `बीजस्य` (`{del:भीजस्य}{ins:बीजस्य}`) | SPL | error | high | भीज is not a word; the same speech has उत्तमबीजैः and बीजान् for the same bundle. |

## Patterns

Pat-A (SPL/error/high, 18 verdicts): simple-ष printed as प in body type — कृपिकः→कृषिकः (9×), कृपिकस्य→कृषिकस्य, कृपिकदम्पती→कृषिकदम्पती, कृपिकदम्पत्योः→कृषिकदम्पत्योः, कृपिं→कृषिं (3×), कृपिः→कृषिः, कृपिकार्यं→कृषिकार्यं, मूपिकाः→मूषिकाः; e.g. p01:P4 w5 `नाम कृपिकः आसीत्`, p02:P6 w4 `विपण्यां कृपिकदम्पती दृष्टवान्`, p04:P5 w1 `{pc}कृपिं कृतवान्`. Replacement keeps print's ि (minimal one-sort change, per smallest-change rule); classical कृषकः for the farmer is noted but not adopted. Title कृषिः and body तूष्णीं/वर्षे (correct ष) confirm the sort substitution.

## Unverified

U1 (p02:P5 w7 `वाणिज्यं प्रचलत् आसीत्`, MRP/likely/medium*): प्रचलत् lacks the augment (प्र+अचलत् → प्राचलत् expected); held as `{sug-del:प्रचलत्}{sug-ins:प्राचलत्}` because print intent is unknown with images closed and this is the sole imperfect of चल् in the story; settling needs the print re-checked or a second प्र+imperfect instance.

## Coverage

p001:P1 layout : skip layout
p001:P2 title : skip title (trimmed at scan edge, see Summary)
p001:P3 x-com note : skip x-com print record (title ष vs body प)
p001:P4 एकस्मिन् ग्रामे : Pat-A (कृपिकः, कृपिं)
p001:P5 रामः तु : clean
p001:P6 "सुखम् इत्यस्य : clean (print DQ/SQ nesting kept as seen)
p001:P7 सर्वं श्रुत्वा : clean
p001:P8 एकस्मिन् दिने : clean
p001:P9 'भवान् सर्वान् : clean
p001:P10 'कोऽयं विचारः : clean
p001:P11 author : skip metadata (byline kept as print)
p002:P1 layout : skip layout (left-col-first order asserted)
p002:P2 एव दिने : clean
p002:P3 रामः मनसि : clean
p002:P4 अपरस्मिन् दिने : clean
p002:P5 ग्रामस्य विपणिं : U1
p002:P6 सः तस्यां : Pat-A (कृपिकदम्पती)
p002:P7 तत् वचनं : clean
p002:P8 रामः ध्यानेन : clean
p002:P9 रात्रौ रामः : Pat-A (कृपिकः)
p003:P1 layout : skip layout
p003:P2 ग्रामे भवान् : clean
p003:P3 तस्मिन् दिने : clean (stray-mark omission documented in x-com)
p003:P4 रात्रौ निद्राकरणतः : Pat-A (कृपिकः, मूपिकाः)
p003:P5 तदा पत्नी : clean
p003:P6 तत् वचनं : Pat-A (कृपिकदम्पत्योः)
p003:P7 गाढनिद्रायां मग्नः : skip-anchor (deblocked starts here; para opens with {del:कृपिकः} verdict) : Pat-A (कृपिकः)
p003:P8 'एतौ अतीव : clean
p003:P9 आसीत्। सः : clean
p003:P10 अस्मिन् कोलाहले : Pat-A (कृपिकः ×2)
p004:P1 layout : skip layout
p004:P2 रामः तूष्णीं : F2, Pat-A (कृपिकः)
p004:P3 रामः --- : clean
p004:P4 पुनः हसन् : skip-anchor (deblocked starts here; para opens with {del:कृपिकः} verdict) : F1, Pat-A (कृपिकः)
p004:P5 कृतवान्। धनं : skip-anchor (deblocked starts here; para opens with {del:कृपिं} verdict) : F3, Pat-A (कृपिं ×2, कृपिः, कृपिकार्यं, कृपिकः)
J1 p001:P6 {pb} -> p001:P7 {pc} (continues) : ok (रामः सर्वं श्रुत्वा ... मौनं तिष्ठति स्म)
J2 p001:P10 {pb} -> p002:P2 {pc} (continues) : ok (एकस्मिन् एव दिने ... चौर्यं करोतु)
J3 p002:P4 {pb} -> p002:P5 {pc} (continues) : ok (तस्य ग्रामस्य विपणिं प्राप्तवान्; left-col-first order, unique grammatical fit)
J4 p002:P9 {pb} -> p003:P2 {pc} (continues) : ok (अस्मिन् ग्रामे भवान् तिष्ठति ...)
J5 p003:P8 {pb} -> p003:P9 {pc} (continues) : ok (एकः स्यूतः आसीत्)
J6 p003:P10 {pb} -> p004:P2 fresh (clean break) : ok (terminal ।, fresh para)
J7 p004:P4 {pb} -> p004:P5 {pc} (continues) : ok (भूमौ कृपिं कृतवान्)
J8 p004:P5 {pb} -> END (clean break) : ok (story ends स्वगृहं गतवान्।)
