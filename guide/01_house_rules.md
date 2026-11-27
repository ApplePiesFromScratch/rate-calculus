# 01. House rules

These rules hold in every guide, every example and every answer you write with this method. Each one comes with its reason.

## Rule 1. No independent variable

**What it says:** never write a quantity as a function of a free-running variable that nothing produces, such as `x(t)` with `t` ticking along on its own, or `f(x)` with `x` an arbitrary input standing outside the machine.

**What you do instead:** write each quantity as a **Reading** (value, rate), and compare Readings with each other using `rate(A, B)`. A rate is always *against something*: the bathtub's level against the clock's count, the area against the width, one car against another.

**Why:**
- A free variable is something nobody computed, but every later number leans on it. The book's promise is that no number is asserted to exist ahead of the steps that produce it (Before We Start).
- Every "rate of change" is really a comparison of two changes. Writing it as `rate(A, B)` keeps both parties in view, and that is how you catch the comparisons that have nothing to land on (`theta`, guide 03).

**How to rewrite a problem stated with a variable** (do this every time):

1. Find the quantity the problem treats as running on its own (often time `t`, sometimes `x`).
2. Make it a Reading like any other: `clock = isolate(0, 1)` says "this one counts 1 per tick; everything else is compared with it."
3. Write each other quantity as a Reading built from moves (`isolate`, `mix`, `+`, `-`, `/`), never as "a formula in t".
4. Ask questions as comparisons: `rate(level, clock)`, `rate(area, width)`.
5. If you need to know *when* something happens, read it from a gap (guide 11): `when = -value / rate`. That is a number read off a Reading, not a variable you stepped through.
6. If you need to *run* a system forward, step it in latches (guide 16). The count of latches is a reading of how many steps were taken; it drives nothing.

**A clock is read only as its change.** When a program does read a clock, it reads how much the clock moved since the last reading (a difference of two readings), never the clock's absolute value as if it were a variable everything depends on.

```check
# the bathtub, compared with the clock that counts its minutes
clock = isolate(0, 1)
tub = isolate(8, 2)
rate(tub, clock) == 2
# the same question against a still thing has nothing to land on
candle = isolate(15, 0)
rate(tub, candle) == THETA
```

## Rule 2. Every number is the output of steps you can name

No number appears unless the moves that produce it can be written down. When an answer is not a fraction (the square root of 2, e), the answer is a **rule**: give it a precision, it gives a fraction and a proof of how close the fraction is (guide 12).

## Rule 3. A refusal is named, never inherited

When a move has no answer, the machine says so by name:

- `theta`: a rate against a reading whose rate is 0 (guide 03);
- `no quotient`: division by a reading whose value is 0 (guide 09).

It never returns "a very large number", "basically zero", infinity, NaN, or a crash from the host language. A refusal is a statement the method makes and means.

## Rule 4. Say which rules are forced and which are chosen

Some rules are **forced**: once what came before is fixed, they cannot come out any other way. Division (guide 09) and the curve rule (guide 10) are forced. Others are **chosen**, because the choice is useful. The mix rule itself is the main one; the mouth's half-to-even is another. The book marks each choice with a box titled *A choice, not a discovery*, and so do these guides. The box says what the choice buys.

## Rule 5. Three kinds of statement (book Unit 15)

| Kind | What it is | How it is checked | Example |
|---|---|---|---|
| 1 | checked by calculation or proof | run the rule or the argument | "At x = 3 the rate of x*x is 6." |
| 2 | about the world, through a model | measurement; it can be wrong | "A dropped ball falls about 4.9*t*t metres in t seconds, ignoring air." |
| 3 | about what everything ultimately is | nothing can check it | "Numbers exist whether or not anyone thinks about them." |

This method makes kind 1 and kind 2 statements only. Guide 21 adds tiers for how strongly a kind 2 claim stands.

## Rule 6. Say what was run and what was not

Every report, README or answer lists what was actually run, where it was run, and what was not run. "It compiles" is not "it ran". "It ran in the emulator" is not "it ran on the board". If a check was skipped, say SKIPPED; never fold it into a pass.

## Rule 7. Never claim something cannot be done

Write what was tried and what happened: "three approaches failed; here is how each failed." A failed search is a fact about the search. The word `impossible` is refused for that reason. A proof that *no fraction* squares to 2 is fine: it is a finite, checked statement about fractions (book Unit 9), and it does not say the question has no answer.

## Rule 8. Write a reading as a reading, not as a thing (de-reification)

A number you measured is a reading: it came from a rule, at a cut, with a grain. Write it that way.

- Weak: "the swirl", "the system's memory", "the market's mood".
- Strong: "the turning counted round 4 × 4 loops", "the rate of the balance against the month count, read at month 12".

The second form names the rule and the cut, so anyone can take the reading again (Part V, Unit V3).

These words are refused in writing because they turn readings into things: `living`, `alive`, `organism`, `creature`, `being` (as a noun), `entity`, `entities`, `chaos`, `intelligence`, `impossible`. `tools/wordlint.py` flags them. A word inside backticks or quotes is only being named, and passes, as here. For "chaos", write what actually happened: a tool reached the limit of what it can read ("the float run lost the trajectory after 40 steps; the exact run did not").

## Rule 9. Whole numbers where the work must be exact and fast

On a chip, in a game, in a long simulation: hold quantities as whole numbers, carry remainders, and land a fraction on a whole number once, at the edge (guide 15).

## Rule 10. Ratios are read as first order

A ratio such as `rate(A, B)` or `when = -value / rate` reads the situation as it is now, at this step. If the rates themselves are changing, read again at the next step; do not carry the old ratio forward as a constant. Carrying constants through fast-changing situations writes yesterday's reading into today's rule.

## Rule 11. Every self-check has a planted fault beside it

If you write a check, write a deliberately broken version beside it and confirm the check catches it. This repo does it for every rule: `ratecalc/_plant.py`, run by `tools/check_all.py`.

## Rule 12. Do not edit a checker to make it pass

A checker, a planted fault and a bench script are the witnesses. Editing one to turn it green removes the witness. Fix the claim or the code, or report the failure.

## Mistakes people make with these rules

- **Writing `y = 3t + 2` and calling it a model.** Write `y = isolate(2, 3)` against `clock = isolate(0, 1)`, then `rate(y, clock) == 3`.
- **Treating `theta` as infinity.** It is not a big number; it is the honest name for a question with nothing to compare against.
- **Saying "the model proves the world does X".** A model's statements about the world are kind 2: they are checked by measurement.
