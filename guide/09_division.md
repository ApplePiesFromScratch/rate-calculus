# 09. Division, derived, and how far the machine reaches

## The question

Which functions can the machine handle exactly, and where does it stop? (book Unit 8)

## The rule is derived, not picked

Division undoes multiplication. So whatever the quotient (q, s) is, multiplying it by the divisor must rebuild the dividend:

```text
(v2, r2) * (q, s) = (v1, r1)
mix rule on the left:  (v2*q,  r2*q + v2*s) = (v1, r1)
first slots:   v2*q = v1                 so  q = v1 / v2
second slots:  r2*q + v2*s = r1          so  s = (r1 - r2*q) / v2
                                              = (r1*v2 - r2*v1) / v2²
```

Only the mix rule was picked (guide 04). Requiring that division undo it leaves no freedom. **This rule is forced.** It needs v2 ≠ 0, for the same reason ordinary division does.

## The edge: the divisor's value is 0

`1/x` at x = (0, 1): q = 1/0. No answer. The machine refuses with **`no quotient`**. Nothing can be adjusted to fix this, because ordinary division by 0 has no answer either.

Note the difference from `theta`: `theta` is a *rate* against a still Reading (rate slot 0); `no quotient` is a *division* by a Reading whose *value* is 0.

## Steps

1. Write dividend (v1, r1) and divisor (v2, r2).
2. If v2 = 0, the answer is `no quotient`. Stop and say so.
3. q = v1/v2.
4. s = (r1*v2 − r2*v1) / v2².
5. **Check by multiplying back:** divisor × (q, s) must give the dividend exactly. Always do this; it costs one mix.

## Worked examples (book Unit 8)

```check
# 1/x at x = (3, 1)
one_over_x = const(1) / isolate(3)
one_over_x == R(F(1, 3), F(-1, 9))
isolate(3) * one_over_x == R(1, 0)
# (x*x + 1) / (x - 1) at x = (3, 1)
x = isolate(3)
(x * x + 1) / (x - 1) == R(5, F(1, 2))
# divide (6, 4) by (2, 0)
R(6, 4) / R(2, 0) == R(3, 2)
R(2, 0) * R(3, 2) == R(6, 4)
# the edge
const(1) / isolate(0) == NO_QUOTIENT
```

## What the machine reaches

Combine +, −, ×, ÷ as often as you like, starting from x and constants, and the machine reports an exact value and an exact rate at every point where no divisor's value is 0.

Three kinds of question sit outside that reach, each with its own guide. None needs anything beyond the machine already built:

1. what number squares to 2 (guide 12);
2. what function's rate always equals its own value (guide 13);
3. what pair of functions have rates that feed each other (guide 13).

## Try it yourself

1. (10, 5) ÷ (5, 0). *Answer:* (2, 1).
2. 1/x at x = (2, 1). *Answer:* (1/2, −1/4).
3. x/(x + 1) at x = (1, 1). *Answer:* (1/2, 1/4).
4. 1/(x*x) at x = (2, 1). *Answer:* (1/4, −1/4).
5. At x = (3, 1), does the machine reach (a) x*x*x + 2, (b) 1/(x − 3), (c) (x + 1)/(x − 2)? *Answer:* (a) yes; (b) no, divisor value 0; (c) yes, (4, −3).

```check
R(10, 5) / R(5, 0) == R(2, 1)
const(1) / isolate(2) == R(F(1, 2), F(-1, 4))
isolate(1) / (isolate(1) + 1) == R(F(1, 2), F(1, 4))
const(1) / (isolate(2) * isolate(2)) == R(F(1, 4), F(-1, 4))
const(1) / (isolate(3) - 3) == NO_QUOTIENT
(isolate(3) + 1) / (isolate(3) - 2) == R(4, -3)
```

## Mistakes people make

- **Dividing the rate slots** (that is `rate`, a different question).
- **Skipping the multiply-back check.**
- **Turning `no quotient` into infinity** or a crash. Name it.

## Next

Guide 10: a rate that has its own rate.
