# 14. Headings: turning exactly, with whole numbers

## The question

Guide 13's S and C have S*S + C*C at rate 0, but the value 1 is only approached as terms are added. Is there a construction where it is exactly 1, provably, with no series? And can it turn a grid of whole-number points without two points landing on one? (consolidated edition, Unit 14; Part V, Unit V7)

## The heading rule (a choice, not a discovery)

A **heading** is a pair of whole numbers, written (P : Q). It gives two fractions:

```text
c = (Q*Q - P*P) / (P*P + Q*Q)
s = 2*P*Q / (P*P + Q*Q)
```

**Why c*c + s*s is exactly 1:** (Q² − P²)² + (2PQ)² = (P² + Q²)², by expanding, for every pair. Divided by (P² + Q²)², it is 1. It is a single finite algebra fact, not approached.

heading(1, 2) = (3/5, 4/5): the 3-4-5 triangle is inside the computation.

> **A choice, not a discovery.** This is one way to turn a whole-number pair into a pair that squares to 1, picked because it matches how the 3-4-5 triangle and its relatives are built. A heading never mentions an angle. It shares a pattern with sine and cosine (c*c + s*s = 1, matching composition), not an identity: it cannot answer "what is the cosine of 30 degrees".

```check
heading(1, 2) == (F(3, 5), F(4, 5))
heading(1, 3) == (F(4, 5), F(3, 5))
heading(2, 3) == (F(5, 13), F(12, 13))
heading(2, 1) == (F(-3, 5), F(4, 5))
all(heading(P, Q)[0] ** 2 + heading(P, Q)[1] ** 2 == 1 for P in range(0, 12) for Q in range(1, 12))
unit(1, 2) == (3, 4, 5)
```

## Combining two headings

```text
P' = P1*Q2 + P2*Q1
Q' = Q1*Q2 - P1*P2
```

(1 : 2) combined with (1 : 1) gives (3 : 1), and heading(3, 1) = (−4/5, 3/5). Combining the two (c, s) pairs directly, c1c2 − s1s2 and s1c2 + c1s2, gives the same pair.

```check
combine((1, 2), (1, 1)) == (3, 1)
heading(3, 1) == (F(-4, 5), F(3, 5))
c1, s1 = heading(1, 2)
c2, s2 = heading(1, 1)
(c1 * c2 - s1 * s2, s1 * c2 + c1 * s2) == heading(3, 1)
combine((1, 2), (1, 2)) == (4, 3)
heading(4, 3) == (F(-7, 25), F(24, 25))
combine((1, 2), (1, 4)) == (6, 7)
unit(6, 7) == (13, 84, 85)
```

## A turn rate

Seed P with rate 1 and Q with rate 0. The turn rate is 2(Q·rate(P) − P·rate(Q))/(P² + Q²) = 2Q/(P² + Q²). heading(1, 2) turns at 4/5; heading(1, 1) at 1. The combined heading (3 : 1), with P' and Q' carrying their own rates from the combine rule, turns at 9/5 = 4/5 + 1. Under combining, turn rates add.

```check
P = isolate(3, 3)
Q = isolate(1, -2)
2 * (Q.value * P.rate - P.value * Q.rate) / (P.value ** 2 + Q.value ** 2) == F(9, 5)
```

*(P' = P1Q2 + P2Q1 has rate Q2 + Q1 = 3 when P1 and P2 each move at 1; Q' = Q1Q2 − P1P2 has rate −(P2 + P1) = −2.)*

## Turning every point of a grid (Part V, Unit V7)

Rounding the turned position of each point does not work in general: two points can land on one. **Three shears do:**

1. slide x by y·P/Q (landed with the mouth, guide 15);
2. slide y by x·2PQ/(P² + Q²) (landed);
3. slide x by y·P/Q again (landed).

Each slide changes one coordinate by an amount that depends only on the other, which that slide does not change. Sliding back the same amount, landed the same way, restores it exactly. So no two points can land together.

On the 61 × 61 grid (3721 points):

| heading | rounded turn | three shears |
|---|---|---|
| (1 : 2) | 0 collisions | 0 collisions |
| (1 : 4) | 860 collisions | 0 collisions |

**The trap:** (1 : 2), (2 : 3), (1 : 7) and (3 : 4) happen to lose no point when rounded. A test drawn only from that family would have passed a rounded turn. (1 : 4) shows the difference. Test with more than one family.

```check
pts = [(x, y) for x in range(-30, 31) for y in range(-30, 31)]
len(pts) - len({turn_point_rounded(x, y, 1, 4) for x, y in pts}) == 860
len(pts) - len({turn_point_shears(x, y, 1, 4) for x, y in pts}) == 0
len(pts) - len({turn_point_rounded(x, y, 1, 2) for x, y in pts}) == 0
turn_point_shears(-5, -7, 1, 4) == tuple(-v for v in turn_point_shears(5, 7, 1, 4))
```

The last line checks the mirror: turning −p gives minus the turn of p, because the mouth is mirror-true. A floor would not be.

## Steps

1. Pick whole numbers P, Q. `unit(P, Q)` gives (c, s, d) with c*c + s*s = d*d.
2. To turn a fraction pair exactly, multiply by (c/d, s/d).
3. To compose turns, combine headings (P' , Q'), never angles.
4. To turn whole-number points without collisions, use three landed shears.

## Try it yourself

1. heading(3, 4)? *Answer:* (7/25, 24/25).
2. Combine (1 : 2) with (2 : 1). *Answer:* (5 : 0), so (−1, 0): a half turn.

```check
heading(3, 4) == (F(7, 25), F(24, 25))
combine((1, 2), (2, 1)) == (5, 0)
heading(5, 0) == (-1, 0)
```

## Next

Guide 15: whole numbers.
