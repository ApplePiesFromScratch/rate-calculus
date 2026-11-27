"""certify: a rate with its receipt (after math-of-logic's kernel, pl/PROCESS.py, MIT, Math of Logic).

certify(fn, at) reads rate(fn(x), x) at x = isolate(at), then runs the gauge: on a listed grid of values and seeds, the
rate must not depend on the seed. It returns a certificate that says
  statement   what was read
  value       the rate at `at`
  cut         the grid it was checked on (the claim does not lift off this grid)
  discharged  grid points that gave an answer, of `scope` points tried (theta points are counted, not hidden)
  tier        FORCED-on-cut if every grid point discharged and the gauge held; EMPIRICAL if some did; UNPAID if none
  falsifier   what would kill it
An empty grid is refused: all([]) is True in Python, and a certificate with nothing weighed is not ok.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from .reading import isolate, rate, Refusal, show


@dataclass
class Certificate:
    statement: str
    value: object
    ok: bool
    discharged: int
    scope: int
    tier: str
    cut: str
    falsifier: str


def certify(fn, at, values=(-4, -3, -2, -1, 1, 2, 3, 4), seeds=(1, 2, Fraction(1, 2), -1)):
    x0 = isolate(at)
    r0 = rate(fn(x0), x0)
    discharged = scope = 0
    gauge = True
    for v, k in product(values, seeds):
        scope += 1
        try:
            a = rate(fn(isolate(v, k)), isolate(v, k))
            b = rate(fn(isolate(v, 1)), isolate(v, 1))
        except (ZeroDivisionError, TypeError, AttributeError):
            continue                      # a refusal inside fn (e.g. no quotient): not discharged
        if isinstance(a, Refusal) or isinstance(b, Refusal):
            continue
        discharged += 1
        if a != b:
            gauge = False
    ok = gauge and discharged > 0 and scope > 0 and not isinstance(r0, Refusal)
    tier = ("FORCED-on-cut" if discharged == scope else "EMPIRICAL") if ok else "UNPAID"
    return Certificate(statement=f"rate(fn(x), x) at {show(at)} is {r0 if isinstance(r0, Refusal) else show(r0)}; gauge on the listed grid",
                       value=r0, ok=ok, discharged=discharged, scope=scope, tier=tier,
                       cut=f"values={list(values)} seeds={[show(k) for k in seeds]}",
                       falsifier="a grid point where the rate depends on the seed")
