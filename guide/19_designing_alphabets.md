# 19. Designing your own alphabet and mixing rule

## The question

The book picks one alphabet (pairs of fractions) and one mixing rule, and closes by pointing to "how to build a different one on a different alphabet". How do you design an alphabet and a mixing rule on purpose, to carry what you need or to produce an output you want?

## What this repo has already built, read as designs

| design | letters | mixing rule | what was forced | what was chosen | what it buys |
|---|---|---|---|---|---|
| Reading (guide 02) | (value, rate) | mix (guide 04) | division (guide 09) | the mix rule | exact rates through any chain |
| Triple (guide 10) | (value, rate, curve) | mix, plus the curve rule | the curve rule (the mix rule twice) | to carry a third slot | the rate of the rate |
| Lever (guide 17) | value plus one rate per source, plus a touched set | mix per slot | everything, once mix is fixed | to keep the touched set | absent / still / moving |
| Heading (guide 14) | (P : Q), whole numbers | combine | c*c + s*s = 1 | the heading formula | exact turns with whole numbers |
| Carry (guide 15) | (count, carry) | add top; while carry ≥ bottom, pulse | the books | half to even at the mouth | whole pulses with no drift |
| TSUZURI (microcontroller track) | letters designed by the chip | one table: (left, middle, right) → letter below | that a conflict forces a split | the starting alphabet, the merge order | a picture spelled exactly from a seed row |

Every row has the same parts. That is the template.

## The template: ten steps

1. **Say the output you want, as a check.** Not "a nice picture": "these 2,560 cells, ink or paper, exactly." Not "a fast physics": "the total heat kept exactly every step, and no place below zero."
2. **List what must be carried** for that check to be possible. If the output depends on how fast something changes, carry a rate. If it depends on which inputs touched it, carry a touched set.
3. **Choose the letters**: the smallest structure that carries the list. Write the alphabet down: what one letter is, and how many there are (or that they are fractions).
4. **Choose one mixing rule and fix it.** Write it once. Every later combination uses it. If you find yourself wanting a second rule for "the second time", the first rule was not general enough.
5. **Derive, do not pick, everything you can.** Inverses (guide 09), higher slots (guide 10) and per-source slots (guide 17) follow from the first rule. Mark which rules are forced and which are chosen, and say what each choice buys.
6. **Check closure.** Every rule's output must be a letter. Where it is not, name the refusal.
7. **Check the books.** What does the rule keep? Write it as an equation you check every step, and add a range check beside it (conservation is not correctness).
8. **Define the reading**: how letters fold onto what you show. Keep the reading out of the rules: a rule never reads a reading.
9. **Certify against the output.** Run the rule from the start and compare every reading with the target. Count matches: "2560 of 2560", not "looks right".
10. **Plant faults and change cuts.** Break each rule once and confirm the certificate catches it. Change at least two choices (the starting alphabet, the order of steps, the seed) and see which results move.

## A worked design: letters that spell a picture (TSUZURI, in small)

**Output wanted:** a picture of rows of cells, ink or paper. Every row below the first must come from the row above by one table: cell = MIX(left, middle, right).

**Steps 2 to 4:** start with the alphabet = the two colours. MIX is a lookup table from three letters to one.

**Step 5, what is forced:** wherever one triple above must give two different letters below (a **conflict**), the alphabet is too coarse. The fix is forced: split the middle parent's letter by what it becomes below (the letter learns its future). The alphabet only grows; it must close, because each split separates cells that need separating.

**Chosen:** the starting alphabet, which conflict to split first, and a greedy squeeze afterwards that merges letters of the same colour two at a time, keeping a merge only if the table stays a function.

**Step 9:** play MIX from the seed row and compare every cell's colour with the target.

Results on the chip, desk and emulator, all equal (from the TSUZURI work):

| target | conflicts with the colours alone | letters after refining | after squeezing | play |
|---|---|---|---|---|
| SIERPINSKI | 0 | 2 | 2 | 2560/2560 |
| DISC | 100 | 111 | 46 | 2560/2560 |
| WORD ("RULE") | 128 | 153 | 89 | 2560/2560 |
| RINGS | 1278 | 195 | 39 | 2560/2560 |

**What it shows:** the cost of a target belongs to the alphabet and the mixing rule as much as to the target. The Sierpinski picture costs 2 letters, because XOR of the two neighbours is already its rule. The rings, with 1,278 conflicts at the start, squeeze to 39 letters. The squeeze is greedy, so 39 is a roof, not proved the smallest: no floor was computed.

`examples/13_custom_alphabet` runs a small version of this in Python, with a planted fault.

## A second worked design: a Reading over `uint8`

Suppose a chip can hold only 8-bit numbers and you want rates. Make the letters (value, rate) with each slot a `uint8`, and use the mix rule with every product and sum taken mod 256.

- **Closed:** yes, mod 256 keeps every output in the alphabet.
- **The books:** none; the alphabet wraps.
- **Division:** forced to need an inverse of the divisor's value mod 256, which exists only for odd values. So division refuses on every even value, not just 0. The derivation in guide 09 still forces the rule; the alphabet changes where it refuses.

```check
def mix8(a, b): return ((a[0] * b[0]) % 256, (a[1] * b[0] + a[0] * b[1]) % 256)
mix8((4, 1), (4, 1)) == (16, 8)
mix8((20, 1), (20, 1)) == (144, 40)
collisions(lambda v: v * 2) == 128
collisions(lambda v: v * 3) == 256
```

The second line: 400 mod 256 = 144. The rate 40 is still exact, because 40 < 256. Once a rate passes 255 it wraps too: the alphabet says so, and a design document must say so.

## Check closure by scanning every input

A mixing rule works on an alphabet only if every output lands back in it. On a finite alphabet, check every input (`scan_closure`).

- The mix rule on bits {0, 1}: (1, 1) × (1, 1) gives rate 2, which is not a bit. It leaks on 1 input of 16.
- The same strips combined with XOR or with OR close on all 16. XOR is arithmetic mod 2, where 2 = 0, so there the rate of x*x is genuinely 0.
- On {0, 1, 2} the plain rule leaks on 28 of 81 inputs; reduced mod 3 it closes on all 81.
- Ordinary division on {1, 2, 3, 4} leaves the alphabet on 8 of 16 pairs.

```check
scan_closure({0, 1}, {0, 1}, lambda v1, r1, v2, r2: (v1 * v2, r1 * v2 + v1 * r2))[:2] == (1, 16)
scan_closure({0, 1}, {0, 1}, lambda v1, r1, v2, r2: (v1 * v2, (r1 * v2) ^ (v1 * r2)))[:2] == (0, 16)
scan_closure({0, 1}, {0, 1}, lambda v1, r1, v2, r2: (v1 * v2, (r1 * v2) | (v1 * r2)))[:2] == (0, 16)
scan_closure({0, 1, 2}, {0, 1, 2}, lambda v1, r1, v2, r2: (v1 * v2, r1 * v2 + v1 * r2))[:2] == (28, 81)
scan_closure({0, 1, 2}, {0, 1, 2}, lambda v1, r1, v2, r2: ((v1 * v2) % 3, (r1 * v2 + v1 * r2) % 3))[:2] == (0, 81)
scan_closure2({1, 2, 3, 4}, lambda a, b: F(a, b))[:2] == (8, 16)
```

When a scan finds a leak you have three honest choices: **wrap** the output back into the alphabet (a new rule, stated), **refuse** the input (θ), or **grow** the alphabet to hold it (a stated migration). Choosing silently is the one dishonest choice.

## Moving between alphabets: morphisms

A map f from one alphabet to another is a **morphism** only if it commutes with the rules: f(rule_a(a, b)) = rule_b(f(a), f(b)) for every pair. Check it on every pair, and print the first pair that fails.

On three truth values {0, 1/2, 1}, the map "1 stays 1, everything else becomes 0" commutes with AND as min, but fails for NOT (v → 1 − v): at 1/2, f(NOT 1/2) = 0 while NOT f(1/2) = 1.

```check
f = lambda v: 1 if v == 1 else 0
morphism(f, lambda a, b: min(a, b), lambda a, b: min(a, b), [0, F(1, 2), 1]) == (True, None)
morphism(f, lambda a, b: 1 - a, lambda a, b: 1 - a, [0, F(1, 2), 1]) == (False, (F(1, 2), 0))
```

Porting code, converting types and translating a model into another tool are all maps between alphabets. Check that each map commutes with the rules you rely on, or scope the claim to the rules it does commute with.

## The six-step mapping (propagation-logic's admission gate)

To bring any formal system into this way of working:

1. **Identify V**: what does it return or produce?
2. **Identify G**: what can be done to elements of V?
3. **Identify θ**: what counts as accepted, and what happens at the edge?
4. **Derive the forced laws by enumeration**: on a finite V, check every input under every rule; on a continuous V, verify identities exactly (symbolically or in fractions). A law is FORCED only if the check decides it.
5. **Find failures by counterexample**: one witness is enough, and the check should print it.
6. **Find morphisms** to other systems: maps that commute with the rules.

When a source document and the enumerator disagree, the enumerator wins and the record says so.

## Five guardrails

1. No named V, G, θ: not a claim yet.
2. Two presentations agree: grow V before calling them one G.
3. A step leaves V: fire θ, or run a registered migration. Never append silently.
4. A label that changes no knob is a comment.
5. Work happened: a ledger line, or the ledger is wrong.

## Mistakes people make

- **Two mixing rules for "different cases".** One rule, fixed once.
- **A reading that feeds a rule.** The moment a rule reads a summary, the rule optimises the summary (Part V, Unit V8).
- **Checking that the books hold and stopping there.** Add the range check.
- **Calling a greedy result optimal.** A greedy result is a roof. Say so, or compute a floor.

## Next

Guide 20: checking your work.
