# Example 11: a motor that takes whole steps, driven at 4/3 steps a tick. The carry against a float accumulator.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

c = Carry(4, 3)
first = "".join(str(c.tick()) for _ in range(24))
held = c.books()
for _ in range(100000 - 24):
    c.tick()
    held = held and c.books()
print("carry 4/3: first 24 ticks", first)
print(f"after 100000 ticks: count {c.count}, carry {c.acc}; d*count + carry == n*ticks and 0 <= carry < d every tick: {held}")
acc, sent, wrong = 0.0, 0, 0
exact = Carry(4, 3)
for _ in range(100000):
    acc += 4 / 3
    out = int(acc) - sent        # float: pulses = whole part of the running total, minus pulses already sent
    sent += out
    if out != exact.tick():
        wrong += 1
print(f"float accumulator: {sent} pulses after 100000 ticks, differs from the carry on {wrong} ticks")
seven = Carry(7, 3)
print("carry 7/3, ticks 1-6:", [seven.tick() for _ in range(6)], "books:", seven.books())
