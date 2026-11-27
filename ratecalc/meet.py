"""When two moving things meet (consolidated edition, Unit 9), without an independent variable.

Subtract readings piece by piece to get the gap (value, rate). The gap runs out after
  when = -value / rate   latches (counted in the same unit the rates are counted per)
This is a reading taken from the gap itself; nothing is stepped through it. A still gap (rate 0) refuses: THETA.
when is first order: it reads the gap's rate as it is now. If the rates themselves change, read again.
In two directions the closest approach comes at
  when = -(gx.value*gx.rate + gy.value*gy.rate) / (gx.rate^2 + gy.rate^2)
and the squared distance there is exact, with no square root.
"""
from fractions import Fraction
from ._plant import PLANT
from .reading import Reading, THETA, lift


def gap(b, a):
    return lift(b) - lift(a)


def when(g):
    g = lift(g)
    if g.rate == 0:
        return THETA
    w = g.value / g.rate
    return w if PLANT == "meet-sign" else -w


def grow(g):
    """The gap's rate over its own value (Part V, Unit V3). THETA-like refusal when the value is 0 is the caller's call."""
    g = lift(g)
    return g.rate / g.value


def closest(gx, gy):
    """Return (when, squared distance at that when). Refuses (THETA) if neither gap moves."""
    gx, gy = lift(gx), lift(gy)
    speed2 = gx.rate * gx.rate + gy.rate * gy.rate
    if speed2 == 0:
        return THETA, gx.value * gx.value + gy.value * gy.value
    w = -(gx.value * gx.rate + gy.value * gy.rate) / speed2
    x = gx.value + w * gx.rate
    y = gy.value + w * gy.rate
    return w, x * x + y * y
