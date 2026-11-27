# 05. Adding, subtracting, and plain numbers

## The question

How do Readings add and subtract, and what is a plain number like 2 in this alphabet? (book Units 6, 7)

## The rules

- **Add piece by piece:** (v1, r1) + (v2, r2) = (v1 + v2, r1 + r2).
- **Subtract piece by piece:** (v1, r1) − (v2, r2) = (v1 − v2, r1 − r2).
- **A plain number c is the Reading (c, 0).** It has a value and is not changing, like the puddle in guide 02. `const(c)` builds it; the library also lifts a bare number to (c, 0) automatically.

**Multiplying by a plain number is still mix**, against a rate-0 Reading: mix((v, r), (c, 0)) = (v*c, r*c + v*0) = (v*c, r*c). Both slots get multiplied by c, because the second strip vanishes.

**Why add piece by piece:** the amount of a sum is the sum of the amounts, and the rate of a sum is the sum of the rates. Two hoses filling one tub fill it at the sum of their rates.

## Steps

1. To add or subtract, line the slots up and work slot by slot.
2. To bring in a plain number, write it as (c, 0) first.
3. To multiply by a plain number, multiply both slots by it (that is mix with (c, 0)).

## Worked examples

```check
t = isolate(2)
mix(t, 2) == R(4, 2)
mix(t, const(2)) == R(4, 2)
R(4, 4) + R(6, 3) == R(10, 7)
x = isolate(3)
x * x - x == R(6, 5)
# 3*x written as additions, and as a mix with (3, 0): the same
x + x + x == 3 * x
3 * x == R(9, 3)
# adding a plain number changes the value, never the rate
x + 1 == R(4, 1)
```

## Try it yourself

1. (12, 14) + 1? *Answer:* (13, 14).
2. x = isolate(5): x*x − x? *Answer:* (25, 10) − (5, 1) = (20, 9).
3. 4 * isolate(2, 3)? *Answer:* (8, 12).

## Mistakes people make

- **Giving a plain number rate 1.** `isolate(2)` is (2, 1), a moving thing. The plain number 2 is (2, 0).
- **Adding a constant to the rate.** "+ 1" means + (1, 0): only the value moves.

## Next

Guide 06: running whole expressions, one move at a time.
