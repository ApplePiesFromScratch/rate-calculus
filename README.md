# Rate Calculus: a how-to

**Every number is a rule.** This repo teaches, step by step, a way of working with quantities that change: one alphabet, three moves, no independent variable, and every number checked by a program. It is built on James Pugmire's workbook *Every Number Is A Rule*, and adds the useful pattern, evolutionary modelling, fluids without Navier–Stokes, code as alphabets, and the rigor that keeps it honest, with lessons you write yourself.

It is for anyone: students, engineers, programmers, modellers, and AI assistants working alongside them. No background is assumed past fractions. Nothing needs installing past Python 3.

## Start here

1. Read [guide/00_setup_and_how_to_read.md](guide/00_setup_and_how_to_read.md). It walks you from "I have never opened a terminal" to running every check.
2. Run every check once:

   ```text
   python3 tools/check_all.py
   ```

3. Read the guides in order ([guide/README.md](guide/README.md)), doing each checked example by hand first.
4. Run the examples that match your field ([examples/](examples)).
5. Do the lessons ([lessons/README.md](lessons/README.md)): you write the code; a checker that has been shown to catch wrong answers grades it.

## The method on one screen

```text
alphabet   a Reading is a pair of fractions (value, rate)
isolate    isolate(v, r) builds one; isolate(v) means rate 1: the thing everything is compared with
rate       rate(A, B) = A's rate / B's rate; refuses with theta when B's rate is 0
mix        (v1, r1) * (v2, r2) = (v1*v2, r1*v2 + v1*r2): chosen once, used everywhere
+ and -    piece by piece; a plain number c is (c, 0)
divide     derived from mix, not a fourth move; refuses when the divisor's value is 0
when       a gap's -value / rate: latches until it runs out, read now, read again next step
rules      a number that is not a fraction is a rule: name a precision, get a fraction and a proven bound
whole      on a chip or in a long run: carry remainders, land once at the edge (the mouth)
step       run a system in latches by transfer: one take, one give; the books close every latch
```

```text
>>> from ratecalc import *
>>> x = isolate(3)
>>> x * x
(9, 6)
>>> rate(x * x, x)
Fraction(6, 1)
>>> rate(isolate(8, 2), isolate(15, 0))
theta (isolator r=0: the reading compared against is not changing)
```

## What is in the repo

| folder | what it holds |
|---|---|
| `guide/` | 30 guides, one idea each, in order; every number in them is run by `tools/check_docs.py` |
| `examples/` | 16 runnable examples: bathtub, rectangle, money, falling ball, epidemic, fluid, evolution, code, turning, pictures, the C core; each README has the exact output, checked |
| `lessons/` | 11 practice lessons with checkers, planted wrong answers and reference solutions |
| `ratecalc/` | the library, exact Python, standard library only |
| `core_c/` | the same moves in C99, whole numbers only, with named refusals |
| `book/` | the workbook the guides are built on (Parts I to V) |
| `chat/` | a kit to paste into any AI chat so it works by these rules |
| `tools/` | `check_all.py` (the one command), `check_docs.py`, `wordlint.py`, `ledger.py`, `seal.py` |
| `ledger/` | a hash-chained ledger for your kill lines, seals and attempts |
| `FALSIFIERS.md` | the headline numbers, and what would show each one false (checked) |
| `AGENTS.md` | instructions for AI assistants working in this repo |

## The rules in brief

No independent variable: compare readings with `rate(A, B)`; read the clock only as its change. Every number is the output of steps you can name. Refusals are named, never inherited. Say which rules are forced and which are chosen. Make kind 1 and kind 2 claims only, tiered. Say what ran and what did not. Never claim something cannot be done. Write readings as readings, not things. Every check has a planted fault beside it. Never edit a checker to make it pass. Full text: [guide/01_house_rules.md](guide/01_house_rules.md).

## Related work

- The microcontroller track (ESP32-C3 sketches, emulator setup, board practice): https://github.com/ApplePiesFromScratch/Microcontrollers-and-robotics-beta
- `propagation-logic` and `math-of-logic`: formal systems as V / G / θ carriers, with tiered, executable claims. See [CREDITS.md](CREDITS.md).

## Licence

MIT, copyright 2026 James Pugmire. See [LICENSE](LICENSE) and [CREDITS.md](CREDITS.md).
