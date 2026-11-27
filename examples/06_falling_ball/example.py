# Example 06: a ball dropped from 80 m, stepped in latches with no time variable. Two grains, and the books.
# Model (kind 2: checked by dropping balls; it ignores air): speed gains 49/5 m/s per second; place gains speed.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

def drop(grain):
    """grain = seconds one latch stands for (a cut). Order inside a latch (a choice): speed first, then place."""
    height, speed, latches = F(80), F(0), 0
    while height > 0:
        speed += F(49, 5) * grain
        height -= speed * grain
        latches += 1
    return latches, height, speed

for grain in (F(1, 10), F(1, 100)):
    n, h, s = drop(grain)
    print(f"grain {show(grain)} s: lands after {n} latches = {show(n * grain)} s, height {show(h)} m, speed {show(s)} m/s")
# The same question asked by reading 'when' off the height, first order: re-read every latch.
h = isolate(80, 0)
print("at the drop, when(height) =", when(h), "- the ball is not moving yet: nothing to read")
h = R(F(751, 10), -F(49, 5))
print("one second in: height", h, "- first-order when =", show(when(h)), "s from here; the speed keeps growing, so read again next latch")
