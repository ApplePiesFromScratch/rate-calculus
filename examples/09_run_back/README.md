# Example 09: Out and exactly back

**What it shows:** The run-back step on 32 places, 2000 latches out and 2000 back, whole numbers against floats.

**Guides:** 16 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/09_run_back/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/09_run_back/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
whole numbers: 32 of 32 places moved after 2000 latches out; 32 of 32 home exactly after 2000 back
floats:        0 of 32 home exactly; 32 within half a unit
```

## What each line means

- Whole numbers: every place moved, and every place came home exactly, though the push rounds every latch.
- Floats: none came home exactly, though all are within half a unit.

## Change it and predict

- Replace the mouth in `push_whole` with `//` (a floor). Predict: do they still come home? *Answer:* yes: the rounding lives inside the push, which both directions share.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
