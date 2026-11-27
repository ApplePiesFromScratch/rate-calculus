# Example 09: 32 places on a ring, each pulled by its two neighbours, 2000 latches out and 2000 back.
# Step:  next   = 2*now - before + push(now)
# Back:  before = 2*now - next   + push(now)        (the same line, solved for the other end)
# The push rounds (the mouth), and the rounding is the same in both directions, so whole numbers come home exactly.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

N = 32
def push_whole(now):
    return [mouth(now[(i - 1) % N] + now[(i + 1) % N] - 2 * now[i], 8) for i in range(N)]

def push_float(now):
    return [(now[(i - 1) % N] + now[(i + 1) % N] - 2 * now[i]) / 8 for i in range(N)]

def forward(before, now, push, k):
    for _ in range(k):
        p = push(now)
        before, now = now, [2 * n - b + q for n, b, q in zip(now, before, p)]
    return before, now

def back(before, now, push, k):
    for _ in range(k):
        p = push(before)
        before, now = [2 * b - n + q for b, n, q in zip(before, now, p)], before
    return before, now

start_before = [((i * 37) % 23) * 10 for i in range(N)]
start_now = [v + (i % 3) - 1 for i, v in enumerate(start_before)]

b, n = forward(start_before, start_now, push_whole, 2000)
moved = sum(1 for x, y in zip(n, start_now) if x != y)
b2, n2 = back(b, n, push_whole, 2000)
print("whole numbers:", moved, "of", N, "places moved after 2000 latches out;",
      sum(1 for x, y in zip(b2, start_before) if x == y), "of", N, "home exactly after 2000 back")
fb, fn = forward([float(v) for v in start_before], [float(v) for v in start_now], push_float, 2000)
fb2, fn2 = back(fb, fn, push_float, 2000)
print("floats:       ", sum(1 for x, y in zip(fb2, start_before) if x == y), "of", N, "home exactly;",
      sum(1 for x, y in zip(fb2, start_before) if abs(x - y) < 0.5), "within half a unit")
