# 04. The third move: `mix`

## The question

If two things are both changing and you combine them by multiplication, how fast does the result change? (book Unit 3)

## The picture first: the growing rectangle

A rectangle's width is growing and its height is growing, at the same time. The area gains new space from two directions:

- a thin strip along the right edge, as wide as the width is growing and as tall as the current height;
- a thin strip along the top edge, as tall as the height is growing and as wide as the current width.

Miss either strip and you have undercounted. The starting area plus exactly these two strips is what `mix` outputs.

```text
        v1 (width)          growing at r1
   +-------------------+---+
   |                   |   |  <- strip r1*v2
v2 |     v1 * v2       |   |
   |                   |   |
   +-------------------+---+
   |  strip v1*r2      |
   +-------------------+
```

## The rule (a choice, not a discovery)

```text
mix( (v1, r1), (v2, r2) )  outputs  (v1*v2,  r1*v2 + v1*r2)
```

- new value = `v1*v2` (ordinary multiplication);
- new rate = `r1*v2 + v1*r2` (the two strips, added).

This rule is **fixed once, here, and used everywhere** after. `A * B` means `mix(A, B)`: it is the only multiplication a Reading ever uses.

> **A choice, not a discovery.** Nothing outside the book forces this rule; it is picked because it counts both strips of the rectangle. What it buys: every later rate comes out exact, through any number of steps (guides 06, 08). Once it is picked, division (guide 09) and the curve rule (guide 10) are forced by it.

## Steps (do these on paper for every mix until they are automatic)

1. Write both Readings: (v1, r1) and (v2, r2).
2. New value: multiply the values, v1*v2.
3. First strip: r1*v2 (the first one's rate, spread across the second one's value).
4. Second strip: v1*r2 (the other way round).
5. New rate: add the two strips.
6. Write the output pair.

## Worked examples (book Unit 3)

`x = isolate(4)`, so x = (4, 1). `mix(x, x)`: value 4*4 = 16; strips 1*4 = 4 and 4*1 = 4; rate 8. Output (16, 8). `rate(mix(x, x), x)` = 8/1 = 8.

`x = isolate(3)`: value 9; strips 3 and 3; rate 6. Output (9, 6).

**Notice:** seeded with rate 1, both strips equal the value itself, so the rate is always double the value fed in.

```check
x = isolate(4)
mix(x, x) == R(16, 8)
x * x == R(16, 8)
rate(x * x, x) == 8
y = isolate(3)
y * y == R(9, 6)
rate(y * y, y) == 6
z = isolate(6)
z * z == R(36, 12)
# two different readings
mix(isolate(5, 2), isolate(3, -1)) == R(15, 2*3 + 5*(-1))
```

## Why not just multiply the two rates?

For x = isolate(3) that would give 1*1 = 1. The real output is 6. Multiplying the rates throws away both strips. `tools/check_all.py` plants exactly this mistake (`RC_PLANT=mix-rate-product`) and confirms that the checks catch it.

```check
isolate(3) * isolate(3) != R(9, 1)
```

## Try it yourself

For each, find `mix(x, x)` and `rate(mix(x, x), x)`, showing both strips:

1. x = isolate(7). *Answer:* strips 7 and 7; (49, 14); 14.
2. x = isolate(9). *Answer:* (81, 18); 18.
3. Predict `rate(mix(x, x), x)` for x = isolate(12), then check. *Answer:* 24.

## Mistakes people make

- **Forgetting a strip.** The rate has two terms, always.
- **Using a different multiplication somewhere later** (for instance, multiplying values only). Once you pick the mix rule, it is the rule for every product.
- **Mixing a plain number as if it had rate 1.** A plain number has rate 0 (guide 05).

## Next

Guide 05: adding, subtracting, and plain numbers.
