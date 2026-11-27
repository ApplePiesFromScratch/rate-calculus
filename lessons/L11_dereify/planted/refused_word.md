# A timer, de-reified

| the map | what it reifies | the relation | what I use |
|---|---|---|---|
| elapsed = now - start | time as a variable read off a clock | a count of latches between two events | a counter that latches once per frame |
| a timeout of 500 ms | a duration as a property of the wait | a budget of latches against the work each latch does | a countdown of frames, refused by name at 0 |
| a frame rate in fps | a rate as a property of the program | work per frame against the wire's bytes per second | the board's own printed frame cost |
| delay(10) | the chaos of waiting | a gap in which nothing latches | nothing: every frame does work |

## What pays

- a counter counts latches: FORCED (it is incremented once per latch, by construction)
- the frame cost: EMPIRICAL (printed by the board)
- the countdown's length: STIPULATED (chosen, named in the sketch)

Kill line: a counter value that differs between desk and chip on the same frame.
Known: frame counters and tick budgets are ordinary embedded practice; the reading in the book's words is what this adds.
