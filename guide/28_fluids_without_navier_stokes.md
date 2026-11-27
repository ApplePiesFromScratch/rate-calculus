# 28. Fluid dynamics without Navier–Stokes

## The question

A course models moving air or water with the Navier–Stokes equations: partial derivatives in a free-running time t and space x, a viscosity term, and a pressure that keeps the flow from being squeezed. Can a fluid be modelled with this method instead: no independent variable, no imported equation, whole numbers, and books that close exactly every step?

Yes. The construction here follows the project's NAGARE and FLOWING work and runs in `ratecalc/flow.py`.

## What the textbook does, and what it leaves open

```text
MASS    ∂ρ/∂t + ∇·(ρu) = 0
MOTION  ∂u/∂t + (u·∇)u = −∇p/ρ + ν∇²u + g
ENERGY  ∂T/∂t + u·∇T = κ∇²T + Q
```

To run these, a course picks a time step DT, a grid, and a solver (for example, stable fluids with a pressure projection by Jacobi sweeps). Each choice is a cut. The equations are written in t and x; the solver discretises them; and whether mass, heat and momentum are kept exactly depends on the solver and the iteration count, not on the equations. In the project's side-by-side run, the textbook method's heat book swung from −0.4% to +46.5% during a puff (heat it held that nothing put in), at the iteration count usually taught.

## What this method does instead

Each **place** (a cell of a grid) holds three whole numbers:

- **stuff** `s`: how much air is there;
- **carried rate**, kept as momentum (`mx`, `my`): stuff times how far it is carried in a latch;
- **warmth** `w`.

**Every change is a hand-on between neighbours** (one take, one give), or an entry from outside that is counted. There is no DT: a latch is one round of trades.

| letter | what it does | what it replaces in the textbook |
|---|---|---|
| PUSH | at each face, the crowding on both sides pushes them apart: rate taken from one side, given to the other. A place feels the difference between its two faces, so even crowding cancels | the pressure gradient −∇p |
| DRAG | at each face, neighbours trade rate by how much they differ, along the face's line more strongly than across it | viscosity ν∇²u |
| EXCHANGE | stuff is handed down its own difference to the neighbour, with its share of rate and warmth. PUSH reads two places apart and cannot see an alternation; this sees it | the grid's checkerboard fix |
| LIFT | a place warmer than the box as a whole is handed upward rate, a cooler one downward. The context is the box's own warmth; the ground's hand is counted | buoyancy (Boussinesq) |
| MOVE | at each face, stuff is carried by the rate there, from the upwind side, with its share of rate and warmth | advection (u·∇) |
| FEED, VENT | a heater puts warmth in at the floor; the cold lid takes a share out; both counted | sources and boundary conditions |
| WALLS | each wall face pushes its place away with the place's own crowding, and rate carried into a wall is turned round; counted | no-slip / no-flux walls |

**Every trade reads the places as the latch found them.** All trades are handed on together afterwards. (If faces are swept one after another, each reading the last one's result, a still box drifts.)

## The books, every latch

- **stuff** = start;
- **warmth** = start + fed − vented;
- **momentum**, each direction = start + what the walls and the ground gave;
- **range**: stuff > 0 and warmth ≥ 0 in every place.

The books close **exactly**, not to a tolerance. That is forced by construction: every letter is one take and one give, or a counted entry. A planted line that *sets* a warmth instead of trading it (here, halving the middle place's warmth in place) opens the books at exactly that latch, so the books can see a set.

```check
b = Box()
do b.puff(16, 17, 4000)
ok = all(all(b.books()) and b.in_range() for _ in range(300) if b.latch() is None)
ok
b.warm_row() < 6
min(b.s) > 900 and max(b.s) < 1100
p = Box()
p.plant = "assign"
do p.puff(16, 10, 4000)
do p.latch()
all(p.books()) == False
```

Reading it: a puff laid at the floor (row 17 of 20) rises to within the top six rows in 300 latches. Every place's stuff stays within 10% of its start (the air is compressible: it carries crowding ripples, which is sound). All books close on every latch. The planted set, with a puff laid at the middle, opens them at the first latch.

## Readings, each with its cut

- **Warm row:** the warmth-weighted row of the warmth above the box's mean (rows count down from the lid). The cut: above-mean warmth, the whole box.
- **Turning:** the rate carried round a 2 × 2 loop. A different loop size reads a different turning; say which.
- **Speed:** momentum over stuff in a place. It moves with the grain of the grid.

None of these readings is "the flow". Each is a rule applied at a cut (guide 07).

## How it compares, honestly

- **What it is not:** a solution of the Navier–Stokes equations. The letters were built from the method. Results are compared with the textbook by readings, not assumed to match.
- **Constants are choices:** KP (push), KD (drag), KE (exchange), KL (lift), KM (move). The pace of a rise depends on them, so a pace is not a result unless both sides' constants are named.
- **Where it differs, it differs for a reason the rules show.** In the project's runs, a steady heater's warmth pooled at the floor instead of rising in a thin column, because LIFT reads warmth against the box as a whole, and a steady heater warms the whole box. The rule ran literally; the reading came out different from the textbook's. Report such a difference with its reason, not as an error to hide.
- **Sound is kept**; the textbook's incompressible projection removes it.

## Steps: modelling a fluid this way

1. **Choose the places** (a grid) and what each holds: stuff, momentum per direction, and any carried quantity (warmth, dye, salt).
2. **Write each letter as a trade at a face**, reading the latch as it was found. Never set a place's value from a formula of its neighbours (guide 16).
3. **Write every outside entry as counted**: feeds, vents, walls, ground.
4. **Write the books** and check them every latch, beside the range.
5. **Plant a set** and confirm the books open at that latch.
6. **Choose the constants**, name them, and run at two settings of each (two cuts).
7. **Read** with named cuts: warm row, turning round a stated loop, speed at a stated grain.
8. **Compare** with any other method by readings, and report differences with the rule that produces them.
9. **Write kill lines before the comparison** (guide 20): for example, "the puff's warm row is above row 6 by latch 300", or "a book opens".

## Try it yourself

1. Run `examples/15_fluid` and read the warm row every 50 latches.
2. Double KL (lift) and run again. Which readings move? *Answer:* the pace of the rise; the books do not.
3. Turn the heater on instead of a puff. Where does the warmth go, and why? (Use the LIFT row of the table.)

## Mistakes people make

- **Sweeping faces in order**, each reading the last one's result: a still box drifts.
- **Pushing by the difference of crowding instead of the crowding on both sides**: places empty and pile up.
- **Relating lift to the neighbour instead of the context**: a puff shreds into streaks.
- **Absorbing rate at a wall without the wall's push**: stuff piles against the walls.
- **Treating "matches Navier–Stokes" as the pass mark.** The pass marks are the books, the range and readings with kill lines written first.

## Next

Guide 29: a bridge sheet for students who must also sit a standard course.
