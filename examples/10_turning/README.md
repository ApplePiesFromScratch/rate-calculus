# Example 10: Exact turns with whole numbers

**What it shows:** Headings, composition, and three shears against a rounded turn on a 61 × 61 grid.

**Guides:** 14 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/10_turning/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/10_turning/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
(1:2) -> c 3, s 4, d 5; c*c + s*s == d*d: True
(2:3) -> c 5, s 12, d 13; c*c + s*s == d*d: True
(1:4) -> c 15, s 8, d 17; c*c + s*s == d*d: True
(1:2) composed 2 times -> (4:3), unit (-7/25, 24/25)
(1:2) composed 3 times -> (11:2), unit (-117/125, 44/125)
(1:2) composed 4 times -> (24:-7), unit (-527/625, -336/625)
(1:2) on 3721 points: rounded turn 0 collisions, three shears 0 collisions
(1:4) on 3721 points: rounded turn 860 collisions, three shears 0 collisions
(1:7) on 3721 points: rounded turn 0 collisions, three shears 0 collisions
(2:5) on 3721 points: rounded turn 504 collisions, three shears 0 collisions
```

## What each line means

- Each heading's whole-number unit, with c*c + s*s = d*d.
- (1:2) composed with itself.
- Collisions on 3721 points: the rounded turn loses points for (1:4) and (2:5); three shears lose none for any heading.

## Change it and predict

- Add (3:7) to the list. Predict three shears' collisions. *Answer:* 0.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
