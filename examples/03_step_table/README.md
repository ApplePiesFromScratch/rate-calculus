# Example 03: A step table for any expression

**What it shows:** Running an expression one move a row, including a division and a refusal.

**Guides:** 06, 09 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/03_step_table/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/03_step_table/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
f = x*x*x + 2*x + 1 at x = (2, 1)
  1. xx = mix((2, 1), (2, 1)) -> (4, 4)
  2. xxx = mix((4, 4), (2, 1)) -> (8, 12)
  3. 2x = mix((2, 1), (2, 0)) -> (4, 2)
  4. s = add((8, 12), (4, 2)) -> (12, 14)
  5. f = add((12, 14), (1, 0)) -> (13, 14)
  value check: 2*2*2 + 2*2 + 1 = 13
g = (x*x + 1) / (x - 1) at x = (3, 1)
  1. xx = mix((3, 1), (3, 1)) -> (9, 6)
  2. top = add((9, 6), (1, 0)) -> (10, 6)
  3. bot = sub((3, 1), (1, 0)) -> (2, 1)
  4. g = div((10, 6), (2, 1)) -> (5, 1/2)
  multiply back: (10, 6)
h = 1 / (x - 3) at x = (3, 1)
  1. bot = sub((3, 1), (3, 0)) -> (0, 1)
  2. h = div((1, 0), (0, 1)) -> no quotient (the divisor's value is 0)
```

## What each line means

- Each numbered row is one move: its inputs, then its output pair.
- The value check recomputes the value by plain arithmetic.
- `multiply back`: the divisor times the quotient gives the dividend exactly.
- The last table ends in `no quotient`: the divisor's value is 0 at x = 3.

## Change it and predict

- Add a row that squares f. Predict the rate before running. *Answer:* for f = (13, 14), f*f = (169, 364).

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
