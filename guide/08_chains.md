# 08. Chains: rooms that feed each other

## The question

What if a quantity depends on another quantity, instead of being isolated directly? (book Unit 6)

## The machine with two rooms

Room 1 takes t and outputs u = mix(t, 2). Room 2 takes u and outputs y = mix(u, u). y does not depend on t directly, only through u.

**Book Unit 6, Demonstration 2, at t = isolate(2):**

- t = (2, 1)
- u = mix(t, 2) = (4, 2)
- y = mix(u, u): value 16; strips 2*4 = 8 and 4*2 = 8; output (16, 16)
- rate(y, t) = 16/1 = 16

Room by room instead:

- rate(y, u) = 16/2 = 8
- rate(u, t) = 2/1 = 2
- rate(y, u) × rate(u, t) = 16

Both paths give the same number.

**Why both paths agree:** rate(y, u) has u's rate slot on the bottom; rate(u, t) has u's rate slot on top. Multiplied, u's rate cancels, the way (8/2)*(2/1) simplifies before you multiply. **Room 2 never has to know t exists**: u carries everything Room 2 needs. A course calls this the chain rule; here it is a cancellation you can see.

```check
t = isolate(2)
u = mix(t, 2)
y = mix(u, u)
u == R(4, 2)
y == R(16, 16)
rate(y, t) == 16
rate(y, u) * rate(u, t) == rate(y, t)
t5 = isolate(5)
u5 = mix(t5, 2)
y5 = mix(u5, u5)
y5 == R(100, 40)
rate(y5, t5) == 40
rate(y5, u5) * rate(u5, t5) == 40
```

## Steps

1. Draw the rooms: a box per step, an arrow from each input to each output.
2. Seed the first input with `isolate`.
3. Run each room's moves on the Reading that arrives, and pass its output Reading on.
4. Ask `rate(last, first)` for the whole chain, or `rate(out, in)` room by room. They multiply.
5. If any room's input has rate 0, any rate against it is `theta` (guide 03): the chain has nothing to land on there.

## Why this matters for programs

A program is a chain of rooms (functions). If you feed a Reading in at the start and every function uses only the moves, the Reading that comes out carries the exact rate of the whole program against its input. No function has to be rewritten to "know about rates". Guide 18 builds on this.

```check
# a three-room chain: square, add 1, triple
def room1(a): return a * a
def room2(a): return a + 1
def room3(a): return 3 * a
x = isolate(2)
out = room3(room2(room1(x)))
out == R(15, 12)
rate(out, x) == rate(out, room2(room1(x))) * rate(room2(room1(x)), room1(x)) * rate(room1(x), x)
```

*(`def` lines run as code in the checker, the same as assignments.)*

## Try it yourself

With u = mix(t, 2) and y = mix(u, u), find y, rate(y, t), and rate(y, u) × rate(u, t):

1. t = isolate(1). *Answer:* u (2, 2); y (4, 8); 8; (8/2)(2/1) = 8.
2. t = isolate(3). *Answer:* u (6, 2); y (36, 24); 24.
3. t = isolate(4). *Answer:* u (8, 2); y (64, 32); 32.

## Mistakes people make

- **Rebuilding y from t by a remembered formula** instead of passing u through. The rooms are the method.
- **Forgetting that a room with a still input refuses** rates against that input.

## Next

Guide 09: division, derived from mix.
