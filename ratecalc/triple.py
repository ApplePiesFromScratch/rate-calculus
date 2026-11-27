"""A rate that has its own rate (consolidated edition, Unit 8): (value, rate, curve).

The curve rule is not picked: it is Unit 3's rule used twice, once on each strip.
  mix((v1,r1,c1),(v2,r2,c2)) = (v1*v2, r1*v2 + v1*r2, c1*v2 + 2*r1*r2 + v1*c2)
Seed x as (v, 1, 0): its rate against itself is 1, and a constant 1 has no rate of its own.
"""
from fractions import Fraction
from .reading import F, show


class Triple:
    __slots__ = ("value", "rate", "curve")

    def __init__(self, value, rate=0, curve=0):
        self.value, self.rate, self.curve = F(value), F(rate), F(curve)

    def __mul__(self, o):
        o = o if isinstance(o, Triple) else Triple(o)
        return Triple(self.value * o.value,
                      self.rate * o.value + self.value * o.rate,
                      self.curve * o.value + 2 * self.rate * o.rate + self.value * o.curve)
    __rmul__ = __mul__

    def __add__(self, o):
        o = o if isinstance(o, Triple) else Triple(o)
        return Triple(self.value + o.value, self.rate + o.rate, self.curve + o.curve)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Triple) else Triple(o)
        return Triple(self.value - o.value, self.rate - o.rate, self.curve - o.curve)

    def __eq__(self, o):
        return (self.value, self.rate, self.curve) == (o.value, o.rate, o.curve)

    def __repr__(self):
        return f"({show(self.value)}, {show(self.rate)}, {show(self.curve)})"


def isolate3(value):
    return Triple(value, 1, 0)
