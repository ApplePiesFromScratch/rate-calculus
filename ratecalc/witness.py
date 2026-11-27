"""Witnesses, load and drag (Part V, Unit V9). A choice, not a discovery.

C: distinct witnesses a claim held in. L: alterations it needed. D: the load of what it rests on.
v = C / (C + L + D). At L >= C, stop patching: keep the core that needed no patch, vent the rest as a new claim.
Effort already spent is not a term.
"""
from fractions import Fraction


def standing(C, L, D):
    v = Fraction(C, C + L + D)
    return v, ("reconfigure" if L >= C else "keep")
