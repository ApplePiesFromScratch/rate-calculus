#!/usr/bin/env python3
"""score.py THRESHOLD [tune]: how many tuning readings a threshold gets right (label 1 when reading >= THRESHOLD).
Run it on the tuning set as often as you like. The sealed set is read only by read_sealed.py, once."""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def score(t, name):
    rows = list(csv.DictReader(open(os.path.join(HERE, "data", name + ".csv"))))
    return sum((int(r["reading"]) >= t) == (r["label"] == "1") for r in rows), len(rows)
if __name__ == "__main__":
    t = int(sys.argv[1]); right, n = score(t, "tune")
    print(f"threshold {t}: right on the tuning set {right}/{n}")
