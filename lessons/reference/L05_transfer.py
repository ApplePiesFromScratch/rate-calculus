def step(h):
    n = len(h); flow = [0] * n
    for i in range(n):                       # each face gives an eighth of the difference, landed toward zero
        j = (i + 1) % n; d = h[i] - h[j]
        flow[i] = int(d / 8) if abs(d) < 8 * 10**12 else d // 8
    new = list(h)
    for i in range(n):
        j = (i + 1) % n; new[i] -= flow[i]; new[j] += flow[i]
    return new
