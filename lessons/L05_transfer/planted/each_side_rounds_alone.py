def step(h):
    n = len(h); new = list(h)
    for i in range(n):
        j = (i + 1) % n; d = h[i] - h[j]
        new[i] -= d // 8                     # the giver lands down...
        new[j] += -((-d) // 8)               # ...the receiver lands up: units are made on every odd face
    return new
