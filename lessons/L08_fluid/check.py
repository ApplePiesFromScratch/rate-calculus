#!/usr/bin/env python3
"""L08 check: a fluid on a ring of 64 places, by trades at faces only (guide 28). No Navier-Stokes, no time step.

  python3 lessons/L08_fluid/check.py             # checks lessons/work/L08_fluid.py
  python3 lessons/L08_fluid/check.py --planted
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness

TASK = "L08_fluid"
HERE = os.path.dirname(os.path.abspath(__file__))


def check(path):
    m = harness.load_module(path)
    R = []
    N = 64
    s = [1000] * N; mo = [0] * N
    for i in range(30, 35):
        s[i] = 2000
    S0, M0, top0 = sum(s), sum(mo), max(s)
    whole = stuff_book = mom_book = positive = True
    first_bad = None
    lowest_top = top0
    mirror_ok = True
    for k in range(3000):
        if k in (0, 7, 150, 2999):            # mirror: the ring read the other way round must give the mirrored latch
            rs, rm = m.step(s[::-1], [-v for v in mo[::-1]])
            fs, fm = m.step(list(s), list(mo))
            mirror_ok = mirror_ok and rs == fs[::-1] and rm == [-v for v in fm[::-1]]
        before = (list(s), list(mo))
        s, mo = m.step(s, mo)
        if (s, mo) == before and k == 0:
            first_bad = first_bad or "nothing moved"
        whole = whole and all(isinstance(v, int) for v in s + mo)
        if sum(s) != S0 and stuff_book:
            stuff_book = False; first_bad = first_bad or f"stuff book opened at latch {k + 1}"
        if sum(mo) != M0 and mom_book:
            mom_book = False; first_bad = first_bad or f"momentum book opened at latch {k + 1}"
        positive = positive and min(s) > 0
        lowest_top = min(lowest_top, max(s))
    R.append(("whole numbers every latch", whole, ""))
    R.append(("stuff = start every latch", stuff_book, first_bad or ""))
    R.append(("momentum = start every latch (a ring has no walls)", mom_book, first_bad or ""))
    R.append(("every place keeps stuff > 0", positive, f"min {min(s)}"))
    R.append(("the bump spreads: its top falls below 3/4 of the start at some latch", lowest_top * 4 < top0 * 3, f"lowest top {lowest_top}, start {top0}"))
    R.append(("mirror: reading the ring the other way gives the mirrored latch (no sweep-order bias)", mirror_ok, ""))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L08_fluid.py"), os.path.join(HERE, "planted"))
