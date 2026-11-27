# 13. Rate laws: E, and S with C

## The question

How do you build a function whose rate always equals its own value, or two functions whose rates feed each other? (book Units 10, 11)

## E: rate equals value

> **A choice, not a discovery.** E(0) = 1 and rate(E) = E are a definition, picked because the pattern (grows faster the bigger it gets) is useful, like money growing continuously.

The machine cannot hold E as one polynomial (see below), so build polynomials that follow the law as closely as you like, and **name exactly what is missing** at each stage:

- P0 = 1. Rate 0; the law wants 1. Shortfall 1.
- Add a piece with rate 1: x. P1 = 1 + x. Rate 1; the law wants 1 + x. Shortfall x.
- Add a piece with rate x: half of x*x. P2 = 1 + x + x*x/2. Shortfall x*x/2.
- In general the next piece is x^n/n!, which is exactly the shortfall the previous stage carried.

| n | value of P(n) at 1 | rate | shortfall |
|---|---|---|---|
| 0 | 1 | 0 | 1 |
| 1 | 2 | 1 | 1 |
| 2 | 5/2 | 2 | 1/2 |
| 3 | 8/3 | 5/2 | 1/6 |
| 4 | 65/24 | 8/3 | 1/24 |
| 5 | 163/60 | 65/24 | 1/120 |
| 6 | 1957/720 | 163/60 | 1/720 |

Each rate equals the previous value. The shortfall is exactly 1/n!.

```check
[E_poly(n, 1)[0] for n in range(7)] == [1, 2, F(5, 2), F(8, 3), F(65, 24), F(163, 60), F(1957, 720)]
all(E_poly(n, 1)[2] == F(1, [1, 1, 2, 6, 24, 120, 720][n]) for n in range(7))
all(E_poly(n, 1)[1] == E_poly(n - 1, 1)[0] for n in range(1, 7))
E_poly(3, 2) == (F(19, 3), 5, F(4, 3))
E_poly(4, F(1, 2)) == (F(211, 128), F(79, 48), F(1, 384))
```

**Why no single polynomial satisfies the law:** a degree-n polynomial's rate has degree n − 1. A polynomial can equal its own rate only if both are 0, and E(0) = 1 rules that out. So E is the rule: for any n, run n stages, and the shortfall is exactly 1/n!.

### Precision on demand

Ask for E(1) within 1/1000. After P(6), the next term is 1/7!, and each later term is at most 1/8 of the one before. The whole tail is at most 1/7! × (1 + 1/8 + 1/64 + …) = 1/7! × 8/7 = 1/4410. Since 1/4410 < 1/1000, P(6) = 1957/720 answers the request, proven by finite fraction arithmetic. E(1) is the number people write as e.

```check
E_tail_bound(6) == F(1, 4410)
E_tail_bound(6) < F(1, 1000)
```

## S and C: two rates that feed each other

> **A choice, not a discovery.** S(0) = 0, C(0) = 1, rate(S) = C, rate(C) = −S. Whether these match the sine and cosine measured on triangles is a separate claim (kind 2), not proven here.

Build both series term by term, so each one's rate lands on the other's value at the previous stage:

- S3 = x − x³/6 at 1: value 5/6, rate 1/2. C2 = 1 − x²/2 at 1: value 1/2. The rate of S3 is the value of C2.
- S5 = x − x³/6 + x⁵/120 at 1: value 101/120, rate 13/24. C4 at 1: value 13/24, rate −5/6, which is minus the value of S3.

```check
S_poly(3, 1) == (F(5, 6), F(1, 2))
C_poly(2, 1) == (F(1, 2), -1)
S_poly(3, 1)[1] == C_poly(2, 1)[0]
S_poly(5, 1) == (F(101, 120), F(13, 24))
C_poly(4, 1) == (F(13, 24), F(-5, 6))
C_poly(4, 1)[1] == -S_poly(3, 1)[0]
S_poly(3, 2) == (F(2, 3), -1)
C_poly(2, 2)[0] == -1
```

### What the rate laws alone show

At any point where S has value s and C has value c, S reads (s, c) and C reads (c, −s). Then S*S + C*C = (s² + c², 2sc − 2sc) = (s² + c², 0). **The rate is exactly 0, at every point you check**, by algebra.

```check
S = R(F(3, 5), F(4, 5))
C = R(F(4, 5), F(-3, 5))
S * S + C * C == R(1, 0)
S * C == R(F(12, 25), F(7, 25))
S2 = R(F(5, 13), F(12, 13))
C2 = R(F(12, 13), F(-5, 13))
S2 * S2 + C2 * C2 == R(1, 0)
```

That is a fact about the rate at each point you check. It is not a claim that S*S + C*C stays 1 at every point at once. That would need a separate argument the book does not build. For a construction where c*c + s*s is exactly 1, provably, see guide 14.

## Steps: building any function from its rate law

1. Write the law as a choice: starting values and which rate equals which value.
2. Start with the constant that satisfies the starting value.
3. Compute the shortfall: what the law wants minus what the current rate gives.
4. Add the piece whose rate is that shortfall.
5. Repeat until the shortfall's bound is below the precision requested. Report the stage, the value and the bound.

## Next

Guide 14: headings, a second way to turn, exactly.
