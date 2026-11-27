# Example 03: a step table for any expression, printed one move a row.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

def table(title, x, steps):
    print(title)
    vals = {"x": x}
    for k, (name, op, a, b) in enumerate(steps, 1):
        A = vals[a] if isinstance(a, str) else const(a)
        B = vals[b] if isinstance(b, str) else const(b)
        out = {"mix": lambda: A * B, "add": lambda: A + B, "sub": lambda: A - B, "div": lambda: A / B}[op]()
        vals[name] = out
        print(f"  {k}. {name} = {op}({A}, {B}) -> {out}")
    return out

f = table("f = x*x*x + 2*x + 1 at x = (2, 1)", isolate(2),
          [("xx", "mix", "x", "x"), ("xxx", "mix", "xx", "x"), ("2x", "mix", "x", 2), ("s", "add", "xxx", "2x"), ("f", "add", "s", 1)])
print("  value check: 2*2*2 + 2*2 + 1 =", 2 * 2 * 2 + 2 * 2 + 1)
g = table("g = (x*x + 1) / (x - 1) at x = (3, 1)", isolate(3),
          [("xx", "mix", "x", "x"), ("top", "add", "xx", 1), ("bot", "sub", "x", 1), ("g", "div", "top", "bot")])
print("  multiply back:", (isolate(3) - 1) * g)
h = table("h = 1 / (x - 3) at x = (3, 1)", isolate(3), [("bot", "sub", "x", 3), ("h", "div", 1, "bot")])
