from itertools import product

def scan_closure(Vv, Vr, mix):
    leaks = total = 0
    for v1, r1, v2, r2 in product(Vv, Vr, Vv, Vr):
        total += 1
        v, r = mix(v1, r1, v2, r2)
        if v not in Vv:
            leaks += 1
    return leaks, total

def morphism(f, rule_a, rule_b, V):
    for a, b in product(V, V):
        if f(rule_a(a, b)) != rule_b(f(a), f(b)):
            return False, (a, b)
    return True, None
