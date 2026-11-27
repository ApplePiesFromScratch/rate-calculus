"""The alphabet and the three moves (book Units 1 to 8).

A Reading is a pair of fractions (value, rate). Nothing else is in the alphabet.
  isolate(v, r=1)   builds a Reading                      (Unit 1)
  rate(A, B)        A's rate slot over B's rate slot       (Unit 2); THETA when B's rate is 0 (Unit 6)
  mix(A, B)  = A*B  (v1*v2, r1*v2 + v1*r2)                 (Unit 3), fixed once, used everywhere
  A + B, A - B      piece by piece                          (Units 6, 7)
  A / B             derived from mix, not a fourth move     (Unit 8); refused when B's value is 0
Every slot is a Fraction, so every output is exact.
"""
from fractions import Fraction
from ._plant import PLANT


def F(x, d=None):
    """F(3, 4), F('3/4'), F(3) or F(Fraction) -> an exact Fraction. Floats are refused: a float is another alphabet."""
    if isinstance(x, float) or isinstance(d, float):
        raise TypeError("a float is not in this alphabet; write the fraction, e.g. F(1, 10) or F('1/10')")
    if isinstance(x, bool) or isinstance(d, bool):
        raise TypeError("a bool is not in this alphabet (Python lets True act as 1; this library does not)")
    return Fraction(x) if d is None else Fraction(x, d)


class Refusal:
    """A named refusal: the machine declines on purpose and says why. Not a number, not zero, not a host error."""
    def __init__(self, name, why):
        self.name, self.why = name, why
    def __repr__(self):
        return f"{self.name} ({self.why})"
    def __eq__(self, other):
        return isinstance(other, Refusal) and other.name == self.name
    def __hash__(self):
        return hash(self.name)


THETA = Refusal("theta", "isolator r=0: the reading compared against is not changing")
NO_QUOTIENT = Refusal("no quotient", "the divisor's value is 0")


class Reading:
    __slots__ = ("value", "rate")

    def __init__(self, value, rate):
        self.value, self.rate = F(value), F(rate)

    # ---- the third move and the piece-by-piece moves
    def __mul__(self, other):
        o = lift(other)
        if PLANT == "mix-rate-product":
            return Reading(self.value * o.value, self.rate * o.rate)
        return Reading(self.value * o.value, self.rate * o.value + self.value * o.rate)
    __rmul__ = __mul__

    def __add__(self, other):
        o = lift(other)
        return Reading(self.value + o.value, self.rate + o.rate)
    __radd__ = __add__

    def __sub__(self, other):
        o = lift(other)
        return Reading(self.value - o.value, self.rate - o.rate)

    def __rsub__(self, other):
        return lift(other) - self

    def __neg__(self):
        return Reading(-self.value, -self.rate)

    # ---- division, derived in Unit 8: (v2, r2) * (q, s) = (v1, r1) forces q = v1/v2, s = (r1*v2 - r2*v1)/v2^2
    def __truediv__(self, other):
        o = lift(other)
        if o.value == 0:
            return NO_QUOTIENT
        q = self.value / o.value
        if PLANT == "div-sign":
            s = (o.rate * self.value - self.rate * o.value) / (o.value * o.value)
        else:
            s = (self.rate * o.value - o.rate * self.value) / (o.value * o.value)
        return Reading(q, s)

    def __rtruediv__(self, other):
        return lift(other) / self

    def __eq__(self, other):
        if isinstance(other, Refusal):
            return False
        o = lift(other)
        return self.value == o.value and self.rate == o.rate

    def __hash__(self):
        return hash((self.value, self.rate))

    def __iter__(self):
        yield self.value
        yield self.rate

    def __repr__(self):
        return f"({show(self.value)}, {show(self.rate)})"


def show(x):
    """Print a Fraction the way the book writes it: 3, -1/9, 665857/470832."""
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def lift(x):
    """A plain number is the Reading (number, 0): Unit 6, 'multiplying by a plain number'."""
    if isinstance(x, Reading):
        return x
    if isinstance(x, tuple) and len(x) == 2:
        return Reading(*x)
    return Reading(x, 0)


def R(value, rate):
    """Write a Reading directly: R(8, 2) is (8, 2)."""
    return Reading(value, rate)


def isolate(value, rate=1):
    """Unit 1. isolate(v) is short for isolate(v, 1): the thing everything else is compared to."""
    return Reading(value, rate)


def const(value):
    """A plain number as a Reading: (value, 0)."""
    return Reading(value, 0)


def mix(a, b):
    """Unit 3: mix((v1,r1),(v2,r2)) outputs (v1*v2, r1*v2 + v1*r2)."""
    return lift(a) * lift(b)


def rate(a, b):
    """Unit 2: rate(A, B) = A's rate slot / B's rate slot. Never looks at either value. THETA when B's rate is 0."""
    a, b = lift(a), lift(b)
    if b.rate == 0:
        if PLANT == "theta-zero":
            return Fraction(0)
        return THETA
    return a.rate / b.rate


def power(x, n):
    """x mixed with itself: n - 1 mixes (book: 'Any Number Of Mixes'). n >= 1."""
    if n < 1:
        raise ValueError("power needs n >= 1 (n mixes of x with itself)")
    out = lift(x)
    for _ in range(n - 1):
        out = out * x
    return out
