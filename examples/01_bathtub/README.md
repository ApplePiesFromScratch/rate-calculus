# Example 01: A bathtub, a clock and a candle

**What it shows:** Readings, `rate` against a clock, the `theta` refusal, and reading `when` off a gap.

**Guides:** 02, 03, 11, 15 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/01_bathtub/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/01_bathtub/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
tub: (8, 2)
rate(tub, clock): 2 gallons a minute
rate(tub, candle): theta (isolator r=0: the reading compared against is not changing)
room left: (32, -2)
when the room runs out: 16 minutes
check: 32 + 16 * (-2) = 0
tub with the plug out: (8, -3)
when it empties: 8/3 minutes
landed for a display (the mouth, once): 3 minutes
when the room runs out now: -32/3
```

## What each line means

- `tub: (8, 2)`: 8 gallons now, 2 gallons a minute in.
- `rate(tub, clock)`: the tub against the clock that counts minutes.
- `rate(tub, candle)`: the candle is not changing, so there is nothing to compare against: `theta`.
- `room left`: the rim (a plain number, rate 0) minus the tub: a gap.
- `when the room runs out`: −32 / −2 = 16 minutes, read off the gap. The next line checks it by a product of two readings.
- With the plug out the tub drains at 3 a minute net; `when` it empties is 8/3 minutes, landed to 3 only for a display.
- The last line is negative: the room is growing, so it never runs out under these rates.

## Change it and predict

- Change the faucet to 0 (`isolate(8, 0)`). Predict `when the room runs out` first. *Answer:* `theta`.
- Change the plug to −2. Predict `when it empties`. *Answer:* the tub is still (rate 0): `theta`.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
