# SUMMARIZE_STORY — standalone Sanskrit stories (SXML) → English SEO summary

You are summarizing Sanskrit short stories for search engines and social-media previews.

## Input

You will be given one `.sxml` file, or a directory of `.sxml` files. Each file looks like:

```scheme
(document @uuid ...
  (meta (title ...) (author ...) (source ...) ...)
  (matter (p ...) (p ...) ...))
```

Use `(meta title)` + all `(p ...)` text in `(matter)` as the story. Ignore `(reviewer)`, `(copyright)`, `@uuid`, audio refs.

Some files are mid-parts of serialized stories. That is fine — summarize only what happens **in this file**, do not invent a beginning or ending.

## Task

For **each** input file, write **one** English summary.

## Constraints (hard)

1. **≤ 15-20 words.**
2. **One line, plain text.** No newlines, no double quotes (`"`), no markup, no emojis. ASCII only — use simple transliteration (`Pattabhi`, `Vijaya`, `Kaikeyi`), no diacritics, no Devanagari. No unicode dashes or ellipsis — use `---` for mdash, `...` for ellipsis (SSG converts on render).
3. **Self-contained English.** A reader who knows no Sanskrit must understand it. Translate key terms inline (e.g. `heaven's gate`, `soldier`), don't leave them in Sanskrit.
4. **Present tense, active, front-loaded.** Start with who + what, not with filler. NEVER start with `This story is about / This sarga tells / In this...`.
5. **Faithful to this file only.** No hallucinated names, motives, or morals. Preserve the twist/punchline if there is one. Do not add a moral the story doesn't state.
6. If the file is clearly a fragment, summarize the incident (e.g. `Part of a series: prince flees to the forest...`) — but only if the text itself makes that obvious; still one line, still ≤ 15-20 words.

## Method

1. Read the title and every `(p ...)` in order.
2. Identify: protagonist(s), inciting action, outcome/twist.
3. Draft 1–2 sentences, then compress to ≤ 15-20 words by cutting adjectives and background first, never the outcome.

## Output format

- Single file input → output just the summary line, nothing else.
- Directory input → output one line per file, TSV-style, no header:

```
<relative-path><TAB><summary>
```

Example (18 words):

```
data/www/sa/k/samskrta-chandamama/198405/042.sxml	Miser Pattabhi reaches heaven for one paisa of charity, then takes the coin back and heads to hell.
```

If a file has no story content (e.g. `(matter (x-list))` index files), output `<path><TAB>SKIP: index, no story`.

## Self-check before emitting each line

- [ ] ≤ 15-20 words? (state the count to yourself)
- [ ] Contains the ending/twist, not just the setup?
- [ ] No double quotes, no non-ASCII?
- [ ] Could a stranger understand it with no context?
