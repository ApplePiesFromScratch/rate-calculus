def mouth(n, d):
    neg = n < 0; m = -n if neg else n
    q, r = divmod(m, d)
    if 2 * r > d or (2 * r == d and q % 2 == 1):
        q += 1
    return -q if neg else q

def step(s, m):
    """One latch on a ring: PUSH by shared crowding, DRAG, EXCHANGE and MOVE, all read from the latch as found."""
    N = len(s)
    ds, dm = [0] * N, [0] * N
    for a in range(N):
        b = (a + 1) % N
        t = mouth((s[a] + s[b]) * 6, 32); dm[a] -= t; dm[b] += t                     # PUSH
        t = mouth((m[a] - m[b]) * 2, 16); dm[a] -= t; dm[b] += t                     # DRAG
        f = mouth((s[a] - s[b]) * 1, 16) + mouth((m[a] + m[b]) * 1, 8)               # EXCHANGE + MOVE
        if f:
            d, r = (a, b) if f > 0 else (b, a)
            f = min(abs(f), s[d] // 8)
            if f:
                cm = mouth(m[d] * f, s[d])
                ds[d] -= f; ds[r] += f; dm[d] -= cm; dm[r] += cm
    out_m = [m[i] + dm[i] for i in range(N)]
    out_m[28] = out_m[28] // 2      # a set, not a trade (off the bump's centre, where momentum is not 0)
    return [s[i] + ds[i] for i in range(N)], out_m
