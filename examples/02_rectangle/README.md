# Example 02: The growing rectangle

**What it shows:** `mix` as the area of a rectangle whose sides both grow, strip by strip.

**Guides:** 04 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/02_rectangle/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/02_rectangle/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
width (6, 2)  height (4, 1)
area now      v1*v2 = 24
right strip   r1*v2 = 8
top strip     v1*r2 = 6
mix(width, height) = (24, 14)
rate(area, clock) = 14 square metres a minute
rate(area, width) = 7 square metres per metre of width
wrong rule (multiply the rates): (24, 2) loses 12 of the rate
```

## What each line means

- The width and height Readings.
- The starting area and the two strips, each computed separately.
- `mix(width, height)`: value 24, rate 8 + 6 = 14.
- The area against the clock and against the width.
- The wrong rule (multiplying the rates) and how much of the rate it loses.

## Change it and predict

- Make the height still (`isolate(4, 0)`). Predict the rate. *Answer:* 8: only the right strip is left.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
