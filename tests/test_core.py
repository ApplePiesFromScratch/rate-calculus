#!/usr/bin/env python3
"""The core's own tests. Each test runs twice: once against the right answer (must pass) and once against a planted
wrong answer beside it (must be refused). A test that cannot refuse a wrong answer is not a test.
Usage: python3 tests/test_core.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ratecalc import *

CASES = [
    # (name, computed, right, planted wrong)
    ("isolate(8, 2)", isolate(8, 2), R(8, 2), R(2, 8)),
    ("rate((10,4),(5,2))", rate(isolate(10, 4), isolate(5, 2)), 2, F("1/2")),
    ("mix x*x at 4", isolate(4) * isolate(4), R(16, 8), R(16, 1)),
    ("x*x*x at 2", power(isolate(2), 3), R(8, 12), R(8, 6)),
    ("seed cancels at seed 10", rate(isolate(5, 10) * isolate(5, 10), isolate(5, 10)), 10, 100),
    ("seed 1/3", rate(isolate(6, F("1/3")) * isolate(6, F("1/3")), isolate(6, F("1/3"))), 12, 4),
    ("chain y=(2t)^2 at 2", rate(mix(mix(isolate(2), 2), mix(isolate(2), 2)), isolate(2)), 16, 8),
    ("theta", rate(isolate(8, 2), isolate(15, 0)), THETA, 0),
    ("1/x at 3", const(1) / isolate(3), R(F("1/3"), F("-1/9")), R(F("1/3"), F("1/9"))),
    ("(x*x+1)/(x-1) at 3", (isolate(3) * isolate(3) + 1) / (isolate(3) - 1), R(5, F("1/2")), R(5, 2)),
    ("1/x at 0 refuses", const(1) / isolate(0), NO_QUOTIENT, R(0, 0)),
    ("triple x^3 at 3", isolate3(3) * isolate3(3) * isolate3(3), Triple(27, 27, 18), Triple(27, 27, 9)),
    ("sqrt2 averaging x4", sqrt2_averaging(4)[-1], F(665857, 470832), F(577, 408)),
    ("x4^2 - 2", sqrt2_averaging(4)[-1] ** 2 - 2, F(1, 221682772224), 0),
    ("E P6 at 1", E_poly(6, 1)[0], F(1957, 720), F(163, 60)),
    ("E shortfall P6", E_poly(6, 1)[2], F(1, 720), F(1, 120)),
    ("E tail after P6", E_tail_bound(6), F(1, 4410), F(1, 5040)),
    ("S5 at 1", S_poly(5, 1), (F(101, 120), F(13, 24)), (F(5, 6), F(1, 2))),
    ("C4 at 1", C_poly(4, 1), (F(13, 24), F(-5, 6)), (F(1, 2), -1)),
    ("stage 3/n < 1/100", stage_for(3, F(1, 100)), 301, 300),
    ("halvings for 1/1000", halving_steps_for(F(1, 1000)), 10, 9),
    ("heading(1,2)", heading(1, 2), (F(3, 5), F(4, 5)), (F(4, 5), F(3, 5))),
    ("combine (1,2),(1,1)", combine((1, 2), (1, 1)), (3, 1), (1, 3)),
    ("mouth 5/2", mouth(5, 2), 2, 3),
    ("mouth -7/2", mouth(-7, 2), -4, -3),
    ("mouth -1/2", mouth(-1, 2), 0, -1),
    ("toward zero -7/2", toward_zero(-7, 2), -3, -4),
    ("meet", when(gap(isolate(10, -3), isolate(0, 5))), F(5, 4), F(25, 2)),
    ("closest near miss", closest(R(5, -2), R(5, 0)), (F(5, 2), 25), (F(5, 2), 0)),
    ("collisions x+x", collisions(lambda x: x + x), 128, 256),
    ("collisions x*5", collisions(lambda x: x * 5), 256, 128),
    ("standing 2,3,1", standing(2, 3, 1), (F(1, 3), "reconfigure"), (F(1, 3), "keep")),
]


def carry_case():
    c = Carry(4, 3)
    s = "".join(str(c.tick()) for _ in range(24))
    held = c.books()
    for _ in range(100000 - 24):
        c.tick(); held = held and c.books()
    return (s, c.count, held)


CASES.append(("carry 4/3 x 100000", carry_case(), ("112" * 8, 133333, True), ("112" * 8, 133334, True)))

good = bad = 0
for name, got, right, wrong in CASES:
    ok = got == right and not (got == wrong)
    good += ok; bad += not ok
    if not ok:
        print(f"FAIL {name}: got {got!r}, right {right!r}, planted wrong {wrong!r}")
print(f"test_core: {good} passed, {bad} failed (each with a planted wrong answer refused)")
sys.exit(1 if bad else 0)
