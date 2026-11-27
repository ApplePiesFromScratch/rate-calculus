#!/usr/bin/env python3
"""L02 check: which answer belongs to which cut. Your table, measured with your own L01 readings, against the map
guide 07 records. Write lessons/work/L02_cuts.json as

  {"rate(rope,A)": {"naming": "moves"|"stays", "direction": ..., "seed": ..., "scale": ...},
   "rate(B,A)": {...}, "grow": {...}, "when": {...}}

A at 0 with rate 5, B at 10 with rate -3, rope = A - B as named. The cuts: naming (rope = B - A), direction (every
place and rate negated), seed (every rate slot times -1), scale (every place and rate times 3).
Do not open this file's answer table before you have measured. If you did, log a self event and say so.

  python3 lessons/L02_two_cuts/check.py
  python3 lessons/L02_two_cuts/check.py --planted
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "common"))
import harness
TASK = "L02_two_cuts"
TRUTH = {"rate(rope,A)": {"naming": "moves", "direction": "stays", "seed": "stays", "scale": "stays"},
         "rate(B,A)": {"naming": "stays", "direction": "stays", "seed": "stays", "scale": "stays"},
         "grow": {"naming": "stays", "direction": "stays", "seed": "moves", "scale": "stays"},
         "when": {"naming": "stays", "direction": "stays", "seed": "moves", "scale": "stays"}}


def check(path):
    try:
        m = json.load(open(path))
    except Exception as e:
        return [("reads as JSON", False, repr(e)[:100])]
    R = []
    for ans, row in TRUTH.items():
        for cut, want in row.items():
            got = m.get(ans, {}).get(cut)
            R.append((f"{ans} under the {cut} cut", got == want, f"you wrote {got!r}"))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L02_cuts.json"), os.path.join(HERE, "planted"))
