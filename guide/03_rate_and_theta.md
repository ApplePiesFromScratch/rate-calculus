# 03. The second move: `rate`, and `theta`

## The question

Given two Readings, how fast is one changing compared with the other? (book Unit 2)

## The rule

`rate(A, B)` divides A's rate slot by B's rate slot. **It never looks at either value.**

**Why it ignores the values:** "how much faster is A changing than B" is a question about speed, not about where each one started. A car at 60 mph is going twice as fast as a car at 30 mph, whether the fast car started at mile 0 or mile 500.

**Anything compared with itself gives 1:** `rate(x, x) = r / r = 1` for any nonzero rate. That is why `isolate(v)` seeds with rate 1: it marks the thing everything else is compared with.

## When there is nothing to compare against: `theta` (book Unit 6)

If B's rate is 0, `rate(A, B)` would divide by 0. The machine refuses on purpose and names the refusal **`theta`** ("isolator r=0").

**Why there is no answer:** "how many times faster is the bathtub filling than the candle is growing" only makes sense if the candle is changing at all. It is not.

**Zero apples, ten apples:** if you have 0 apples and a friend has 10, your friend does not have "10 times as many". "How many times more" needs a nonzero amount to be a multiple of. `theta` is the honest name for that, not a stand-in for "huge" or "basically zero".

## Steps

1. Write both quantities as Readings (guide 02).
2. Check B's rate slot. If it is 0, the answer is `theta`. Stop and say so.
3. Otherwise divide A's rate by B's rate.
4. Say the answer in words: "A is changing 2 times as fast as B." A negative answer means they move in opposite directions.

## Worked examples

```check
A = isolate(10, 4)
B = isolate(5, 2)
rate(A, B) == 2
x = isolate(7)
rate(x, x) == 1
E = isolate(9, 6)
G = isolate(2, 3)
rate(E, G) == 2
# the values never matter: change them and the rate stays
rate(isolate(1000, 4), isolate(-3, 2)) == 2
# theta
bathtub = isolate(8, 2)
candle = isolate(15, 0)
rate(bathtub, candle) == THETA
# theta is not zero and not a number
rate(bathtub, candle) != 0
# zero VALUES are no trouble: rate never reads them
rate(isolate(0, 6), isolate(0, 1)) == 6
```

## In the library

```text
>>> rate(isolate(10, 4), isolate(5, 2))
Fraction(2, 1)
>>> rate(isolate(8, 2), isolate(15, 0))
theta (isolator r=0: the reading compared against is not changing)
```

When you write your own code on top of `rate`, test for the refusal before using the answer:

```text
r = rate(A, B)
if r == THETA:
    print("no comparison: B is not changing")
else:
    ...
```

## Try it yourself

1. `rate(isolate(30, 8), isolate(10, 4))`? *Answer:* 2.
2. `rate(isolate(6, 9), isolate(1, 3))`? *Answer:* 3.
3. `rate(x, x)` for `x = isolate(50, 6)`, without dividing? *Answer:* 1: anything compared with itself.
4. `rate(isolate(40, 5), isolate(20, 0))`? *Answer:* `theta`. The second reading is not changing.
5. A friend says that answer "must be a huge number". What is wrong with that? *Answer:* "huge" still treats it as a well-shaped question with a large answer. A ratio to exactly 0 is not a number at all.

## Mistakes people make

- **Dividing the values.** `rate` uses rate slots only.
- **Replacing `theta` with a big number or with infinity** to keep code running. The refusal is the information; keep it.
- **Forgetting which is on top.** `rate(A, B)` is A over B; `rate(B, A)` is its reciprocal.

## Next

Guide 04: what happens to the rate when two changing things are multiplied.
