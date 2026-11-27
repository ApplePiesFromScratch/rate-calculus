#!/usr/bin/env python3
"""L09 check: the useful pattern's six clauses as rules (guide 26). Your Flux must hold its books every latch, never move
the front back, never take the field below zero, keep a pattern within THETA after it reconfigures, and give the same
served / refused / reconfigured / L as the library's Flux (ratecalc/pattern.py) on two scenarios.

  python3 lessons/L09_pattern/check.py             # checks lessons/work/L09_pattern.py
  python3 lessons/L09_pattern/check.py --planted
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness
sys.path.insert(0, harness.REPO)
from ratecalc.pattern import Flux as RefFlux

TASK = "L09_pattern"
HERE = os.path.dirname(os.path.abspath(__file__))
SCEN = {
    "four patterns, drained at 1000": ([("simple", 2, {0, 1}, 2, 1, 2), ("venting", 2, {1, 2}, 3, 1, 4), ("heavy", 2, {2, 3}, 3, 0, 1), ("lonely", 1, {9}, 2, 1, 8)], 400, 2000, 1000),
    "two patterns sharing a cell": ([("simple", 2, {0, 1}, 2, 1, 2), ("heavy", 2, {1, 2}, 3, 0, 1)], 400, 500, None),
}


def run(cls, pats, field, n, drain_at):
    f = cls(field)
    for name, C, cells, take, vn, vd in pats:
        f.add(name, C=C, cells=set(cells), take=take, vent_num=vn, vent_den=vd)
    books = field_ok = theta_ok = True
    for k in range(n):
        if drain_at is not None and k == drain_at:
            f.drain(f.field - 4)
        f.latch()
        books = books and f.books()
        field_ok = field_ok and f.field >= 0
        theta_ok = theta_ok and all(q.L <= f.THETA for q in f.p if q.reconfigs)
    return f, books, field_ok, theta_ok


def check(path):
    m = harness.load_module(path)
    R = []
    for name, (pats, field, n, drain_at) in SCEN.items():
        try:
            mine, books, field_ok, theta_ok = run(m.Flux, pats, field, n, drain_at)
            ref = run(RefFlux, pats, field, n, drain_at)[0]
            got = [(q.name, q.served, q.refused, q.reconfigs, q.L) for q in mine.p]
            want = [(q.name, q.served, q.refused, q.reconfigs, q.L) for q in ref.p]
            R.append((f"{name}: books close every latch (field + every L = start - drained)", books, ""))
            R.append((f"{name}: the field never goes below zero (theta, not a debt)", field_ok, ""))
            R.append((f"{name}: the front never moves back", not mine.front_moved_back, ""))
            R.append((f"{name}: a reconfigured pattern stays within THETA", theta_ok, ""))
            R.append((f"{name}: served / refused / reconfigured / L match the library", got == want, f"got {got}, want {want}"))
        except Exception as e:
            R.append((name, False, "raised " + repr(e)[:120]))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L09_pattern.py"), os.path.join(HERE, "planted"))
