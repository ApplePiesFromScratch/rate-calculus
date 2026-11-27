#!/usr/bin/env python3
"""L07 check: alphabets and mixing rules: scan every input for closure, and test maps between alphabets (guide 19).

  python3 lessons/L07_alphabet/check.py             # checks lessons/work/L07_alphabet.py
  python3 lessons/L07_alphabet/check.py --planted
"""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness

TASK = "L07_alphabet"
HERE = os.path.dirname(os.path.abspath(__file__))
LEIB = lambda v1, r1, v2, r2: (v1 * v2, r1 * v2 + v1 * r2)


def check(path):
    m = harness.load_module(path)
    R = []
    def c(name, fn):
        try:
            got, want = fn()
            R.append((name, got == want, "" if got == want else f"got {got!r}, want {want!r}"))
        except Exception as e:
            R.append((name, False, "raised " + repr(e)[:100]))
    c("mix on bits leaks on 1 of 16", lambda: (m.scan_closure({0, 1}, {0, 1}, LEIB), (1, 16)))
    c("strips by XOR close on bits", lambda: (m.scan_closure({0, 1}, {0, 1}, lambda a, b, c_, d: (a * c_, (b * c_) ^ (a * d))), (0, 16)))
    c("mix on {0,1,2} leaks on 28 of 81", lambda: (m.scan_closure({0, 1, 2}, {0, 1, 2}, LEIB), (28, 81)))
    c("mix mod 3 closes on 81", lambda: (m.scan_closure({0, 1, 2}, {0, 1, 2}, lambda a, b, c_, d: ((a * c_) % 3, (b * c_ + a * d) % 3)), (0, 81)))
    c("a rule that leaks only in the rate slot is counted", lambda: (m.scan_closure({0, 1}, {0, 1}, lambda a, b, c_, d: (0, b + d)), (4, 16)))
    c("values {0,1}, rates {0,1,2}: mix closes", lambda: (m.scan_closure({0, 1}, {0, 1, 2}, lambda a, b, c_, d: (a * c_, min(2, b * c_ + a * d))), (0, 36)))
    f = lambda v: 1 if v == 1 else 0
    V3 = [0, F(1, 2), 1]
    c("'1 stays 1, else 0' commutes with AND as min on three values", lambda: (m.morphism(f, min, min, V3), (True, None)))
    c("... and fails for NOT, with the witness (1/2, 0)", lambda: (m.morphism(f, lambda a, b: 1 - a, lambda a, b: 1 - a, V3), (False, (F(1, 2), 0))))
    c("doubling mod 8 into mod 4 commutes with addition", lambda: (m.morphism(lambda v: v % 4, lambda a, b: (a + b) % 8, lambda a, b: (a + b) % 4, range(8)), (True, None)))
    c("mod 8 into mod 3 fails for addition: witness (1, 7)", lambda: (m.morphism(lambda v: v % 3, lambda a, b: (a + b) % 8, lambda a, b: (a + b) % 3, range(8)), (False, (1, 7))))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L07_alphabet.py"), os.path.join(HERE, "planted"))
