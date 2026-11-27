# Example 16: four patterns drawing on one field, run by the six clauses of the useful pattern. Halfway, the context
# changes (the field is drained, counted). Nothing is scored by a fitness number: served, refused and reconfigured are read.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

f = Flux(400, THETA=60, KAPPA=4)
f.add("simple", C=2, cells={0, 1}, take=2, vent_num=1, vent_den=2)
f.add("venting", C=2, cells={1, 2}, take=3, vent_num=1, vent_den=4)
f.add("heavy", C=2, cells={2, 3}, take=3, vent_num=0, vent_den=1)
f.add("lonely", C=1, cells={9}, take=2, vent_num=1, vent_den=8)
print("field 400, THETA 60, KAPPA 4/16 (choices); patterns: name C take vent cells")
for q in f.p:
    print(f"  {q.name:8s} C {q.C} take {q.take} vent {q.vent_num}/{q.vent_den} cells {sorted(q.cells)}")
held = True
for k in range(1, 2001):
    if k == 1001:
        f.drain(f.field - 4)
        print("latch 1000: the context changes: the field is drained to 4 (counted as drained)")
    f.latch()
    held = held and f.books() and not f.front_moved_back
    if k in (1000, 2000):
        print(f"after {k} latches: field {f.field}, drained {f.drained}")
        for q in f.p:
            print(f"  {q.name:8s} served {q.served:4d} refused {q.refused:4d} reconfigured {q.reconfigs:3d} L {q.L:3d} vented {q.vented}")
print("books (field + every L = 400 - drained) held every latch, and the front never moved back:", held)
