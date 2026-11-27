def step(h):
    n = len(h); new = list(h)
    for i in range(n):                       # each face moves three quarters of the difference: a peak gives
        j = (i + 1) % n; d = h[i] - h[j]     # one and a half times what it holds, and the giver is never asked
        f = 3 * d // 4 if d >= 0 else -(3 * -d // 4)
        new[i] -= f; new[j] += f
    return new
