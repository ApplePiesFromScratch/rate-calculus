# 26. The useful pattern, run as rules

## The question

James Pugmire's framework, *the useful pattern*, describes how relational patterns propagate: they gain a loaded history, the history sets what they demand of the gradients around them, the simplest propagate fastest, they meet drag, and past their stability boundary they reconfigure. How do you turn that into rules a program runs and a check can fail?

## The text, in brief (James's words, quoted)

- "As relational patternings propagate they gain a loaded history relative to available gradients they remain stable in."
- "The simplest patterns ... will propegate the fastest relative to more complex structure."
- "When complexity demands exceed available gradients patterns reconfigure to more relationally coherent structuring."
- "Fitness is just: does your loaded history match the local coherence space?"

The method takes these as clauses and gives each one a rule, a book that checks it, and a kill line that would show it false. Mapping James's words to these rules is a choice (STIPULATED). His reading of his own text outranks this guide.

## Six clauses, as rules (`ratecalc/pattern.py`)

| clause | the rule | the book that checks it | kill line |
|---|---|---|---|
| UP1 loaded history | a served pattern takes `take` units from the field into its loaded history L | field + every L = G0 − drained | a latch where the sum opens |
| UP2 demand set by history | its next due mark moves forward by (C + L + D)/C | the front never moves back | a front that moves back |
| UP3 simplest propagates fastest | the earliest due mark is served next (ties: lighter L), so propagation goes at C/(C + L + D) | min over due marks picks the next | a heavier pattern served before a lighter one at equal due |
| UP4 drag | D = the loaded history of other patterns met in shared cells, computed from contact each latch | drag from contact, never declared | drag present with no shared cell |
| UP5 reconfigure past the boundary | past THETA: keep KAPPA/16 of L, vent the rest to the field, start again at the front | vented + kept = L before | a pattern past THETA that keeps all of L |
| UP6 vent simplicity | after each service, a pattern gives a share of L back to the field | the vented amount enters the field | a vent that leaves the field unchanged |

Underneath, it is the book's arithmetic: every quantity is a whole number that is **moved, never set**, the due marks are exact fractions, and a pattern served when the field cannot cover its take lays nothing: a named refusal, counted.

```check
f = Flux(400)
a = f.add("simple", C=2, cells={0, 1}, take=2, vent_num=1, vent_den=2)
b = f.add("heavy", C=2, cells={2, 3}, take=3, vent_num=0, vent_den=1)
_ = [f.latch() for _ in range(500)]
f.books()
(a.served, b.served, b.reconfigs) == (428, 72, 4)
b.L <= f.THETA
f.front_moved_back == False
g = Flux(400)
a2 = g.add("simple", C=2, cells={0, 1}, take=2, vent_num=1, vent_den=2)
b2 = g.add("heavy", C=2, cells={1, 2}, take=3, vent_num=0, vent_den=1)
_ = [g.latch() for _ in range(500)]
g.books()
(a2.served, b2.served) == (232, 268)
```

Reading the two runs (two cuts: where the patterns sit):

- **Apart** (no shared cell): the light, venting pattern is served 428 times in 500 latches; the heavy one that never vents, 72 times, passing THETA 4 times and each time keeping a core and venting the rest.
- **Sharing one cell:** the simple pattern now meets the heavy one's loaded history as drag (UP4), and is served 232 times; the heavy one, 268. The simple pattern did not change; its context did.

The books close on every latch in both runs. A reading such as "the simple pattern is served most" holds at one cut and not the other, so it belongs to the cut as much as to the patterns (guide 07).

## The procedure behind it (ontic structural logic)

James names three inference shapes. As a procedure a model can follow:

1. **State the relation, not the thing.** "Warmth relative to the box", not "hot stuff".
2. **Map its loaded history**: what came before and stayed stable (the books, the ledger).
3. **Map the band of conditions it stays stable in**: at least two cuts (guide 07).
4. **Ask three questions of your own labels:**
   - Does a label stand in for a thing?
   - Does the account add anything it does not use (parsimony)?
   - What output would show it false (a kill line)?

## The paradox breakdown, as a check on your own writing

James's five steps, used on a draft:

| step | what to look for | the fix |
|---|---|---|
| 1 reify a process | a verb turned noun: "the swirl", "the budget" | name the relation and the cut |
| 2 define it by relations | comparisons, couplings, places | keep those: they are the content |
| 3 assert it is intrinsic | "really", "just has", "in itself", "the true value" | delete, or name which cut |
| 4 the contradiction | said to be non-relational, only described relationally | the relational description was the answer |
| 5 meta-moves | "in one sense ... in another sense", "profound", "mystery" | run a test at two cuts instead |

## Steps: running the pattern on your own system

1. **List the field**: what is available to be drawn on, as a whole number of units, and what can leave it (counted).
2. **List the patterns**: for each, its support C, where it sits (cells), what one service takes, what share it vents.
3. **Choose THETA and KAPPA** (stability boundary, kept core). Both are choices; name them.
4. **Run latches.** Check the books every latch, and that the front never moves back.
5. **Read** served counts, loaded histories, reconfigurations and refusals. Each is a reading at a cut (the cells you chose, THETA, the take).
6. **Change the context** (drain or feed the field) and read again. That is guide 27.

## What this guide does not claim

- That these six rules are the only reading of James's text.
- That any reading here extends to fields the text speaks of beyond these runs (cosmology, measurement, mind). Those are not tested here.
- **Tiers:** the books are FORCED (whole numbers moved, checked every latch); the readings are EMPIRICAL on the runs shown; the mapping from words to rules is STIPULATED.
