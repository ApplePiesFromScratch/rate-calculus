# 29. A bridge to standard courses

## The question

You learned with Readings and `rate(A, B)`. Your exam is written in a standard calculus course's symbols. How do you pass it without giving up this method's bookkeeping?

## The bridge sheet

Write their symbols in the exam. Keep this method's bookkeeping in the margin.

| they write | you did | say if asked |
|---|---|---|
| f′(x) | `rate(f, x)` | "the derivative with respect to x" |
| dy/dx | `rate(y, x)` | two rates; in a chain the middle one cancelled |
| (uv)′ = u′v + uv′ | mix | the product rule |
| chain rule | `rate(q, y) × rate(y, x)` | the chain rule |
| quotient rule | derived division (guide 09) | the quotient rule |
| lim (f(x + h) − f(x))/h as h → 0 | not taken | "I used the algebraic rate; the same number on polynomials and rational functions" |
| vertical asymptote | `no quotient` | "undefined / does not exist" |
| 0/0 at a point (L'Hôpital) | `rate(top, bottom)` | "the derivatives' ratio" |
| f″(x) | the curve slot (guide 10) | "the second derivative" |
| related rates | `rate(A, B)` between two readings | the same steps, in their layout |
| eˣ, sin, cos | rules with proven bounds (guides 12, 13) | "the series" |
| ∫ f | not covered by the book | use the course's method |

Do not argue foundations in the exam booklet. The bookkeeping is for your own checking.

## Counted, not felt: why this route takes fewer steps

For f(x) = x² at x = 3:

- **Pair path:** 5 operations on fractions give 6.
- **Difference-quotient path with h = 1/2:** 5 operations give 13/2, which is 6 + h.

Getting from 6 + h to 6 is not an addition, subtraction, multiplication or division. It is a limit, a different kind of step that the pair path never needed.

```check
x = isolate(3)
(x * x).rate == 6
h = F(1, 2)
((3 + h) * (3 + h) - 3 * 3) / h == 6 + h
```

## Reading 0/0 correctly

(x² − 1)/(x − 1) at x = 1: top and bottom values are both 0. Dividing the values refuses, correctly. Dividing the rates was never stuck:

```check
a = isolate(1)
(a * a - 1) / (a - 1) == NO_QUOTIENT
rate(a * a - 1, a - 1) == 2
```

L'Hôpital's rule is not "differentiate again and hope". It is "the first operator was the wrong one to ask".

## Teacher notes

| standard | here |
|---|---|
| y = f(x), x independent | two Readings; seed the one you compare against |
| f′(x) | `rate(f, x)` |
| chain rule | `rate(q, y) × rate(y, x)` |
| product rule | mix: the rule, not a new law |
| limit definition | not used; a finite difference's leftover is named when one is used |
| vertical asymptote | a named refusal |
| related rates | the same kernel, a second reading |

When a student writes dy/dx, ask: which two rates, and did a third just cancel?

## Next

Back to the guide index (`guide/README.md`), or the lessons (`lessons/README.md`).
