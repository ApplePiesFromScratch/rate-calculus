# Example 08: Ask for a precision, get a fraction and a proof

**What it shows:** Rules for √2 and e that stop at the precision requested, with the proven bound printed.

**Guides:** 12, 13 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/08_precision_on_demand/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/08_precision_on_demand/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
requested precision: 1/1000000
sqrt 2 by halving: 20 steps, low 741455/524288, high 1482911/1048576, gap 1/1048576 < request: True
  low^2 < 2 < high^2: True
sqrt 2 by averaging: 3 steps, 577/408, x^2 - 2 = 1/166464
e: stage 9, value 98641/36288, proven tail bound 11/36288000 < request: True
stage for 1/n within the request: n = 1000001
```

## What each line means

- The request.
- Halving: how many steps, the bracket, its gap, and the check low² < 2 < high².
- Averaging: three steps already give a gap of 1/166464.
- e: the stage whose proven tail bound is under the request.
- The stage for 1/n.

## Change it and predict

- Change REQUEST to F(1, 10**12). Predict the halving steps. *Answer:* 40.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
