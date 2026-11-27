#!/usr/bin/env python3
"""L05 check: move a kept quantity; never set it. Heat on a ring of 64 places spreads by transfer between neighbours.

  python3 lessons/L05_transfer/check.py             # checks lessons/work/L05_transfer.py
  python3 lessons/L05_transfer/check.py --planted
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness
TASK = "L05_transfer"
HERE = os.path.dirname(os.path.abspath(__file__))


def check(path):
    m = harness.load_module(path)
    R = []
    h = [0] * 64
    for i in range(20, 28): h[i] = 1000
    h[40] = 7; h[50] = 1
    total0 = sum(h); spread0 = max(h)
    broken = negative = notint = 0
    try:
        for k in range(2000):
            h = m.step(list(h))
            notint += not all(isinstance(v, int) for v in h)
            broken += sum(h) != total0
            negative += sum(1 for v in h if v < 0)
        R.append(("64 places returned every step", len(h) == 64, f"{len(h)} places"))
        R.append(("whole numbers on every step", notint == 0, f"{notint} steps with a non-integer"))
        R.append((f"total {total0} held on all 2000 steps", broken == 0, f"broken on {broken} steps, ends at {sum(h)}"))
        R.append(("no place ever negative (conservation is not correctness: count the negatives too)", negative == 0, f"{negative} negative readings"))
        R.append(("it spread: the tallest place fell below half its start", max(h) < spread0 // 2, f"max {max(h)} from {spread0}"))
    except Exception as e:
        R.append(("ran without raising", False, repr(e)[:120]))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L05_transfer.py"), os.path.join(HERE, "planted"))
