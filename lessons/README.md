# Lessons: practice you write yourself, graded by a checker that has been checked

Each lesson asks you to write one file in `lessons/work/`. A checker then runs it and prints one line per check, ending `PASS (n of n checks held)` or `FAIL`. Every checker has been run against planted wrong answers (`planted/`) and shown to catch each one, so a PASS means something.

## How to do a lesson, step by step

1. **Read the guides the lesson names.** Do the guide's checked examples by hand first.
2. **Read the lesson's spec below**: the file to write, the functions it must provide, and what is checked.
3. **Write your prediction down** before you start: which check do you expect to be hardest, and why?
4. **Write your file** in `lessons/work/` under the exact name given. Use only Python's standard library. Do not import `ratecalc` in your work file: the point is to build the moves yourself.
5. **Run the checker:**

   ```text
   python3 lessons/L01_readings/check.py
   ```

6. **Read every FAIL line.** Each names the check and what it got and wanted. Fix your file, not the checker.
7. **Log the attempt** in the ledger (it is hash-chained; nothing is edited or deleted):

   ```text
   python3 tools/ledger.py add run "L01 attempt 2: FAIL on the derived division"
   ```

8. **Repeat until PASS.** A failure you then fix is a `fail` event followed by an `intervene` event.
9. **See that the checker can fail:**

   ```text
   python3 lessons/L01_readings/check.py --planted
   ```

   It must say `caught N of N planted faults`.

**Do not open `planted/` or `reference/` before you pass.** `planted/` holds wrong implementations and `reference/` holds working ones, kept so `tools/check_all.py` can show each checker passes a correct file and fails every wrong one. If you looked first, log a `self` event: the lesson then witnesses less.

## The lessons

| # | Lesson | Your file | Guides |
|---|---|---|---|
| L01 | Readings and the three moves | `L01_readings.py` | 02 to 11 |
| L02 | Which answer belongs to which cut | `L02_cuts.json` | 07, 11 |
| L03 | Rules with proven bounds | `L03_rules.py` | 12, 13 |
| L04 | Headings and exact turns | `L04_heading.py` | 14, 15 |
| L05 | Transfer, never assign | `L05_transfer.py` | 16 |
| L06 | The lever | `L06_lever.py` | 17 |
| L07 | Alphabets: closure and morphisms | `L07_alphabet.py` | 18, 19 |
| L08 | A fluid on a ring | `L08_fluid.py` | 28, 16 |
| L09 | The useful pattern | `L09_pattern.py` | 26, 27 |
| L10 | A kill line, sealed before the read | `L10_KILL_LINES.md`, `L10_REPORT.md` | 20 |
| L11 | De-reify one map | `L11_MAP.md` | 01, 26 |

### L01 readings: `work/L01_readings.py`

Provide:

```python
THETA                    # a named refusal: not a number (not an int, float or Fraction); returned, never raised
isolate(v, r=1)          # -> (Fraction(v), Fraction(r)); refuses a float argument by raising
add(a, b), sub(a, b)     # piece by piece
mix(a, b)                # (v1*v2, r1*v2 + v1*r2)
div(a, b)                # derived: q = v1/v2, s = (r1*v2 - r2*v1)/v2**2; THETA when b's value is 0
rate(a, b)               # a's rate slot over b's; THETA when b's rate slot is 0
when(gap)                # latches until the value runs out: -value/rate; THETA when the rate is 0
```

Checked: 30 cases from the book's demonstrations, the seed cancelling on random expressions, division undoing mix on random pairs, and the refusals. Planted: 6 (rates multiplied, theta as a huge number, a dropped strip, when upside down, theta reading as 0, floats inside).

### L02 two cuts: `work/L02_cuts.json`

With your L01 module: A = isolate(0, 5), B = isolate(10, −3), rope = A − B. Measure which of `rate(rope,A)`, `rate(B,A)`, `grow` (rope's rate over its value) and `when(rope)` move under four cuts:

- **naming:** rope = B − A;
- **direction:** every place and rate negated;
- **seed:** every rate times −1;
- **scale:** every place and rate times 3.

Write `{"rate(rope,A)": {"naming": "moves" or "stays", ...}, ...}`. Planted: 3.

### L03 rules: `work/L03_rules.py`

Provide:

```python
sqrt2_bracket(gap)  # -> (low, high, steps): Fractions with low*low < 2 < high*high and high - low < gap, by halving
                    #    from [1, 2], in the fewest steps; a float gap is refused with TypeError
e_within(tol)       # -> (value, bound, n): the first stage n whose proven tail bound 1/(n+1)! * (n+2)/(n+1) is
                    #    below tol, value = 1 + 1/1! + ... + 1/n!, and that bound
stage(top, tol)     # -> the first whole n with top/n < tol
```

Checked: five gaps, five tolerances (including the edge 1/4410), four stages, a float refused. Planted: 4.

### L04 heading: `work/L04_heading.py`

Provide:

```python
unit(P, Q)               # (Q*Q - P*P, 2*P*Q, P*P + Q*Q), whole numbers
compose(h1, h2)          # (P1*Q2 + P2*Q1, Q1*Q2 - P1*P2)
turn_point(x, y, P, Q)   # the whole-number plane turned by (P:Q) with three shears, each landed by the mouth
unturn_point(x, y, P, Q) # its inverse
```

Checked: exact units on 624 headings; composition against turning the units on 100 pairs; on a 61 × 61 box for five headings: no two points to one, unturn(turn(p)) = p, turn(−p) = −turn(p), each image within 2 units of the exact turn. Planted: 4.

### L05 transfer: `work/L05_transfer.py`

Provide `step(h) -> list` on 64 places in a ring: heat spreads by transfer between neighbours. Checked over 2,000 steps: whole numbers; the total held every step; no place ever negative; it spread (the tallest place below half its start). Planted: 3, one of which holds the total exactly while half the places go negative.

### L06 lever: `work/L06_lever.py`

Provide `source(name, value)` returning a lever object with `+` and `*` (with plain numbers too), `.value`, `.state(name)` (`"absent"`, `"still"` or `"moving"`) and `.rate_of(name)`. Checked: the book's price × qty example with fee, floor and tax; y = a × b + b × b; 200 random points of a polynomial in two sources. Planted: 3.

### L07 alphabet: `work/L07_alphabet.py`

Provide:

```python
scan_closure(Vv, Vr, mix)        # -> (leaks, total): every input of a pair rule over finite slot alphabets
morphism(f, rule_a, rule_b, V)   # -> (True, None), or (False, (a, b)) with the first pair, in order, where
                                 #    f(rule_a(a, b)) != rule_b(f(a), f(b))
```

Checked: the leaks of the mix rule on bits and on {0, 1, 2}, XOR and mod-3 closures, a leak in the rate slot only, and four maps between alphabets. Planted: 3.

### L08 fluid: `work/L08_fluid.py`

Provide `step(s, m) -> (s, m)` on a ring of 64 places with whole-number stuff `s` and momentum `m`. Use only trades at faces (PUSH by the crowding on both sides, and any of DRAG, EXCHANGE and MOVE you need), each reading the latch as it was found. Do not change the lists you are given.

Checked over 3,000 latches from a bump of crowding: whole numbers; stuff and momentum each equal to the start every latch; every place keeps stuff > 0; the bump spreads; and the **mirror**: the ring read the other way round gives the mirrored latch, so your faces carry no sweep-order bias. Planted: 3 (push by the difference, a momentum set instead of traded, faces swept in place).

### L09 pattern: `work/L09_pattern.py`

Provide a class `Flux(field, THETA=60, KAPPA=4)` with `add(name, C, cells, take, vent_num, vent_den)` (returning a pattern with `.name`, `.served`, `.refused`, `.reconfigs`, `.L`), `latch()`, `drain(amount)`, `books()`, `.field`, `.p` (the patterns in order), `.THETA` and `.front_moved_back`. Run the six clauses exactly as the table in guide 26 states them, ties broken by the lighter L and then by order. Checked on two scenarios: the books every latch, the field never below zero, the front never moving back, a reconfigured pattern within THETA, and served / refused / reconfigured / L equal to the library's run. Planted: 4.

### L10 kill line: files and the ledger

1. Tune a threshold on the tuning set as often as you like: `python3 lessons/L10_kill_line/score.py 30`.
2. Write `work/L10_KILL_LINES.md`: the claim, a line with `pass mark` and a number (out of 200, on the sealed set), and a line with `kill line` naming the output that would show it false.
3. Seal it: `python3 tools/seal.py lessons/work/L10_KILL_LINES.md`.
4. Read the sealed set **once**: `python3 lessons/L10_kill_line/read_sealed.py <threshold>`.
5. Write `work/L10_REPORT.md` quoting both scores exactly and saying whether the kill line fired.

Checked: the chain unbroken; the seal before the read; one read; scores quoted; the verdict matches the numbers. Planted: 3.

### L11 de-reify: `work/L11_MAP.md`

Take one map (a model, a diagram or a sentence that writes readings as things) and rewrite it as relations (guide 01, rule 8; guide 26). The file must hold:

- a table whose header has four columns: **map | what it reifies | the relation | what you use**, with at least 4 rows;
- a section **What pays** where every kept property carries one tier word: FORCED, EMPIRICAL, CONDITIONAL, STIPULATED, PRESUMED or UNPAID;
- a line starting `Kill line:` naming an output that would show your relations wrong;
- a line starting `Known:` naming which parts are known techniques (prior art), or `Known: none found` with where you looked;
- no refused word outside quotes (`tools/wordlint.py`).

The checker reads the shape and the words only. Whether the relations are right is for a person to read. Planted: 4.
