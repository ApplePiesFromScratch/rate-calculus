# Example 14: The C core

**What it shows:** The same moves in C99 with whole-number fractions and named refusals, including overflow.

**Guides:** 15, 18 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/14_c_core/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/14_c_core/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
mix((4,1),(4,1)) = (16/1, 8/1)
rate(x*x, x) = 8/1
rate(tub, candle): theta (isolator r=0)
1/x at 3 = (1/3, -1/9)
1/x at 0: no quotient
a product past int64: refused (overflow)
mouth: 5/2 -> 2, -7/2 -> -4, 7/2 -> 4
carry 7/3: 2 2 3 2 2 3 | books held
```

## What each line means

- Each line is one move or refusal from the C core (`core_c/`).
- Without a C compiler the example prints `SKIPPED`, which is not a pass.

## Change it and predict

- Change the carry to 4/3 in `demo.c`. Predict the first six pulses. *Answer:* 1 1 2 1 1 2.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
