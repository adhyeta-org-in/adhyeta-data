## Summary

Range p018 (scans 18–24, Vetala story धर्मः अधर्मः च): 3 findings, all high confidence — 2 error (F1 ligature drop, F2 proper-noun slip) and 1 style (F3 supplied opening quote). Systematic issue: scans 19 and 20 are transposed in the source JPGs, rupturing three joints (see Moves M1); the file stays in scan order for the compiler. Orth scanner (`scan.py orth`) on 57 deblocked lines: 0 hits. One Phase-A print-noise stroke (raised mark after धनलोभेन, p024:P6) examined and dropped as non-quote. No held candidates; nothing unverified. Loc below is `pNN:Pm` (scan sequence + chunk per lint `P` numbers) with the first two words as anchor and 1-based word counts excluding blocks.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p018:P3 अत्यन्तक्लिष्टस्य प्रश्नस्य w90 | `द्वयोः वणिजोः क वन प्रसङ्गः` | `द्वयोः वणिजोः कश्चन प्रसङ्गः` | SPL | error | high | indefinite pronoun needs कश्चन; श्च ligature dropped leaving a space (verified at 3x) |
| F2 | p020:P9 महायोगी किञ्चित्कालपर्यन्तं w19 | `वर्जनाभम् एव अनुसर्तुम्` | `वज्रनाभम् एव अनुसर्तुम्` | CNS | error | high | proper noun spelled वज्रनाभ everywhere else in the story (verified at 3x: print reads र्ज) |
| F3 | p021:P11 भयङ्कराकारः अतिभयङ्करं w4 | `हसन् एतस्यां गुहायां…नास्ति"` (open missing) | `{ins:"}` before एतस्यां | STY | style | high | speech opens here with certain position (हसन् is narration); print's close sits at p022:P2 |

## Moves

M1 — read the p020 page span before the p019 page span (swap scans 19/20). In file order three joints rupture with no grammatical fit: J1 `तं` + `प्राप्नुवन्ति।`, J3 `साष्टाङ्गनमस्कारः` + `प्रसङ्गं`, J5 `प्रेरणां` + `करणीयः।`. In swapped order each fits uniquely: `तं प्रसङ्गं कथयामि`, `साष्टाङ्गनमस्कारः करणीयः`, `प्रेरणां प्राप्नुवन्ति` (subject अनेके वणिजः). Supporting evidence: scan 20 carries printed folio २८ while scan 19 is unnumbered (odd art page, folio 29 covered), and the art narrative runs yogi-meeting (20) before indoor-invitation (19). File left in scan order; compiler to apply on user acceptance.

## Patterns

Proper-noun consistency (1 correction + 12 checked clean): F2 is the only वज्रनाभ slip; सत्यपाल, पद्मनाभ, सीता, रत्नगुप्त, गुणसेन, वराहगिरि, त्रिविक्रम spell consistently throughout.

## Unverified

None. Every Phase-A candidate ruled from text; no item held for the user.

## Coverage

p018:P1 {x-com:layout: : skip (layout chunk)
p018:P2 धर्मः अधर्मः : skip (title)
p018:P3 अत्यन्तक्लिष्टस्य प्रश्नस्य : F1 (J1 ruptured, see M1)
p018:P4 {category: : skip (metadata footer)
p019:P1 {x-com:layout: : skip (layout chunk)
p019:P2 प्राप्नुवन्ति। एतदर्थम् : clean (leading joint ruptured, see J1/M1)
p019:P3 पद्मनाभस्य आदेशानुसारं : clean
p019:P4 प्रामाणिकभावेन तेन : clean
p019:P5 एतत् वचनं : clean
p019:P6 अतः एव : clean (trailing joint ruptured, see J3/M1)
p020:P1 {x-com:layout: : skip (layout chunk)
p020:P2 प्रसङ्गं कथयामि। : clean (leading joint ruptured, see J3/M1)
p020:P3 कस्मिंश्चित् नगरे : clean
p020:P4 वज्रनाभः तु : clean
p020:P5 वज्रनाभस्य पितामहः : clean
p020:P6 बहुवारं पौत्रं : clean
p020:P7 "किन्तु वत्स, : clean
p020:P8 अन्ते पद्मनाभः : clean
p020:P9 महायोगी किञ्चित्कालपर्यन्तं : F2 (trailing joint ruptured, see J5/M1)
p021:P1 {x-com:layout: : skip (layout chunk)
p021:P2 करणीयः। महायोगिना : clean (leading joint ruptured, see J5/M1)
p021:P3 वज्रनाभे उत्तमपरिवर्तनस्य : clean
p021:P4 गुहायां घनान्धकारः : clean
p021:P5 महतः शिलाखण्डस्य : clean
p021:P6 भीत्या वज्रनाभस्य : clean
p021:P7 सत्यपालः यथाकथञ्चित् : clean
p021:P8 "तर्हि समीचीनम्। : clean
p021:P9 उत्तरक्षणे एव : clean
p021:P10 किञ्चित्कालानन्तरं सत्यपालः : clean
p021:P11 भयङ्कराकारः अतिभयङ्करं : F3
p022:P1 {x-com:layout: : skip (layout chunk)
p022:P2 अन्यः कोऽपि : clean (F3 mate closes here)
p022:P3 "एताः हरितशिलाः : clean
p022:P4 "उत्तमगुणः एव : clean
p022:P5 वज्रनाभः सन्तोषेण : clean
p022:P6 "न हि, : clean
p022:P7 अलं वा? : clean
p022:P8 स्वीयानि सर्वाणि : clean
p022:P9 तस्य उत्तरेण : clean
p023:P1 {x-com:layout: : skip (layout chunk)
p023:P2 महत्तरपापकर्तारं वणिजं : clean
p023:P3 अन्ते भयङ्कराकारः : clean
p023:P4 "तस्य उत्तमता : clean
p023:P5 "सः सीतायाः : clean
p023:P6 साहाय्यं प्राप्य : clean
p023:P7 तथापि वज्रनाभः : clean
p023:P8 भयङ्कराकारः अपि : clean
p023:P9 तदा गुहायाः : clean
p023:P10 "भवतः मनः : clean
p023:P11 "सत्कार्याणां श्रवणमात्रेण : clean
p024:P1 {x-com:layout: : skip (layout chunk)
p024:P2 तर्हि साक्षात् : clean
p024:P3 गन्धर्वः हरितशिलां : clean
p024:P4 वेतालः एवंरीत्या : clean
p024:P5 तदा त्रिविक्रमः : clean
p024:P6 दृष्ट्वा केवलं : clean (dropped x-illegible stroke after धनलोभेन ruled print noise)
p024:P7 एवंरीत्या महाराजस्य : clean
J1 p018:P3 -> p019:P2 : M1 (rupture in file order; fits as p018:P3 -> p020:P2)
J2 p019:P3 -> p019:P4 : ok
J3 p019:P6 -> p020:P2 : M1 (rupture in file order; fits as p019:P6 -> p021:P2)
J4 p020:P5 -> p020:P6 : ok
J5 p020:P9 -> p021:P2 : M1 (rupture in file order; fits as p020:P9 -> p019:P2)
J6 p021:P4 -> p021:P5 : ok
J7 p021:P11 -> p022:P2 : ok (F3 edge-spanning pair)
J8 p022:P6 -> p022:P7 : ok
J9 p022:P9 -> p023:P2 : ok
J10 p023:P5 -> p023:P6 : ok
J11 p023:P11 -> p024:P2 : ok
J12 p024:P5 -> p024:P6 : ok
J13 p024:P7 -> END : ok (clean break)
