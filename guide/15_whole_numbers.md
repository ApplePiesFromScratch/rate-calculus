# 15. Whole numbers: the mouth and the carry

## The question

On a chip, in a long simulation, or anywhere exact and fast matters, quantities must be held as whole numbers. How do you keep a fractional rate without drift, and where should a fraction become a whole number? (Part V, Units V1, V2)

## The carry: a rate as whole pulses (Unit V1)

A wheel should turn 4/3 of a step every tick, and a motor takes only whole steps. Keep the remainder for the next tick:

1. Each tick, add the rate's top (n) to a running remainder (the **carry**).
2. **While** the carry is at least the bottom (d), send one whole pulse and take d off.
3. Count the pulses.

The **books**, true after every tick: `d × count + carry = n × ticks`, with `0 ≤ carry < d`. Nothing is lost, so nothing drifts.

**7/3 by hand:**

```text
tick 1: emit 2, carry 1, count 2;  3*2 + 1 = 7  = 7*1
tick 2: emit 2, carry 2, count 4;  3*4 + 2 = 14 = 7*2
tick 3: emit 3, carry 0, count 7;  3*7 + 0 = 21 = 7*3
```

**Why "while" and not "if":** at 7/3 one tick can owe three pulses. An `if` sends one and lets the carry grow without bound. The books still hold, because they count the carry, so the bound `0 ≤ carry < d` must be part of the check. **Books that hold are not a rule that works.** `tools/check_all.py` plants the `if` (`RC_PLANT=carry-if`) and confirms the checks catch it.

```check
c = Carry(7, 3)
[c.tick() for _ in range(3)] == [2, 2, 3]
c.books()
c.count == 7
k = Carry(4, 3)
"".join(str(k.tick()) for _ in range(24)) == "112" * 8
k5 = Carry(5, 4)
[k5.tick() for _ in range(6)] == [1, 1, 1, 2, 1, 1]
```

At 4/3 for 100,000 ticks the count is 133,333 and the books held every tick (`tests/test_core.py`). A float accumulator adding 1.333… each tick rounds wherever 4/3 cannot be written in binary; Part V reports it wrong on 33,333 of those ticks.

## The mouth: landing once (Unit V2)

**The mouth** turns a fraction into a whole number:

- the nearest whole number;
- an exact half goes to the **even** neighbour;
- mouth(−x) = −mouth(x) (mirror-true).

It is used **once, at the edge**, where a quantity leaves the rules (a pixel, a motor step, a printed cent), never in the middle of a chain.

> **A choice, not a discovery.** Half to even is picked because it is the usual rule that is unbiased over many halves and keeps the mirror: a heading (P : Q) and (−P : −Q) stay the same heading after landing.

The two common "round down" rules disagree on negatives, which is why neither is used as the mouth:

```check
toward_negative(-7, 2) == -4
toward_zero(-7, 2) == -3
[mouth(1, 2), mouth(3, 2), mouth(5, 2), mouth(-1, 2), mouth(-3, 2)] == [0, 2, 2, 0, -2]
[mouth(5, 2), mouth(7, 2), mouth(-5, 2), mouth(-7, 2), mouth(10, 3)] == [2, 4, -2, -4, 3]
all(mouth(-n, d) == -mouth(n, d) for n in range(-300, 301) for d in range(1, 30))
[mouth(9, 2), mouth(11, 2), mouth(-9, 2)] == [4, 6, -4]
```

**Why once:** each landing can lose up to half a unit. Landing once loses it once. Landing after every multiply piles the losses up, and a product of landed numbers carries them all.

**A shift is a landing too:** `x >> 1` divides by 2 and lands toward the more negative number. On 3 it gives 1 where the mouth of 3/2 gives 2; on −1 it gives −1 where the mouth gives 0.

## Steps: moving any calculation to whole numbers

1. Choose a scale (a whole number S) so the fractions you need become whole: hold `value × S`.
2. Keep every rate as a fraction n/d of whole numbers, and send it with a carry.
3. Check the books every step: `d × count + carry = n × ticks` and `0 ≤ carry < d`.
4. Land with the mouth only where a whole number must leave the rules.
5. Never land in the middle of a chain.

## Next

Guide 16: stepping a changing system without a clock.
