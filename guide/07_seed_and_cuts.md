# 07. The seed cancels, and every choice is a cut

## The question

`isolate(5)` used seed rate 1. Would a different seed change later answers? And what about every other choice you make: names, directions, scales? (book Unit 5; Part V, Unit V3)

## Part 1: the seed cancels (book Unit 5)

Test it instead of assuming it. Seed x = isolate(5, s) for four seeds:

| seed | x | x*x | rate(x*x, x) |
|---|---|---|---|
| 1 | (5, 1) | (25, 10) | 10 |
| 2 | (5, 2) | (25, 20) | 10 |
| 3 | (5, 3) | (25, 30) | 10 |
| 10 | (5, 10) | (25, 100) | 10 |

The rate slot inside x*x changes every time. `rate(x*x, x)` does not move.

**Why:** `rate` divides x*x's rate slot by x's rate slot. The seed lands in both the top and the bottom in matching amounts, and cancels. Doubling the top and bottom of a fraction together does not change it.

```check
all(rate(isolate(5, s) * isolate(5, s), isolate(5, s)) == 10 for s in [1, 2, 3, 10, F(1, 3), -7])
x = isolate(6, F(1, 3))
x * x == R(36, 4)
rate(x * x, x) == 12
```

**What this tells you to do:** ask questions as `rate(A, B)`, comparisons between two Readings that share the same seed. A raw rate slot on its own (the 20 or the 100 above) belongs to the seed as much as to the quantity.

## Part 2: every choice an observer makes is a cut (Part V, Unit V3)

The same test works on every choice you make while setting up a problem. Each choice is a **cut**: a naming, a direction, a seed, a grain, a scale.

**Example:** car A at 0 moving 5; car B at 10 moving −3. Three readings are taken under five cuts.

- `rate(rope, A)`: the rope's rate against A's.
- `grow = rope rate / rope value`.
- `rate(B, A)`.

| Cut | A | B | rope | rate(rope, A) | grow | rate(B, A) | when |
|---|---|---|---|---|---|---|---|
| named A − B | (0, 5) | (10, −3) | (−10, 8) | 8/5 | −4/5 | −3/5 | 5/4 |
| named B − A | (0, 5) | (10, −3) | (10, −8) | −8/5 | −4/5 | −3/5 | 5/4 |
| road pointed the other way | (0, −5) | (−10, 3) | B − A = (−10, 8) | −8/5 | −4/5 | −3/5 | 5/4 |
| seed −1 (every rate negated) | (0, −5) | (10, 3) | B − A = (10, 8) | −8/5 | 4/5 | −3/5 | −5/4 |
| everything scaled by 3 | (0, 15) | (30, −9) | B − A = (30, −24) | −8/5 | −4/5 | −3/5 | 5/4 |

- **`rate(rope, A)` moves** when the ends are renamed.
- **`grow` and `when` move with the seed**, because they count per latch: negate every rate and the count runs the other way.
- **`rate(B, A)` moves with none of them.** It is a comparison of two readings under the same cuts.

```check
A = isolate(0, 5)
B = isolate(10, -3)
rate(A - B, A) == F(8, 5)
rate(B - A, A) == F(-8, 5)
grow(A - B) == F(-4, 5)
grow(B - A) == F(-4, 5)
when(B - A) == F(5, 4)
when(A - B) == F(5, 4)
rate(B, A) == F(-3, 5)
# seed -1
A2 = isolate(0, -5)
B2 = isolate(10, 3)
grow(B2 - A2) == F(4, 5)
when(B2 - A2) == F(-5, 4)
rate(B2, A2) == F(-3, 5)
# scaled by 3
A3 = isolate(0, 15)
B3 = isolate(30, -9)
rate(B3, A3) == F(-3, 5)
grow(B3 - A3) == F(-4, 5)
when(B3 - A3) == F(5, 4)
```

## Units are a cut too

Measure the same bathtub in litres instead of gallons and every rate number moves; the comparison you meant does not, once both readings use the same unit. A rate number without its unit belongs to the unit.

```check
tub_gal = isolate(8, 2)
clock_min = isolate(0, 1)
clock_s = isolate(0, 60)
rate(tub_gal, clock_min) == 2
rate(tub_gal, clock_s) == F(1, 30)
```

## Two different makings, one pair: grow the alphabet before calling them the same

x*x at x = isolate(3) gives (9, 6). 3*x at x = isolate(3, 2) also gives (9, 6). Same pair, different makings. Calling them "the same" because the pair matches merges two rules. Before calling two presentations one rule, grow the alphabet (test more points, more seeds, a third slot) until they either keep agreeing or split. Here they split as soon as a second point is tried:

```check
isolate(3) * isolate(3) == R(9, 6)
3 * isolate(3, 2) == R(9, 6)
isolate(4) * isolate(4) != 3 * isolate(4, 2)
```

Equality is a scale: it says the readings agree **on the dimensions weighed**. Say which ones.

## The rule

> **No reading is believed until it has been taken at two cuts.** A number that moves when you change a cut belongs to the cut as much as to the thing (Part V, Unit V3).

## Steps: the two-cut test

1. List the choices you made: names, the order of subtraction, which way is positive, the seed, the units, the grain (how finely you counted), where you measured.
2. Pick at least two of them and change each one.
3. Recompute the reading.
4. A reading that does not move is about the situation. A reading that moves is partly about your choice; report it together with the cut ("grow = −4/5 per latch, seed +1").

## Grain is a cut too

The same turning was counted at seven grains (Part V, Unit V3): the peak count was 16 at fine grains, then 32, 104, 62, 31 and 32 at coarse grains. At coarse grains, the counting rule counted the stairs of the landed staircase. Read at one grain, 104 would have been reported as a fact about the turning.

## Try it yourself

1. Scale every place and rate by 3. Which of `rate(B, A)`, `grow` and `when` move? *Answer:* none: each is a ratio of two quantities scaled together.
2. Name two cuts a thermometer imposes on "the temperature of the room." *Answer:* for example, where it sits, how long it averages, its scale.

## Mistakes people make

- **Reporting a raw rate slot** (it carries the seed).
- **Testing at one cut and calling the number a property.**

## Next

Guide 08: chains, where one quantity depends on another.
