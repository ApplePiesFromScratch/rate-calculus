# 12. A number that is not a fraction is a rule

## The question

What do you do when the answer to a question is not a fraction? (book Units 9, 12, 13, 14)

## First, settle that it is not a fraction (book Unit 9)

A square with sides 1 has a diagonal d with d*d = 2. Is there a fraction a/b, in lowest terms, with (a/b)² = 2?

1. Then a² = 2b², so a² is even, so a is even (odd × odd is odd). Write a = 2c.
2. Then 4c² = 2b², so b² = 2c², so b is even too.
3. Now a and b are both even, so a/b was not in lowest terms. Contradiction.

No fraction squares to exactly 2. That proof is finite and settles the question. It does **not** say the question has no answer. It says the answer is not a fraction.

## The answer is a rule

A **rule**, here, is a finite procedure. You give it a positive fraction (how close you need to be); it gives back a whole number (how many steps to run); running that many steps produces a fraction, with a proof that the fraction is that close. Every part is finite. You never run it forever: you run it once, for the precision you asked for, and it stops (book Unit 12).

### Rule 1: closing in by halving

Start with 1 (its square is too small) and 2 (too big). Check the midpoint: if its square is too small it becomes the new low end, otherwise the new high end. The gap halves every step, and every number stays an exact fraction.

| step | low | high | gap | midpoint checked |
|---|---|---|---|---|
| 0 | 1 | 2 | 1 | |
| 1 | 1 | 3/2 | 1/2 | 3/2 squared = 9/4, too big |
| 2 | 5/4 | 3/2 | 1/4 | 5/4 squared = 25/16, too small |
| 3 | 11/8 | 3/2 | 1/8 | 11/8 squared = 121/64, too small |
| 4 | 11/8 | 23/16 | 1/16 | 23/16 squared = 529/256, too big |

After k steps the gap is exactly 1/2^k. To reach a requested gap, run the first k with 1/2^k below it: ten steps for 1/1000, seventeen for 1/100,000.

```check
low, high, rows = sqrt2_halving(4)
(low, high) == (F(11, 8), F(23, 16))
[r[3] for r in rows] == [F(1, 2), F(1, 4), F(1, 8), F(1, 16)]
halving_steps_for(F(1, 1000)) == 10
halving_steps_for(F(1, 100000)) == 17
low5, high5, rows5 = sqrt2_halving(5)
(low5, high5) == (F(45, 32), F(23, 16))
```

### Rule 2: closing in by averaging

Start at x = 1. Each step, replace x with the average of x and 2/x.

```text
x0 = 1
x1 = 3/2
x2 = 17/12
x3 = 577/408
x4 = 665857/470832
```

Square x4: 443365544449/221682772224. Two over the same bottom is 443365544448/221682772224. They differ by exactly 1: the gap is 1/221682772224 after four steps. Halving needs about forty steps for a gap that small. Averaging's gap shrinks roughly by squaring each step; halving's always halves.

```check
sqrt2_averaging(4) == [1, F(3, 2), F(17, 12), F(577, 408), F(665857, 470832)]
x4 = sqrt2_averaging(4)[-1]
x4 * x4 - 2 == F(1, 221682772224)
halving_steps_for(F(1, 221682772224)) == 38
```

Either rule **is** the square root of 2, in every sense that matters for computing with it. Name a precision; the rule hands you a fraction within it and a proof of how good it is.

> **A choice, not a discovery.** Giving the rule a symbol, √2, is a choice made because the rule comes up often. The label adds nothing the rule did not already have.

## "Limit" is a rule with a requested precision (book Unit 12)

**The rule 1/n:** get within 1/500 of 0. Solve 1/n < 1/500: n > 500, so n = 501. Check with no decimals: 1/501 < 1/500 exactly when 500 < 501.

**The sums of halves:** 1, 3/2, 7/4, 15/8, … The gap to 2 after n steps is exactly 1/2^n. For a gap under 1/100, run 7 steps (2^7 = 128).

**A hole in a fraction:** f(x) = (x*x − 1)/(x − 1) refuses at x = 1 (0/0). Away from 1, x*x − 1 = (x − 1)(x + 1), so f(x) = x + 1 at every x except 1. Feed it x = 1 + 1/n: f = 2 + 1/n. Within 1/50 of 2 needs n = 51. This is algebra, not a process approaching anything.

Where courses say "limit", what is actually there is a rule: give it a tolerance, it gives back a stage, checked by a finite calculation. Nothing needs to sit anywhere waiting to be approached.

```check
stage_for(1, F(1, 500)) == 501
stage_for(3, F(1, 100)) == 301
stage_for(5, F(1, 1000)) == 5001
x = isolate(1 + F(1, 51))
((x * x - 1) / (x - 1)).value == 2 + F(1, 51)
(isolate(1) * isolate(1) - 1) / (isolate(1) - 1) == NO_QUOTIENT
```

## "Algebraic" and "transcendental" are rule labels (book Unit 13)

- **Algebraic:** reachable by the rule "find a root of a whole-number polynomial". √2 is a root of x*x − 2. Every fraction p/q is a root of qx − p.
- **Transcendental:** not reachable by *that* rule. It is a theorem (stated in the book, not derived) that e is not the root of any whole-number polynomial.

Neither word means harder to compute, less precise, less real or further away. Both √2 and e have rules, finite per step, with proven precision on request. The labels sort numbers by which rule answers one narrow question, the way "even" and "odd" do.

## What the machine never needed (book Unit 14)

| number or function | rule | per-step arithmetic |
|---|---|---|
| rate of x*x*x + 2x + 1 | mix and add on Readings | fractions, finite |
| 1/x, (x + 1)/(x − 2) | derived quotient | fractions, finite |
| √2 | halving, or averaging | fractions, finite |
| e = E(1) | shortfall construction (guide 13) | fractions, finite |
| sin(1), cos(1) | coupled shortfall construction (guide 13) | fractions, finite |
| "a rule gets within any distance you name" | naming a stage for a tolerance | fractions, finite |

Nothing required a number that is not a fraction to exist ahead of time, or "all the numbers there could be" as one object.

## Steps: answering any "what number is…" question

1. Try to show the answer is a fraction. If it is, you are done.
2. If you prove no fraction works, do not stop: build a rule.
3. Give the rule a bracket or a starting point, and a step that keeps every number a fraction.
4. Prove how fast the gap shrinks (halving: 1/2^k exactly).
5. For a requested precision, compute how many steps, run exactly that many, and report the fraction and the proven gap.

## Try it yourself

1. Run halving one step past step 4. *Answer:* midpoint 45/32, squared 2025/1024 < 2048/1024, so it is the new low; range 45/32 to 23/16, gap 1/32.
2. For the rule 3/n, find a stage within 1/100. *Answer:* 301.
3. Which whole-number polynomial has 3/4 as a root? *Answer:* 4x − 3.

## Next

Guide 13: functions defined by their rates.
