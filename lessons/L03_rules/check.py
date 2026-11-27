#!/usr/bin/env python3
"""L03 check: rules that answer a requested precision with a fraction and a proven bound (guide 12, 13).

  python3 lessons/L03_rules/check.py             # checks lessons/work/L03_rules.py
  python3 lessons/L03_rules/check.py --planted   # the checker must catch every planted fault
"""
import os, sys
from fractions import Fraction as F
from math import factorial
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness

TASK = "L03_rules"
HERE = os.path.dirname(os.path.abspath(__file__))


def check(path):
    m = harness.load_module(path)
    R = []
    def c(name, fn):
        try:
            ok, detail = fn()
            R.append((name, ok, detail))
        except Exception as e:
            R.append((name, False, "raised " + repr(e)[:100]))
    for gap in (F(1, 2), F(1, 16), F(1, 1000), F(1, 10 ** 6), F(3, 7)):
        def b(gap=gap):
            low, high, steps = m.sqrt2_bracket(gap)
            k = 0
            while F(1, 2 ** k) >= gap:
                k += 1
            ok = all(isinstance(v, F) for v in (low, high)) and low * low < 2 < high * high and high - low < gap and steps == k
            return ok, f"got {low}, {high}, {steps}; want a bracket of fractions under {gap} in {k} steps"
        c(f"sqrt 2 bracket under {gap}: fractions, low^2 < 2 < high^2, gap under the request, fewest steps", b)
    for tol in (F(1, 10), F(1, 1000), F(1, 10 ** 6), F(1, 4410), F(1, 4411)):
        def e(tol=tol):
            value, bound, n = m.e_within(tol)
            true_bound = lambda k: F(1, factorial(k + 1)) * F(k + 2, k + 1)
            k = 0
            while true_bound(k) >= tol:
                k += 1
            want = sum(F(1, factorial(j)) for j in range(k + 1))
            return (value == want and bound == true_bound(k) and n == k), f"got stage {n}, value {value}, bound {bound}; want stage {k}"
        c(f"e within {tol}: the first stage whose proven tail bound is under the request", e)
    for top, tol, want in ((1, F(1, 500), 501), (3, F(1, 100), 301), (5, F(1, 1000), 5001), (1, F(1, 2), 3)):
        c(f"stage for {top}/n under {tol} is {want}", lambda top=top, tol=tol, want=want: (m.stage(top, tol) == want, f"got {m.stage(top, tol)}"))
    def refuses_float():
        try:
            m.sqrt2_bracket(0.001)
        except TypeError:
            return True, ""
        return False, "a float request was accepted"
    c("a float request is refused (TypeError)", refuses_float)
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L03_rules.py"), os.path.join(HERE, "planted"))
