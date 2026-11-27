from fractions import Fraction as F
class _Theta:
    def __repr__(self): return "THETA"
THETA = 0
def _f(v):
    if isinstance(v, float): raise TypeError("no fraction from a float")
    return F(v)
def isolate(v, r=1): return (_f(v), _f(r))
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def mix(a, b): return (a[0] * b[0], a[1] * b[0] + a[0] * b[1])
def div(a, b):
    if b[0] == 0: return THETA
    q = a[0] / b[0]
    return (q, (a[1] * b[0] - b[1] * a[0]) / (b[0] * b[0]))
def rate(a, b): return THETA if b[1] == 0 else a[1] / b[1]
def when(g): return THETA if g[1] == 0 else -g[0] / g[1]
