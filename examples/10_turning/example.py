# Example 10: headings. Exact turns with whole numbers, composition, and three shears on a grid.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

for P, Q in [(1, 2), (2, 3), (1, 4)]:
    c, s, d = unit(P, Q)
    print(f"({P}:{Q}) -> c {c}, s {s}, d {d}; c*c + s*s == d*d: {c * c + s * s == d * d}")
h = (1, 2)
for k in range(2, 5):
    h = combine(h, (1, 2))
    c, s = heading(*h)
    print(f"(1:2) composed {k} times -> ({h[0]}:{h[1]}), unit ({show(c)}, {show(s)})")
pts = [(x, y) for x in range(-30, 31) for y in range(-30, 31)]
for P, Q in [(1, 2), (1, 4), (1, 7), (2, 5)]:
    r = len(pts) - len({turn_point_rounded(x, y, P, Q) for x, y in pts})
    s = len(pts) - len({turn_point_shears(x, y, P, Q) for x, y in pts})
    print(f"({P}:{Q}) on {len(pts)} points: rounded turn {r} collisions, three shears {s} collisions")
