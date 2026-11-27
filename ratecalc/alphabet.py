"""Alphabets and mixing rules as data (after propagation-logic's V / G / theta, MIT, MathofLogic).

V      the alphabet: what values may appear
G      the mixing rules: what maps are allowed on V
theta  what counts as accepted, and what happens when a write misses V (refuse, or a registered migration)

scan_closure(Vv, Vr, mix)  checks every input of a pair rule over finite slot alphabets; returns (leaks, total, first leak).
morphism(f, rule_a, rule_b, V) checks f(rule_a(a, b)) == rule_b(f(a), f(b)) on every pair; returns the first witness that fails.
drop_rate(reading)          migrates a Reading to a plain value only if its rate is 0: a live rate has no slot in a plain
                            value, so dropping it is refused (channel preservation).
"""
from itertools import product
from .reading import Reading, Refusal

LIVE_RATE = Refusal("live rate", "a Reading with a nonzero rate cannot become a plain value without losing its rate")


def scan_closure(Vv, Vr, mix):
    leaks, total, first = 0, 0, None
    for v1, r1, v2, r2 in product(Vv, Vr, Vv, Vr):
        total += 1
        v, r = mix(v1, r1, v2, r2)
        if v not in Vv or r not in Vr:
            leaks += 1
            first = first or ((v1, r1), (v2, r2), (v, r))
    return leaks, total, first


def scan_closure2(V, op):
    """A binary rule on one finite alphabet: (leaks, total, first leak)."""
    leaks, total, first = 0, 0, None
    for a, b in product(V, V):
        total += 1
        out = op(a, b)
        if out not in V:
            leaks += 1
            first = first or (a, b, out)
    return leaks, total, first


def morphism(f, rule_a, rule_b, V):
    for a, b in product(V, V):
        if f(rule_a(a, b)) != rule_b(f(a), f(b)):
            return False, (a, b)
    return True, None


def drop_rate(x):
    if not isinstance(x, Reading):
        return x
    return LIVE_RATE if x.rate != 0 else x.value
