# Example 11: A motor driven at 4/3 steps a tick

**What it shows:** The carry against a float accumulator, over 100,000 ticks.

**Guides:** 15 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/11_carry_motor/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/11_carry_motor/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
carry 4/3: first 24 ticks 112112112112112112112112
after 100000 ticks: count 133333, carry 1; d*count + carry == n*ticks and 0 <= carry < d every tick: True
float accumulator: 133333 pulses after 100000 ticks, differs from the carry on 40452 ticks
carry 7/3, ticks 1-6: [2, 2, 3, 2, 2, 3] books: True
```

## What each line means

- The first 24 ticks repeat 112.
- After 100,000 ticks: 133,333 pulses, carry 1, and the books with their bound held every tick.
- The float accumulator here (pulses = whole part of a running float total) differs from the carry on 40,452 ticks. (Part V reports a different float method wrong on 33,333 ticks; the method is the cut.)
- 7/3: one tick can owe three pulses.

## Change it and predict

- Change the rate to 1/3. Predict the first six ticks. *Answer:* 0 0 1 0 0 1.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
