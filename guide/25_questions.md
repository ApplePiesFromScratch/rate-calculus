# 25. Questions people ask

**Is this the same as ordinary calculus?**
For everything the book covers, it produces the same numbers: power rule, chain rule, quotient rule, second derivatives, e, sine and cosine series. What differs is the account. Nothing is a function of a free variable, no completed set of real numbers is declared, and "limit" is replaced by a rule with a requested precision and a proven bound. The book does not cover integrals, existence and uniqueness proofs for rate laws, or several changing quantities at once (book, What This Book Does Not Cover).

**Is a Reading the same as a dual number?**
The arithmetic matches what courses call dual numbers, used in forward-mode automatic differentiation. The book builds it from the growing rectangle and keeps `rate(A, B)` as the question, with `theta` as a named refusal. Those two habits are what the method adds.

**Why refuse floats?**
A float is a different alphabet. It lands every intermediate result on a binary fraction, so the order of operations changes answers (guide 18). Use floats when you choose that alphabet on purpose, not by accident.

**Doesn't `when` use time anyway?**
`when` is a number read from a gap: −value / rate. It counts latches in the unit the rates are counted per. Nothing runs through it, and nothing depends on it as an input.

**How do I simulate something without t?**
Step it in latches (guide 16). Each latch moves every quantity by its rate times the grain, with transfer for kept quantities and the books checked every latch. The latch count is a reading.

**My program uses `if`. Does the Reading carry still work?**
Within each branch, yes. At the boundary the two branches give two rates. Report both, and treat the boundary as a cut (guide 18).

**What if my numbers get huge?**
Python fractions grow as needed. In C, `core_c` refuses with `RC_OVERFLOW` instead of wrapping. On a chip, move to whole numbers with a scale and carries (guide 15).

**Where do the microcontroller sketches fit?**
The microcontroller track is its own repository: https://github.com/ApplePiesFromScratch/Microcontrollers-and-robotics-beta (sketches for an ESP32-C3 with a 2-inch panel, demos, practice, emulator setup, the board mapping). It is one application of the method among the examples here; this repo's `core_c/` and `examples/14_c_core` are the bridge to it.

**Can I use this with an AI chat assistant?**
Yes: paste `chat/CHAT_START.md` into a new chat first. It gives the assistant the rules, the moves, the presumption table and the report format.
