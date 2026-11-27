def mouth(top, den):
    if den < 0: top, den = -top, -den
    a = abs(top); q, r = divmod(a, den)
    if 2 * r > den or (2 * r == den and q % 2): q += 1
    return -q if top < 0 else q
def unit(P, Q): return (Q * Q - P * P, 2 * P * Q, P * P + Q * Q)
def compose(h1, h2):
    (P1, Q1), (P2, Q2) = h1, h2
    return (P1 * Q2 + P2 * Q1, Q1 * Q2 - P1 * P2)
def turn_point(x, y, P, Q):
    c, s, d = unit(P, Q)
    return (mouth(c * x - s * y, d), mouth(s * x + c * y, d))
def unturn_point(x, y, P, Q):
    c, s, d = unit(P, Q)
    return (mouth(c * x + s * y, d), mouth(-s * x + c * y, d))
