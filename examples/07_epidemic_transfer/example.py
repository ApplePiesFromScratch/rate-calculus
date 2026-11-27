# Example 07: three groups of people (well, ill, recovered), moved only by transfer. Whole people, books every latch.
# The rates are choices for the demonstration (kind 2 only after they are measured): each latch, ill * well * 3 / (10 * N)
# move from well to ill, and ill * 1 / 10 move from ill to recovered. Each move is landed once (toward the more negative
# number) and applied as one take and one give.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

def run(latches, grain_num=1, grain_den=1):
    N = 10000
    well, ill, rec = N - 10, 10, 0
    books_ok = True
    peak = (0, 0)
    for k in range(latches):
        catch = (ill * well * 3 * grain_num) // (10 * N * grain_den)
        heal = (ill * grain_num) // (10 * grain_den)
        well, ill = well - catch, ill + catch           # one take, one give
        ill, rec = ill - heal, rec + heal
        books_ok = books_ok and well + ill + rec == N and min(well, ill, rec) >= 0
        if ill > peak[1]:
            peak = (k + 1, ill)
    return well, ill, rec, books_ok, peak

w, i, r, ok, peak = run(200)
print(f"grain 1: after 200 latches well {w}, ill {i}, recovered {r}; books and range held every latch: {ok}")
print(f"         peak ill {peak[1]} at latch {peak[0]}")
w, i, r, ok, peak = run(400, 1, 2)
print(f"grain 1/2: after 400 latches well {w}, ill {i}, recovered {r}; books and range held every latch: {ok}")
print(f"         peak ill {peak[1]} at latch {peak[0]} (= {show(F(peak[0], 2))} grain-1 latches)")
print("the peak moves with the grain: report it with its grain")
