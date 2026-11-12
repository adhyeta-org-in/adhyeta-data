---
name: sanskrit-proofreading
description: Proofread Devanagari Sanskrit text and report errors with location, suggested fix, category and confidence, without silently rewriting the text. Built for Chandamama-style stories and other narrative prose with an occasional embedded verse (सुभाषित), including OCR / scan cleanup of printed editions. Use this skill whenever the user asks to proofread, check, correct, copy-edit or review Sanskrit, pastes Sanskrit story text, mentions Sanskrit OCR output, sandhi or grammar mistakes, Devanagari typos or broken conjuncts, or wants the meter (छ्न्दस्) of a Sanskrit verse checked, even if they never say "proofread". Do not use for translation, for roman-script Sanskrit, for Hindi or Marathi proofreading, or for Vedic accent (स्वर) work.
---

# Sanskrit proofreading

Proofreads Sanskrit narrative prose (the चन्दमामा / पञ्चतन्त्र / विक्रम-वेताल register) and the occasional embedded verse. The deliverable is a **findings report**, not a rewritten text, unless the user explicitly asks for a corrected version.

## Principles

1. **Report, don't rewrite.** Sanskrit has real variation (Epic and Vedic forms, ārṣa usages, optional sandhi, editorial conventions). Return each suspected error as a finding with a suggestion, a category and a confidence level. Never silently normalise the user's text.
2. **Confidence over bluffing.** LLMs are unreliable at Sanskrit morphology and sandhi. If you are not sure a form is wrong, say so and mark it `unverified`. If you are not sure a form is right, flag it low-confidence rather than approving it. See "Verification" below.
3. **Cheap passes first.** Mechanical and orthographic problems (especially OCR artifacts) are the most frequent errors in scanned stories and the most certain. Grammar comes after.
4. **Stay in Devanagari.** Quote and suggest in Devanagari. Do not transliterate.
5. **Never change meaning to fix form.** If a fix needs a different word rather than a different spelling, say it is a content change and give it low or medium confidence.

## Workflow

### Step 0: Intake

Establish, from the input if possible and otherwise by asking at most one short question:

- Script: Devanagari only. If the input is in another script, ask for a Devanagari version.
- Origin: OCR of a printed edition (assume yes if the text looks noisy), typed text, or a translation from Hindi / Marathi / Telugu / English. Translations carry typical calques, see `.agents/refs/sanskrit/prose-checks.md`.
- Whether the user wants a report only (default) or also a corrected text.

### Step 1: Mechanical scan

Run the shared scanner by path using system `python3`. It uses only the standard library.

```
python3 .agents/tools/sanskrit/scan.py orth story.txt
```

Run it only on the story text, not on documentation or mixed English notes. It emits JSON findings for what the sidecar linter cannot see: orphan or stacked vowel signs, full stops or Latin `I`/`l`/`1`/`!` standing in for danda, other-script look-alike glyphs, Hindi/Marathi-only letters (ऑ ॉ ॅ ळ …), ZWJ/ZWNJ, replacement characters, and lines that look like verses. (Pipes, colons-for-visarga, stray Latin/digits, NFC, and spacing belong to the story linter and are not rescanned here.) Treat every scanner hit as a hypothesis and confirm against context. Then read `.agents/refs/sanskrit/ocr-and-orthography.md` for the pass the scanner cannot do (confusable letters, dropped halant or अनुस्वार).

Scanner `severity` (`high` / `medium` / `low`) is triage priority, not the report verdict. The report uses `.agents/refs/sanskrit/error-taxonomy.md` severity (`error` / `likely` / `variant` / `style`). As a rule of thumb: confirmed `high` scanner hits usually become `error`; `medium` hits usually become `likely` if confirmed; `low` hits often become `style` or `variant`. Always re-judge severity from the taxonomy after confirming the finding.

### Step 2: Word-level pass

Read the text sentence by sentence. For each word ask: is this a real Sanskrit form, and is it spelled right? Use `.agents/refs/sanskrit/ocr-and-orthography.md` for confusion pairs and `.agents/refs/sanskrit/error-taxonomy.md` for category codes. Look hardest at proper nouns (character and place names recur through a story, so they must be spelled consistently) and at words that are valid but implausible in context, which are the signature of OCR substitution.

### Step 3: Sandhi, morphology and syntax

Follow `.agents/refs/sanskrit/prose-checks.md`. In order: sandhi at word boundaries, case endings and verb forms, agreement (subject-verb, adjective-noun, participle-agent), कारक and voice usage, compound structure, and narrative-style conventions (tense, `इति` quotation, क्त्वा same-subject rule).

### Step 4: Verse (only if present)

Verses are usually the lines ending in `॥`, or short quoted sayings in the middle of a story. Extract only the verse lines to a file and run:

```
python3 .agents/tools/sanskrit/scan.py meter verse.txt
```

Then follow `.agents/refs/sanskrit/verse.md`. Do not run the meter scanner on prose: sentences ending in a single danda are not verse.

### Step 5: Report

Compile findings per `.agents/refs/sanskrit/report-format.md`. Sort findings by position in the text, fold repeated problems into one pattern entry, and lead with a short summary (counts by severity, the one or two systematic problems, and anything you could not verify). Prove full coverage: build the per-paragraph coverage appendix as you go — one disposition line per paragraph, written when you finish that paragraph and never reconstructed afterwards — and ship it with the report; a report without the appendix is incomplete.

## Verification

Use external references for anything you are not highly sure of, if you have web access or tools. Otherwise mark the finding `unverified`.

- Sanskrit Heritage Platform (sanskrit.inria.fr): morphological and sandhi analysis of a string.
- Cologne Digital Sanskrit Dictionaries (sanskrit-lexicon.uni-koeln.de): Monier-Williams, Apte, etc., for whether a word exists and what it means.
- Digital Corpus of Sanskrit (DCS): attestation of a form or construction.

## Do not

- Do not "correct" archaic or Epic forms, or optional-sandhi choices, without labelling them as variants.
- Do not convert the whole text to another script in the output.
- Do not report more than about 40 findings in the main list for long texts: summarise repeated patterns ("`व` for `ब` throughout, 14 cases, examples at …") and list one example per pattern.
- Do not claim a verse is "in meter X" from the scanner alone. The scanner counts syllables and weights; you still have to check the pāda pattern against the named meter.
