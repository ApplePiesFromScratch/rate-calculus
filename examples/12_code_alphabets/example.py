# Example 12: code as alphabets and mixing rules. One expression, five alphabets; division rules; collisions; a Reading carry.
from fractions import Fraction
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

def f(x): return x * x - x

print("f(x) = x*x - x")
print("  fractions  f(3)   =", f(Fraction(3)))
print("  Readings   f(3)   =", f(isolate(3)), "(value, rate)")
print("  uint8      f(20)  =", f(20) % 256, " (380 wrapped mod 256)")
print("  booleans   f(b)   =", [(b * b - b) % 2 for b in (0, 1)], "for b = 0, 1 (x*x = x: the polynomial collapses)")
print("  floats     f(0.1) =", repr(f(0.1)), " fractions f(1/10) =", f(Fraction(1, 10)))
print("(0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3) in floats:", (0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3))
print("-7 / 2 landed: Python //", -7 // 2, " C toward zero", toward_zero(-7, 2), " mouth", mouth(-7, 2))
for name, rule in [("x + x", lambda v: v + v), ("x * 5", lambda v: v * 5), ("x >> 1", lambda v: v >> 1),
                   ("x ^ (x >> 3)", lambda v: v ^ (v >> 3)), ("x & 15", lambda v: v & 15)]:
    n = collisions(rule)
    print(f"  uint8 {name:12s} {n:3d} of 256 distinct outputs: {'one-to-one' if n == 256 else 'loses information'}")

def price_with_tax(p, qty, tax): return p * qty * (1 + tax)
t = price_with_tax(source("p", F(1999, 100)), source("qty", 3), source("tax", F(15, 100)))
print("lever through code: total", show(t.value), " rate per p", show(t.rate_of("p")), " per qty", show(t.rate_of("qty")),
      " per tax", show(t.rate_of("tax")))
def clipped(x): return x if x.value < 10 else const(10)
print("a branch reads the value: clipped at 9 ->", clipped(isolate(9)), " at 11 ->", clipped(isolate(11)), "(a rate per branch)")
