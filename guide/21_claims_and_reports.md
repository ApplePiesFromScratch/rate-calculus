# 21. Claims, tiers and reports

## The question

What kind of statement are you making, how strongly does it stand, and how do you write it so a reader can check it? (book Unit 15; project)

## Three kinds of statement (book Unit 15)

- **Kind 1:** checked by calculation or proof. "At x = 3 the rate of x*x is 6."
- **Kind 2:** about the world, through a model. Checked by measurement; it can be wrong.
- **Kind 3:** about what everything ultimately is. Nothing can check it.

Make kind 1 and kind 2 statements only. Watch for a kind 1 fact dressed in kind 3 language: "transcendental" is a checked fact about polynomials (guide 12), not a claim about a deeper order of number.

**No method is free of assumptions.** Every calculation here rests on fraction arithmetic being consistent and on finite checks being reliable. State assumptions where they appear.

## Tiers: how strongly a claim stands

Tag each claim with one tier:

| tier | meaning | example |
|---|---|---|
| FORCED | follows by calculation or proof from what was fixed | division's rule, once mix is fixed |
| EMPIRICAL | measured, with the witness named | "board run, 27 Nov: 0 bytes dropped" |
| CONDITIONAL | holds if a named condition holds | "exact, if no product leaves int64" |
| STIPULATED | a choice, stated as one | "half to even at the mouth" |
| PRESUMED | assumed and not yet checked: say so, and say what would check it | "the C3's counter stops in sleep (from a file comment)" |
| UNPAID | a debt: a claim the work leans on that nobody has checked | "this file states Valiant's conjecture" |
| OPEN | a famous open problem: nobody verifies it here | P vs NP |

**FORCED-on-cut** is FORCED on a named finite list: enumerated completely there, and not lifted off it.

**The paid fraction**: of all the claims in a piece of work, the share that are FORCED, EMPIRICAL or CONDITIONAL here, checked by something that ran. Print it. A citation is a call to trust; it is priced at zero until it has a replica here.

## The report

Every write-up, README or answer ends with these parts, in this order:

1. **What came out**: the result, with its tier.
2. **What was run**: each command, where it ran (desk, emulator, device), and what it printed.
3. **What was not run**: plainly. "Compiles" is not "runs". "Emulator" is not "board". A skipped check is SKIPPED.
4. **Please run**: what the reader with the real device should run, and what to report.
5. **Please report**: the exact lines to send back.
6. **Planted fault**: which fault was planted beside the check, and that it was caught.
7. **Choices**: each "a choice, not a discovery", with what it buys.

## Writing style

- Use the book's words: Reading, isolate, mix, rate, theta, rule, requested precision, proven bound, the mouth, the carry, the books, a cut.
- Write readings as readings: name the rule, the cut and the grain (house rule 8).
- Say what was done, not how hard it was. No adjectives of effort or importance.
- Never write that something cannot be done; write what was tried and how each attempt failed.
- Quote a source's own words for its status. Coverage turns claims into facts; the source's own text rarely does.

## A filled-in example

> **Result (FORCED):** at x = 3, (x*x + 1)/(x − 1) reads (5, 1/2).
> **Run:** `python3 tools/check_docs.py` on a laptop: every line of guide 09's division block passed.
> **Not run:** the C core on a device.
> **Planted fault:** `RC_PLANT=div-sign` turns that line red.
> **Choices:** the mix rule (guide 04). The division rule is forced by it.

## Next

Guide 22: the modelling recipe.
