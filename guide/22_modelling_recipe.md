# 22. The modelling recipe: any problem, step by step

## The question

You have a problem from any field: money, motion, populations, a machine, a program. How do you set it up and solve it with this method, from nothing, without leaving out a step?

## The recipe

### Phase A: say what you want

1. **Write the question as a check you could run.** "When will the tank be empty, to the latch?" "Is the rate of profit against price positive at this price?" "Do the drones come within 2 m?"
2. **Write the kind of claim it will be.** Kind 1 (calculation) or kind 2 (about the world: needs measurement). If kind 2, name the measurement that would check it.

### Phase B: build the readings

3. **List every quantity**, with units.
4. **For each, find its value now and its rate now**, and against what the rate is counted (per minute, per unit of price, per latch).
5. **Choose the comparison quantity**, the one everything is compared with, and seed it with rate 1: `clock = isolate(0, 1)` or `price = isolate(12)`. This replaces the independent variable (house rule 1).
6. **Write every other quantity as a Reading** built from `isolate`, plain numbers `(c, 0)`, and the moves. Write still things with rate 0.
7. **Check units**: every rate in one comparison is per the same thing.

### Phase C: ask with the moves

8. **For "how fast compared with"**: `rate(A, B)`. Refuse on `theta`.
9. **For "what if combined"**: build the expression with a step table (guide 06). For many inputs, use levers (guide 17).
10. **For "when"**: make a gap and read `when = −value / rate` (guide 11). Two directions: `closest`.
11. **For a number that is not a fraction**: a rule with a requested precision (guide 12).
12. **For a quantity defined by its rate law**: the shortfall construction (guide 13).
13. **For a system that runs forward**: the stepping recipe (guide 16), with transfer for kept quantities, the books every latch, and the grain as a cut.
14. **For turning**: headings (guide 14).
15. **For a device or a fast loop**: whole numbers, the carry, the mouth (guide 15).
16. **For code**: read it as an alphabet and mixing rules (guide 18).

### Phase D: check

17. **Recompute values by plain arithmetic; multiply back divisions.**
18. **Two cuts:** change the naming, the seed, the grain, the units. Report what moved.
19. **Plant a fault** beside each check.
20. **For a kind 2 claim:** write the kill line before the measurement; measure; compare.

### Phase E: report

21. **Write the report** (guide 21): result with tier, run, not run, please run, planted fault, choices.

## Worked example: a draining tank and a refilling pump

**Question (step 1):** a tank holds 500 L and drains at 10 L/min. A pump that adds 4 L/min starts now. When does the tank empty, and how fast is the level changing compared with the pump's delivery?

**Kind (step 2):** kind 1 given the rates; kind 2 for a real tank (measure the drain).

**Readings (steps 3 to 7):**

- clock = isolate(0, 1), counted in minutes;
- drain contribution: the tank alone = isolate(500, −10);
- pump delivered = isolate(0, 4);
- tank with pump = tank + pump = (500, −6).

**Ask (steps 8 to 10):**

- when the tank empties: the tank's level is its own gap to zero: when = −500/−6 = 250/3 minutes;
- rate(tank with pump, pump) = −6/4 = −3/2: the level falls 3/2 L for every litre the pump delivers;
- rate(tank with pump, clock) = −6 L/min.

```check
clock = isolate(0, 1)
tank = isolate(500, -10)
pump = isolate(0, 4)
level = tank + pump
level == R(500, -6)
when(level) == F(250, 3)
rate(level, pump) == F(-3, 2)
rate(level, clock) == -6
# land the when on whole minutes only at the edge, for a display
mouth_of(when(level)) == 83
```

**Check (steps 17 to 19):** after 250/3 minutes at −6 L/min, the change is −500, which uses up the 500. Two cuts: measure in seconds (rates ÷ 60), and `when` becomes 5000 seconds, the same moment. The planted fault `meet-sign` turns the `when` line red.

```check
level = isolate(500, -10) + isolate(0, 4)
level_s = isolate(500, F(-6, 60))
when(level_s) == 5000
when(level_s) == when(level) * 60
```

**Report (step 21):** `when` = 250/3 min (FORCED, given the stated rates; EMPIRICAL only once the drain is measured). Run: this guide's checks. Not run: any measurement. Choices: none beyond the mix rule.

## Next

Guide 23: mistakes and presumptions.
