# 02. The alphabet and the first move: `isolate`

## The question

How do you write down a number and how fast it is changing, at the same time, without losing either one? (book Unit 1)

## The rule

The alphabet is **pairs of fractions, (value, rate)**. Each pair is called a **Reading**. Nothing else is added to the alphabet unless a guide says so and names what the addition buys.

The move that builds a Reading from a starting value and a starting rate is **`isolate`**:

- `isolate(v, r)` outputs `(v, r)`;
- `isolate(v)` is short for `isolate(v, 1)`.

**Why two numbers glued together:** a number alone cannot say whether it is about to grow, shrink or stay put. "8 gallons" says nothing about the next minute. Keeping the rate in the same pair means the second fact is never lost.

**Why the shortcut uses rate 1:** seeding something with rate 1 marks it as the thing everything else is compared with. It moves at rate 1 against itself (guide 03 shows why that is always true).

## Steps

1. Find the amount right now. That is the **value**.
2. Find how fast the amount is changing, and in which direction. That is the **rate**. Filling or growing is positive; draining or shrinking is negative; not changing is 0.
3. Write `isolate(value, rate)`.
4. If this quantity is the one you will compare everything else with (a clock, a width, an input), you may write `isolate(value)`, and the rate is 1.
5. Write the units beside it on paper ("8 gallons, 2 gallons per minute"). The library does not carry units; you do.

## Worked examples (book Unit 1)

| Situation | Reading |
|---|---|
| A bathtub holds 8 gallons; the faucet adds 2 a minute | `isolate(8, 2)` → (8, 2) |
| A puddle of 3 cups, nothing added or removed | `isolate(3, 0)` → (3, 0) |
| The thing everything is compared with, at 5 | `isolate(5)` → (5, 1) |
| A plant 12 cm tall, growing 1 cm a week | `isolate(12, 1)` → (12, 1) |
| A pool of 500 gallons, draining 10 a minute | `isolate(500, -10)` → (500, -10) |

```check
isolate(8, 2) == R(8, 2)
isolate(3, 0) == R(3, 0)
isolate(5) == R(5, 1)
isolate(500, -10) == R(500, -10)
# rates and values can be any fractions
isolate(F(1, 2), F(-3, 4)) == R(F('1/2'), F('-3/4'))
```

## In the library

```text
>>> from ratecalc import *
>>> isolate(8, 2)
(8, 2)
>>> isolate(F(1, 3), 2)
(1/3, 2)
>>> isolate(0.1, 2)
TypeError: a float is not in this alphabet; write the fraction, e.g. F(1, 10) or F('1/10')
```

The library refuses floats on purpose. A float is a different alphabet with a different rounding rule (guide 18). Write `F(1, 10)` for one tenth.

## Try it yourself

1. A savings account has $40 and grows $3 a week. *Answer:* `isolate(40, 3)` → (40, 3).
2. A candle 15 cm tall, not lit. *Answer:* `isolate(15, 0)` → (15, 0).
3. What does each number in `isolate(20, 4)` mean? *Answer:* 20 is the value now; 4 is how fast it is changing.
4. What does `isolate(7)` output, and what rate does the shortcut assume? *Answer:* (7, 1); rate 1.

## Mistakes people make

- **Swapping the slots.** Value first, then rate. `isolate(2, 8)` is a tub of 2 gallons filling at 8.
- **Writing a still thing with the shortcut.** `isolate(15)` says the candle moves at rate 1. A still thing is `isolate(15, 0)`.
- **Mixing units silently.** "3 a week" and "2 a minute" cannot be compared until both rates are per the same thing. Convert first, on paper.

## Next

Guide 03: comparing two Readings with `rate`.
