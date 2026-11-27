# 27. Evolutionary modelling

## The question

How do you model change over generations — of populations, designs, strategies, or your own models and claims — with no independent variable, no "fitness function" handed down, and books that close?

## The idea in one line (James's text)

"Evolution is just that process, not entities competing but coherence gradients testing whether accumulated relational history still matches available gradients. 'Fitness' is just: does your loaded history match the local coherence space?"

So in this method:

- nothing is scored by an outside fitness number;
- each pattern carries its loaded history L;
- the **context** (the field) sets what is available;
- whether a pattern keeps propagating is **read** from the run: served, refused, reconfigured.

## Two scales, one rule

| scale | the patterns | the field | loaded history L | reconfigure |
|---|---|---|---|---|
| a modelled population | strategies, designs, species-like patterns in a model | available resource, counted | what each has laid down | keep a core, vent the rest |
| your own models and claims | the claims you are developing | witnesses you can still gather | load L: alterations the claim needed | at L ≥ C, keep the unpatched core, vent the rest as a new claim (guide 20) |

The same three numbers do the work at both scales: support C, load L, drag D, with standing C / (C + L + D).

## Part 1: a population in a changing context (`examples/16_evolution`)

Four patterns draw on one field:

| pattern | support C | take | vent | cells |
|---|---|---|---|---|
| simple | 2 | 2 | half its L | {0, 1} |
| venting | 2 | 3 | a quarter | {1, 2} |
| heavy | 2 | 3 | none | {2, 3} |
| lonely | 1 | 2 | an eighth | {9} |

Halfway through, the context changes: the field is drained (counted). Then the run is read again.

**How to read it:**

- **Served counts** show which loaded histories match the context.
- **Reconfigurations** show which patterns hit their stability boundary.
- **Refusals** show when the context could not cover a pattern's demand.

No pattern is called fitter. Each reading names its cut: THETA, KAPPA, the take, the cells.

```check
f = Flux(400)
s = f.add("simple", C=2, cells={0, 1}, take=2, vent_num=1, vent_den=2)
h = f.add("heavy", C=2, cells={2, 3}, take=3, vent_num=0, vent_den=1)
_ = [f.latch() for _ in range(300)]
before = (s.served, h.served)
do f.drain(f.field - 2)
_ = [f.latch() for _ in range(300)]
f.books()
h.refused > 0
s.served > before[0]
```

After the drain, the field cannot always cover the heavy pattern's take of 3. It is refused (it lays nothing), while the simple pattern, whose own vents keep the field supplied, goes on being served. That is "does your loaded history match the local coherence space", read from the run rather than asserted.

## Part 2: evolving your own models (the method applied to itself)

Every model you build is a pattern in the field of evidence. Develop it the same way:

1. **Start simple.** The model with the least loaded history (fewest mechanisms, fewest exceptions) that the witnesses support goes first.
2. **Count witnesses C**: distinct ways it could have failed and did not (guide 20).
3. **Count load L**: every alteration it needed (a mechanism added, a scope narrowed, a constant tuned after looking).
4. **Count drag D**: the load of what it rests on.
5. **Read its standing**: v = C / (C + L + D).
6. **Reconfigure past the boundary.** At L ≥ C, stop patching. Keep the core that needed no patch, and vent the rest as a separate claim starting at L = 0.
7. **Vent simplicity.** Publish what failed, with how it failed. A model that never gives back its failures carries them as load.
8. **Effort already spent is not a term.** Sunk cost is not in the formula.

```check
standing(4, 0, 1) == (F(4, 5), "keep")
standing(3, 3, 0)[1] == "reconfigure"
```

## Steps: building an evolutionary model of your own

1. Define the **field**: what is available, in whole units, and what can leave it (counted as drained).
2. Define each **pattern's** support, take, vent and cells.
3. Choose THETA and KAPPA, and **write the kill lines before running** (guide 20): for example, "a heavier pattern served before a lighter one at equal due" or "the books open".
4. Run. Check the books and the front every latch.
5. **Change the context** at least once, and run at two settings of every choice (two cuts).
6. Report served, refused and reconfigured counts with their cuts, never "the fittest".

## Mistakes people make

- **Handing down a fitness number** and optimising it. A reading fed back into a rule is optimised for the reading, not for the situation (Part V, Unit V8).
- **Declaring drag** instead of computing it from contact.
- **Calling a reconfiguration a failure.** It is the rule that keeps a pattern inside its stability band.
- **Patching a model past L ≥ C.**

## Next

Guide 28: fluid dynamics without Navier–Stokes.
