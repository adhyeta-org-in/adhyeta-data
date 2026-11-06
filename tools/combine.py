#!/usr/bin/env python3
"""Regenerate summaries/hooks/beats.tsv from fragments/ for any work dir.

Usage: python3 tools/combine.py <srcdir>   (srcdir holds fragments/)
Writes summaries.tsv, hooks.tsv, beats.tsv next to fragments/.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.fragments import combine_fragments


def main(argv: list) -> None:
    srcdir = argv[1]
    counts = combine_fragments(srcdir)
    for kind, n in counts.items():
        print(f"{kind}: {n}")


if __name__ == "__main__":
    main(sys.argv)
