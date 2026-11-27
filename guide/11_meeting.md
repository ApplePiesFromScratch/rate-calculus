# 11. When two moving things meet

## The question

Given two moving things, each a Reading, can you find out whether and when they meet, using only subtraction and division, and with no independent variable? (consolidated edition, Unit 9)

## The gap

Subtract one Reading from the other, piece by piece (guide 05). The **gap** is just another Reading.

Car A at 0 moving 5; car B at 10 moving −3:

```text
A = isolate(0, 5)       B = isolate(10, -3)
gap = B - A = (10, -8)
```

The gap's value, 10, is how far apart they are. Its rate, −8, says the gap is closing under this naming. Name it A − B and both slots flip sign; the meeting does not move (guide 07).

## The rule: read `when` off the gap

```text
when = -value / rate
```

`when` is a number read from the gap itself: how many latches (counted in whatever unit the rates are counted per) until the gap's value runs out at its current rate. Nothing is stepped through it; no variable runs.

For gap (10, −8): when = −10/−8 = 5/4.

**Check:** after 5/4 latches at rate −8, the gap has moved −8 × 5/4 = −10, which uses up the 10. The check is a product of two readings, not a function of a variable.

**Why divide the gap's rate by its own value:** comparing the gap with A or B would answer a question about two different things. The gap against itself answers "how fast is it closing, compared with how much is left", which is when it runs out. `grow = rate / value = −4/5` is that comparison, and `when` is its reciprocal with the sign kept: 1/(4/5) = 5/4. It is not 10/(4/5) = 12.5.

**Two refusals:**

- If the gap's rate is 0, nothing is closing: `when` is `theta`.
- A negative `when` means the gap is opening under the current rates; they met that many latches *before* this reading, or never will.

**First order:** `when` reads the rates as they are now (house rule 10). If either thing speeds up or slows down, read again at the next step. Do not carry the old `when` forward as a constant.

```check
A = isolate(0, 5)
B = isolate(10, -3)
g = gap(B, A)
g == R(10, -8)
when(g) == F(5, 4)
g.value + when(g) * g.rate == 0
grow(g) == F(-4, 5)
when(gap(isolate(20, -2), isolate(0, 2))) == 5
when(gap(isolate(5, 1), isolate(5, 1))) == THETA
when(gap(isolate(10, 3), isolate(0, 1))) == -5
```

## Two directions: closest approach

On a plane, take a gap in each direction, gx and gy. The squared distance between the two movers, as a Reading, is gx*gx + gy*gy. Its rate is 0 at the closest approach. That gives:

```text
when_closest = -(gx.value*gx.rate + gy.value*gy.rate) / (gx.rate² + gy.rate²)
```

Then read each gap's value at that `when` and add the squares. No square root is needed: "do they come within 5?" is answered by comparing the squared distance with 5*5, exactly.

**A genuine meeting:** A at (0, 0) moving (1, 0); B at (10, 0) moving (−1, 0). gx = (10, −2), gy = (0, 0). when = 5; squared distance 0.

**A near miss:** A at (0, 0) moving (1, 0); B at (5, 5) moving (−1, 0). gx = (5, −2), gy = (5, 0). when = 5/2; the gap there is (0, 5); squared distance 25. They never meet; the closest they come is a distance whose square is exactly 25.

```check
closest(R(10, -2), R(0, 0)) == (5, 0)
closest(R(5, -2), R(5, 0)) == (F(5, 2), 25)
closest(R(10, -2), R(5, -2)) == (F(15, 4), F(25, 2))
# the squared distance as a Reading has rate 0 at that when
gx = R(5, -2)
gy = R(5, 0)
w = closest(gx, gy)[0]
gxw = R(gx.value + w * gx.rate, gx.rate)
gyw = R(gy.value + w * gy.rate, gy.rate)
(gxw * gxw + gyw * gyw).rate == 0
```

## Steps

1. Write each mover as a Reading per direction.
2. Subtract to get the gap in each direction.
3. One direction: `when = −value / rate`; refuse on rate 0.
4. Two directions: compute `when_closest`, then the squared distance there.
5. Say which naming and which unit the latches are counted in.

## Try it yourself

1. A = isolate(0, 3), B = isolate(30, −7). *Answer:* gap (30, −10); when 3.
2. A = isolate(5, 1), B = isolate(5, −1). *Answer:* gap (0, −2); when 0: they are together at this reading.
3. A at (0, 0) moving (2, 0); B at (8, 6) moving (−2, 0). *Answer:* gx (8, −4), gy (6, 0); when 2; squared distance 36.

```check
when(gap(isolate(30, -7), isolate(0, 3))) == 3
when(gap(isolate(5, -1), isolate(5, 1))) == 0
closest(R(8, -4), R(6, 0)) == (2, 36)
```

## Mistakes people make

- **Writing `10 + t*(-8) = 0` and solving for t.** Same number, but it brings in a free-running variable. Read `when` off the gap instead.
- **Taking a square root to compare distances.** Compare squares.

## Next

Guide 12: numbers that are not fractions.
