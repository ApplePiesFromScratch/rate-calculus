# 10. A rate that has its own rate

## The question

The rate slot says how fast a value is changing. Can the rate itself be changing, and does the machine need a new rule to track it? (consolidated edition, Unit 8)

## Extend the pair to a triple

Write `(value, rate, curve)`, where **curve** is the rate of the rate (a car's speeding up or slowing down). Seed x as (v, 1, 0): x's rate against itself is 1, and the constant 1 has no rate of its own, so its curve is 0.

## Finding the curve rule, not guessing it

The value and rate slots still follow the mix rule. For the curve, ask for the rate of the rate: apply the mix rule a second time, to each strip separately.

```text
new rate = r1*v2 + v1*r2                     (the two strips)

rate of (r1*v2) = c1*v2 + r1*r2              (c1 is r1's own rate)
rate of (v1*r2) = r1*r2 + v1*c2              (c2 is r2's own rate)

new curve = c1*v2 + 2*r1*r2 + v1*c2
```

No new rule was written: it is the mix rule used twice. **The curve rule is forced** once the mix rule is fixed.

```text
mix( (v1,r1,c1), (v2,r2,c2) ) = ( v1*v2,  r1*v2 + v1*r2,  c1*v2 + 2*r1*r2 + v1*c2 )
```

**Why the 2 on the middle term:** each strip contributes one r1*r2 when you take its rate, and there are two strips.

## Steps

1. Seed with `isolate3(v)` = (v, 1, 0).
2. Mix exactly as before for value and rate.
3. For the curve: c1*v2, plus 2*r1*r2, plus v1*c2.
4. Check the value against plain arithmetic.

## Worked example: x*x*x at x = isolate3(3)

- Step 1, x*x: value 9; rate 3 + 3 = 6; curve 0 + 2·1·1 + 0 = 2. Output (9, 6, 2).
- Step 2, (9, 6, 2) × (3, 1, 0): value 27; rate 18 + 9 = 27; curve 2·3 + 2·6·1 + 9·0 = 18. Output (27, 27, 18).

A course would call 18 the second derivative of x cubed at 3 (6 × 3).

```check
x = isolate3(3)
x * x == Triple(9, 6, 2)
x * x * x == Triple(27, 27, 18)
y = isolate3(2)
y * y * y == Triple(8, 12, 12)
z = isolate3(4)
z * z == Triple(16, 8, 2)
w = isolate3(5)
w * w * w == Triple(125, 75, 30)
```

## Try it yourself

1. x = isolate3(4): x*x? *Answer:* (16, 8, 2).
2. x = isolate3(5): x*x*x? *Answer:* (125, 75, 30). The curve is 6 × 5.

## Mistakes people make

- **Dropping the 2.** The middle term comes from both strips.
- **Seeding the curve with 1.** The seed's rate is the constant 1, whose own rate is 0.

## Next

Guide 11: finding when two moving things meet.
