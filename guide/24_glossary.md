# 24. Glossary

**absent / still / moving** — the three states of a source for a lever total: never touched; touched with rate 0 here; touched with a nonzero rate. Guide 17.

**alphabet** — the set of things the moves act on. In the book: pairs of fractions. In a computer: the values a type can hold. Guides 02, 18.

**the books** — an equation that must hold every step, recording that nothing was made or lost: `d × count + carry = n × ticks` for the carry; total in = total out + total held for a transfer. Guide 15.

**the carry** — sending a rate n/d as whole pulses by keeping the remainder: add n each tick; while the remainder is at least d, send a pulse and take d off. Guide 15.

**chain (rooms)** — quantities that depend on each other step by step; `rate(y, t) = rate(y, u) × rate(u, t)` because u's rate cancels. Guide 08.

**a choice, not a discovery** — a rule picked because it is useful, with what it buys stated. Opposite: forced. Guide 01.

**closest approach** — the latch at which the squared distance between two movers has rate 0, read from the gaps. Guide 11.

**collisions** — two inputs that give one output. A count of distinct outputs over an alphabet measures what an instruction loses. Guide 16.

**const(c)** — the plain number c as a Reading, (c, 0). Guide 05.

**curve** — the rate of the rate, the third slot of a Triple. Guide 10.

**cut** — a choice an observer makes: a naming, a direction, a seed, a grain, a scale, a place. A reading that moves with a cut belongs partly to the cut. Guide 07.

**de-reification** — writing a reading as a reading (rule, cut, grain), not as a thing. Guide 01.

**forced** — a rule that cannot come out any other way once earlier rules are fixed. Guide 01.

**gap** — the difference of two Readings, piece by piece; itself a Reading. Guide 11.

**grain** — how finely something is counted; how much of the comparison quantity one latch stands for. A cut. Guides 07, 16.

**grow** — a gap's rate over its own value. Guide 11.

**heading (P : Q)** — a pair of whole numbers giving c = (Q² − P²)/(P² + Q²), s = 2PQ/(P² + Q²), with c*c + s*s exactly 1. Guide 14.

**isolate(v, r)** — the first move: builds the Reading (v, r). `isolate(v)` = `isolate(v, 1)`. Guide 02.

**kill line** — a pass mark written, and recorded unchangeably, before the run it judges. Guide 20.

**kind 1, 2, 3** — checked by calculation; about the world through a model; about what everything ultimately is. Guide 21.

**latch** — one step of a system run forward. The count of latches is a reading; it drives nothing. Guide 16.

**lever** — a value with one rate per source and a touched set. Guide 17.

**mix** — the third move: (v1, r1) × (v2, r2) = (v1 v2, r1 v2 + v1 r2). Fixed once. Guide 04.

**the mouth** — landing a fraction on a whole number: nearest, half to even, mirror-true; used once, at the edge. Guide 15.

**no quotient** — the named refusal when dividing by a Reading whose value is 0. Guide 09.

**planted fault** — a deliberate break placed beside a check to prove the check can fail. Guide 20.

**rate(A, B)** — the second move: A's rate slot over B's rate slot. Guide 03.

**Reading** — a pair (value, rate). Guide 02.

**reading (lowercase)** — any number taken from a system by a rule at a cut, including what a program prints. Guides 07, 18.

**refusal** — a named "no answer": `theta`, `no quotient`, overflow. Never an inherited host error. Guide 01.

**rule (for a number)** — a finite procedure that, given a requested precision, returns a fraction and a proof of how close it is. Guide 12.

**run back** — next = 2·now − before + push(now), undone by before = 2·now − next + push(now). Guide 16.

**sealed set** — readings held back and read once, after tuning stops. Guide 20.

**seed** — the rate given to the comparison quantity; it cancels in `rate(A, B)`. Guide 07.

**shortfall** — what a rate law wants minus what the current stage gives; the next piece to add. Guide 13.

**standing v = C/(C + L + D)** — witnesses over witnesses plus load plus drag. Guide 20.

**theta** — the named refusal for a rate against a Reading whose rate is 0. Guide 03.

**three shears** — turning whole-number points by three landed slides, each exactly undoable. Guide 14.

**tier** — FORCED, EMPIRICAL, CONDITIONAL, STIPULATED, PRESUMED, UNPAID. Guide 21.

**transfer** — moving a kept quantity as one take and one give. Guide 16.

**when** — −value / rate of a gap: the latches until it runs out at its current rate. Guide 11.

**witness** — a distinct way a result could have failed and did not. Guide 20.
