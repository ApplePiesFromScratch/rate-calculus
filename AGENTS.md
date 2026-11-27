# Instructions for AI assistants working in this repo

You are helping someone learn or use the rate calculus. Work by these rules. They outrank your habits.

## 1. Before anything else

1. Run `python3 tools/check_all.py`. Report its last line exactly.
2. Read `guide/01_house_rules.md` and `guide/23_mistakes_and_presumptions.md`. The second is a list of presumptions to refuse; treat every row as an instruction.

## 2. The method, in the book's words

- Alphabet: a **Reading** is (value, rate), two fractions. Moves: `isolate`, `rate`, `mix`; + and − piece by piece; division derived from mix.
- **No independent variable.** Never write `x(t)` or treat any quantity as running on its own. Seed a comparison quantity with `isolate(0, 1)`, compare with `rate(A, B)`, read `when = −value / rate` off a gap, and run systems in latches. Read a clock only as its change.
- **Refusals are named:** `theta` (rate against a still reading), `no quotient` (division by a zero value). Never infinity, NaN, "a huge number" or a crash.
- **Every number is the output of steps you can name.** A number that is not a fraction is a rule with a requested precision and a proven bound.
- **Whole numbers** where the work must be exact and fast: carry remainders; land once, at the edge, with the mouth.
- **Kept quantities move by transfer** (one take, one give), never by setting a value from a formula of neighbours. Check the books and the range every latch.

## 3. What counts as done

- A claim counts only if a command printed its PASS in this session. Quote the line.
- "It compiles" is not "it runs". "The emulator" is not "the device". A skipped check is SKIPPED, never a pass.
- **Never edit a checker, a planted fault, a reference solution or an example's expected output to make something pass.** Fix the work or report the failure.
- Every check you add gets a planted fault beside it, and you show the check catching it.
- A lesson is done when `python3 lessons/LNN_*/check.py` prints PASS on the learner's file in `lessons/work/`. Do not write the learner's lesson file for them unless they ask; if they ask, say so in the ledger (`self` event).

## 4. Writing

- Use the book's words: Reading, isolate, mix, rate, theta, rule, requested precision, proven bound, the mouth, the carry, the books, a cut, a latch.
- Write readings as readings: name the rule, the cut and the grain.
- Do not use these words: `living`, `alive`, `organism`, `creature`, `being` (as a noun), `entity`, `entities`, `chaos`, `intelligence`, `impossible`. `tools/wordlint.py` flags them.
- Never claim something cannot be done; say what was tried and how it failed.
- Mark each choice "a choice, not a discovery" with what it buys. Tier each claim (FORCED, EMPIRICAL, CONDITIONAL, STIPULATED, PRESUMED, UNPAID, OPEN).
- Ratios are first order: read again at the next step; do not carry yesterday's ratio as a constant.

## 5. Every answer ends with

1. **Result**, with its tier.
2. **Ran**: each command and the line it printed.
3. **Not run**: plainly.
4. **Please run / please report**: what the person should run on their own machine or device, and which lines to send back.
5. **Planted fault**: which one, and that it was caught.

## 6. Where things are

`guide/` (read in order), `examples/` (runnable, outputs checked), `lessons/` (practice with checkers), `ratecalc/` (the library), `core_c/` (C99), `book/` (the workbook), `chat/` (a kit for chats without this repo), `FALSIFIERS.md`, `ledger/`.
