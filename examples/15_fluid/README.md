# Example 15: A warm puff in a box of air, without Navier–Stokes

**What it shows:** Fluid motion from trades at faces only: the puff rises, the books close exactly every latch, a planted set is caught, and a constant is changed as a cut.

**Guides:** 28, 16 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/15_fluid/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/15_fluid/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
box 32 x 20, stuff 1000 a place; constants KP 6 KD 2 KE 1 KL 24 KM 1 (choices)
latch  50: warm row 15.56  stuff 882..1053  fed 100000 vented 0  turning round (15,10) -21
latch 100: warm row 12.73  stuff 923..1063  fed 100000 vented 0  turning round (15,10) -95
warmth above the mean at latch 120 (row 0 is the lid):
  |                                |
  |                                |
  |                                |
  |                                |
  |                                |
  |                                |
  |               ...              |
  |              ..:..             |
  |             ..:*:..            |
  |            ..:*#*:..           |
  |            .:*###*:.           |
  |            .:*###*:.           |
  |            .:**#**:.           |
  |            .::*#*::.           |
  |            ...:*::..           |
  |             ...*...            |
  |               .:.              |
  |               .:.              |
  |               .:.              |
  |                .               |
latch 150: warm row  9.52  stuff 955..1062  fed 100000 vented 0  turning round (15,10) -106
latch 200: warm row  6.49  stuff 956..1078  fed 100000 vented 37  turning round (15,10) -75
latch 250: warm row  4.11  stuff 968..1091  fed 100000 vented 2276  turning round (15,10) -52
latch 300: warm row  2.98  stuff 968..1060  fed 100000 vented 9166  turning round (15,10) -21
latch 350: warm row  2.47  stuff 971..1036  fed 100000 vented 16238  turning round (15,10) -22
latch 400: warm row  2.25  stuff 978..1032  fed 100000 vented 21778  turning round (15,10) -15
books (stuff, warmth, momentum x, momentum y) and range held every latch: True
planted set (warmth halved in place, not traded): the books opened at latch 1
two cuts at latch 150: KL 24 -> warm row 9.52; KL 48 -> warm row 4.92; books held in both: True
```

## What each line means

- The settings: every constant is a choice.
- Every 50 latches: the warm row (it falls as the puff rises: row 0 is the lid), the range of stuff (compressible air: about ±10%), warmth fed and vented at the lid, and the turning round one 2 × 2 loop.
- The picture at latch 120 is a reading for the eye: warmth above the box's mean, in five shades.
- The books held every latch.
- The planted set opened the books at its first latch.
- Two cuts: doubling the lift changes the pace; the books hold at both.

## Change it and predict

- Turn the heater on (`b.heater = (16, 400)`) instead of the puff. Predict where the warmth goes. Then run it and read the picture.
- Halve KP. Predict whether the range of stuff widens or narrows.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
