"""The lever: a value with one rate slot per source (Part V, Unit V6).

Each source is in one of three states for a total:
  absent  never touched the total
  still   touched it, rate 0 here
  moving  touched it, with a nonzero rate
Keeping only 'touched' calls a multiplied-by-0 source a dependency; keeping only the rate calls fee*fee at fee=0 irrelevant.
"""
from fractions import Fraction
from .reading import F, show


class Lever:
    __slots__ = ("value", "rates", "touched")

    def __init__(self, value, rates=None, touched=None):
        self.value = F(value)
        self.rates = {k: F(v) for k, v in (rates or {}).items()}
        self.touched = set(touched or ()) | set(self.rates)

    def __mul__(self, o):
        o = o if isinstance(o, Lever) else Lever(o)
        keys = set(self.rates) | set(o.rates)
        r = {k: self.rates.get(k, 0) * o.value + self.value * o.rates.get(k, 0) for k in keys}
        return Lever(self.value * o.value, r, self.touched | o.touched)
    __rmul__ = __mul__

    def __add__(self, o):
        o = o if isinstance(o, Lever) else Lever(o)
        keys = set(self.rates) | set(o.rates)
        return Lever(self.value + o.value, {k: self.rates.get(k, 0) + o.rates.get(k, 0) for k in keys}, self.touched | o.touched)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Lever) else Lever(o)
        return self + o * Lever(-1)

    def __rsub__(self, o):
        return Lever(o) - self

    def __truediv__(self, o):
        """Derived as in book Unit 8, slot by slot: q = v1/v2, rate_k = (r1_k*v2 - r2_k*v1)/v2^2. Refused on a zero value."""
        from .reading import NO_QUOTIENT
        o = o if isinstance(o, Lever) else Lever(o)
        if o.value == 0:
            return NO_QUOTIENT
        keys = set(self.rates) | set(o.rates)
        r = {k: (self.rates.get(k, 0) * o.value - o.rates.get(k, 0) * self.value) / (o.value * o.value) for k in keys}
        return Lever(self.value / o.value, r, self.touched | o.touched)

    def __rtruediv__(self, o):
        return Lever(o) / self

    def state(self, source):
        if source not in self.touched:
            return "absent"
        return "moving" if self.rates.get(source, 0) != 0 else "still"

    def rate_of(self, source):
        return self.rates.get(source, Fraction(0))


def source(name, value):
    """A named input: its rate against itself is 1."""
    return Lever(value, {name: 1}, {name})
