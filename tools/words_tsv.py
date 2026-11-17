#!/usr/bin/env python3
"""Build words.tsv (word, total count, doc count) from Chandamama .md files.

Usage: python3 tools/words_tsv.py <srcdir> <outfile>
- walks <srcdir> for *.md, skipping any path containing /draft/
- brace annotations: ins/del/sug-ins/sug-del/category/author/note contribute
  their inner text; all other {...} (pb, pc, pgb, wb, x-com, ...) are dropped
- tokens are maximal runs of Devanagari letters/signs (no punctuation,
  no digits); stray braces fall out as separators
"""
import os
import re
import sys
from collections import Counter

BRACE_RE = re.compile(r"\{([^{}]*)\}")
KEEP = {"ins", "del", "sug-ins", "sug-del", "category", "author", "note"}
TOKEN_RE = re.compile(r"[\u0900-\u0963\u0971-\u097F]+")


def clean(text: str) -> str:
    def sub(m: re.Match) -> str:
        key, sep, rest = m.group(1).partition(":")
        if sep and key in KEEP:
            return " " + rest + " "
        return " "

    return BRACE_RE.sub(sub, text).replace("{", " ").replace("}", " ")


def main(argv: list) -> None:
    srcdir, outfile = argv[1], argv[2]
    counts: Counter = Counter()
    docs: Counter = Counter()
    nfiles = 0
    for root, dirs, files in os.walk(srcdir):
        dirs[:] = [d for d in dirs if d != "draft"]
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            if "/draft/" in path:
                continue
            with open(path, encoding="utf-8") as f:
                toks = TOKEN_RE.findall(clean(f.read()))
            counts.update(toks)
            for t in set(toks):
                docs[t] += 1
            nfiles += 1
    rows = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    with open(outfile, "w", encoding="utf-8") as f:
        for word, count in rows:
            f.write(f"{word}\t{count}\t{docs[word]}\n")
    print(f"files: {nfiles}, types: {len(rows)}, "
          f"tokens: {sum(counts.values())}")


if __name__ == "__main__":
    main(sys.argv)
