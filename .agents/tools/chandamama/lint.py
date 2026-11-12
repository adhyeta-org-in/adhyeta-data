#!/usr/bin/env python3
"""Lint a Chandamama story file (merged story: page spans closed by {pgb}).

Usage:
  python3 lint.py [--json] [--phase extract|proofread] <story.md>
  python3 lint.py --refresh-joints <story.md>   # rewrite ## Joints from edge markers

Quote model (straight quotes only): the printer's doubled single-quote
'' is transcribed as one "; an avagraha ' inside a word (as in कोऽपि)
is not a quote. An opening mark must close with the same mark; nesting
is only SQ DQ ... DQ SQ or DQ SQ ... SQ DQ, properly nested, never
crossed, never doubled ("" or '' back to back). A " cannot follow a "
and an SQ cannot follow an SQ.
"""
import json
import os
import re
import sys
import unicodedata
from collections import OrderedDict

# Closed vocabulary mirrors .agents/refs/chandamama-blocks.md — update together.
CLOSED = ("pb", "wb", "pc", "pgb", "del", "ins", "author", "note", "category", "misc", "sug-ins", "sug-del", "x-com", "x-missing", "x-illegible")
MAGAZINE_NOSPACE = {"चन्दमामा", "चन्द्रमामा", "चंदमामा"}
ILLUSTRATOR = {"VEERA", "CHITRA", "Jaya"}
BLOCK_RE = re.compile(r"\{([^{}]*)\}")
UNICODE_PUNCT = {"—": "use triple-dash", "–": "use triple-dash", "…": "use three-dots", "‘": "use ascii-quote", "’": "use ascii-quote", "“": "use ascii-dquote", "”": "use ascii-dquote"}


def deblock(text):
    return re.sub(r"\{[^{}]*\}", "", text)


def check_block(inner, phase=None):
    if ":" in inner:
        kind, _, val = inner.partition(":")
        kind = kind.strip()
        if kind not in CLOSED:
            return "unknown-block {%s}" % inner
        if phase == "extract" and kind in ("del", "ins"):
            return "verdict-in-extract {%s} (transcription emits {sug-del:}/{sug-ins:} candidates, never {del:}/{ins:} verdicts)" % inner
        if kind == "pc":
            return "pc-takes-no-value {%s}" % inner
        if kind == "wb":
            return "wb-takes-no-value {%s}" % inner
        if kind == "pb":
            return "pb-takes-no-value {%s}" % inner
        if kind == "pgb":
            if val.strip() == "":
                return "empty-pgb {%s} (bare {pgb} takes no colon; give the folio as {pgb: \u096d\u096f})" % inner
            if not re.fullmatch(r"[\u0966-\u096f ]+", val.strip()):
                return "bad-pgb-number {%s}" % inner
            return None
        if kind in ("del", "ins", "author", "note", "category", "misc", "sug-ins", "sug-del", "x-com", "x-missing", "x-illegible") and val.strip() == "":
            return "empty-block {%s}" % inner
        return None
    if inner.strip() not in CLOSED:
        return "unknown-block {%s}" % inner
    if phase == "extract" and inner.strip() in ("del", "ins"):
        return "verdict-in-extract {%s} (transcription emits {sug-del:}/{sug-ins:} candidates, never {del:}/{ins:} verdicts)" % inner
    return None


def quote_stream(text):
    """Normalized stream for quote checks: recorded {ins}/{del} quote
    marks applied, blocks stripped, avagrahas removed, printer '' folded
    to ". Returns (stream, had_printer_dq)."""
    s = text.replace('{ins:"}', '"').replace("{ins:'}", "'").replace('{del:"}', "").replace("{del:'}", "")
    s = deblock(s)
    had_printer_dq = "''" in s
    return s.replace("''", '"'), had_printer_dq


def check_quotes(text, is_first_body, is_last_para):
    errors, notes = [], []
    s, had_printer_dq = quote_stream(text)
    if had_printer_dq:
        errors.append('printer-dq-use-double-quote (transcribe \'\' as ")')
    if '""' in s:
        errors.append('doubled-dq (" cannot follow ")')
    m = re.search("\"'([^\"']*)'\"", s)
    if m:
        errors.append('empty-nesting ("\'%s\'" wraps nothing outside the inner pair: one misread two-stroke mark, never nesting)' % m.group(1)[:30])
    toks = [c for c in s if c in "\"'"]
    stack = []
    for tok in toks:
        if stack and stack[-1] == tok:
            stack.pop()
        elif tok in stack:
            errors.append("crossed-quotes (nest only SQ DQ ... DQ SQ or DQ SQ ... SQ DQ)")
            break
        else:
            stack.append(tok)
            if len(stack) > 2:
                errors.append("deep-nesting (three levels like \"abc 'def \"ghi\" jkl' mnop\" are probable error; sequential pairs like \"abc 'def' ghi 'jkl' mnop\" are fine)")
                break
    dq, sq = s.count('"'), s.count("'")
    has_edge = "{pb" in text or "{wb" in text  # "{pb" also matches "{pgb}": a page edge counts as a break
    has_pc = text.startswith("{pc}")
    if dq % 2 == 1 or sq % 2 == 1:
        detail = "dq=%d sq=%d" % (dq, sq)
        if has_pc:
            notes.append("paired-continuation %s (pairing verified in issue lint)" % detail)
        elif is_last_para and has_edge:
            notes.append("quotes-open-past-pb %s (pair with next {pc})" % detail)
        elif is_first_body:
            notes.append("quotes-continue-from-prev %s (pair with prev {pb} or cross-file quote)" % detail)
        else:
            notes.append("mid-para-imbalance %s (multi-para span across paras, or dropped mark?)" % detail)
    return dq, sq, errors, notes


def check_furniture(text):
    errors = []
    body = deblock(text)
    for ln in body.split("\n"):
        if ln.strip() and re.sub(r"[\s०-९0-9]+", "", ln.strip()) in MAGAZINE_NOSPACE:
            errors.append("furniture-leak magazine-name (strip it, never transcribe)")
    stripped = body.strip()
    if stripped and re.fullmatch(r"[०-९0-9 \t]+", stripped):
        errors.append("bare-numeral-para (page furniture, strip it)")
    m = re.search(r"\b(VEERA|CHITRA|Jaya)\b", body)
    if m:
        errors.append("illustrator-word %s (strip it)" % m.group(1))
    for m in BLOCK_RE.finditer(text):
        inner = m.group(1)
        if ":" in inner:
            kind, _, val = inner.partition(":")
            if kind.strip() == "misc" and re.sub(r"[\s०-९0-9]+", "", val.strip().strip("\"'")) in MAGAZINE_NOSPACE:
                errors.append("furniture-in-misc (magazine name must be stripped, not kept)")
    return errors


TERMINAL_PUNCT = ("।", "॥", "?", "!")
EDGE_END_RE = re.compile(r"\{(?:pb|wb)\}(\s|\{[^{}]*\})*$")
LAYOUT_RE = re.compile(r"\s*\{x-com:layout:[^{}]*\}\s*")


def is_layout_para(text):
    """True for a standalone layout-declaration chunk (transparent to
    first-body and pc-pairing checks)."""
    return bool(LAYOUT_RE.fullmatch(text))


def edge_complete(text):
    """None if text does not end with an edge marker, else whether the
    deblocked words before it end with terminal punctuation."""
    if not EDGE_END_RE.search(text):
        return None
    t = deblock(text).rstrip().rstrip("\"'")
    return t.endswith(TERMINAL_PUNCT)


def lint_paragraph(idx, start_line, text, first_body=False, last=False, after_edge=False, phase=None):
    errors, notes = [], []
    if unicodedata.normalize("NFC", text) != text:
        errors.append("not-nfc")
    for ch, hint in UNICODE_PUNCT.items():
        if ch in text:
            errors.append("unicode-punct %r (%s)" % (ch, hint))
    dq, sq, q_err, q_note = check_quotes(text, first_body, last)
    errors.extend(q_err)
    notes.extend(q_note)
    if re.search(r"\|\|", text):
        errors.append("pipe-for-danda ||")
    elif re.search(r"(?<!\{)\|(?!\})", text):
        errors.append("pipe-for-danda |")
    if re.search(r"(?<=[\u0900-\u097f]):", text):
        errors.append("colon-for-visarga")
    for m in BLOCK_RE.finditer(text):
        err = check_block(m.group(1), phase)
        if err:
            errors.append(err)
    if re.search(r"\{(?:sug-)?ins:[^{}]*\}\{(?:sug-)?del:", text):
        errors.append("del-after-ins (span first: {del}/{sug-del} before {ins}/{sug-ins})")
    if "{pc}" in text and not ((first_body or after_edge) and text.startswith("{pc}")):
        errors.append("misplaced-pc ({pc} opens a continued para only: page-first body, or right after {pb}/{wb})")
    for m in re.finditer(r"\{(?:pb|wb)\}", text):
        if not re.fullmatch(r"(\s|\{[^{}]*\})*", text[m.end():]):
            errors.append("misplaced-pb ({pb}/{wb} must be followed by blocks or whitespace only, never bare text)")
            break
    errors.extend(check_furniture(text))
    nodq = deblock(text)
    for m in re.finditer(r"[A-Za-z]+", nodq):
        errors.append("latin-in-devanagari %r" % m.group())
        break
    for m in BLOCK_RE.finditer(text):
        inner = m.group(1)
        if ":" in inner:
            kind, _, val = inner.partition(":")
            if kind.strip() not in ("x-missing", "x-illegible", "x-com") and re.search(r"[A-Za-z]", val):
                errors.append("latin-in-block {%s} (story blocks hold Devanagari; English only in x-missing/x-illegible)" % inner)
                break
    for m in re.finditer(r"[0-9]+", nodq):
        errors.append("ascii-digit %r" % m.group())
        break
    if re.search(r" {2,}", text):
        errors.append("double-space")
    if text.rstrip("\n") != text.rstrip("\n").rstrip(" \t"):
        errors.append("trailing-space")
    if re.search(r" +[।,:;?!]", text):
        errors.append("space-before-punct")
    t = text.replace("---", "\x00")
    if re.search(r" - |[^\s{\x00]-(?=[ \"'(!?।])", t):
        errors.append("bare-hyphen-use-mdash (dash before space/quote/paren/punct is most probably ---; a wrap hyphenation joins instead)")
    if re.search(r"-\{pb", text):
        errors.append("hyphen-before-pb (mid-word cut takes {wb} with the hyphen dropped; dialogue dash takes ---)")
    return {"para": idx, "line": start_line, "text": text, "dq": dq, "sq": sq, "blocks": len(BLOCK_RE.findall(text)), "errors": errors, "notes": notes}


def split_paras(raw):
    lines = raw.split("\n")
    paras = []
    buf, start = [], 1
    for i, ln in enumerate(lines, 1):
        if ln.strip() == "":
            if buf:
                paras.append({"text": "\n".join(buf), "line": start})
                buf = []
        else:
            if not buf:
                start = i
            buf.append(ln)
    if buf:
        paras.append({"text": "\n".join(buf), "line": start})
    return paras


def devanagari_paras(paras):
    return [p for p in paras if re.search(r"[\u0900-\u097F]", deblock(p["text"]))]


PGB_END_RE = re.compile(r"\{pgb(?::[\u0966-\u096f ]+)?\}\s*$")
JOINT_EDGE_RE = re.compile(r"\{(?:pb|wb)\}")


def is_join_transparent(text):
    """True for chunks carrying no story text and no edge marker
    (layout lines, metadata/x-com-only chunks): invisible to join chaining.
    A lone {pc} is never transparent — it is the continuation signal."""
    if text.startswith("{pc}"):
        return False
    if EDGE_END_RE.search(text):
        return False
    return deblock(text).strip() == ""


def split_story_pages(path):
    """Split a story file into [(tag, chunks)] in page order.

    Pages are {pgb}-terminated spans in scan order; tags derive from the
    filename (p<START>.md -> p<START>, p<START+1>, ...). chunks are
    {"text","line"} like split_paras; numbering restarts per page so
    pNN:Pm anchors keep working. The ## Joints appendix is scaffolding,
    not story text: skipped."""
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    for i, ln in enumerate(lines):
        if ln == "## Joints":
            lines = lines[:i]
            break
    chunks = split_paras("\n".join(lines))
    pages, cur = [], []
    for ch in chunks:
        cur.append(ch)
        if PGB_END_RE.search(ch["text"]):
            pages.append(cur)
            cur = []
    if any(c["text"].strip() != "" for c in cur):
        pages.append(cur)  # untagged tail: fails missing-pgb below
    m = re.match(r"p(\d+)", os.path.splitext(os.path.basename(path))[0])
    if m:
        width = len(m.group(1))
        tags = ["p%0*d" % (width, int(m.group(1)) + i) for i in range(len(pages))]
    else:
        tags = ["pg%d" % (i + 1) for i in range(len(pages))]
    saw_pgb = any(PGB_END_RE.search(c["text"]) for pg in pages for c in pg)
    return list(zip(tags, pages)), saw_pgb


def logical_paras(pages):
    """Merge {pb}/{wb} + {pc} joins into logical paras.
    Returns [(tag, start_no, end_tag, end_no, text)]."""
    seq = []
    for tag, chunks in pages:
        for n, ch in enumerate(chunks, 1):
            seq.append((tag, n, ch["text"]))
    out = []
    i = 0
    while i < len(seq):
        tag, n, text = seq[i]
        etag, eno, last_text = tag, n, text
        while True:
            m = EDGE_END_RE.search(text)
            j = i + 1
            while j < len(seq) and is_join_transparent(seq[j][2]):
                j += 1
            nxt = seq[j] if j < len(seq) else None
            if not (m and nxt and nxt[2].startswith("{pc}")):
                break
            join = "" if m.group(0).startswith("{wb") else " "
            text = text[:m.start()] + join + nxt[2][len("{pc}"):]
            etag, eno, last_text = nxt[0], nxt[1], nxt[2]
            i = j
        out.append((tag, n, etag, eno, last_text if (tag, n) == (etag, eno) else text))
        i += 1
    return out


def lint_story(path, phase=None):
    pages, saw_pgb = split_story_pages(path)
    results = {}
    findings = []
    if not saw_pgb:
        return results, ["not-a-story-file %s (no {pgb} page-end markers)" % path]
    prev_tag, prev_ends, prev_edge = None, False, False
    for tag, chunks in pages:
        dev_idx = [i for i, ch in enumerate(chunks) if re.search(r"[\u0900-\u097F]", deblock(ch["text"]))]
        last_dev = dev_idx[-1] if dev_idx else -1
        body_idx = 0
        out = []
        for i, ch in enumerate(chunks):
            is_title = ch["text"].startswith("# ")
            is_layout = is_layout_para(ch["text"])
            if not is_title and not is_layout:
                body_idx += 1
            out.append(lint_paragraph(i + 1, ch["line"], ch["text"], first_body=(body_idx == 1 and not is_title), last=(i == last_dev), after_edge=prev_edge, phase=phase))
            if not is_layout:
                prev_edge = bool(re.search(r"\{(?:pb|wb)\}(\s|\{[^{}]*\})*$", ch["text"]))
        results[tag] = out
        devs = devanagari_paras(out)
        bodies = [p for p in out if not p["text"].startswith("# ") and not is_layout_para(p["text"])]
        ends_pb = bool(devs) and ("{pb" in devs[-1]["text"] or "{wb" in devs[-1]["text"])
        starts_pc = bool(bodies) and bodies[0]["text"].startswith("{pc}")
        if devs and not ends_pb:
            findings.append("missing-pb %s does not end with {pb} (every page ends with {pb} or {wb})" % tag)
        if starts_pc and prev_tag is not None and not prev_ends:
            findings.append("unpaired-pc %s opens with {pc} but %s does not end with {pb}/{wb}" % (tag, prev_tag))
        prev_tag, prev_ends = tag, ends_pb
    for tag, chunks in pages:
        for n, ch in enumerate(chunks, 1):
            for m in re.finditer(r"\{pgb(?::[^\{\}]*?)?\}", ch["text"]):
                if ch["text"][m.end():].strip() != "":
                    findings.append("misplaced-pgb %s:P%d {pgb} must end its chunk (last token of the page)" % (tag, n))
        if not re.search(r"\{pgb(?::[\u0966-\u096f ]+)?\}\s*$", chunks[-1]["text"]):
            findings.append("missing-pgb %s does not end with {pgb} (pgb is the last token of every page)" % tag)
    flat = []
    for tag, chunks in pages:
        out = results[tag]
        for n, ch in enumerate(chunks, 1):
            flat.append((tag, n, ch["text"], out[n - 1]))
    for idx, (tag, n, text, para) in enumerate(flat):
        if re.search(r"\{wb\}(\s|\{[^{}]*\})*$", text):
            j = idx + 1
            while j < len(flat) and is_join_transparent(flat[j][2]):
                j += 1
            nxt = flat[j][2] if j < len(flat) else None
            if nxt is not None and not nxt.startswith("{pc}"):
                findings.append("word-break-without-continuation %s:P%d {wb} is not followed by {pc} (a mid-word cut must continue)" % (tag, n))
        complete = edge_complete(text)
        if complete is None:
            continue
        j = idx + 1
        while j < len(flat) and is_join_transparent(flat[j][2]):
            j += 1
        opens_pc = j < len(flat) and flat[j][2].startswith("{pc}")
        if complete and opens_pc:
            para["notes"].append("pc-after-complete (edge ends with terminal punct yet next opens {pc} — confirm the para truly continues)")
        elif not complete and not opens_pc:
            para["notes"].append("possible-swallowed-continuation (edge ends mid-sentence yet next opens fresh — confirm the break)")
    logical = logical_paras(pages)
    for k, (tag, n, etag, eno, text) in enumerate(logical):
        loc = "%s:P%d" % (tag, n) if (tag, n) == (etag, eno) else "%s:P%d->%s:P%d" % (tag, n, etag, eno)
        dq, sq, q_err, q_note = check_quotes(text, False, False)
        for e in q_err:
            findings.append("%s : %s" % (loc, e))
        odd = (dq % 2 == 1 or sq % 2 == 1)
        claimed_behind = text.startswith("{pc}")
        claimed_ahead = (k == len(logical) - 1) and bool(EDGE_END_RE.search(span_last_text(pages, etag, eno)))
        if odd and not claimed_behind and not claimed_ahead:
            if phase == "extract":
                findings.append("note unbalanced-quotes %s dq=%d sq=%d (extract residual: print kept as seen; proofreader supplies {ins:} or keeps + documents)" % (loc, dq, sq))
            else:
                findings.append("unbalanced-quotes %s dq=%d sq=%d (supply the missing mark via {ins:}; page-turn continuation claims {pc})" % (loc, dq, sq))
            continue
        for note in q_note:
            if note.startswith("mid-para-imbalance"):
                continue
            findings.append("note %s : %s" % (loc, note))
        if odd and claimed_ahead:
            findings.append("note quotes-open-past-end %s dq=%d sq=%d (serial continues next issue; pair with its opening)" % (loc, dq, sq))
    return results, findings


def span_last_text(pages, etag, eno):
    """Raw text of a page's Nth chunk (for edge detection on spans)."""
    for t, chunks in pages:
        if t == etag and 1 <= eno <= len(chunks):
            return chunks[eno - 1]["text"]
    return ""


def build_joints(pages):
    """[(joint_no, tag, chunk_no, marker, target)] in reading order."""
    seq = []
    for tag, chunks in pages:
        for n, ch in enumerate(chunks, 1):
            seq.append((tag, n, ch["text"]))
    out = []
    for i, (tag, n, text) in enumerate(seq):
        for m in JOINT_EDGE_RE.finditer(text):
            j = i + 1
            while j < len(seq) and is_join_transparent(seq[j][2]):
                j += 1
            if j < len(seq):
                ntag, nn, ntext = seq[j]
                first = ntext.split("\n", 1)[0]
                if first.startswith("{pc}"):
                    tgt = "%s:P%d {pc} (continues)" % (ntag, nn)
                elif first.startswith("# "):
                    tgt = "%s:P%d title (clean break)" % (ntag, nn)
                else:
                    tgt = "%s:P%d fresh (clean break)" % (ntag, nn)
            else:
                tgt = "END (clean break)"
            out.append("J%d %s:P%d %s -> %s" % (len(out) + 1, tag, n, m.group(0), tgt))
    return out


def refresh_joints(path):
    """Rewrite the ## Joints index of a story file from its edge markers."""
    pages, saw_pgb = split_story_pages(path)
    if not saw_pgb:
        print("not-a-story-file %s (no {pgb} page-end markers)" % path)
        return 1
    joints = build_joints([(t, c) for t, c in pages])
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    for i, ln in enumerate(lines):
        if ln == "## Joints":
            lines = lines[:i]
            break
    while lines and lines[-1].strip() == "":
        lines.pop()
    lines.append("")
    lines.append("## Joints")
    lines.extend(joints)
    lines.append("")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print("joints refreshed (%d) in %s" % (len(joints), path))
    return 0


def fmt_para(p):
    parts = []
    if p["errors"]:
        parts.append("; ".join(p["errors"]))
    if p["notes"]:
        parts.append("note(" + "; ".join(p["notes"]) + ")")
    return "P%d L%d dq=%d sq=%d blocks=%d : %s" % (p["para"], p["line"], p["dq"], p["sq"], p["blocks"], "; ".join(parts) if parts else "clean")


def main():
    raw = sys.argv[1:]
    as_json = "--json" in raw
    phase = None
    if "--phase" in raw:
        i = raw.index("--phase")
        if i + 1 >= len(raw) or raw[i + 1].startswith("--"):
            print("usage: lint.py [--json] [--phase extract|proofread] <story.md>", file=sys.stderr)
            sys.exit(2)
        phase = raw[i + 1]
        if phase not in ("extract", "proofread"):
            print("unknown --phase %r (want extract|proofread)" % phase, file=sys.stderr)
            sys.exit(2)
        raw = raw[:i] + raw[i + 2:]
    refresh = "--refresh-joints" in raw
    raw = [a for a in raw if a != "--refresh-joints"]
    # --story is accepted and ignored: every lint run is a story-file run.
    # (Kept so the `--phase X --story <story.md>` form in the skills keeps working.)
    raw = [a for a in raw if a != "--story"]
    args = [a for a in raw if a != "--json"]
    if refresh:
        if len(args) != 1 or os.path.isdir(args[0]):
            print("usage: lint.py --refresh-joints <story.md> (rewrites ## Joints from edge markers)", file=sys.stderr)
            sys.exit(2)
        sys.exit(refresh_joints(args[0]))
    if not args:
        print("usage: lint.py [--json] [--phase extract|proofread] <story.md>", file=sys.stderr)
        sys.exit(2)
    path = args[0]
    if os.path.isdir(path):
        print("usage: lint.py [--json] [--phase extract|proofread] <story.md> (single story file, not a directory)", file=sys.stderr)
        sys.exit(2)
    results, findings = lint_story(path, phase)
    if as_json:
        print(json.dumps({"story": path, "phase": phase, "findings": findings, "pages": {t: [{k: p[k] for k in ("para", "line", "dq", "sq", "blocks", "errors", "notes")} for p in ps] for t, ps in results.items()}}, ensure_ascii=False, indent=2))
    else:
        for t in sorted(results):
            bad = [p for p in results[t] if p["errors"]]
            notes = sum(1 for p in results[t] if p["notes"] and not p["errors"])
            print("%s: %s" % (t, "clean" if not bad and not findings else "%d error paras%s" % (len(bad), ", notes in %d" % notes if notes else "")))
            for p in bad:
                print("  " + fmt_para(p))
        pat = OrderedDict()
        for t in sorted(results):
            for p in results[t]:
                for e in p["errors"]:
                    pat.setdefault(e, []).append("%s:P%d" % (t, p["para"]))
        if pat:
            print("PATTERNS:")
            for msg, locs in sorted(pat.items(), key=lambda kv: -len(kv[1])):
                print("  x%d: %s [%s]" % (len(locs), msg, ", ".join(locs[:10]) + ("..." if len(locs) > 10 else "")))
        for fd in findings:
            print("STORY: " + fd)
        nerr = sum(1 for ps in results.values() for p in ps if p["errors"])
        print("summary: %d pages, %d error paras, %d story findings" % (len(results), nerr, len(findings)))
    sys.exit(1 if any(p["errors"] for ps in results.values() for p in ps) or any(not f.startswith("note ") for f in findings) else 0)


if __name__ == "__main__":
    main()
