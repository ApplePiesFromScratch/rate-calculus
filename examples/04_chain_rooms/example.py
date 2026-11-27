# Example 04: rooms. Functions written for numbers, run on Readings, give exact rates through the chain.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

def room1(t): return mix(t, 2)          # u = 2t
def room2(u): return u * u              # y = u*u
def room3(y): return y + 3 * y - 7      # z = 4y - 7

t = isolate(2)
u = room1(t); y = room2(u); z = room3(y)
print("t", t, " u", u, " y", y, " z", z)
print("rate(z, t) directly:        ", show(rate(z, t)))
links = rate(z, y) * rate(y, u) * rate(u, t)
print("room by room, multiplied:   ", show(rate(z, y)), "*", show(rate(y, u)), "*", show(rate(u, t)), "=", show(links))
still = isolate(5, 0)
print("a room fed a still reading: rate(room2(still), still) =", rate(room2(still), still))
