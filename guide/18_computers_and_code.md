# 18. Computers and code as alphabets and mixing rules

## The question

The book builds one machine: an **alphabet** (pairs of fractions) and **mixing rules** fixed once and used everywhere. A computer is also a machine of that shape. How do you read a computer, a programming language or a piece of code as an alphabet with mixing rules, and what does that buy you?

## The correspondence

| In the book | In a computer | Example |
|---|---|---|
| alphabet | the set of values a type can hold | `uint8`: the 256 whole numbers 0 to 255 |
| a letter | one value | `200` |
| mixing rule, fixed once | an operation or instruction, exactly as the machine does it | `uint8` add: (a + b) mod 256 |
| a chain of rooms (guide 08) | a program: functions feeding functions | `room3(room2(room1(x)))` |
| a named refusal (`theta`, `no quotient`) | a trap, exception or error code, if the language names it | division by zero, overflow |
| a reading (guide 07) | what leaves the program: a print, a pixel, a packet, a log line | `print(total)` |
| the mouth (guide 15) | the place a value is landed to fit an output | rounding to cents, to a pixel |
| the books (guide 15) | an invariant checked every step | "money in = money out + money held" |
| a choice, not a discovery | a design decision in the language or the program | integer division toward zero (C) or toward −∞ (Python) |
| forced | what the hardware or the earlier choices leave no room for | two's-complement wrap of a 32-bit add |

**What it buys:**

- You stop asking "is this number right?" and start asking "**which alphabet is this number in, and which rule made it?**". Most bugs are a value read in one alphabet that was made in another.
- You can **predict** where a program will refuse, wrap, round or lose information, from the alphabet and the rules alone, before running it.
- You can **carry Readings through code** and get exact rates of a program's output against its inputs, for free.
- You can **design** alphabets and rules on purpose to get a desired output (guide 19).

## Part 1: the same expression in five alphabets

Take f(x) = x*x − x, and two sums, in five alphabets a computer offers. Same symbols, different mixing rules, different outputs.

| alphabet | its rule for + and × | f(3) | 1/10 + 2/10 = 3/10 ? | (a + b) + c = a + (b + c) ? |
|---|---|---|---|---|
| fractions (`F`) | exact | 6 | yes | yes |
| Readings (`R`) | mix (guide 04) | (6, 5): value and rate | yes | yes |
| `uint8` | wrap mod 256 | 6 (but f(20) = 380 mod 256 = 124) | no fractions at all | yes |
| booleans {0, 1} | × is AND, + is XOR | x*x − x = 0 for every letter | no fractions at all | yes |
| floats (IEEE 754 double) | round to nearest binary fraction after each step | 6.0 | **no**: 0.1 + 0.2 ≠ 0.3 | **no** |

```check
x = isolate(3)
x * x - x == R(6, 5)
F(1, 10) + F(2, 10) == F(3, 10)
(20 * 20 - 20) % 256 == 124
all((b * b - b) % 2 == 0 for b in (0, 1))
0.1 + 0.2 != 0.3
(0.1 + 0.2) + 0.3 != 0.1 + (0.2 + 0.3)
F(1, 10) + F(2, 10) + F(3, 10) == F(1, 10) + (F(2, 10) + F(3, 10))
```

**Reading the table:**

- **Booleans:** in arithmetic, x*x and x are different polynomials. In the Boolean alphabet, x*x = x for every letter, so they collapse into one. A cost or a difference measured in one alphabet does not carry over to another. (The same point holds at the scale of mathematics: how hard a polynomial is to compute depends on the field and the circuit alphabet it is computed in.)
- **Floats:** the float rule lands every intermediate result on the nearest binary fraction. That one landing per step is a mouth in the middle of every chain (guide 15 says never do that), which is why the order of additions changes the answer. Floats are not wrong; they are a different alphabet with a stated rule. Know when you are in it. `ratecalc` refuses floats so you cannot slip into it by accident.
- **uint8:** the alphabet wraps. 200 + 100 is 44. That is not an error in the alphabet; it is its rule. It is an error in a program that meant fractions.

## Part 2: rounding is a mixing rule, and languages disagree

Integer division is a rule a language designer **chose**:

| language | −7 / 2 | rule |
|---|---|---|
| Python `//` | −4 | toward the more negative number |
| C, Java, Rust `/` on integers | −3 | toward zero |
| the mouth (this method) | −4 (half to even), and −3/2 → −2 | nearest, half to even, mirror-true |

```check
toward_negative(-7, 2) == -4
toward_zero(-7, 2) == -3
mouth(-7, 2) == -4
mouth(-3, 2) == -2
mouth(3, 2) == 2
```

Code moved from one language to another keeps its symbols and silently changes its rule. When you port code, list each operator's rule in both languages.

## Part 3: each instruction is a mixing rule you can count

An instruction maps letters to letters. Count how many distinct outputs it gives over the whole alphabet (guide 16):

```check
collisions(lambda v: v + v) == 128
collisions(lambda v: v * 5) == 256
collisions(lambda v: v ^ (v >> 3)) == 256
collisions(lambda v: v >> 1) == 128
collisions(lambda v: v & 0x0F) == 16
```

- 256 of 256: one-to-one; the instruction can be undone exactly.
- 128 of 256: two inputs per output; one bit is gone and no later rule can bring it back.

**A program can be run backwards exactly only if every instruction in it is one-to-one** (or if, like the run-back step in guide 16, the rounding lives inside a push that both directions share). The microcontroller track's TIDE sketch builds a whole instruction set with no two-to-one instruction.

## Part 4: the computer's whole state is one letter

Take every bit of a computer's memory and registers together. That is one letter in an alphabet of 2^(number of bits) letters. Each clock step of the processor is a mixing rule from one letter to the next. A program run is a chain of those rules.

This view explains three things that otherwise look like magic or bad luck:

1. **Same alphabet, same rules, same input → same output, byte for byte.** That is why a "desk twin" (the program compiled for a PC with the same whole-number rules) matches the chip exactly. When the two disagree, the disagreement shows exactly where their alphabets differ: float, timing, cache, uninitialised memory.
2. **Timing is a separate alphabet.** The rules for values can match while time does not. A chip's cycle counter counts work done, not time passed: on the ESP32-C3 it nearly stops while a task sleeps. Read `rate(cycles, ticks)`: about cycles-per-tick while awake, near 0 while asleep. The ratio itself shows that the task slept, with no stopwatch.
3. **The clock is read only as its change.** Code that does `now = clock(); elapsed = now - last; last = now` compares two readings. Code that feeds `clock()` into a formula as if it were the variable everything depends on brings an independent variable back in (house rule 1).

## Part 5: carrying Readings through code

Any function written only with +, −, ×, ÷ works unchanged on Readings, because `ratecalc` gives Readings those operators with the book's rules. Feed a Reading in, and the output carries its exact rate against the input. A course calls this forward-mode automatic differentiation; here it is guide 08's rooms.

```check
def balance(p, r): return p * (1 + r) * (1 + r)
rate_in = isolate(F(5, 100))
out = balance(1000, rate_in)
out == R(F(11025, 10), 2100)
def area(w, h): return w * h
area(isolate(4), 3) == R(12, 3)
```

Here `out` says: at 5% a year for two years, 1000 becomes 1102.50, and the balance moves 2100 per unit of rate. That means 21 per percentage point, exact.

**Three things break the carry. Each is a rule of the code, not of the Readings:**

1. **A float anywhere in the chain:** the Reading's fractions get mixed into the float alphabet. `ratecalc` refuses floats; your code should too.
2. **A branch on a value** (`if x > 0:`): a branch reads the value and picks a rule. The Reading's rate is the rate *of the branch taken*. At the boundary, two branches give two rates: report both, and treat the boundary as a cut (guide 07).
3. **Landing in the middle** (`round()`, `int()`, `//`): the landing has no rate. Land once, at the edge.

For more than one input, use the lever (guide 17): one rate per source.

## Part 6: refusals in code

| situation | weak (inherited from the host) | strong (named by the method) |
|---|---|---|
| rate against a still reading | ZeroDivisionError, inf, NaN | `THETA` |
| division by a zero value | crash, inf | `NO_QUOTIENT` |
| a product leaves the integer alphabet | silent wrap | `RC_OVERFLOW` (the C core), or saturate *and count* |
| a print waits for a reader that is not reading | the program stalls | a ring buffer that drops *and counts* |
| a hardware queue never answers | wait for ever | a bounded wait, then give up *and count* |

Every refusal is a value the program can test and report. A count of drops is a ledger (books for the refusals themselves).

## Part 7: a reading is a fold of many letters onto few

What a program shows is rarely its state. It is a **reading**: a rule that folds many letters onto few.

- A colour map folds many cell letters onto two colours. In the TSUZURI sketch (microcontroller track), many hidden letters spell a picture that has only ink and paper.
- A hash folds a whole buffer onto 32 bits. Two different buffers can give the same hash (a collision), so a hash match is a reading, not proof the buffers match.
- A dashboard number folds a whole system onto one figure at one cut.

Write a reading as a reading: name the fold, the cut and the grain (house rule 8).

## Part 8: V, G and theta

The project's companion repos (`propagation-logic`, `math-of-logic`) name the three parts of every formal system, a program included:

- **V**, the alphabet: what values may appear;
- **G**, the mixing rules: what maps are allowed on V;
- **θ (theta)**, the threshold: what counts as accepted, and what happens when a write misses V.

When a write misses V there are two honest moves: **refuse** (fire θ, by name), or **grow V out loud** through a registered migration, and pay for it on the ledger. The dishonest move is a silent append: the value lands somewhere the alphabet never listed (an overflow that wraps, a NaN that spreads, undefined behaviour that still emits *something*).

**A live rate cannot be dropped silently.** Moving a Reading to a plain value is a migration, and it is allowed only when the rate is 0:

```check
drop_rate(R(5, 0)) == 5
drop_rate(R(5, 2)) == LIVE_RATE
```

## Part 9: a computer is a stack of cuts

Each layer keeps some distinctions and ignores the rest, so that one distinction can propagate:

| layer | V | G | θ (where it refuses) |
|---|---|---|---|
| analog | voltages | physics | metastability |
| bit | {0, 1} after a threshold | AND, XOR, NOT | a voltage that is neither |
| word | 8, 32, 64 bits | wrap mod 2^n | overflow: wrap, or a trap |
| instruction set | opcodes | decode and execute | illegal instruction |
| memory | addresses | load, store | page fault |
| runtime | objects | the language's operations | TypeError, recursion limit |
| float | sign, exponent, mantissa | rounded + − × ÷ | NaN, Inf |
| model | tokens, weights | matrix products | out of vocabulary, underflow |

A higher layer does not uncover the lower one; it ignores it. A bug is very often a lower layer's θ showing through a higher layer that did not list it.

## Part 10: bugs by mechanism

| bug | mechanism in this method's words |
|---|---|
| integer overflow | a word alphabet wraps where the program meant whole numbers |
| off-by-one | an index alphabet's edge read as if it were inside |
| null dereference | a refusal written as a value and then used |
| use after free, dangling pointer | a letter kept after the thing that made it was gone |
| data race | two orders of the same moves; the leftover is a torn read |
| deadlock | two waits on each other; no write lands |
| injection (SQL, shell, format string) | data letters run as rules |
| float 0.1 + 0.2 | the float alphabet's rounding, read as fractions |
| NaN poisoning | a refusal that compares unequal to itself and spreads |
| hash collision | a fold of many letters onto few, read as identity |
| time wrap (2038) | a counter alphabet wraps |
| tests green, program wrong | a listed set of cases read as "for all" |

Four outcomes: **crash** (θ fires), **freeze** (writes stop landing), **hack** (an attacker chooses a letter outside your V), **silent wrong** (a leftover kept as if it were the intended reading).

**θ runs at different times:** at compile time (types, ownership), at run time (exceptions, traps), or never (undefined behaviour). Moving θ earlier does not remove the edge; it refuses before the operating system has to.

## Part 11: designing a language (or a library) without the usual errors

1. **Every value has a listed V.** A byte is {0..255}; `+` on bytes names which rule it is (wrap, widen, saturate).
2. **Partial maps show their hole.** Division returns a quotient or a named refusal, and the type says so.
3. **Bool is not a number.** `True + True` should not be allowed. (`ratecalc` refuses a bool where a number belongs.)
4. **Data cannot become rules** without an explicit, listed crossing.
5. **Floats are named as floats**, not as "reals".
6. **A test is a listed set of cases.** Green means those cases landed, not "for all".
7. **Effects are listed** (files, network, clock), and the clock is read only as its change.

## Steps: read any piece of code as an alphabet and mixing rules

Do this for a function, a module, a protocol or a whole device.

1. **List the letters.** For every variable, write its type and its range. Count them (`uint8`: 256; `bool`: 2; a struct: the product).
2. **List the mixing rules.** For every operation, write exactly what the machine does: wrap or saturate, rounding direction, what happens at the edge. Use the language's specification, not your expectation.
3. **Check closure.** Does every rule keep its output in the alphabet? Every place it does not is an edge: overflow, NaN, out of range, exception. Name each one.
4. **Check the algebra you rely on.** Do you assume a + b = b + a (strings: no), (a + b) + c = a + (b + c) (floats: no), a × (b + c) = a × b + a × c (floats: no; saturating integers: no)? Test each with values from the alphabet.
5. **Count collisions** for the rules you need to undo or to tell apart.
6. **Find the edges where values leave.** Prints, pixels, packets, files. Land each value there once, with a stated rule.
7. **Find the books.** What must be kept? Check it every step, beside a range check.
8. **Find the clocks.** Read each one only as its change.
9. **Carry a Reading through** the parts that use only +, −, ×, ÷, to get exact rates. Mark branches and landings.
10. **Plant one fault per rule** you depend on, and confirm a check catches it.
11. **Run on two machines** (desk and target), or in two alphabets (exact fractions and the production type), and compare line by line. Every difference names a place where the alphabets differ.

## Try it yourself

1. In `uint8`, what is 250 + 10? Is `x → x + 10` one-to-one? *Answer:* 4; yes (256 distinct outputs).
2. In Python, which is True: `-7 // 2 == -3` or `-7 // 2 == -4`? *Answer:* the second.
3. Which line breaks the Reading carry: `y = x * x + 1`, `y = round(x * 10)`, `y = x / (x - 2)`? *Answer:* the second: a landing in the middle.

```check
(250 + 10) % 256 == 4
collisions(lambda v: v + 10) == 256
-7 // 2 == -4
```

## Mistakes people make

- **Debugging a value without asking which alphabet it is in.**
- **Assuming a rule from one language holds in another** (division, shifts, overflow).
- **Treating a float result as a fraction**, or a hash match as equality.
- **Feeding the absolute clock into formulas.**
- **Letting a refusal become a crash or a silent default.**

## Next

Guide 19: designing your own alphabet and mixing rule to get a desired output.
