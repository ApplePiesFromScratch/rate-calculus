def step(h):
    n = len(h)
    return [(h[(i - 1) % n] + 2 * h[i] + h[(i + 1) % n]) // 4 for i in range(n)]
