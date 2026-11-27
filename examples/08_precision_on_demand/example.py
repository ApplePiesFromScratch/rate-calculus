# Example 08: ask for a precision, get a fraction and a proof. Change REQUEST and run again.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

REQUEST = F(1, 1000000)
print("requested precision:", show(REQUEST))
k = halving_steps_for(REQUEST)
low, high, _ = sqrt2_halving(k)
print(f"sqrt 2 by halving: {k} steps, low {show(low)}, high {show(high)}, gap {show(high - low)} < request: {high - low < REQUEST}")
print(f"  low^2 < 2 < high^2: {low * low < 2 < high * high}")
xs = sqrt2_averaging(3)
x = xs[-1]
print(f"sqrt 2 by averaging: 3 steps, {show(x)}, x^2 - 2 = {show(x * x - 2)}")
n = 0
while E_tail_bound(n) >= REQUEST:
    n += 1
v = E_poly(n, 1)[0]
print(f"e: stage {n}, value {show(v)}, proven tail bound {show(E_tail_bound(n))} < request: {E_tail_bound(n) < REQUEST}")
print(f"stage for 1/n within the request: n = {stage_for(1, REQUEST)}")
