#!/usr/bin/env python3
"""L01 check: your readings module against the book's own demonstrations, the seed, theta, and the derived division.

  python3 lessons/L01_readings/check.py              # checks lessons/work/L01_readings.py
  python3 lessons/L01_readings/check.py --planted    # the checker must catch every planted fault
"""
import os, sys, random, numbers
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness

TASK = "L01_readings"
HERE = os.path.dirname(os.path.abspath(__file__))


def check(path):
    m = harness.load_module(path)
    R = []
    def c(name, fn):
        try:
            got, want = fn()
            R.append((name, got == want, "" if got == want else f"got {got!r}, want {want!r}"))
        except Exception as e:
            R.append((name, False, "raised " + repr(e)[:100]))
    T = m.THETA
    iso, mix, add, sub, div, rate, when = m.isolate, m.mix, m.add, m.sub, m.div, m.rate, m.when
    def pair(r):
        return (F(r[0]), F(r[1])) if r is not T else T

    # Unit 1, 2, 3
    c("U1 isolate(8, 2)", lambda: (pair(iso(8, 2)), (8, 2)))
    c("U1 isolate(5) seeds rate 1", lambda: (pair(iso(5)), (5, 1)))
    c("U2 rate((10;4),(5;2)) = 2", lambda: (rate(iso(10, 4), iso(5, 2)), 2))
    c("U3 x=isolate(4): x*x = (16; 8)", lambda: (pair(mix(iso(4), iso(4))), (16, 8)))
    c("U3 x=isolate(3): rate(x*x, x) = 6", lambda: (rate(mix(iso(3), iso(3)), iso(3)), 6))
    # Unit 4: powers at 2 up to 6
    def power(x, n):
        p = x
        for _ in range(n - 1):
            p = mix(p, x)
        return p
    for n in range(2, 7):
        c(f"U4 x=isolate(2): x^{n} = ({2**n}; {n * 2**(n-1)})", lambda n=n: (pair(power(iso(2), n)), (2**n, n * 2**(n - 1))))
    # Unit 5: the seed cancels, negative seed included
    for s in (1, 2, 3, 10, -3):
        c(f"U5 seed {s}: rate(x*x, x) at 5 = 10", lambda s=s: (rate(mix(iso(5, s), iso(5, s)), iso(5, s)), 10))
    # Unit 6: chain, and theta
    def chain():
        t = iso(2); u = mix(t, iso(2, 0)); y = mix(u, u)
        return (pair(y), rate(y, t), rate(y, u) * rate(u, t)), ((16, 16), 16, 16)
    c("U6 the two-room chain at t=2", chain)
    c("U6 THETA is not a number", lambda: (isinstance(T, numbers.Number), False))
    c("U6 rate(bathtub, candle) is THETA", lambda: (rate(iso(8, 2), iso(15, 0)) is T, True))
    c("U2 rate(x, x) with a still slot is THETA, not 1", lambda: (rate(iso(7, 0), iso(7, 0)) is T, True))
    # Unit 7
    def u7a():
        x = iso(2); return pair(add(mix(x, x), add(add(x, x), x))), (10, 7)
    def u7b():
        x = iso(2); return pair(add(add(mix(mix(x, x), x), add(x, x)), iso(1, 0))), (13, 14)
    c("U7 x*x + 3x at 2 = (10; 7)", u7a)
    c("U7 x*x*x + 2x + 1 at 2 = (13; 14)", u7b)
    # Unit 10: derived division
    c("U10 1/x at (3;1) = (1/3; -1/9)", lambda: (pair(div(iso(1, 0), iso(3))), (F(1, 3), F(-1, 9))))
    def u10b():
        x = iso(3); return pair(div(add(mix(x, x), iso(1, 0)), sub(x, iso(1, 0)))), (5, F(1, 2))
    c("U10 (x*x+1)/(x-1) at 3 = (5; 1/2)", u10b)
    c("U10 (6;4)/(2;0) = (3; 2)", lambda: (pair(div(iso(6, 4), iso(2, 0))), (3, 2)))
    c("U10 1/x at (0;1) is THETA", lambda: (div(iso(1, 0), iso(0)) is T, True))
    # when as a count of latches (guide 11): when = -value/rate
    c("U9 when((10;-8)) = 5/4 latches", lambda: (when(iso(10, -8)), F(5, 4)))
    c("U9 when((10;0)) is THETA", lambda: (when(iso(10, 0)) is T, True))
    # no fraction built from a float
    def floats():
        try:
            iso(0.1)
            return "accepted", "refused"
        except Exception:
            return "refused", "refused"
    c("FRACTIONS rule 1: isolate(0.1) is refused", floats)
    # properties on random expressions
    rnd = random.Random(20261125)
    def rand_expr(x, depth):
        if depth == 0:
            return x if rnd.random() < 0.6 else iso(rnd.randint(-5, 5), 0)
        a, b = rand_expr(x, depth - 1), rand_expr(x, depth - 1)
        op = rnd.choice("+-*")
        return add(a, b) if op == "+" else sub(a, b) if op == "-" else mix(a, b)
    def seed_cancels():
        bad = 0
        for k in range(300):
            st = rnd.getstate(); v = F(rnd.randint(-9, 9), rnd.randint(1, 5))
            answers = set()
            for s in (F(1), F(7, 2), F(-1)):
                rnd.setstate(st); rnd.randint(-9, 9); rnd.randint(1, 5)
                x = iso(v, s); y = rand_expr(x, 3); r = rate(y, x)
                answers.add(r if r is not T else "THETA")
            bad += len(answers) != 1
        return bad, 0
    c("seed cancels on 300 random expressions (seeds 1, 7/2, -1)", seed_cancels)
    def undo():
        bad = 0
        for k in range(500):
            a = iso(F(rnd.randint(-20, 20), rnd.randint(1, 6)), F(rnd.randint(-20, 20), rnd.randint(1, 6)))
            b = iso(F(rnd.choice([i for i in range(-20, 21) if i]), rnd.randint(1, 6)), F(rnd.randint(-20, 20), rnd.randint(1, 6)))
            q = div(a, b)
            bad += q is T or pair(mix(q, b)) != pair(a)
        return bad, 0
    c("division undoes mix on 500 random pairs", undo)
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L01_readings.py"), os.path.join(HERE, "planted"))
