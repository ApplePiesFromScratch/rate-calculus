# Example 16: Four patterns in a changing context

**What it shows:** The six clauses of the useful pattern, run as rules, with a change of context halfway.

**Guides:** 26, 27 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/16_evolution/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/16_evolution/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
field 400, THETA 60, KAPPA 4/16 (choices); patterns: name C take vent cells
  simple   C 2 take 2 vent 1/2 cells [0, 1]
  venting  C 2 take 3 vent 1/4 cells [1, 2]
  heavy    C 2 take 3 vent 0/1 cells [2, 3]
  lonely   C 1 take 2 vent 1/8 cells [9]
after 1000 latches: field 327, drained 0
  simple   served  487 refused    0 reconfigured   0 L   2 vented 972
  venting  served  134 refused    0 reconfigured   0 L   9 vented 393
  heavy    served  160 refused    0 reconfigured   9 L  48 vented 0
  lonely   served  219 refused    0 reconfigured   0 L  14 vented 424
latch 1000: the context changes: the field is drained to 4 (counted as drained)
after 2000 latches: field 1, drained 323
  simple   served  932 refused  213 reconfigured   0 L   2 vented 1862
  venting  served  135 refused   84 reconfigured   0 L   3 vented 402
  heavy    served  163 refused   84 reconfigured   9 L  57 vented 0
  lonely   served  319 refused   70 reconfigured   0 L  14 vented 624
books (field + every L = 400 - drained) held every latch, and the front never moved back: True
```

## What each line means

- The field, THETA and KAPPA (choices), and each pattern's support, take, vent and cells.
- After 1000 latches: served, refused, reconfigured, loaded history and vented, per pattern.
- The context changes: the field is drained (counted).
- After 2000 latches: the simple pattern, whose vents keep the field supplied, is still served; the heavy one, which never vents, is refused when the field cannot cover its take.
- The books closed every latch and the front never moved back.

## Change it and predict

- Give the heavy pattern a vent of 1/4. Predict its refusals after the drain.
- Move the lonely pattern into cell 0. Predict what happens to the simple pattern's served count (drag).

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
