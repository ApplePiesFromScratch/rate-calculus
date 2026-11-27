#!/usr/bin/env python3
"""L11 check: one map de-reified (guide 01, rule 8; guide 26). This checks the shape and the words only. Whether the
relations you wrote are right is for a person to read: ask someone who knows the map.

lessons/work/L11_MAP.md must hold:
  - a table whose header has the four columns: map | what it reifies | the relation | what you use (any wording
    containing 'map', 'reif', 'relation', 'use'), with at least 4 rows;
  - a section 'What pays' where every kept property carries one tier word:
    FORCED, EMPIRICAL, CONDITIONAL, STIPULATED, PRESUMED, UNPAID;
  - a line starting 'Kill line:' naming an output that would show your relations wrong;
  - a line starting 'Known:' naming which parts are known techniques (prior art), or 'Known: none found' with where you looked;
  - no refused word outside quotes (tools/wordlint.py).

  python3 lessons/L11_dereify/check.py
  python3 lessons/L11_dereify/check.py --planted
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "common")); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import harness, wordlint
TASK = "L11_dereify"
TIERS = r"\b(FORCED|EMPIRICAL|CONDITIONAL|STIPULATED|PRESUMED|UNPAID)\b"


def check(path):
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    R = []
    hdr = next((i for i, l in enumerate(lines) if l.startswith("|") and all(k in l.lower() for k in ("map", "reif", "relation", "use"))), None)
    rows = 0
    if hdr is not None:
        for l in lines[hdr + 2:]:
            if not l.startswith("|"):
                break
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            rows += len(cells) >= 4 and all(cells[:4])
    R.append(("four-column table: map | reifies | relation | use", hdr is not None, "no such header"))
    R.append(("at least 4 filled rows", rows >= 4, f"{rows} rows"))
    m = re.search(r"^#+\s*What pays.*?$(.*?)(^#+\s|\Z)", text, re.S | re.M | re.I)
    body = m.group(1) if m else ""
    items = [l for l in body.splitlines() if l.strip().startswith(("-", "*", "|")) and not set(l.strip()) <= set("|-: ")]
    untiered = [l for l in items if not re.search(TIERS, l)]
    R.append(("a 'What pays' section", bool(m), ""))
    R.append(("every kept property in it carries a tier word", bool(items) and not untiered, f"{len(untiered)} of {len(items)} lines without a tier"))
    R.append(("a 'Kill line:' line", bool(re.search(r"^Kill line:\s*\S", text, re.M)), ""))
    R.append(("a 'Known:' line (prior art named, or where you looked)", bool(re.search(r"^Known:\s*\S", text, re.M)), ""))
    flags = wordlint.scan(path)
    R.append(("no refused words outside quotes", not flags, "; ".join(f"line {i}: {w}" for i, w, _ in flags[:4])))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L11_MAP.md"), os.path.join(HERE, "planted"))
