# Falsifiers

A claim here is only as good as the line that would kill it. Each line below is run by `tools/check_docs.py`; if any one fails, the story built on it is wrong and the guides that lean on it must be re-read.

| claim | dies if | guide |
|---|---|---|
| rate(x*x, x) at 3 is 6 | the result is not 6 | 04 |
| the seed cancels | any seed in the list gives another rate | 07 |
| a rate against a still reading refuses | it returns a number | 03 |
| division is forced by mix | multiplying back does not rebuild the dividend | 09 |
| x4 of the averaging rule is within 1/221682772224 of √2 (squared) | the gap is anything else | 12 |
| e's tail after P(6) is at most 1/4410 | the bound is anything else | 13 |
| a heading's c*c + s*s is exactly 1 | any heading in the grid fails | 14 |
| three shears lose no point; rounding loses 860 for (1 : 4) on 61 × 61 | either count moves | 14 |
| the carry at 4/3 sends 133,333 pulses in 100,000 ticks with the books held | the count or the books move | 15 |
| the flow box keeps stuff, warmth and momentum books exactly | any book opens in 300 latches | 28 |
| a planted set opens the flow books at once | it does not | 28 |
| the pattern flux keeps field + every L = G0 | the sum opens | 26 |
| an empty certificate grid is UNPAID | it reads as paid | 20 |

```check
rate(isolate(3) * isolate(3), isolate(3)) == 6
all(rate(isolate(3, k) * isolate(3, k), isolate(3, k)) == 6 for k in [1, 2, F(1, 2), 10, F(1, 3), -1, F(7, 9)])
rate(isolate(8, 2), isolate(15, 0)) == THETA
x = isolate(3)
q = (x * x + 1) / (x - 1)
(x - 1) * q == x * x + 1
sqrt2_averaging(4)[-1] ** 2 - 2 == F(1, 221682772224)
E_tail_bound(6) == F(1, 4410)
all(heading(P, Q)[0] ** 2 + heading(P, Q)[1] ** 2 == 1 for P in range(12) for Q in range(1, 12))
pts = [(a, b) for a in range(-30, 31) for b in range(-30, 31)]
len(pts) - len({turn_point_shears(a, b, 1, 4) for a, b in pts}) == 0
len(pts) - len({turn_point_rounded(a, b, 1, 4) for a, b in pts}) == 860
c = Carry(4, 3)
all(c.tick() is not None and c.books() for _ in range(100000)) and c.count == 133333
bx = Box()
do bx.puff(16, 17, 4000)
all(bx.latch() is None and all(bx.books()) for _ in range(300))
pb = Box()
pb.plant = "assign"
do pb.puff(16, 10, 4000)
do pb.latch()
not all(pb.books())
f = Flux(400)
do f.add("a", C=2, cells={0}, take=2, vent_num=1, vent_den=2)
do f.add("b", C=1, cells={0}, take=3, vent_num=0, vent_den=1)
all(f.latch() is None and f.books() for _ in range(1000))
certify(lambda z: z * z, 3, values=()).tier == "UNPAID"
```

Not claimed here, so not falsified here: that the flow box solves the Navier–Stokes equations; that the pattern's rules are how anything ultimately is; that a green check is a floor under arithmetic.
