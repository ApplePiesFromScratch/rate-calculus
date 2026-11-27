# Example 15: a warm puff rising in a box of air, with no Navier-Stokes, no time step and whole numbers only.
# Every change is a trade at a face (PUSH, DRAG, EXCHANGE, MOVE) or a counted entry (LIFT's ground, FEED, VENT, WALLS).
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

def picture(b):
    """A reading for the eye: warmth above the box's mean, in five shades. The cut: the mean, the whole box."""
    tot = sum(b.w)
    shades = " .:*#"
    top = max(max(b.w[c] * b.N - tot for c in range(b.N)), 1)
    for y in range(b.H):
        row = ""
        for x in range(b.W):
            ex = b.w[b.i(x, y)] * b.N - tot
            row += shades[0] if ex <= 0 else shades[min(4, 1 + 4 * ex // (top + 1))]
        print("  |" + row + "|")

b = Box()
print(f"box {b.W} x {b.H}, stuff {b.s[0]} a place; constants KP {b.KP} KD {b.KD} KE {b.KE} KL {b.KL} KM {b.KM} (choices)")
b.puff(16, 17, 4000)
held = True
for k in range(1, 401):
    b.latch()
    held = held and all(b.books()) and b.in_range()
    if k % 50 == 0:
        print(f"latch {k:3d}: warm row {float(b.warm_row()):5.2f}  stuff {min(b.s)}..{max(b.s)}  "
              f"fed {b.fed} vented {b.vented}  turning round (15,10) {b.turning(15, 10)}")
    if k == 120:
        print("warmth above the mean at latch 120 (row 0 is the lid):")
        picture(b)
print("books (stuff, warmth, momentum x, momentum y) and range held every latch:", held)
p = Box(); p.plant = "assign"; p.puff(16, 10, 4000)
opened = None
for k in range(1, 50):
    p.latch()
    if not all(p.books()):
        opened = k; break
print("planted set (warmth halved in place, not traded): the books opened at latch", opened)
two = Box(KL=48); two.puff(16, 17, 4000)
for _ in range(150):
    two.latch()
one = Box(); one.puff(16, 17, 4000)
for _ in range(150):
    one.latch()
print(f"two cuts at latch 150: KL 24 -> warm row {float(one.warm_row()):.2f}; KL 48 -> warm row {float(two.warm_row()):.2f}; "
      f"books held in both: {all(one.books()) and all(two.books())}")
