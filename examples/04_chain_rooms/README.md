# Example 04: Rooms: functions written for numbers, run on Readings

**What it shows:** A chain of three functions gives the exact rate of the whole chain, which equals the product of the rooms' rates.

**Guides:** 08, 18 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/04_chain_rooms/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/04_chain_rooms/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
t (2, 1)  u (4, 2)  y (16, 16)  z (57, 64)
rate(z, t) directly:         64
room by room, multiplied:    4 * 8 * 2 = 64
a room fed a still reading: rate(room2(still), still) = theta (isolator r=0: the reading compared against is not changing)
```

## What each line means

- The Reading after each room.
- The rate of the last against the first, directly.
- The same, room by room, multiplied: the middle rates cancel.
- A room fed a still Reading: any rate against it is `theta`.

## Change it and predict

- Replace room3 with `y * y`. Predict rate(z, t). *Answer:* 512 (z = 256 at t = 2, rate 2·16·16 = 512).

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
