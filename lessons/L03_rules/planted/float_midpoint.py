from fractions import Fraction
from math import factorial

def _need_fraction(x):
    return Fraction(x)

def sqrt2_bracket(gap):
    gap = _need_fraction(gap)
    low, high, steps = Fraction(1), Fraction(2), 0
    while high - low >= gap:
        mid = Fraction((float(low) + float(high)) / 2)
        if mid * mid > 2:
            high = mid
        else:
            low = mid
        steps += 1
    return low, high, steps

def e_within(tol):
    tol = _need_fraction(tol)
    n = 0
    while Fraction(1, factorial(n + 1)) * Fraction(n + 2, n + 1) >= tol:
        n += 1
    value = sum(Fraction(1, factorial(k)) for k in range(n + 1))
    return value, Fraction(1, factorial(n + 1)) * Fraction(n + 2, n + 1), n

def stage(top, tol):
    top, tol = _need_fraction(top), _need_fraction(tol)
    n = 1
    while top / n >= tol:
        n += 1
    return n
