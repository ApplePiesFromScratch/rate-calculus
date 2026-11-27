# Example 13: Letters that spell a picture

**What it shows:** Designing an alphabet and one MIX table that spell a target picture exactly, with a planted fault.

**Guides:** 19 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/13_custom_alphabet/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/13_custom_alphabet/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
XOR  : colours-alone conflicts   0, letters refined   2, squeezed   2, MIX entries   8, play 288/288 CERTIFIED
DISC : colours-alone conflicts  32, letters refined  15, squeezed  14, MIX entries 102, play 288/288 CERTIFIED
RINGS: colours-alone conflicts 136, letters refined  23, squeezed  10, MIX entries 138, play 288/288 CERTIFIED
```

## What each line means

- Per target: conflicts with the colours alone, letters after refining, letters after squeezing, table entries, and the play certificate.
- XOR needs no extra letters: its own rule is XOR of the two neighbours.
- Run with `--plant` to keep merges untested: DISC and RINGS then fail the certificate.

## Change it and predict

- Run `python3 examples/13_custom_alphabet/example.py --plant`. Predict which targets fail. *Answer:* DISC and RINGS (XOR tries no merges).

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
