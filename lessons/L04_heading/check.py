#!/usr/bin/env python3
"""L04 check: a direction as two whole numbers (P : Q). Exact unit, exact composition, and an exact turn of the
whole-number plane by three shears that loses no point.

  python3 lessons/L04_heading/check.py             # checks lessons/work/L04_heading.py
  python3 lessons/L04_heading/check.py --planted
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
import harness
TASK = "L04_heading"
HERE = os.path.dirname(os.path.abspath(__file__))
HEADINGS = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 7), (5, 12), (2, 1), (-1, 2), (1, -3)]


def check(path):
    m = harness.load_module(path)
    R = []
    def add(name, bad, detail=""):
        R.append((name, bad == 0, f"{bad} {detail}".strip()))
    try:
        add("unit(1, 2) = (3, 4, 5)", int(tuple(m.unit(1, 2)) != (3, 4, 5)), str(m.unit(1, 2)))
        bad = 0
        for P in range(-12, 13):
            for Q in range(-12, 13):
                if P or Q:
                    c, s, d = m.unit(P, Q)
                    bad += c * c + s * s != d * d or not all(isinstance(v, int) for v in (c, s, d))
        add("c*c + s*s == d*d, whole numbers, on all 624 headings in -12..12", bad, "failed")
        bad = 0
        for h1 in HEADINGS:
            for h2 in HEADINGS:
                c1, s1, d1 = m.unit(*h1); c2, s2, d2 = m.unit(*h2); c, s, d = m.unit(*m.compose(h1, h2))
                bad += (c, s, d) != (c1 * c2 - s1 * s2, s1 * c2 + c1 * s2, d1 * d2)
        add("compose agrees with turning the units, exactly, on 100 pairs", bad, "disagree")
        add("(1:2) then (1:2) is (4:3)", int(tuple(m.compose((1, 2), (1, 2))) != (4, 3)), str(m.compose((1, 2), (1, 2))))
        box = [(x, y) for x in range(-30, 31) for y in range(-30, 31)]
        # (1:2), (2:3), (1:7), (3:4) alone would not catch a rounded rotation: for that family rounding is a bijection
        # (found while planting faults for this task, 25 Nov 2026; see README). (1:4), (2:5), (1:6), (4:9) are outside it.
        for P, Q in ((1, 2), (1, 4), (2, 5), (1, 6), (4, 9)):
            img = [tuple(m.turn_point(x, y, P, Q)) for x, y in box]
            c, s, d = m.unit(P, Q)
            add(f"({P}:{Q}) turn loses no point: {len(box)} points, {len(box)} images", len(box) - len(set(img)), "collisions")
            add(f"({P}:{Q}) unturn(turn(p)) == p", sum(tuple(m.unturn_point(*m.turn_point(x, y, P, Q), P, Q)) != (x, y) for x, y in box), "not home")
            add(f"({P}:{Q}) turn(-p) == -turn(p)", sum(tuple(m.turn_point(-x, -y, P, Q)) != (-a, -b) for (x, y), (a, b) in zip(box, img)), "mirror fails")
            add(f"({P}:{Q}) each image within 2 units of (c x - s y, s x + c y)/d", sum(abs(a * d - (c * x - s * y)) > 2 * d or abs(b * d - (s * x + c * y)) > 2 * d for (x, y), (a, b) in zip(box, img)), "too far")
    except Exception as e:
        R.append(("ran without raising", False, repr(e)[:120]))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, os.path.join(harness.LESSONS, "work", "L04_heading.py"), os.path.join(HERE, "planted"))
