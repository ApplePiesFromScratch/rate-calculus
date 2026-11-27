# Example 05: savings and a loan. Every step is an exact fraction; amounts are landed to cents once, at the print.
# A lever gives the rate per input. The loan's 'when' is read again each month: it changes, so it is first order.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

def cents(x):
    """Land an exact amount on whole cents with the mouth, once, for display."""
    c = mouth_of(x * 100)
    sign = "-" if c < 0 else ""
    return f"{sign}{abs(c) // 100}.{abs(c) % 100:02d}"

def hundredths(x):
    c = mouth_of(x * 100)
    return f"{c // 100}.{c % 100:02d}"

# 1. Compound growth: each month multiplies by (1 + yearly/12). Deposit and yearly rate are sources of a lever.
def after(months, deposit, yearly):
    b = deposit
    for _ in range(months):
        b = b * (1 + yearly / 12)
    return b

b = after(12, source("deposit", 1000), source("yearly", F(6, 100)))
print("1000 at 6% a year, compounded monthly, 12 months:", cents(b.value))
print("  exact value has a bottom of", len(str(b.value.denominator)), "digits; it is landed only here")
print("  rate per unit of deposit:", hundredths(b.rate_of("deposit")))
print("  rate per percentage point of the yearly rate:", cents(b.rate_of("yearly") / 100))
print("  state of 'fee' (never touched):", b.state("fee"))

# 2. A loan: 5000 owed, 1% a month interest, 300 paid each month.
owed = F(5000)
for month in range(4):
    g = R(owed, owed / 100 - 300)          # (owed now, change per month at this reading)
    print(f"month {month}: owed {cents(owed)}, change {cents(g.rate)} a month, first-order when {hundredths(when(g))} months")
    owed = owed + owed / 100 - 300
months, owed = 0, F(5000)
while owed > 0:
    owed = owed + owed / 100 - 300
    months += 1
print(f"stepped month by month: paid off in month {months}, the last payment {cents(-owed)} more than needed")
print("the first-order when (20) read at month 0 was too long: interest shrinks as the debt shrinks; read again each month")
