# 23. Mistakes and presumptions

Each row is a presumption that looks harmless and is not, what to do instead, and where it is explained. Read this before writing your first model, and again when a result surprises you. AI assistants should treat this table as instructions.

| # | Presumption | Do instead | Guide |
|---|---|---|---|
| 1 | "Let t be time" | seed a comparison quantity with `isolate(0, 1)`; read `when` off gaps | 01, 11 |
| 2 | A rate is a property of one quantity | a rate is a comparison, `rate(A, B)` | 03 |
| 3 | Division by a still rate gives a big number | it is `theta`, a named refusal | 03 |
| 4 | Multiply the rate slots | mix: add both strips | 04 |
| 5 | A plain number has rate 1 | a plain number is (c, 0) | 05 |
| 6 | A remembered formula is as good as running the moves | run the moves; the formula is an unchecked second claim | 06 |
| 7 | A raw rate slot is meaningful on its own | it carries the seed; compare two readings | 07 |
| 8 | One measurement at one setting is a fact | take it at two cuts | 07 |
| 9 | Division always works | refuse on a zero value: `no quotient` | 09 |
| 10 | √2 or e must exist before we can use them | they are rules with proven bounds | 12 |
| 11 | "Approaches a limit" | "a rule, a requested precision, a proven bound" | 12 |
| 12 | Transcendental means less real | a narrow fact about polynomials | 12 |
| 13 | c*c + s*s = 1 makes a heading a sine | shared pattern, not identity | 14 |
| 14 | Round as you go | land once, at the edge, with the mouth | 15 |
| 15 | `if carry >= d` is enough | `while`; and check 0 ≤ carry < d | 15 |
| 16 | The books holding means it works | add a range check: conservation is not correctness | 15, 16 |
| 17 | Set a place from its neighbours | transfer: one take, one give | 16 |
| 18 | Floats are just approximate fractions | floats are a different alphabet with their own rule | 18 |
| 19 | Integer division is the same everywhere | Python and C disagree on negatives | 18 |
| 20 | A hash match means equal | a hash is a reading; collisions happen | 18 |
| 21 | The cycle counter is a clock | it counts work; on some chips it stops in sleep | 18 |
| 22 | Read the clock's value | read only its change | 01, 18 |
| 23 | A greedy result is optimal | it is a roof; compute a floor or say none was | 19 |
| 24 | A check that passed works | plant a fault; it must fail on the fault | 20 |
| 25 | More runs in the same setting are more evidence | one context is one witness | 20 |
| 26 | Tune, then report the score on the tuning set | read a sealed set once, against a kill line written first | 20 |
| 27 | Keep patching a claim | at load ≥ witnesses, reconfigure | 20 |
| 28 | The emulator agreeing means the device agrees | the device report outranks it; time, cache and sleep differ | 18, 21 |
| 29 | "Compiles" means "runs" | report run, not run, skipped | 21 |
| 30 | If the checker fails, adjust the checker | never edit a checker, a plant or a bench script | 01 |
| 31 | A reading can name what it measured as a thing | write the rule, the cut and the grain | 01 |
| 32 | Say it cannot be done | say what was tried and how it failed | 01 |
| 33 | Carry a ratio forward as a constant | ratios are first order; read again next step | 01 |
| 34 | Effort already spent counts in favour of a design | it is not a term | 20 |
