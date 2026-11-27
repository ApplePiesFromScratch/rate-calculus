# Example 05: Savings and a loan

**What it shows:** Exact money arithmetic with a lever for the rate per input, landing to cents once, and `when` read again each month because it is first order.

**Guides:** 05, 11, 15, 17 (in `guide/`).

## Steps

1. Open a terminal in the repo's top folder (guide 00, steps 2 to 4).
2. Run:

   ```text
   python3 examples/05_money/example.py
   ```

3. Compare what it prints with the expected output below, line by line. `tools/check_docs.py` does the same comparison on every run.
4. Read each line with the notes under **What each line means**.
5. Open `examples/05_money/example.py` and read it top to bottom: every number it prints comes from the moves written there.
6. Do **Change it and predict**: write your prediction down *before* you run. A prediction written after the run witnesses nothing.

## Expected output

```output
1000 at 6% a year, compounded monthly, 12 months: 1061.68
  exact value has a bottom of 25 digits; it is landed only here
  rate per unit of deposit: 1.06
  rate per percentage point of the yearly rate: 10.56
  state of 'fee' (never touched): absent
month 0: owed 5000.00, change -250.00 a month, first-order when 20.00 months
month 1: owed 4750.00, change -252.50 a month, first-order when 18.81 months
month 2: owed 4497.50, change -255.02 a month, first-order when 17.64 months
month 3: owed 4242.48, change -257.58 a month, first-order when 16.47 months
stepped month by month: paid off in month 19, the last payment 202.72 more than needed
the first-order when (20) read at month 0 was too long: interest shrinks as the debt shrinks; read again each month
```

## What each line means

- The balance after a year, landed to cents only at the print. The exact value's bottom has 25 digits.
- The rate per unit of deposit (1.06: each extra dollar becomes 1.06) and per percentage point of the yearly rate.
- `fee` was never touched: `absent`.
- Each month: owed, the change at that reading, and the first-order `when`. It shrinks each month.
- Stepped month by month, the loan is paid off in month 19: the first reading (20) was too long, because interest shrinks as the debt does.

## Change it and predict

- Change the payment to 50. Predict what the first-order `when` says. *Answer:* the change is 0 a month: `theta`.

## What was run

This output was produced by running the script; `tools/check_docs.py` re-runs it and fails if any line changes. Nothing here was run on hardware unless the line says so.
