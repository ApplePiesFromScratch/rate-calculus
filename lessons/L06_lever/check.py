#!/usr/bin/env python3
"""L06 check: the lever, a value with one rate per source and the three states absent / still / moving (guide 17).

  python3 lessons/L06_lever/check.py             # checks lessons/work/L06_lever.py
  python3 lessons/L06_lever/check.py --planted
"""
import os, sys, random
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness

TASK = "L06_lever"
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
    S = m.source
    def demo():
        p, q, fee, fl = S("price", 12), S("qty", 3), S("fee", 0), S("floor", 5)
        return p * q + fee * fee + fl * 0
    c("total = price*qty + fee*fee + floor*0 at 12, 3, 0, 5: value 36", lambda: (demo().value, 36))
    c("price moving at 3", lambda: ((demo().state("price"), demo().rate_of("price")), ("moving", 3)))
    c("qty moving at 12", lambda: ((demo().state("qty"), demo().rate_of("qty")), ("moving", 12)))
    c("fee still (touched, rate 0 here)", lambda: (demo().state("fee"), "still"))
    c("floor still (multiplied by 0)", lambda: (demo().state("floor"), "still"))
    c("tax absent (never touched)", lambda: (demo().state("tax"), "absent"))
    def tax():
        t = demo() * S("tax", 2)
        return (t.value, t.rate_of("price"), t.rate_of("qty"), t.rate_of("tax")), (72, 6, 24, 36)
    c("times tax at 2: 72, rates 6, 24, 36", tax)
    def ab():
        a, b = S("a", 2), S("b", 3); y = a * b + b * b
        return (y.value, y.rate_of("a"), y.rate_of("b")), (15, 3, 8)
    c("y = a*b + b*b at 2, 3: 15, rate per a 3, per b 8", ab)
    rng = random.Random(7)
    def rand_poly():
        for _ in range(200):
            a, b = rng.randint(-5, 5), rng.randint(-5, 5)
            A, B = S("a", a), S("b", b)
            y = A * A * B + 3 * A + B * B * B
            want = (a * a * b + 3 * a + b ** 3, 2 * a * b + 3, a * a + 3 * b * b)
            if (y.value, y.rate_of("a"), y.rate_of("b")) != want:
                return (a, b, (y.value, y.rate_of("a"), y.rate_of("b"))), want
        return True, True
    c("200 random points of a*a*b + 3a + b^3: value and both rates exact", rand_poly)
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L06_lever.py"), os.path.join(HERE, "planted"))
