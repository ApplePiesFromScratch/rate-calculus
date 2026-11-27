# 16. Stepping a changing system with no clock

## The question

Guides 02 to 15 read a situation at one moment. How do you run a system forward, step by step, without a free-running time variable, without drift, and so that it can run back? (Part V, Units V4, V5; project)

## The latch

A **latch** is one step of the system. In each latch, every quantity moves by its rate times the **grain**, the amount of the counting quantity that one latch stands for.

- The grain is a **cut** (guide 07). Report it, and take the run at two grains.
- The count of latches is a reading of how many steps were taken. It drives nothing.
- If a program reads a clock to pace its latches, it reads only the clock's change since the last latch (house rule 1).

## Steps: the stepping recipe

1. **List the kept quantities** (what must not be made or lost: water, money, heat, charge).
2. **List the readings** that change, each as a value and the rule that gives its rate *from the current values* (never from a variable).
3. **Choose the grain** as a fraction (for example 1/10 of a minute per latch). Choose the order of the moves within a latch; that order is a choice, so name it.
4. **Move kept quantities by transfer**: take an amount from one place and give the same amount to another, in one move. Never set a place's new value from a formula of its neighbours.
5. **Check the books every latch**: the total of every kept quantity equals what came in minus what went out.
6. **Check for wrong signs or out-of-range values** too, because conservation is not correctness.
7. **Run at two grains** and compare. A reading that moves with the grain belongs partly to the grain.

## Transfer, never assign (Unit V5)

Heat spreading along a row of places: each face between two places moves a share of their difference from the higher to the lower, as one take and one give.

```check
row = [0, 8, 0]
transfer_step(row, 1, 4) == [2, 4, 2]
sum(transfer_step(row, 1, 4)) == 8
r = [0] * 30 + [8435] + [0] * 30
all(sum(r := transfer_step(r, 1, 4)) == 8435 for _ in range(2000))
b = [0] * 30 + [8435] + [0] * 30
sum(b := assign_blur_step(b)) < 8435
```

The assignment blur sets each place to a rounded average of its neighbours, and rounding leaks total every step it rounds.

**Conservation is not correctness:** with three quarters of the difference moved at each face, a peak gives away one and a half times what it holds. The total stays exact while places go below zero. Count the negatives as well as the total. A share of one half or less is safe on a row like this.

```check
r3 = [0] * 31 + [8000] + [0] * 32
_ = [r3 := transfer_step(r3, 3, 4) for _ in range(40)]
sum(r3) == 8000
any(v < 0 for v in r3)
r1 = [0] * 31 + [8000] + [0] * 32
_ = [r1 := transfer_step(r1, 1, 4) for _ in range(40)]
sum(r1) == 8000 and all(v >= 0 for v in r1)
```

## Running back (Unit V4)

Keep two readings, **now** and **before**. Step with:

```text
next = 2*now - before + push(now)
```

Solved for the other end, the same line is the step back:

```text
before = 2*now - next + push(now)
```

The push can be any rule of where things are now, **rounding included**, because it appears in both directions unchanged. So a whole-number system stepped this way runs out and comes home exactly.

```check
def push(p): return -mouth(p * 3, 50)
out = run_forward(7, 9, push, 2000)
out != (7, 9)
run_back(out[0], out[1], push, 2000) == (7, 9)
```

The push here, `−mouth(3p/50)`, is a pull back toward 0 that rounds every latch. The run goes 2000 latches out and 2000 back, and lands on the starting pair exactly. `examples/09_run_back` runs 32 places this way and puts a float run beside it.

**Why float fails here:** every float step lands the state itself, and a landing is two-to-one. The whole-number version lands only inside the push, which both directions share.

### A lost bit is a count of collisions

An instruction on 8-bit numbers can be undone only if no two inputs give the same output. Count the distinct outputs over all 256 inputs:

| instruction | distinct outputs |
|---|---|
| x + x | 128 |
| x × 6 | 128 |
| x × 5 | 256 |
| x + 37 | 256 |
| x xor (x >> 3) | 256 |
| x × 3 // 4 (a rounding) | 192 |

Doubling sends 256 inputs to 128 outputs: two inputs to one output, so a bit is lost and no rule can recover it. Multiplying by 5 loses nothing (5 is odd).

```check
collisions(lambda x: x + x) == 128
collisions(lambda x: x * 6) == 128
collisions(lambda x: x * 5) == 256
collisions(lambda x: x + 37) == 256
collisions(lambda x: x ^ (x >> 3)) == 256
collisions(lambda x: x * 3 // 4) == 192
collisions(lambda x: x * 3) == 256
collisions(lambda x: x * 4) == 64
collisions(lambda x: x + x + 1) == 128
```

## Try it yourself

1. One transfer step on 0, 8, 0 with a quarter of the difference at each face. *Answer:* 2, 4, 2.
2. Is x → 2x + 1 one-to-one on 8-bit numbers? *Answer:* no: 2x + 1 is always odd, so 256 inputs land on 128 outputs.

## Next

Guide 17: the lever, one rate per source.
