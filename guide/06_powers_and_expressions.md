# 06. Powers and whole expressions

## The question

What happens when you chain several mixes and adds in one expression? (book Units 4, 7; consolidated edition, "Any Number Of Mixes")

## The rule

Nothing new. Every step is guide 04's mix or guide 05's piece-by-piece add. The mix rule takes any two Readings, including Readings that came out of earlier mixes, so a longer expression is just more steps.

**Why the rate comes out exact without being asked for:** you write the steps to find a value, one move at a time. Carrying the pair through every step makes the exact rate come out alongside.

## Steps: the step table

Use a table for every expression until you can do it in your head. One row per move.

1. Write the expression with explicit moves: `x*x*x + 2*x + 1` becomes "mix x with x; mix that with x; 2 times x; add; add 1."
2. Seed the input: `x = isolate(2)` = (2, 1).
3. Do one move per row. Write the inputs, both strips for a mix, and the output pair.
4. The last row is the answer: value and rate.
5. Check the value against plain arithmetic.

**Example (book Unit 7, Demonstration 2): f = x*x*x + 2*x + 1 at x = isolate(2)**

| Step | Move | Inputs | Working | Output |
|---|---|---|---|---|
| 1 | mix | (2,1), (2,1) | value 4; strips 2, 2 | (4, 4) |
| 2 | mix | (4,4), (2,1) | value 8; strips 4*2 = 8, 4*1 = 4 | (8, 12) |
| 3 | mix with plain 2 | (2,1), (2,0) | both slots × 2 | (4, 2) |
| 4 | add | (8,12), (4,2) | slot by slot | (12, 14) |
| 5 | add plain 1 | (12,14), (1,0) | value only | (13, 14) |

Value check: 2*2*2 + 2*2 + 1 = 13. The rate, 14, came out with no extra work.

```check
x = isolate(2)
x * x == R(4, 4)
x * x * x == R(8, 12)
x * x * x + 2 * x + 1 == R(13, 14)
f = x * x + 3 * x
f == R(10, 7)
```

## Powers: any number of mixes

Mix x with itself n − 1 times and you get x to the n. At x = isolate(2) the rate is always n times 2 to the n − 1. This is **checked, not asserted**: `power(x, n)` actually runs the mixes.

| n | value | rate | n * 2^(n−1) |
|---|---|---|---|
| 2 | 4 | 4 | 4 |
| 3 | 8 | 12 | 12 |
| 4 | 16 | 32 | 32 |
| 5 | 32 | 80 | 80 |
| 6 | 64 | 192 | 192 |

```check
x = isolate(2)
all(power(x, n) == R(2 ** n, n * 2 ** (n - 1)) for n in range(2, 7))
# and at other starting values: x = 3, powers 2..10
all(power(isolate(3), n) == R(3 ** n, n * 3 ** (n - 1)) for n in range(2, 11))
# cubing: the rate is 3*x*x (book Unit 4)
power(isolate(4), 3) == R(64, 48)
power(isolate(5), 3) == R(125, 75)
```

**Why the exponent turns into a multiplier:** going from x^(n−1) to x^n multiplies the rate by x and adds one more full copy of the value. That turns "n − 1 copies" into "n copies", one mix at a time. A course calls this the power rule; here it is built before it is named.

## Try it yourself

1. f = x*x + x at x = isolate(4). *Answer:* (16, 8) + (4, 1) = (20, 9).
2. f = x*x*x at x = isolate(1). *Answer:* (1, 2), then (1, 3).
3. f = x*x*x − x at x = isolate(3). *Answer:* (27, 27) − (3, 1) = (24, 26).

```check
x = isolate(4)
x * x + x == R(20, 9)
power(isolate(1), 3) == R(1, 3)
power(isolate(3), 3) - isolate(3) == R(24, 26)
```

## Mistakes people make

- **Skipping rows.** Each skipped row is a place a strip gets lost.
- **Using a formula for the rate instead of running the moves.** The point is that the moves produce the rate; a remembered formula is a second, unchecked claim.

## Next

Guide 07: why the seed rate 1 does not matter, and what to do with every other choice you make.
