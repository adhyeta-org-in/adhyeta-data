"""Shared fragment store: per-sarga summary/hook/beats fragments <-> TSVs.

Fragment contract (all works: Ramayana, Mahabharata, Puranas, ...):
  <srcdir>/fragments/<KEY>_summary   single line, no key, no TAB
  <srcdir>/fragments/<KEY>_hook      single line, no key, no TAB
  <srcdir>/fragments/<KEY>_beats     single line, no key, no TAB
where KEY is work-native and sortable (Ramayana: 1.001; MBh later).

Combined files (checked in next to fragments):
  summaries.tsv / hooks.tsv / beats.tsv   lines: <KEY><TAB><text>
  uuids.tsv                               lines: <KEY><TAB><uuid>
  (KEY = index | K | K.SSS for Ramayana; work adapters define their own.)

Stdlib only.
"""

import os

FRAG_SUFFIX = {
    "summaries": "_summary",
    "hooks": "_hook",
    "beats": "_beats",
}

TSV_NAME = {
    "summaries": "summaries.tsv",
    "hooks": "hooks.tsv",
    "beats": "beats.tsv",
}

KINDS = ("summaries", "hooks", "beats")


def load_uuid_map(srcdir: str) -> dict:
    """Stable key->uuid map from uuids.tsv. Empty dict if missing."""
    fp = os.path.join(srcdir, "uuids.tsv")
    out: dict = {}
    if not os.path.exists(fp):
        return out
    with open(fp, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or "\t" not in line:
                continue
            key, u = line.split("\t", 1)
            out[key.strip()] = u.strip()
    return out


def load_text_map(srcdir: str, kinds: tuple = KINDS) -> dict:
    """{(kind, key): text}. Fragment files win over combined TSVs."""
    out: dict = {}
    fragdir = os.path.join(srcdir, "fragments")
    if os.path.isdir(fragdir):
        for name in os.listdir(fragdir):
            for kind in kinds:
                suffix = FRAG_SUFFIX.get(kind, "_" + kind)
                if name.endswith(suffix):
                    key = name[: -len(suffix)]
                    fp = os.path.join(fragdir, name)
                    with open(fp, "r", encoding="utf-8") as f:
                        out[(kind, key)] = f.read().strip().split("\n")[0].strip()
    for kind in kinds:
        tsv = TSV_NAME.get(kind)
        if not tsv:
            continue
        fp = os.path.join(srcdir, tsv)
        if not os.path.exists(fp):
            continue
        with open(fp, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line or "\t" not in line:
                    continue
                key, text = line.split("\t", 1)
                if (kind, key) not in out:
                    out[(kind, key)] = text.strip()
    return out


def combine_fragments(srcdir: str, kinds: tuple = KINDS) -> dict:
    """Regenerate summaries/hooks/beats.tsv from fragments/. Returns {kind: count}."""
    fragdir = os.path.join(srcdir, "fragments")
    counts: dict = {}
    for kind in kinds:
        suffix = FRAG_SUFFIX[kind]
        tsv = TSV_NAME[kind]
        keys = sorted(
            f[: -len(suffix)]
            for f in os.listdir(fragdir)
            if f.endswith(suffix)
        )
        fp = os.path.join(srcdir, tsv)
        with open(fp, "w", encoding="utf-8", newline="\n") as o:
            for k in keys:
                with open(
                    os.path.join(fragdir, k + suffix), encoding="utf-8"
                ) as f:
                    txt = f.read().strip().split("\n")[0].strip()
                o.write(k + "\t" + txt + "\n")
        counts[kind] = len(keys)
    return counts
