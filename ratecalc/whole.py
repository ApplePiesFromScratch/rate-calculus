"""Whole numbers (Part V, Units V1 and V2): the mouth and the carry.

The mouth lands a fraction on a whole number once, at the edge, never in the middle of a chain:
  nearest whole number; an exact half goes to the even neighbour; mouth(-x) = -mouth(x).
The carry sends a rate n/d as whole pulses with books that hold every tick:
  d*count + carry = n*ticks, with 0 <= carry < d.
"""
from fractions import Fraction
from ._plant import PLANT


def mouth(n, d=1):
    """Land n/d on a whole number. Half to even, mirror-true. d > 0."""
    if d <= 0:
        raise ValueError("mouth needs a positive bottom")
    if PLANT == "mouth-floor":
        return n // d
    neg = n < 0
    m = -n if neg else n
    q, r = divmod(m, d)
    if 2 * r > d or (2 * r == d and q % 2 == 1):
        q += 1
    return -q if neg else q


def mouth_of(x):
    x = Fraction(x)
    return mouth(x.numerator, x.denominator)


def toward_negative(n, d):
    """Python's //: lands toward the more negative number."""
    return n // d


def toward_zero(n, d):
    """C's integer division: lands toward zero."""
    q = abs(n) // abs(d)
    return q if (n >= 0) == (d > 0) else -q


class Carry:
    """A rate n/d (n >= 0, d > 0) sent as whole pulses. tick() returns the pulses leaving this tick."""

    def __init__(self, n, d):
        if d <= 0 or n < 0:
            raise ValueError("Carry needs n >= 0 and d > 0")
        self.n, self.d, self.acc, self.count, self.ticks = n, d, 0, 0, 0

    def tick(self):
        self.acc += self.n
        out = 0
        if PLANT == "carry-if":
            if self.acc >= self.d:
                self.acc -= self.d
                out = 1
        else:
            while self.acc >= self.d:
                self.acc -= self.d
                out += 1
        self.count += out
        self.ticks += 1
        return out

    def books(self):
        """True while d*count + carry == n*ticks AND 0 <= carry < d. Books alone are not enough: the bound is part of it."""
        return self.d * self.count + self.acc == self.n * self.ticks and 0 <= self.acc < self.d
