"""Headings (consolidated edition, Unit 14; Part V, Unit V7).

A heading (P : Q) is a pair of whole numbers. It gives a pair (c, s) with c*c + s*s exactly 1:
  c = (Q*Q - P*P) / (P*P + Q*Q),  s = 2*P*Q / (P*P + Q*Q)
Two headings combine: P' = P1*Q2 + P2*Q1, Q' = Q1*Q2 - P1*P2.
A heading never mentions an angle. It shares a pattern with sine and cosine, not an identity.
"""
from fractions import Fraction
from ._plant import PLANT
from .whole import mouth


def unit(P, Q):
    """Whole-number form: (c, s, d) with c*c + s*s == d*d."""
    d = P * P + Q * Q
    c = (P * P - Q * Q) if PLANT == "heading-sign" else (Q * Q - P * P)
    return c, 2 * P * Q, d


def heading(P, Q):
    c, s, d = unit(P, Q)
    return Fraction(c, d), Fraction(s, d)


def combine(h1, h2):
    (P1, Q1), (P2, Q2) = h1, h2
    return (P1 * Q2 + P2 * Q1, Q1 * Q2 - P1 * P2)


def turn_point_shears(x, y, P, Q):
    """Turn a whole-number point by (P : Q) with three shears, each landed by the mouth. Each shear is undone exactly
    by sliding back the same amount, so no two points land on one."""
    c, s, d = unit(P, Q)
    # the half-turn's tangent is P/Q: slide x by -y*P/Q, slide y by x*s/d, slide x by -y*P/Q
    x = x - mouth(y * P, Q)
    y = y + mouth(x * s, d)
    x = x - mouth(y * P, Q)
    return x, y


def turn_point_rounded(x, y, P, Q):
    c, s, d = unit(P, Q)
    return mouth(x * c - y * s, d), mouth(x * s + y * c, d)
