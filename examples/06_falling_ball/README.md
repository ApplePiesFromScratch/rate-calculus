# Example 06: A dropped ball, stepped in latches

**What it shows:** Stepping a system with no time variable, at two grains, and why `when` must be read again each latch.

**Guides:** 11, 16, 21 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/06_falling_ball/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/06_falling_ball/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
grain 1/10 s: lands after 40 latches = 4 s, height -9/25 m, speed 196/5 m/s
grain 1/100 s: lands after 404 latches = 101/25 s, height -869/5000 m, speed 4949/125 m/s
at the drop, when(height) = theta (isolator r=0: the reading compared against is not changing) - the ball is not moving yet: nothing to read
one second in: height (751/10, -49/5) - first-order when = 751/98 s from here; the speed keeps growing, so read again next latch
```

## What each line means

- At a grain of 1/10 s the ball lands after 40 latches (4 s); at 1/100 s, after 404 latches (101/25 s). The landing moves with the grain: report it with its grain.
- At the drop the height is not changing yet: `when` is `theta`.
- One second in, the first-order `when` is 751/98 s from there. The speed keeps growing, so read again next latch.
- Kind 2: the model ignores air. Checking it against a real ball is a measurement.

## Change it and predict

- Use grain 1/1000. Predict whether the landing time grows or shrinks. Then run it.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
