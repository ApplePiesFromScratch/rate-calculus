#!/usr/bin/env python3
"""wordlint.py [PATH ...]: refuse the words that write a reading as a property (ALPHABET's lint), and "impossible".

A word inside `backticks` or "double quotes" is only named, and passes. Fenced code blocks are skipped.
Files listed in tools/lint_skip.txt are skipped, each with its reason (verbatim sources are not ours to edit).
Default: every .md under the repo. Exit 1 on any flag.
"""
import os, re, sys
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFUSED = r"\b(living|alive|organisms?|creatures?|entity|entities|chaos|chaotic|intelligence|impossible|impossibly)\b"
NOUN_BEING = r"\b(a|the|every|each|this|that) beings?\b|\bbeings\b"


def skips():
    """whole files ("path  # reason") and single lines ("path:line  # reason"), each with its reason"""
    p = os.path.join(REPO, "tools", "lint_skip.txt")
    out = set()
    if os.path.exists(p):
        for l in open(p):
            if l.strip() and not l.startswith("#"):
                e = l.split("#")[0].strip()
                out.add(e if e.endswith("/") else os.path.normpath(e.split(":")[0]) + (":" + e.split(":")[1] if ":" in e else ""))
    return out


def scan(path):
    flags, fence = [], False
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.lstrip().startswith("```"):
            fence = not fence; continue
        if fence:
            continue
        bare = re.sub(r"`[^`]*`", "", line)
        bare = re.sub(r"\"[^\"]*\"|“[^”]*”", "", bare)
        for m in list(re.finditer(REFUSED, bare, re.I)) + list(re.finditer(NOUN_BEING, bare, re.I)):
            flags.append((i, m.group(0), line.strip()[:110]))
    return flags


if __name__ == "__main__":
    targets = sys.argv[1:] or [os.path.join(dp, f) for dp, _, fs in os.walk(REPO) for f in fs if f.endswith(".md") or f == "lessons.txt"]
    sk = skips(); total = 0; files = 0
    for t in sorted(targets):
        rel = os.path.normpath(os.path.relpath(t, REPO))
        if rel in sk or any(k.endswith("/") and rel.startswith(k.rstrip("/")) for k in sk) or rel.startswith("tracks" + os.sep):
            continue
        files += 1
        for i, w, l in scan(t):
            if f"{rel}:{i}" in sk:
                continue
            print(f"{rel}:{i}: '{w}' in: {l}"); total += 1
    print(f"wordlint: {'PASS' if not total else 'FAIL'} ({total} flags in {files} files)")
    sys.exit(1 if total else 0)
