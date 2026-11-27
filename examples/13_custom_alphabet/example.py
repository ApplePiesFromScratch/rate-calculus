# Example 13: design an alphabet and a mixing rule that spell a picture (TSUZURI, in small).
# Each cell below row 0 must be MIX(left, middle, right) of the three letters above it: one table for every row.
# Start with the alphabet = the two colours. Where one triple must give two different children (a conflict), split the
# middle parent's letter by its child (forced). Then merge letters of one colour while the table stays a function (greedy).
# Certify: play MIX from the seed row and compare every cell's colour with the target.
import sys
W, H = 24, 12
EDGE = -1

def target(name):
    if name == "XOR":
        t = [[0] * W for _ in range(H)]; t[0][W // 2] = 1
        for r in range(1, H):
            for x in range(W):
                t[r][x] = (t[r - 1][x - 1] if x else 0) ^ (t[r - 1][x + 1] if x < W - 1 else 0)
        return t
    if name == "DISC":
        return [[1 if (2 * x - 23) ** 2 + (2 * r - 11) ** 2 <= 10 ** 2 else 0 for x in range(W)] for r in range(H)]
    return [[1 if ((x - 12) ** 2 + (r - 6) ** 2) // 12 % 2 else 0 for x in range(W)] for r in range(H)]   # RINGS

def build(L):
    table, conflict = {}, None
    for r in range(1, H):
        for x in range(W):
            key = (L[r - 1][x - 1] if x else EDGE, L[r - 1][x], L[r - 1][x + 1] if x < W - 1 else EDGE)
            if key in table and table[key][0] != L[r][x]:
                conflict = conflict or (r, x)
            table.setdefault(key, (L[r][x], (r, x)))
    return table, conflict

def design(T, plant=False):
    L = [row[:] for row in T]                      # the alphabet starts as the colours
    colour = {0: 0, 1: 1}
    nxt = 2
    table, conflict = build(L)
    while conflict:
        r, x = conflict
        m = L[r - 1][x]                            # the middle parent's letter learns its future
        groups = {}
        cells = [(rr, xx) for rr in range(H - 1) for xx in range(W) if L[rr][xx] == m]
        for rr, xx in cells:
            groups.setdefault(L[rr + 1][xx], []).append((rr, xx))
        if len(groups) > 1:
            for k, (child, cs) in enumerate(sorted(groups.items())):
                if k == 0:
                    continue
                for rr, xx in cs:
                    L[rr][xx] = nxt
                colour[nxt] = colour[m]; nxt += 1
        else:
            L[r - 1][x] = nxt; colour[nxt] = colour[m]; nxt += 1
        table, conflict = build(L)
    refined = len(set(v for row in L for v in row))
    # squeeze: merge b into an earlier letter a of the same colour if the table stays a function
    letters = sorted(set(v for row in L for v in row))
    for b in reversed(letters):
        for a in letters:
            if a >= b or colour[a] != colour[b] or not any(b in row for row in L) or not any(a in row for row in L):
                continue
            trial = [[a if v == b else v for v in row] for row in L]
            if plant or build(trial)[1] is None:   # PLANT: keep the merge untested
                L = trial
                break
    table, _ = build(L)
    squeezed = len(set(v for row in L for v in row))
    # play from the seed row
    row = L[0][:]
    match = sum(1 for x in range(W) if colour[row[x]] == T[0][x])
    for r in range(1, H):
        new = []
        for x in range(W):
            key = (row[x - 1] if x else EDGE, row[x], row[x + 1] if x < W - 1 else EDGE)
            new.append(table[key][0] if key in table else 0)
        row = new
        match += sum(1 for x in range(W) if colour[row[x]] == T[r][x])
    return refined, squeezed, len(table), match

plant = "--plant" in sys.argv
for name in ("XOR", "DISC", "RINGS"):
    T = target(name)
    conflicts = 0
    tbl = {}
    for r in range(1, H):
        for x in range(W):
            key = (T[r - 1][x - 1] if x else EDGE, T[r - 1][x], T[r - 1][x + 1] if x < W - 1 else EDGE)
            if key in tbl and tbl[key] != T[r][x]:
                conflicts += 1
            tbl.setdefault(key, T[r][x])
    refined, squeezed, entries, match = design(T, plant)
    verdict = "CERTIFIED" if match == W * H else "FAILED"
    print(f"{name:5s}: colours-alone conflicts {conflicts:3d}, letters refined {refined:3d}, squeezed {squeezed:3d}, "
          f"MIX entries {entries:3d}, play {match}/{W * H} {verdict}")
