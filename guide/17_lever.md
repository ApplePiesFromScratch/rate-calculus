# 17. The lever: a value with one rate per source

## The question

A total depends on several inputs. Which inputs, if changed, would change it, and by how much? (Part V, Unit V6)

## The rule

Guide 02 gave every Reading one rate slot. Give it **one rate slot per source** instead, and keep the set of sources that ever touched it. Then each source is in one of three states:

- **absent:** never touched the total;
- **still:** touched it, with rate 0 here;
- **moving:** touched it, with a nonzero rate.

Multiplication is the mix rule, slot by slot: for each source, rate = (that source's rate in A) × B's value + A's value × (its rate in B). Addition adds slot by slot. Nothing new is chosen: it is guide 04's rule with a list of rate slots.

## Worked example

total = price × qty + fee × fee + floor × 0, at price 12, qty 3, fee 0, floor 5:

| source | state | rate |
|---|---|---|
| price | moving | 3 |
| qty | moving | 12 |
| fee | still | 0 |
| floor | still | 0 |
| tax | absent | |

```check
price = source("price", 12)
qty = source("qty", 3)
fee = source("fee", 0)
floor_ = source("floor", 5)
total = price * qty + fee * fee + floor_ * 0
total.value == 36
total.state("price") == "moving" and total.rate_of("price") == 3
total.state("qty") == "moving" and total.rate_of("qty") == 12
total.state("fee") == "still"
total.state("floor") == "still"
total.state("tax") == "absent"
tax = source("tax", 2)
t2 = total * tax
t2.value == 72 and t2.rate_of("price") == 6 and t2.rate_of("qty") == 24 and t2.rate_of("tax") == 36
```

**Fee is still, not absent:** at fee = 0 the rate of fee × fee is 0, but the total moves once fee leaves 0. **Floor is still for another reason:** it was multiplied by 0. A tool that keeps only "touched or not" would call floor a dependency. A tool that keeps only the rate would call fee irrelevant. The three states keep both facts.

## Steps

1. Make each input a `source(name, value)`. Its rate against itself is 1.
2. Compute the total with the moves only.
3. Read `state(name)` and `rate_of(name)` for each input you care about.
4. Remember that "still" is read **here**. Away from this point the rate can be nonzero.

## Where it is used

- Sensitivity of a price, a bill, a forecast to each input.
- Debugging: which inputs reached this output, and which of them can move it right now.
- On the chip: CANDLE computes each dot's light once as (value; three rates against the flame's move), then lights the room each frame with four multiplies a dot (the microcontroller track).

## Try it yourself

y = a × b + b × b at a = 2, b = 3. *Answer:* y = 15; rate per a: 3; rate per b: a + 2b = 8.

```check
a = source("a", 2)
b = source("b", 3)
y = a * b + b * b
y.value == 15 and y.rate_of("a") == 3 and y.rate_of("b") == 8
```

## Next

Guide 18: computers and code as alphabets and mixing rules.
