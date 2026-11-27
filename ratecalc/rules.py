"""Rules for numbers that are not fractions (book Units 9, 10, 11, 12).

A rule takes a requested precision (a positive fraction) and hands back a fraction with a proof of how close it is.
Nothing runs forever: each request runs a finite number of steps and stops.
"""
from fractions import Fraction
from math import factorial


def sqrt2_halving(steps):
    """Unit 9, Demonstration 2: bracket [low, high] with low^2 < 2 < high^2, halve the gap each step."""
    low, high = Fraction(1), Fraction(2)
    rows = []
    for k in range(1, steps + 1):
        mid = (low + high) / 2
        if mid * mid > 2:
            high = mid
            moved = "high"
        else:
            low = mid
            moved = "low"
        rows.append((k, low, high, high - low, mid, moved))
    return low, high, rows


def halving_steps_for(gap):
    """How many halvings bring the gap (starting at 1) under the requested gap: first k with 1/2^k < gap."""
    gap = Fraction(gap)
    k = 0
    while Fraction(1, 2 ** k) >= gap:
        k += 1
    return k


def sqrt2_averaging(steps):
    """Unit 9, Demonstration 3: x -> (x + 2/x) / 2 from x = 1."""
    x = Fraction(1)
    out = [x]
    for _ in range(steps):
        x = (x + 2 / x) / 2
        out.append(x)
    return out


def E_poly(n, x):
    """Unit 10: P(n) = 1 + x + x^2/2! + ... + x^n/n!, its rate (which is P(n-1)), and the shortfall value - rate = x^n/n!."""
    x = Fraction(x)
    value = sum(x ** k / factorial(k) for k in range(n + 1))
    rate = sum(x ** k / factorial(k) for k in range(n))
    return value, rate, value - rate


def E_tail_bound(n):
    """Unit 10, Demonstration 2 at x = 1: the tail after P(n) is at most 1/(n+1)! * (n+2)/(n+1).
    (Each later term is at most 1/(n+2) of the one before.)"""
    return Fraction(1, factorial(n + 1)) * Fraction(n + 2, n + 1)


def S_poly(n, x):
    """Unit 11: S = x - x^3/3! + x^5/5! - ..., terms up to degree n. Returns (value, rate)."""
    x = Fraction(x)
    v = sum((-1) ** (k // 2) * x ** k / factorial(k) for k in range(1, n + 1, 2))
    r = sum((-1) ** (k // 2) * k * x ** (k - 1) / factorial(k) for k in range(1, n + 1, 2))
    return v, r


def C_poly(n, x):
    """Unit 11: C = 1 - x^2/2! + x^4/4! - ..., terms up to degree n. Returns (value, rate)."""
    x = Fraction(x)
    v = sum((-1) ** (k // 2) * x ** k / factorial(k) for k in range(0, n + 1, 2))
    r = sum((-1) ** (k // 2) * k * x ** (k - 1) / factorial(k) for k in range(2, n + 1, 2))
    return v, r


def stage_for(top, tolerance):
    """Unit 12: for the rule top/n, the first whole n with top/n < tolerance."""
    top, tolerance = Fraction(top), Fraction(tolerance)
    n = top // tolerance + 1
    while Fraction(top, 1) / (n - 1) < tolerance and n > 1:
        n -= 1
    return int(n)
