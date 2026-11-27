# Example 12: Code as alphabets and mixing rules

**What it shows:** One expression in five alphabets, three division rules, collision counts, a lever through ordinary code, and a branch.

**Guides:** 18 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/12_code_alphabets/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/12_code_alphabets/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
f(x) = x*x - x
  fractions  f(3)   = 6
  Readings   f(3)   = (6, 5) (value, rate)
  uint8      f(20)  = 124  (380 wrapped mod 256)
  booleans   f(b)   = [0, 0] for b = 0, 1 (x*x = x: the polynomial collapses)
  floats     f(0.1) = -0.09  fractions f(1/10) = -9/100
(0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3) in floats: False
-7 / 2 landed: Python // -4  C toward zero -3  mouth -4
  uint8 x + x        128 of 256 distinct outputs: loses information
  uint8 x * 5        256 of 256 distinct outputs: one-to-one
  uint8 x >> 1       128 of 256 distinct outputs: loses information
  uint8 x ^ (x >> 3) 256 of 256 distinct outputs: one-to-one
  uint8 x & 15        16 of 256 distinct outputs: loses information
lever through code: total 137931/2000  rate per p 69/20  per qty 45977/2000  per tax 5997/100
a branch reads the value: clipped at 9 -> (9, 1)  at 11 -> (10, 0) (a rate per branch)
```

## What each line means

- f in fractions, Readings, uint8, booleans and floats: same symbols, different rules.
- Float addition is not associative.
- −7/2 landed by three different rules.
- Collision counts over all 256 bytes.
- A lever through a price function: the rate of the total per input.
- A branch reads the value: the rate is per branch.

## Change it and predict

- Add `x * 3` to the collision list. Predict. *Answer:* 256 of 256: 3 is odd.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
