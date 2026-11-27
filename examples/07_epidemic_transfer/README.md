# Example 07: Three groups, moved only by transfer

**What it shows:** A population model where people move between groups only by one take and one give: books and range every latch, at two grains.

**Guides:** 16, 07, 21 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/07_epidemic_transfer/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/07_epidemic_transfer/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
grain 1: after 200 latches well 561, ill 9, recovered 9430; books and range held every latch: True
         peak ill 3134 at latch 42
grain 1/2: after 400 latches well 611, ill 19, recovered 9370; books and range held every latch: True
         peak ill 3089 at latch 80 (= 40 grain-1 latches)
the peak moves with the grain: report it with its grain
```

## What each line means

- After 200 latches at grain 1: each group's count; the books and the range held every latch.
- The peak and the latch it came at.
- The same at grain 1/2 over 400 latches: the peak moves with the grain.
- The rates are choices for the demonstration; the model is kind 2 only after they are measured.

## Change it and predict

- Halve the catching rate (3 → 3/2). Predict: does the peak come earlier or later, higher or lower?

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
