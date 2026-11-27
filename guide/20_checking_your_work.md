# 20. Checking your work

## The question

A result has come out. How do you know it is right, and how strongly does it stand? (Part V, Units V8, V9; project)

## The witnesses, from cheapest to strongest

A **witness** is a distinct way the result could have failed and did not. A thousand runs in one context are one witness, because they can see only one kind of failure.

| witness | what it catches | how |
|---|---|---|
| multiply back | a wrong quotient | divisor × quotient must give the dividend (guide 09) |
| plain arithmetic | a wrong value | recompute the value without Readings |
| the books | something made or lost | the conservation equation every step (guides 15, 16) |
| a range check | conserved but wrong (negatives, overflow) | count values outside the allowed range |
| two cuts | a reading that belongs to your choice | change a naming, a seed, a grain (guide 07) |
| a second implementation | a bug in one implementation | Python and C cores; desk and chip |
| exact beside approximate | float drift | run in fractions beside floats |
| a planted fault | a check that cannot fail | break the rule on purpose; the check must turn red |
| a sealed set | tuning to the test | hold readings back; read them once, after tuning stops |
| a kill line written first | moving the goalposts | write and hash the pass mark before the run |
| a person with the device | everything a model cannot see | the board report outranks the emulator and the model |

## Planted faults

**Every self-check has a planted fault beside it.** For each check, write a broken version of the thing it checks, run the check on it, and confirm the check fails.

This repo does it for every core rule. `ratecalc/_plant.py` lists the plants (mix that multiplies rates, division with the sign flipped, a floor for the mouth, an `if` in the carry, a heading with c flipped, `when` without its minus sign, `theta` returned as 0). `tools/check_all.py` runs every claim in every guide under each plant and requires at least one failure per plant.

A plant can show that two checks are really one. If every fault that check B catches is also caught by check A, B adds nothing; it is not a second witness. Keep it only if some plant lights B and not A.

**Lamp order is cause order.** When one fault lights several checks, note which lit first: the first lamp usually names the cause, and the later ones are its consequences.

**When engines agree with each other and disagree with a reference, suspect the reference.** Two independent implementations that still agree are a second witness for each other; a published value both disagree with is the first thing to re-check.

## Certificates

`certify(fn, at)` reads a rate and hands back its receipt:

- **statement**: what was read;
- **cut**: the grid of values and seeds it was checked on (the claim does not lift off that grid);
- **discharged / scope**: how many grid points gave an answer, of how many tried (refusals are counted, not hidden);
- **tier**: FORCED-on-cut if every point discharged and the rate never depended on the seed, EMPIRICAL if some did, UNPAID if none;
- **falsifier**: what would kill it.

```check
c = certify(lambda z: z * z, 3)
(c.value, c.tier, c.discharged, c.scope) == (6, "FORCED-on-cut", 32, 32)
certify(lambda z: z * z * z, 2).value == 12
certify(lambda z: z * z, 3, values=()).tier == "UNPAID"
```

**An empty grid proves nothing.** In Python, `all([])` is `True`, so a check over no cases reads as a pass. A certificate with nothing weighed is UNPAID; `tools/check_docs.py` likewise fails any guide that should carry claims but carries none, and any example without an output block.

## Sealed sets and kill lines (Part V, Unit V8)

You tune a threshold until it scores well. What does the score describe? The set it was tuned on.

Part V's demonstration: a threshold tuned on 200 readings scored 186/200 on the tuning set and 179/200 on a sealed set read once afterwards. Only the sealed number witnesses the claim.

**Kill line:** before running, write the pass mark ("at least 170 of 200 sealed readings right") and record it where it cannot be quietly changed. In this project a kill line is hashed before the run, and any amendment is logged and hashed before the reads it governs.

**The guards:**

- readings never feed rules;
- draw the reading's cut after the act;
- show the books beside every reading;
- read yourself at cuts you did not tune.

## Standing: witnesses, load and drag (Part V, Unit V9)

Count three things for a claim:

- **C**, the distinct witnesses it held in;
- **L**, its load: the alterations it needed (a mechanism added, a scope narrowed, an exception);
- **D**, its drag: the load of what it rests on.

v = C / (C + L + D). At L ≥ C, stop patching. Keep the core that needed no patch, and vent the rest as a separate claim at L = 0. Effort already spent is not a term.

> **A choice, not a discovery.** The formula is a rule for developing rules, measured on the project's ledgers. It orders what to alter first (the least-witnessed relation). It does not say what to try.

```check
standing(4, 0, 1) == (F(4, 5), "keep")
standing(4, 3, 1) == (F(1, 2), "keep")
standing(2, 3, 1) == (F(1, 3), "reconfigure")
standing(3, 1, 0) == (F(3, 4), "keep")
standing(3, 3, 0)[1] == "reconfigure"
```

Bringing code into line with what a claim already said is not load: it changes neither what the claim says nor what it needs.

## Steps: checking a result

1. Recompute the value by plain arithmetic.
2. Multiply back every division.
3. Check the books and the range at every step, not only at the end.
4. Take the result at two cuts.
5. Run it in a second implementation or a second alphabet (exact beside float).
6. Plant a fault in each rule you rely on; confirm a check catches each one.
7. If you tuned anything, read a sealed set once, against a kill line written before.
8. Count C, L, D. If L ≥ C, reconfigure.
9. Report what ran and what did not (guide 21).

## Next

Guide 21: claims, tiers and reports.
