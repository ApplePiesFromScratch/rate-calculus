# Every Number Is A Rule

### Arithmetic, Algebra, Geometry and a Full Calculus From Three Moves, With What The Chip Work Taught

James Pugmire

This file holds the workbooks the guides are built on, in the order they build on each other:

| part | what it is |
|---|---|
| I | Numbers and Why They Work: arithmetic, every rule with a reason |
| II | Letters That Stand For Numbers: first algebra |
| III | Shapes and Why They Measure Out: first geometry |
| IV | Every Number Is A Rule, Complete Edition: the calculus from isolate, mix and rate |
| V | What The Machines Taught: nine units from building on a chip, in the same format |

Parts I to IV are James Pugmire's text, verbatim. Part V was written in the same format from the project's chip work; its "On the chip" lines name sketches in the microcontroller track (https://github.com/ApplePiesFromScratch/Microcontrollers-and-robotics-beta), and the scripts it names (`docs/teach.py`, `workbook/part5.py`) live there.

**How to use it with this repo:** each guide in `guide/` names the units it comes from. Do a unit's practice before reading its answers, then run the matching checked block in the guide.

---

<!-- PART I BEGIN: sources/numbers-and-why-they-work.md, verbatim -->

*Part I*

*A Workbook*

# Numbers and Why They Work

### A First Book of Arithmetic, Where Every Rule Gets a Reason

James Pugmire


---


## Before We Start

You've been doing arithmetic since you were small. Add, subtract, multiply, divide. You know the steps. This book asks a different question: not "what are the steps," but "why do the steps work?"

Here's why that question matters. If you only know the steps, you're stuck the moment you forget one. If you know why the steps work, you can rebuild a forgotten step yourself, on the spot, because you understand what it was doing in the first place. A rule you understand is a rule you'll always have. A rule you only memorized is a rule that can slip away the moment you're nervous, like during a test.

Every rule in this book gets a reason. Not "because that's the rule," a real reason, the kind you could explain to a friend and have them actually understand it. Some of these reasons might surprise you, even for rules you've been using for years.


### How This Book Works

Every unit has a big question, an explanation with the reason spelled out, a few worked examples done slowly, a "Try It Yourself" problem with a hint, and a set of practice problems using only what that unit has covered. Answers to every practice problem are in the back, organized by unit.

Use a pencil. Do the problems on paper, not in your head. You'll understand a rule differently once you've used it yourself than you will just from reading about it.


---


*Unit 1*

## Place Value: Why Digits Change Meaning


> **Big Question:** Why does the digit 3 mean something different in 30 than it does in 300?

The number 347 isn't just the digits 3, 4, and 7 sitting next to each other. Each digit's *position* tells you what it's worth. The 7 is worth 7 (seven ones). The 4 is worth 40 (four tens). The 3 is worth 300 (three hundreds). Add those up: `300 + 40 + 7 = 347`.


> **Why does position matter?** Because we only have ten digits, 0 through 9, and we need to write numbers far bigger than 9. Position is the trick that lets ten symbols represent numbers as large as you'll ever need to write: each spot you move to the left is worth ten times more than the spot before it. That single idea, called place value, is the reason every rule in the next few units works at all.

Ten digits, and each spot worth ten times the one before it, is called **base ten**. It's the system this whole book uses, almost certainly because people have ten fingers to count on, not because ten is the only number that could have worked. Computers run on base two, using only the digits 0 and 1, with the exact same place-value idea underneath. Base ten is a choice this book makes and sticks with, not a law every number system has to follow.


*Demonstration 1*

```
347  =  3 hundreds + 4 tens + 7 ones
     =  300 + 40 + 7
     =  347
```


*Demonstration 2: a bigger number*

```
5,208  =  5 thousands + 2 hundreds + 0 tens + 8 ones
       =  5000 + 200 + 0 + 8
       =  5208

Notice the 0. It isn't decoration, it's holding the tens spot
open so the 2 stays in the hundreds spot where it belongs. Take
the 0 out and you'd have 528, a completely different number.
```


**Try It Yourself:** Break 6,024 down into thousands, hundreds, tens, and ones, and explain what job the 0 is doing. *Hint: work right to left. What's in the ones spot? Tens? Hundreds? Thousands?* Answer: 6 thousands + 0 hundreds + 2 tens + 4 ones = 6000+0+20+4 = 6024. The 0 holds the hundreds spot open so the 2 stays in the tens spot.


### Practice: Unit 1


1. Break 582 down into hundreds, tens, and ones.

2. Break 3,706 down into thousands, hundreds, tens, and ones.

3. What job is the 0 doing in the number 6,025?

4. Which is bigger, the 5 in 512 or the 5 in 125? Explain using place value, not just "512 is bigger."

---


*Unit 2*

## Addition and Subtraction: What Carrying Actually Does


> **Big Question:** When you "carry the 1" in addition, what are you actually carrying, and why does it work?

Add 38 and 47. Line them up by place value:


*Demonstration 1: 38 + 47*

```
38
 + 47
 ----

Ones column: 8 + 7 = 15. But 15 doesn't fit in one ones-spot,
it's one ten and five ones. Write the 5 in the ones spot, and
move the ten over to the tens column. That's the "carry."

Tens column: 3 + 4 + (the 1 ten you carried) = 8

   38
 + 47
 ----
   85
```


> **Why does carrying work?** Because of place value from Unit 1. Ten ones are worth exactly the same as one ten. When a column adds up to more than 9, you're not making a mistake, you've genuinely built enough ones to trade in for a ten. Carrying is just recording that trade in the next column over, where a ten belongs.


*Demonstration 2: subtraction, borrowing, 72 - 48*

```
72
 - 48
 ----

Ones column: can't take 8 away from 2, there aren't enough ones.
Borrow a ten from the 7 (making it 6), and turn it into 10 extra
ones, joining the 2 to make 12.

Ones: 12 - 8 = 4
Tens: 6 - 4 = 2

   72
 - 48
 ----
   24
```


> **Why does borrowing work?** The same place-value trade, in reverse. A single column isn't allowed to hold a negative count of ones by itself, so when a column doesn't have enough, you break open one ten from the tens column and turn it into 10 more ones. The total value of the number never changes, you've just repacked it differently. (Negative numbers themselves are real and useful, you'll meet them properly in Unit 5, but borrowing is a trick for keeping every single column a normal count of 0 to 9, so you never need one here.)


**Try It Yourself:** Add 156 + 278, showing every carry. *Hint: ones column first, then tens, then hundreds. Carry whenever a column passes 9.* Answer: Ones: 6+8=14, write 4 carry 1. Tens: 5+7+1=13, write 3 carry 1. Hundreds: 1+2+1=4. Answer: 434.


### Practice: Unit 2


1. 56 + 38, showing the carry.

2. 91 - 47, showing the borrow.

3. 245 + 178, showing every carry.

4. 604 - 256, showing every borrow.

5. Explain, in your own words, why a "carry" is worth 10 times more once it lands in the next column.

---


*Unit 3*

## Multiplication: Breaking A Big Problem Into Easy Pieces


> **Big Question:** Why does the multiplication algorithm you learned actually give the right answer?

Multiplication starts as repeated addition. `4 * 3` means "4, three times": `4+4+4=12`. That's a solid way to picture multiplication for whole numbers, but adding a number to itself dozens of times gets slow, so we need a faster way for bigger numbers. That faster way is built on place value again.


> Does "repeated addition" cover every multiplication you'll ever do? Not quite. "3 times 4" is easy as repeated addition: add 3 to itself 4 times. But "3 times one-half" can't literally mean adding 3 to itself half a time, that doesn't make sense as counting. Repeated addition is the right starting picture for whole numbers, the numbers this unit uses, and it's the picture this book leans on to explain the rules below. Multiplying fractions and negative numbers, later in this book, will need a different picture (scaling, instead of counting copies), built on what you learn here rather than replacing it.


*Demonstration 1: 23 * 4*

```
23 is really 20 + 3. Multiplying by 4 means multiplying BOTH
pieces by 4, then adding the results together.

20 * 4 = 80
 3 * 4 = 12
        ----
        92

23 * 4 = 92
```


> **Why does splitting the number work?** Because multiplication spreads out over addition: multiplying a sum by something is the same as multiplying each piece separately and adding the answers. `23 * 4` and `(20+3) * 4` are the exact same problem, written two ways. Splitting 23 into 20+3 just makes each piece small enough to multiply in your head.


*Demonstration 2: a bigger example, 34 * 26*

```
Split BOTH numbers by place value: 34 = 30+4, and 26 stays whole
for now.

30 * 26 = 780
 4 * 26 = 104
         ----
         884

34 * 26 = 884

Check by splitting 26 too, another way: 30*20=600, 30*6=180,
4*20=80, 4*6=24. Add all four: 600+180+80+24 = 884. Same answer,
because you're allowed to split either number, or both.
```


**Try It Yourself:** Multiply 42 * 23 by splitting 42 into 40+2. *Hint: 40*23 first, then 2*23, then add.* Answer: 40*23=920. 2*23=46. 920+46=966.


### Practice: Unit 3


1. 34 * 3, by splitting 34 into 30+4.

2. 27 * 4, by splitting 27 into 20+7.

3. 42 * 23, showing all four partial products (split both numbers).

4. Explain why splitting a number for multiplication doesn't change the answer, using the word "place value" somewhere in your explanation.

---


*Unit 4*

## Division: Undoing Multiplication


> **Big Question:** What is division actually asking?

`12 / 4` is asking: "what number, multiplied by 4, gives 12?" Division and multiplication are opposites, the same way addition and subtraction are opposites. If `3 * 4 = 12`, then `12 / 4 = 3` and `12 / 3 = 4`, for free, no new fact required.


> **Why does thinking of division this way help?** Because it turns a division problem into a multiplication problem you might already know. If someone asks you `56 / 8`, you can ask yourself instead: "8 times what gives 56?" and search your times tables for the answer, rather than treating division as a totally separate skill from multiplication.


*Demonstration 1: 84 / 4*

```
Split 84 by place value: 80 + 4.

80 / 4 = 20      (since 4*20=80)
 4 / 4 = 1       (since 4*1=4)
        ----
        21

84 / 4 = 21.  Check: 21 * 4 = 84. Correct.
```


*Demonstration 2: 156 / 12*

```
What times 12 gets close to 156, without going over?
12 * 10 = 120.  156 - 120 = 36 left over.
What times 12 gets close to 36?
12 * 3 = 36.  Nothing left over.

10 + 3 = 13

156 / 12 = 13.  Check: 13 * 12 = 156. Correct.
```


### When Division Doesn't Come Out Even

Every division so far has landed exactly on a whole number, with nothing left over at the end. That's not always true, and pretending it is would be hiding something real. Numbers don't always split into equal groups perfectly.


*Demonstration 3: 17 / 5, where something is left over*

```
What times 5 gets close to 17, without going over?
5 * 3 = 15.  17 - 15 = 2 left over.
5 * 4 = 20.  That's too much, 20 is bigger than 17.

So 5 goes into 17 three whole times, with 2 left over that
can't be split into another full group of 5.

17 / 5 = 3 remainder 2

Check: 5 * 3 = 15, and 15 + 2 (the leftover) = 17. Correct.
```


> **Why keep the remainder instead of ignoring it?** The 2 left over is real. It didn't disappear, and it isn't a mistake, it's an honest part of the answer: 17 things really do split into 3 full groups of 5 with 2 things left outside any group. Writing "17/5=3" alone and dropping the 2 would be quietly throwing away a true fact about the number 17. Naming the leftover, instead of pretending it isn't there, is a habit worth keeping well beyond this one problem.


**Try It Yourself:** Find 96 / 8, by asking "8 times what gives 96?" Break it into pieces if that helps. *Hint: 8*10=80. 96-80=16. 8 times what gives 16?* Answer: 8*10=80, remainder 16. 8*2=16. So 10+2=12. 96/8=12. Check: 12*8=96.


### Practice: Unit 4


1. 96 / 8, checked by multiplying back.

2. 144 / 12, checked by multiplying back.

3. 108 / 9, checked by multiplying back.

4. 23 / 6. This one has a remainder; find it and check your answer the way Demonstration 3 did.

5. Explain, in one sentence, why checking a division answer means multiplying, not dividing again.

---


*Unit 5*

## Negative Numbers


> **Big Question:** Why does a negative number times a negative number come out positive? That rule feels like it shouldn't be true.

Before the strange rule, the easy part. A negative number is a direction, not a strange kind of stuff. Minus forty dollars is forty dollars owed, not forty anti-dollars sitting in a box. Drawing this as a number line, positives to the right and negatives to the left, is a picture people choose. The line is a tool. It is not a claim that numbers are points on a physical line. Adding moves you one way along that picture. Subtracting moves you the other way.

A minus can also be a relation, not a pile moving. Two cars drive apart. One pays rope out. The other has the rope tied to the bumper. The rope gets longer. Nothing left the first car and arrived in the second. Flip which way you call forward and each car's reading flips. The rope getting longer does not. Owing and forgiving still move a pile. The rope does not.


*Demonstration 1: addition and subtraction with negatives*

```
(-3) + (-5):  start at -3, move 5 more to the left.  ->  -8

(-3) + 7:  start at -3, move 7 to the right.  ->  4

5 - (-2):  subtracting a negative means moving right instead
of left (undoing the negative flips the direction).  ->  7
```


### Now, The Strange One: Negative Times Negative

Instead of just being told the rule, let's find it by following a pattern that's already true, and refusing to let it break.


*Demonstration 2: extending a pattern you already trust*

```
Start with something nobody argues about: (-4) times a
shrinking positive number.

(-4) * 3  =  -12
(-4) * 2  =  -8
(-4) * 1  =  -4
(-4) * 0  =   0

Look at the pattern in the answers: -12, -8, -4, 0. Each time
the second number drops by 1, the answer goes UP by 4.

If that pattern is real, it shouldn't stop just because we
reached 0. Keep going the same way:

(-4) * (-1)  =  0 + 4  =   4
(-4) * (-2)  =  4 + 4  =   8
(-4) * (-3)  =  8 + 4  =  12
```


> Is this a proof, or a choice? Nobody was forced to continue the pattern past zero. We chose to keep the same step, add 4 each time, instead of switching steps once the numbers turned negative. That choice wrote the plus sign. Keeping the same step is what makes negative times negative sit with the multiplication facts you already trust, rather than needing a special exception at zero. It is a choice to keep one step going.

Two different "round down" rules also split once a number is negative. Toward the more negative number, and toward zero, agree on positives and disagree on negatives. This book does not pick one of them yet. Naming which rule you mean is part of the answer.


**Try It Yourself:** Using the same pattern method, find `(-6) * (-1)`. Start from `(-6)*2`, `(-6)*1`, `(-6)*0`, and continue the pattern. *Hint: (-6)*2=-12, (-6)*1=-6, (-6)*0=0. Each step up by 6.* Answer: -12, -6, 0, then continuing up by 6: (-6)*(-1)=6.


### Practice: Unit 5


1. (-6) + 9

2. (-6) - 4

3. 8 - (-5)

4. (-7) * 4

5. (-6) * (-5), using the pattern method from this unit.

6. (-20) / 4

---


*Unit 6*

## Fractions


> **Big Question:** Why do you need a common denominator to add fractions, but not to multiply them?

A fraction is a count of equal pieces. `3/4` means "3 pieces, out of 4 equal pieces that make a whole." The bottom number (denominator) says how big each piece is. The top number (numerator) says how many of those pieces you have.


### Adding Fractions

`1/2 + 1/3` is not `2/5`. Here's why: a half and a third are pieces of *different sizes*. You can't add "2 pieces of one size" to "1 piece of a different size" and call the total a clean count of pieces, until every piece is the same size.


*Demonstration 1: 1/2 + 1/3*

```
Rewrite both fractions using the same size piece (sixths, since
both 2 and 3 divide evenly into 6):

1/2  =  3/6      (each half is really 3 sixths)
1/3  =  2/6      (each third is really 2 sixths)

Now the pieces match:  3/6 + 2/6 = 5/6
```


> **Why doesn't multiplication need matching pieces?** Multiplying fractions isn't counting pieces of the same size, it's asking "what's a part of a part?" `2/3 * 3/4` asks "what's three-quarters of two-thirds?" That question makes sense no matter what size the pieces are, so multiplication just multiplies straight across: numerators together, denominators together.


*Demonstration 2: multiplying fractions*

```
2/3 * 3/4  =  (2*3) / (3*4)  =  6/12  =  1/2

(6/12 simplifies to 1/2 by dividing top and bottom by 6)
```


### Dividing Fractions

Remember from Unit 4: dividing by a number is the same as multiplying by "1 over that number." Dividing by 4 gives the same answer as multiplying by `1/4`, because `4 * 1/4 = 1`. The exact same idea works for fractions: dividing by `1/4` gives the same answer as multiplying by `4/1` (flip it over), because `1/4 * 4/1 = 1`.


*Demonstration 3: 1/2 divided by 1/4*

```
Question: how many quarters fit inside a half?

1/2  /  1/4   =   1/2  *  4/1   =   4/2   =   2

Check by counting: two quarters make a half. Two fits.
```


**Try It Yourself:** Find `3/4 divided by 1/2` by flipping the second fraction and multiplying. *Hint: 3/4 * 2/1 = ?* Answer: 3/4 * 2/1 = 6/4 = 3/2 (or 1 and a half).


### Practice: Unit 6


1. 1/3 + 1/6 (find a common denominator first)

2. 3/5 - 1/5

3. 2/5 * 5/6, simplified

4. 3/4 divided by 1/2

5. 2/3 of 15 (this means `2/3 * 15`)

---


*Unit 7*

## Decimals


> **Big Question:** What is a decimal, really, and how is it connected to fractions?

Unit 1 showed that moving one spot to the left multiplies a digit's value by 10. Decimals just keep going the other direction, past the ones spot: each spot to the *right* of the decimal point divides by 10 again. The first spot after the point is tenths, the next is hundredths, and so on.


> **Why does this mean a decimal is secretly a fraction?** Because "tenths" and "hundredths" are just fraction denominators wearing a different outfit. `0.3` means 3 tenths, which is the fraction `3/10`. `0.75` means 75 hundredths, which is `75/100`. Every decimal is a fraction with a denominator of 10, 100, 1000, and so on, written in a shorter form.


*Demonstration 1: adding decimals, using the fraction underneath*

```
0.3 + 0.45

As fractions: 3/10 + 45/100

Match the denominators (Unit 6): 3/10 = 30/100

30/100 + 45/100 = 75/100 = 0.75

0.3 + 0.45 = 0.75
```

This is also exactly why lining decimals up by their decimal point when you add them works: lining up the points lines up the tenths with tenths, hundredths with hundredths, the same "matching pieces" idea from Unit 6.


*Demonstration 2: multiplying decimals*

```
1.2 * 0.3

As fractions: 12/10 * 3/10 = 36/100 = 0.36

1.2 * 0.3 = 0.36

Notice: one decimal place in 1.2, one decimal place in 0.3, and
two decimal places in the answer, 0.36, because the denominators
are multiplying together too: 10*10=100.
```


**Try It Yourself:** Find 2.5 * 4 by thinking of 2.5 as the fraction 25/10. *Hint: 25/10 * 4 = 100/10 = ?* Answer: 25/10 * 4 = 100/10 = 10. So 2.5*4=10.


### Practice: Unit 7


1. 1.5 + 2.75

2. 6.4 - 2.9

3. 3.2 * 5

4. 9.6 / 1.6 (hint: turn both into fractions over 10 first: 96/10 divided by 16/10)

---


*Unit 8*

## Order of Operations


> **Big Question:** Why does everyone agree to do multiplication before addition? Couldn't we just go left to right?

Try going strictly left to right on `3 + 4 * 2`. You'd get `3+4=7`, then `7*2=14`. But if you do the multiplication first, `4*2=8`, then `3+8=11`. Same problem, two different answers. That's a real problem: math needs every person, everywhere, to get the same answer to the same written problem, or numbers stop being useful for agreeing on anything.


> **Why multiplication before addition, and not the other way around?** Multiplication is a shortcut for repeated addition (Unit 3). `4*2` is shorthand for `4+4`. If you write `3 + 4*2`, you're really writing `3 + (4+4)` in a compressed form, and doing the multiplication first is just unpacking that shorthand before you add. The agreed order isn't arbitrary, it's the order that respects what multiplication actually stands for.


*Demonstration 1: 3 + 4 * 2*

```
Multiply first: 4*2 = 8
Then add: 3 + 8 = 11

3 + 4 * 2 = 11
```

Parentheses come first, before even multiplication, because they're a direct instruction: "treat everything inside me as one already-finished number before you do anything else with it."


*Demonstration 2: (3+4) * 2, and why it's different*

```
Parentheses first: 3+4 = 7
Then multiply: 7 * 2 = 14

(3+4) * 2 = 14

Compare to Demonstration 1's answer of 11. Same three numbers,
same two operations, different answer, because the parentheses
changed which operation had to happen first.
```


**Try It Yourself:** Find `20 - 4 * 3 + 2`. *Hint: do the multiplication first, then work left to right through the addition and subtraction.* Answer: 4*3=12. Then 20-12+2 = 8+2 = 10.


### Practice: Unit 8


1. 5 + 3 * 4

2. (5 + 3) * 4

3. 18 / 3 + 2 * 5

4. 30 - 2 * (4 + 1)

5. Explain, in your own words, why parentheses are allowed to override the usual order.

---


*Closing*

## You Understand These Rules Now, Not Just Remember Them

Every rule in this book had a reason behind it, and now you know all of them: place value explains carrying and borrowing. Splitting a number by place value explains multiplication. Multiplication in reverse explains division. A pattern that refuses to break explains negative times negative. Matching piece sizes explains adding fractions, and division-as-its-reciprocal explains dividing them. Fractions in disguise explain decimals. And respecting what multiplication stands for explains the order of operations.

None of that was arbitrary. Every single rule followed consistently from place value and the handful of choices this book named along the way, base ten, keeping a pattern going, treating multiplication as repeated addition to start. That's what real math looks like: not a pile of separate facts to memorize, but one small set of chosen starting points, followed carefully wherever they lead.

Algebra is next, and it uses every one of these rules constantly, just with letters standing in for numbers you don't know yet. You're ready for it.


---


*Answer Key*

## Check Your Work


### Unit 1


**1.** 582 = 5 hundreds + 8 tens + 2 ones

**2.** 3,706 = 3 thousands + 7 hundreds + 0 tens + 6 ones

**3.** 6,025: the 0 sits in the hundreds spot, holding it open so the 2 stays correctly in the tens spot.

**4.** The 5 in 512 is worth 500 (five hundreds). The 5 in 125 is worth 5 (five ones). Same digit, different position, different value.

### Unit 2


**1.** 56+38=94. Ones: 6+8=14, write 4 carry 1. Tens: 5+3+1=9. Answer: 94.

**2.** 91-47=44. Ones: borrow, 11-7=4. Tens: 8-4=4. Answer: 44.

**3.** 245+178=423. Ones: 5+8=13, write 3 carry 1. Tens: 4+7+1=12, write 2 carry 1. Hundreds: 2+1+1=4. Answer: 423.

**4.** 604-256=348.

**5.** Ten of whatever you carried in the smaller column are worth exactly one of the next column over, because each column is ten times the value of the one before it.

### Unit 3


**1.** 34*3: 30*3=90, 4*3=12, sum=102.

**2.** 27*4: 20*4=80, 7*4=28, sum=108.

**3.** 42*23: 40*20=800, 40*3=120, 2*20=40, 2*3=6, sum=966.

**4.** Splitting a number by place value just rewrites it as a sum (like 34=30+4) without changing its value, and multiplication spreads out evenly over a sum, so multiplying the pieces separately and adding always gives the same answer as multiplying the whole thing at once.

### Unit 4


**1.** 96/8=12. Check: 12*8=96.

**2.** 144/12=12. Check: 12*12=144.

**3.** 108/9=12. Check: 12*9=108.

**4.** 23/6 = 3 remainder 5, since 6*3=18 and 23-18=5. Check: 6*3=18, and 18+5=23.

**5.** Because division and multiplication undo each other; multiplying your answer by the number you divided by should rebuild the original number.

### Unit 5


**1.** (-6)+9 = 3

**2.** (-6)-4 = -10

**3.** 8-(-5) = 13

**4.** (-7)*4 = -28

**5.** (-6)*(-5): pattern from (-6)*2=-12, (-6)*1=-6, (-6)*0=0, going up by 6 each step: (-6)*(-1)=6, (-6)*(-2)=12, (-6)*(-3)=18, (-6)*(-4)=24, (-6)*(-5)=30.

**6.** (-20)/4 = -5

### Unit 6


**1.** 1/3+1/6: 1/3=2/6, so 2/6+1/6=3/6=1/2.

**2.** 3/5-1/5 = 2/5

**3.** 2/5*5/6 = 10/30 = 1/3

**4.** 3/4 divided by 1/2 = 3/4*2/1 = 6/4 = 3/2

**5.** 2/3 of 15 = 2/3*15 = 30/3 = 10

### Unit 7


**1.** 1.5+2.75 = 4.25

**2.** 6.4-2.9 = 3.5

**3.** 3.2*5 = 16.0

**4.** 9.6/1.6: as fractions, 96/10 divided by 16/10 = 96/16 = 6. So 9.6/1.6=6.

### Unit 8


**1.** 5+3*4: multiply first, 3*4=12, then 5+12=17.

**2.** (5+3)*4: parentheses first, 5+3=8, then 8*4=32.

**3.** 18/3+2*5: 18/3=6, 2*5=10, 6+10=16.

**4.** 30-2*(4+1): parentheses first, 4+1=5, then 2*5=10, then 30-10=20.

**5.** Parentheses are a direct instruction to finish what's inside them first, before anything else happens, which lets you deliberately change the order when the usual order isn't what you meant.

---

<!-- PART I END -->


<!-- PART II BEGIN: sources/letters-that-stand-for-numbers.md, verbatim -->

*Part II*

*A Workbook*

# Letters That Stand For Numbers

### A First Book of Algebra, Where Every Rule Gets a Reason

James Pugmire


---


## Before We Start

In the last book, every number you worked with was a specific, known amount: 38, or 3/4, or -6. Algebra asks a new kind of question: what if you don't know the number yet, but you still need to work with it?

That's what a letter like `x` is for. Not a mystery, not a trick, just a stand-in for a number that's either unknown right now or that can be anything, depending on the problem. Everything in this book is built on arithmetic you already know from the last workbook: adding, multiplying, working with negatives and fractions. Nothing new gets invented. You're about to use those same tools on a number that's wearing a letter instead of a digit.


### How This Book Works

Same shape as before: a big question, an explanation with the reason, worked examples done slowly, a "Try It Yourself" with a hint, and practice problems using only what's been covered so far. Answers are in the back, organized by unit.


---


*Unit 1*

## What Is A Variable?


> **Big Question:** What does a letter like `x` actually mean in a math problem?

Suppose you don't know how many stickers are in a bag, but you know that after adding 3 more, you'd have 8. You could write that as `x + 3 = 8`, where `x` holds the place of "however many stickers are in the bag," a number you don't know yet. The letter is a place holder. It is not a second pile of stickers sitting beside the bag.


> **Why use a letter instead of just guessing the number?** Because writing `x + 3 = 8` lets you reason your way to the answer using rules, instead of guessing numbers one at a time and checking. The letter holds the unknown's place in the sentence so you can work with it. It does not bring its own amount.

Variables also show up for a second reason: to describe a rule that works for *any* number, not just one unknown. "Double a number and add 1" can be written `2x + 1` for whatever number `x` happens to be.


*Demonstration 1: turning words into a variable expression*

```
"5 more than a number"        ->   x + 5
"3 less than a number"         ->   x - 3
"a number doubled"             ->   2x
"a number split into 4 equal
 parts"                        ->   x / 4
```


> **Why does "2x" mean "2 times x" with no multiplication sign?** In algebra, writing a number right next to a letter, with nothing between them, is shorthand for multiplication. `2x` means `2 * x`. It's shorter to write and, once you're used to it, quicker to read.


**Try It Yourself:** Write "7 more than a number, then the whole thing tripled" as an expression. (Hint: do the "7 more than" part first, then triple the whole result using parentheses.) *Hint: "a number" is x. "7 more than a number" is x+7. "Tripled" means multiply the whole thing by 3.* Answer: `3(x + 7)`


### Practice: Unit 1


1. Write "9 more than a number" as an expression.

2. Write "a number, cut in half" as an expression.

3. Write "6 less than a number" as an expression.

4. Write "a number doubled, then increased by 5" as an expression.

5. In your own words, explain what a variable is and give an example that isn't from this book.

---


*Unit 2*

## Evaluating Expressions


> **Big Question:** If you're finally told what number a variable stands for, how do you use that to find the value of a whole expression?

"Evaluating" an expression means plugging in a known number for the variable, then working out the arithmetic using the order of operations rules you already know: parentheses, then multiplication and division, then addition and subtraction.


*Demonstration 1: 3x + 2, at x = 5*

```
3x + 2
Substitute x=5:  3(5) + 2
Multiply first:  15 + 2
                 17

3x+2 at x=5 equals 17.
```


*Demonstration 2: x squared plus 1, at x = 3*

```
x^2 + 1
Substitute x=3:  3^2 + 1
Exponent first:  9 + 1
                 10

x^2+1 at x=3 equals 10.
```


> **Why does the order still matter here?** An expression with a variable is really a set of instructions waiting for a number. Once you substitute the number in, it's an ordinary arithmetic problem, and every rule from order of operations still applies exactly the way it always has.


**Try It Yourself:** Evaluate `2x - 7` at `x = 4`. *Hint: substitute first, then multiply before subtracting.* Answer: 2(4)-7 = 8-7 = 1.


### Practice: Unit 2


1. Evaluate `5x` at `x = 6`.

2. Evaluate `4x + 3` at `x = 2`.

3. Evaluate `x^2 - 4` at `x = 5`.

4. Evaluate `2(x + 3)` at `x = 4`.

---


*Unit 3*

## Combining Like Terms


> **Big Question:** Why can you simplify `3x + 5x` into `8x`, but you can't simplify `3x + 5` at all?

Think of `x` as a box, and you don't know what's inside it yet. `3x` means "3 of that box." `5x` means "5 of that box." If you have 3 boxes and get 5 more identical boxes, you now have 8 boxes: `3x + 5x = 8x`, no matter what's actually inside each box.

But `3x + 5` is "3 boxes" plus "5 loose ones," not boxes. You can't combine boxes and loose ones into one clean count, because they aren't the same kind of thing. `3x + 5` simply stays as it is; there's nothing left to combine.


> **Why does this matter?** Terms that have the exact same variable (like two terms that both have `x`) are called "like terms," and only like terms can be added or subtracted together into one term. A plain number by itself, with no variable, is a different kind of term, and can never combine with a term that has a variable attached.


*Demonstration 1: 3x + 5x*

```
3x + 5x  =  (3+5)x  =  8x

Check with a real number, x=2:
  3(2) + 5(2) = 6+10 = 16
  8(2) = 16
Both sides agree.
```


*Demonstration 2: mixing more than one variable, 4a + 3b + 2a*

```
Only combine the terms that match. 4a and 2a both have "a," so
they combine. 3b is a different kind of term, and stays alone.

4a + 2a + 3b  =  6a + 3b

Check with a=2, b=3:
  4(2)+3(3)+2(2) = 8+9+4 = 21
  6(2)+3(3) = 12+9 = 21
Both sides agree.
```


**Try It Yourself:** Simplify `7x + 3 - 2x`. *Hint: only combine the x terms with each other. The 3 has nothing to combine with.* Answer: `7x - 2x = 5x`, and the 3 stays alone: `5x + 3`.


### Practice: Unit 3


1. Simplify `6x + 2x`.

2. Simplify `9y - 4y`.

3. Simplify `5a + 2b + 3a`.

4. Simplify `8x + 6 - 3x - 2`.

5. Explain why `4x + 3y` cannot be simplified any further.

---


*Unit 4*

## The Distributive Property


> **Big Question:** How do you multiply a number by a whole group of terms inside parentheses, like `3(x + 4)`?

You've actually already done this. Back in the arithmetic book, multiplying 23 by 4 worked by splitting 23 into `20 + 3`, multiplying each piece by 4 separately, and adding the results: `20*4 + 3*4`. That was the distributive property the whole time, just with numbers instead of a variable.


> **Why does the same trick work with a variable inside?** Multiplication spreads out over addition no matter what's being added, numbers or a mix of numbers and variables. `3(x+4)` means "3 groups of (x+4)," and each group has one `x` and one 4 inside it, so 3 groups have `3x` and `12` total.


*Demonstration 1: 3(x + 4)*

```
3(x + 4)  =  3*x  +  3*4  =  3x + 12

Check with x=2:
  3(2+4) = 3(6) = 18
  3(2)+12 = 6+12 = 18
Both sides agree.
```


*Demonstration 2: a negative sign inside, 5(2x - 3)*

```
5(2x - 3)  =  5*2x  -  5*3  =  10x - 15

Check with x=4:
  5(2*4-3) = 5(5) = 25
  10(4)-15 = 40-15 = 25
Both sides agree.
```


**Try It Yourself:** Distribute `4(x + 2)`. *Hint: multiply the 4 by each piece inside the parentheses separately.* Answer: `4x + 8`.


### Practice: Unit 4


1. Distribute `4(x + 2)` and check it with `x=3`.

2. Distribute `6(x - 1)` and check it with `x=3`.

3. Distribute `3(2x + 5)` and check it with `x=2`.

4. Distribute, then combine like terms: `2(x+3) + 4x`.

---


*Unit 5*

## Solving One-Step Equations


> **Big Question:** If `x + 7 = 12`, how do you find out what `x` is, using rules instead of guessing?

Picture a balance scale, perfectly level. Whatever's sitting on the left side weighs exactly the same as whatever's on the right side, that's what the equals sign means. `x + 7 = 12` is a balance scale with "x and a 7-pound weight" on the left, and "a 12-pound weight" on the right.

To find `x` alone, remove the 7 from the left side. But a balance scale tips over if you only remove weight from one side, so you have to remove the same amount from *both* sides to keep it level.


> **Why do you have to do the same thing to both sides?** Because the equals sign is a promise that both sides weigh the same. If you only changed one side, that promise would become false. Doing the identical operation to both sides keeps the balance exactly as true as it was before, while letting you simplify one side down to just `x`.


*Demonstration 1: x + 7 = 12*

```
x + 7 = 12
Subtract 7 from both sides (undoing the +7):
x + 7 - 7 = 12 - 7
x = 5

Check: 5 + 7 = 12. True.
```


*Demonstration 2: 3x = 21*

```
3x = 21
Divide both sides by 3 (undoing the *3):
3x / 3 = 21 / 3
x = 7

Check: 3(7) = 21. True.
```


> **Why divide to undo multiplication?** Same idea as Unit 4 of the arithmetic book: multiplication and division undo each other. If `x` got multiplied by 3, dividing by 3 is exactly what reverses that and leaves `x` by itself.


**Try It Yourself:** Solve `x - 4 = 9`. *Hint: what operation undoes subtracting 4? Do it to both sides.* Answer: add 4 to both sides. `x = 13`. Check: 13-4=9.


### Practice: Unit 5


1. Solve `x + 9 = 15`, and check your answer.

2. Solve `x - 6 = 10`, and check your answer.

3. Solve `4x = 32`, and check your answer.

4. Solve `x / 5 = 7`, and check your answer.

5. Explain, using the balance scale idea, why you can't just subtract 7 from the left side of `x+7=12` without doing anything to the right side.

---


*Unit 6*

## Solving Two-Step Equations


> **Big Question:** What do you do when an equation has two operations attached to `x` instead of one, like `2x + 3 = 11`?

Peel the operations off in the reverse order they were applied, one at a time, using the same "do it to both sides" rule from Unit 5. In `2x + 3`, `x` was first multiplied by 2, then had 3 added. Undo the most recent step first: subtract 3, then divide by 2.


*Demonstration 1: 2x + 3 = 11*

```
2x + 3 = 11
Subtract 3 from both sides:
2x = 8
Divide both sides by 2:
x = 4

Check: 2(4)+3 = 8+3 = 11. True.
```


> **Why subtract before dividing, and not the other way around?** If you divided everything by 2 first, you'd have to divide the 3 as well, turning it into an awkward fraction, since the 3 was added AFTER the multiplication, not as part of it. Peeling off the most recently applied operation first keeps every step clean.


*Demonstration 2: 3x - 5 = 16*

```
3x - 5 = 16
Add 5 to both sides:
3x = 21
Divide both sides by 3:
x = 7

Check: 3(7)-5 = 21-5 = 16. True.
```


**Try It Yourself:** Solve `5x + 2 = 27`. *Hint: subtract 2 first, then divide by 5.* Answer: 5x=25, x=5. Check: 5(5)+2=27.


### Practice: Unit 6


1. Solve `3x + 7 = 22`, and check.

2. Solve `2x - 9 = 11`, and check.

3. Solve `4x + 5 = 25`, and check.

4. Explain why you undo addition or subtraction before you undo multiplication or division, when solving a two-step equation.

---


*Unit 7*

## Variables On Both Sides


> **Big Question:** What if `x` shows up on both sides of the equation, like `5x + 3 = 2x + 12`?

The balance scale idea still works. You can subtract a matching amount of `x` from both sides too, not just plain numbers, because that's still doing the identical thing to both sides. Get all the `x` terms onto one side first, then finish it like a normal two-step equation.


*Demonstration 1: 5x + 3 = 2x + 12*

```
5x + 3 = 2x + 12
Subtract 2x from both sides (removing x from the right):
3x + 3 = 12
Subtract 3 from both sides:
3x = 9
Divide both sides by 3:
x = 3

Check: left side 5(3)+3=18. Right side 2(3)+12=18. They match.
```


> **Why does subtracting 2x from both sides help?** It's the exact same "do the same thing to both sides" rule as always, just with a term that has a variable instead of a plain number. Subtracting 2x from both sides keeps the balance true, and it clears x off the side where you don't want it, leaving all the x's together on one side.


*Demonstration 2: 4x - 1 = x + 8*

```
4x - 1 = x + 8
Subtract x from both sides:
3x - 1 = 8
Add 1 to both sides:
3x = 9
Divide both sides by 3:
x = 3

Check: left 4(3)-1=11. Right 3+8=11. They match.
```


### When x Disappears Completely

Every equation so far has had exactly one answer for `x`. Two other outcomes are just as real, and both show up starting now rather than staying hidden until they surprise you somewhere else.


*Demonstration 3: an equation with no solution, 2x + 3 = 2x + 7*

```
2x + 3 = 2x + 7
Subtract 2x from both sides:
3 = 7

That's false. 3 is never equal to 7, no matter what x is, because
x already canceled out completely. There is no number you could
substitute for x that would make the original equation true.

This equation has no solution.
```


> **Why does this happen, and what does it mean?** Both sides were changing at the exact same rate, `2x`, so subtracting `2x` from both sides didn't just simplify the equation, it erased `x` entirely, leaving a plain comparison between two numbers that flatly disagree. Your solving didn't go wrong anywhere; some equations describe a promise that can never be kept, and the algebra tells you so directly instead of pretending an answer exists.


*Demonstration 4: an equation true for every x, 2(x+1) = 2x + 2*

```
2(x+1) = 2x + 2
Distribute the left side:
2x + 2 = 2x + 2

Both sides are already identical. Subtract 2x from both sides:
2 = 2

That's true, always, no matter what x is. Every number you could
possibly substitute for x makes this equation true.

This equation has infinitely many solutions.
```


**Try It Yourself:** Solve `6x + 4 = x + 24`. *Hint: subtract x from both sides first, then finish like a two-step equation.* Answer: 5x+4=24, 5x=20, x=4. Check: left 6(4)+4=28, right 4+24=28.


### Practice: Unit 7


1. Solve `7x + 2 = 3x + 18`, and check both sides.

2. Solve `5x - 6 = 2x + 9`, and check both sides.

3. Solve `8x - 3 = 3x + 22`, and check both sides.

4. Solve `4x + 5 = 4x + 9`. Does it have one solution, no solution, or infinitely many?

5. Solve `3(x+2) = 3x + 6`. Does it have one solution, no solution, or infinitely many?

---


*Unit 8*

## Exponent Rules


> **Big Question:** When you multiply `x^2` by `x^3`, why does the answer turn out to be `x^5`, and not `x^6`?

An exponent is just a count of how many times a number multiplies itself. `x^2` means `x*x`. `x^3` means `x*x*x`. Multiplying them together means writing all of those `x`'s in a row:


*Demonstration 1: x^2 * x^3*

```
x^2 * x^3  =  (x*x) * (x*x*x)  =  x*x*x*x*x  =  x^5

Count the x's: 2 from the first group, 3 from the second, 5
total. That's why the exponents ADD, 2+3=5, not multiply.

Check with x=2:
  2^2 * 2^3 = 4 * 8 = 32
  2^5 = 32
Both sides agree.
```


> **Why do the exponents add instead of multiply?** Because multiplying two power-of-x expressions just means writing all the x's from both expressions in one long row and counting them. Counting how many x's are in two groups combined is addition, not multiplication, the same as combining like terms in Unit 3.


### Dividing Powers

Division does the opposite: it cancels matching x's from top and bottom, the same way `6/2=3` works by canceling shared factors.


*Demonstration 2: x^5 / x^2*

```
x^5 / x^2  =  (x*x*x*x*x) / (x*x)

Two of the x's on top cancel with the two on the bottom:
  =  x*x*x  =  x^3

The exponents SUBTRACT: 5-2=3.

Check with x=2: 2^5/2^2 = 32/4 = 8, and 2^3=8. They match.
```


**Try It Yourself:** Simplify `x^4 * x^2`, then check it using `x=3`. *Hint: add the exponents.* Answer: `x^6`. Check: 3^4*3^2=81*9=729, and 3^6=729.


### Practice: Unit 8


1. Simplify `x^3 * x^4`, and check it with `x=2`.

2. Simplify `x^6 / x^4`, and check it with `x=3`.

3. Simplify `x^2 * x^2`, and check it with `x=5`.

4. Explain, using the "row of x's" idea, why `x^3 * x^3` is `x^6` and not `x^9`.

---


*Unit 9*

## Graphing On The Coordinate Plane


> **Big Question:** How do you picture an equation with two variables, like `y = 2x + 1`, instead of just solving for one number?

An equation with an `x` and a `y` in it isn't asking for one answer, it's describing a whole pattern: for every `x` you pick, there's a matching `y`. A coordinate plane, two number lines crossing at a right angle, lets you plot each matching pair as a single point, `(x, y)`.


*Demonstration 1: building a table for y = 2x + 1*

```
Pick a few values of x, and use the equation to find the
matching y for each one, the same substitution skill from Unit 2.

x=0:  y = 2(0)+1 = 1     point (0, 1)
x=1:  y = 2(1)+1 = 3     point (1, 3)
x=2:  y = 2(2)+1 = 5     point (2, 5)
x=3:  y = 2(3)+1 = 7     point (3, 7)

Plot these four points and they line up perfectly straight.
That's not a coincidence, every equation shaped like y=(number)x
+(number) draws a straight line.
```


### Slope: How Steep The Line Is

Look at the table above. Every time `x` goes up by 1, `y` goes up by 2. That steady rate of climb is called the **slope**, and you can find it from any two points on the line by dividing how much `y` changed by how much `x` changed.


*Demonstration 2: finding slope from two points, (1,3) and (4,9)*

```
slope  =  change in y  /  change in x
       =  (9 - 3) / (4 - 1)
       =  6 / 3
       =  2

Matches the equation y=2x+1, which climbs by 2 every time x
climbs by 1.
```


> **Why is slope the same number no matter which two points you pick?** Because a straight line climbs at the same steady rate everywhere along it. That is what makes it straight. Picking a different pair of points measures the same climb over a different distance, and the ratio works out the same.

The sign of a single change follows which way you called positive. The slope is a ratio of two changes made under the same naming, so flipping both namings leaves the slope put. A vertical line is the other case: change in x is 0, and there is nothing to divide by. Not a huge slope. Not slope 0.


> Does every line have a slope? Not quite every line. Slope divides change in y by change in x, and division refuses to give an answer when you'd be dividing by zero. A perfectly vertical line, straight up and down, never changes its x at all between any two of its points, change in x is always 0, so its slope is undefined, not zero and not some huge number, genuinely undefined. Steepness simply has nothing to measure on the one kind of line where every point shares the same x.


**Try It Yourself:** Find the slope between the points `(0, 1)` and `(2, 5)`. *Hint: change in y over change in x.* Answer: (5-1)/(2-0) = 4/2 = 2.


### Practice: Unit 9


1. Build a table of (x,y) pairs for `y = 3x - 2`, using x = 0, 1, 2, 3.

2. Find the slope between the points `(2, 4)` and `(5, 13)`.

3. Find the slope between the points `(0, 0)` and `(3, 9)`.

4. Try to find the slope between `(3, 1)` and `(3, 7)`. What happens, and why?

5. Explain, in your own words, what the slope of a line actually measures.

---


*Closing*

## You Can Reason With The Unknown Now

Every idea in this book rested on the arithmetic from the last one. Combining like terms was counting matching boxes. The distributive property was the same partial-products idea from multiplying two-digit numbers, just with a letter mixed in. Solving equations was keeping a balance scale level. Exponent rules were counting how many times a number gets written in a row. Nothing here was a new kind of thinking, it was the thinking you already had, aimed at a number that hadn't been found yet.

That's the real shift this book asked you to make: from working with numbers you're handed, to working with numbers you're solving for. Geometry is next, and it uses this same algebra constantly, solving for missing side lengths and missing angles the exact same way you just solved for x.


---


*Answer Key*

## Check Your Work


### Unit 1


**1.** x + 9

**2.** x / 2

**3.** x - 6

**4.** 2x + 5

**5.** A variable is a letter standing in for a number that's unknown or that can change. (Answers will vary; check that the example genuinely uses a letter for an unknown number.)

### Unit 2


**1.** 5(6) = 30

**2.** 4(2)+3 = 11

**3.** 5^2-4 = 25-4 = 21

**4.** 2(4+3) = 2(7) = 14

### Unit 3


**1.** 8x

**2.** 5y

**3.** 8a + 2b

**4.** 5x + 4

**5.** Because 4x and 3y don't share the same variable, they aren't like terms, and only like terms can combine.

### Unit 4


**1.** 4x+8. Check x=3: 4(5)=20, 12+8=20.

**2.** 6x-6. Check x=3: 6(2)=12, 18-6=12.

**3.** 6x+15. Check x=2: 3(9)=27, 12+15=27.

**4.** 2x+6+4x = 6x+6.

### Unit 5


**1.** x=6. Check: 6+9=15.

**2.** x=16. Check: 16-6=10.

**3.** x=8. Check: 4(8)=32.

**4.** x=35. Check: 35/5=7.

**5.** Subtracting from only one side would make the two sides unequal, breaking the balance the equals sign promises.

### Unit 6


**1.** 3x=15, x=5. Check: 3(5)+7=22.

**2.** 2x=20, x=10. Check: 2(10)-9=11.

**3.** 4x=20, x=5. Check: 4(5)+5=25.

**4.** Because addition or subtraction was applied last when building the expression, so it has to be undone first to safely reach the multiplication or division underneath.

### Unit 7


**1.** 4x=16, x=4. Check: left 7(4)+2=30, right 3(4)+18=30.

**2.** 3x=15, x=5. Check: left 5(5)-6=19, right 2(5)+9=19.

**3.** 5x=25, x=5. Check: left 8(5)-3=37, right 3(5)+22=37.

**4.** Subtract 4x from both sides: 5=9, which is false. No solution.

**5.** Distribute: 3x+6=3x+6, true for every x. Infinitely many solutions.

### Unit 8


**1.** x^7. Check x=2: 2^3*2^4=128, 2^7=128.

**2.** x^2. Check x=3: 3^6/3^4=9, 3^2=9.

**3.** x^4. Check x=5: 5^2*5^2=625, 5^4=625.

**4.** x^3*x^3 lines up 3 x's from the first group and 3 more from the second, 6 total, not 9; the exponents count x's, and combining two counts is addition.

### Unit 9


**1.** (0,-2), (1,1), (2,4), (3,7)

**2.** (13-4)/(5-2) = 9/3 = 3

**3.** (9-0)/(3-0) = 3

**4.** Change in x is 3-3=0, and dividing by 0 is refused, so the slope is undefined. The line through these two points is vertical.

**5.** Slope measures how steeply a line climbs, how much y changes for every step x takes.

---

<!-- PART II END -->


<!-- PART III BEGIN: sources/shapes-and-why-they-measure-out.md, verbatim -->

*Part III*

*A Workbook*

# Shapes and Why They Measure Out

### A First Book of Geometry, Where Every Formula Gets a Reason

James Pugmire


---


## Before We Start

The last two books worked entirely with numbers and letters. This one adds shape: triangles, rectangles, circles, boxes. Every formula you'll meet, the area of a triangle, the Pythagorean theorem, the circumference of a circle, gets built from a picture first and a formula second, never the other way around.

You'll still use everything from the last two books constantly: solving equations to find a missing side, substituting numbers into a formula, working with fractions and decimals for measurements that don't come out even. Geometry is algebra and arithmetic, aimed at shapes.


### How This Book Works

Same shape as before: a big question, an explanation with the reason (usually a picture), worked examples, a "Try It Yourself," and practice problems using only what's been covered so far. Answers are in the back, organized by unit.


---


*Unit 1*

## Points, Lines, and Angles


> **Big Question:** What exactly is an angle, and how do you tell different angles apart?

An angle is the amount of turn between two rays (straight lines that start at a point and go on forever in one direction) that share a starting point, called the **vertex**. Angles are measured in **degrees**, written with the symbol `°`. A full turn all the way around back to where you started is 360°.


> **Why 360 degrees, and not some rounder number like 100?** It's a leftover from ancient astronomers, who divided the sky into 360 parts because 360 divides evenly by so many small numbers (2, 3, 4, 5, 6, 8, 9, 10, 12...), which makes cutting a circle into neat, even wedges easy. It's a choice people made a long time ago, not a law of nature, but it's the choice the whole world still uses.

One more choice, bigger than degrees, sits underneath this entire book: everything here is drawn on a flat surface, like a sheet of paper stretched out forever in every direction. That sounds too obvious to be a choice, but it isn't automatic. Draw a triangle on a flat sheet of paper and on a giant curved ball instead, and some of the rules ahead behave differently depending on which one you picked. This book stays flat, the whole way through, the same way it stayed in base ten the whole way through the last book.


*[Diagram: Four angle types, measured by the turn between the two rays. -- see the PDF version for the actual image]*

An acute angle is any angle smaller than a right angle (less than 90°). A right angle is exactly 90°, marked with a small square instead of a curve, the standard symbol for "exactly a quarter turn." An obtuse angle is bigger than 90° but smaller than 180°. A straight angle is exactly 180°, a straight line.


**Try It Yourself:** Is a 35° angle acute, right, obtuse, or straight? What about 150°? *Hint: compare each to 90° and 180°.* Answer: 35° is acute (less than 90°). 150° is obtuse (more than 90°, less than 180°).


### Practice: Unit 1


1. Classify a 90° angle.

2. Classify a 175° angle.

3. Classify a 10° angle.

4. Classify a 91° angle.

5. Two angles sit next to each other along a straight line, so together they must add up to 180°. If one of them is 65°, what is the other?

---


*Unit 2*

## Triangles


> **Big Question:** Why do the three angles inside every flat triangle always add up to exactly 180°, no matter what shape the triangle is?


### Naming Triangles By Their Sides


*[Diagram: Triangles named by how many sides match. -- see the PDF version for the actual image]*


### Why The Angles Always Sum To 180°

Here's a way to see it for yourself instead of taking it on faith. Draw any triangle, color its three corner angles three different colors, then cut them off and slide them together, corner to corner.


*[Diagram: The three angles, placed corner to corner, always form a straight line. -- see the PDF version for the actual image]*


> **Why does this always work, for every flat triangle?** This isn't something that happens to work for a few lucky triangles, it's forced by how a triangle is built, on a flat surface. A more formal proof (drawing a line through one corner parallel to the opposite side) shows the same result algebraically, but the corner-cutting picture is the same fact, made visible.


> Does this still work on a curved surface? No, and this shows exactly what "on a flat surface" was doing in the sentence above. Picture a triangle drawn on the Earth: one corner at the North Pole, and the other two corners on the equator, a quarter of the way around the planet from each other. Each of the two lines running from the pole down to the equator meets the equator at a right angle, 90°, and the angle at the pole between them is also a right angle, 90°, since the two equator points sit a quarter turn apart. Three right angles: `90 + 90 + 90 = 270`, not 180. The rule this unit just built isn't wrong. It was always a rule about flat triangles specifically, and it was true the whole time to say so.


*Demonstration 1: finding a missing angle*

```
A triangle has angles of 50° and 70°. What's the third?

50 + 70 + x = 180
120 + x = 180
x = 60

The third angle is 60°.
```


**Try It Yourself:** A triangle has angles of 90° and 35°. Find the third angle. *Hint: set up 90 + 35 + x = 180, then solve for x like Unit 5 of the algebra book.* Answer: 90+35=125. 180-125=55. The third angle is 55°.


### Practice: Unit 2


1. A triangle has angles of 60° and 60°. Find the third angle. What kind of triangle is this, by its sides, based on what you'd expect?

2. A triangle has angles of 40° and 40°. Find the third angle.

3. A triangle has one angle of 90° and another of 30°. Find the third.

4. Explain, in your own words, why you can always find a triangle's third angle if you know the other two, on a flat surface.

5. A triangle drawn on a curved surface has three right angles, like the North Pole example. What do its angles add up to, and why doesn't that break the rule this unit taught?

---


*Unit 3*

## Perimeter


> **Big Question:** How far would you walk if you traced the entire outside edge of a shape?

**Perimeter** is the total distance around the outside of a shape. It's nothing more than adding up every side length, which means everything you know about addition already applies.


*[Diagram: A rectangle with two sides of 8 and two sides of 5. -- see the PDF version for the actual image]*


*Demonstration 1: perimeter of the rectangle above*

```
Add every side: 8 + 8 + 5 + 5 = 26

Or, since opposite sides of a rectangle always match, use the
shortcut: 2(8) + 2(5) = 16 + 10 = 26

Same answer either way, since 2(8)+2(5) is just a faster way to
add "8 twice and 5 twice."
```


> **Why does the shortcut formula work?** A rectangle always has two pairs of matching sides. Adding a number to itself is the same as doubling it, so "8+8" and "2 times 8" are the exact same amount, just written two different ways. The formula is a shortcut for the addition, not a different idea.


*Demonstration 2: a triangle's perimeter, sides 3, 4, 5*

```
A triangle doesn't usually have matching sides, so there's no
shortcut, just add all three: 3 + 4 + 5 = 12
```


**Try It Yourself:** Find the perimeter of a rectangle with sides 6 and 9. *Hint: 2(6) + 2(9).* Answer: 12 + 18 = 30.


### Practice: Unit 3


1. Perimeter of a rectangle with sides 7 and 10.

2. Perimeter of a triangle with sides 6, 7, and 9.

3. A square has all four sides equal to 5. Find its perimeter. (Hint: a square is just a rectangle where both side lengths match.)

4. A rectangle has a perimeter of 24 and one side is 4. Find the other side. (Hint: set up an equation like Unit 5 of the algebra book: 2(4) + 2x = 24.)

---


*Unit 4*

## Area of Rectangles and Triangles


> **Big Question:** Why does multiplying length times width give you the area of a rectangle?

**Area** is how much flat space a shape covers, measured by counting how many unit squares (squares 1 unit by 1 unit) fit inside it.


*[Diagram: A 6-by-4 rectangle, filled with unit squares. -- see the PDF version for the actual image]*


> **Why does length times width count the squares?** Each of the 4 rows holds exactly 6 squares, since the rectangle is 6 units wide. Four rows of 6 is `4*6`, which is exactly what multiplication already means: 6, repeated 4 times. The formula isn't a separate rule, it's just multiplication doing the counting for you instead of counting one square at a time.


*Demonstration 1: area of the rectangle above*

```
length = 6, width = 4

Area = length * width = 6 * 4 = 24 square units

Count the grid above to check: 4 rows of 6 squares is 24.
```


### Area of a Triangle


*[Diagram: A triangle is always exactly half of the rectangle that surrounds it. -- see the PDF version for the actual image]*


> **Why is a triangle's area half the base times the height?** Build the rectangle whose width is the base and whose height is the perpendicular height. That rectangle's area is base times height. The triangle covers half of it. A diagonal cuts a rectangle into two matching triangles only when the third corner sits on a corner of that rectangle. Other triangles still have area base times height, divided by 2. The diagonal picture is one case of that fact, not every case.


*Demonstration 2: area of a triangle, base 6, height 4*

```
The surrounding rectangle would have area 6*4=24.
The triangle is half of that.

Area = (base * height) / 2 = (6 * 4) / 2 = 24 / 2 = 12 square units
```


**Try It Yourself:** Find the area of a triangle with base 10 and height 6. *Hint: multiply base times height, then divide by 2.* Answer: (10*6)/2 = 60/2 = 30 square units.


### Practice: Unit 4


1. Area of a rectangle with length 9 and width 5.

2. Area of a triangle with base 8 and height 5.

3. Area of a square with side 7. (Hint: a square is a rectangle where length equals width.)

4. A rectangle has area 48 and length 8. Find its width. (Hint: set up 8x=48 and solve, like Unit 5 of the algebra book.)

---


*Unit 5*

## The Pythagorean Theorem


> **Big Question:** In a right triangle, why does `a² + b² = c²` connect the two legs to the longest side?

A right triangle has one 90° angle. The two shorter sides touching that right angle are called **legs**, usually named `a` and `b`. The longest side, opposite the right angle, is the **hypotenuse**, named `c`.


*[Diagram: A square built on each side of a right triangle. -- see the PDF version for the actual image]*


> **Why does this picture prove the formula?** Build an actual square on each side of a right triangle, the way the picture shows. It's a genuine, checkable fact (provable by rearranging the pieces, a classic exercise) that the area of the two small squares always adds up to exactly the area of the big square on the hypotenuse. Since the area of a square is its side length squared, that fact *is* the formula: `a² + b² = c²`. Like the triangle angle sum in Unit 2, this is a flat-surface fact; a "straight-sided" triangle drawn on a curved surface doesn't follow it.


*Demonstration 1: finding the hypotenuse, legs 3 and 4*

```
a=3, b=4. Find c.

a^2 + b^2 = c^2
3^2 + 4^2 = c^2
9 + 16 = c^2
25 = c^2

What number, squared, gives 25? c = 5.

Check: 3^2+4^2 = 9+16 = 25, and 5^2 = 25. They match.
```


*Demonstration 2: finding a missing leg, hypotenuse 10, one leg 6*

```
a=6, c=10. Find b.

a^2 + b^2 = c^2
6^2 + b^2 = 10^2
36 + b^2 = 100
b^2 = 100 - 36 = 64

What number, squared, gives 64? b = 8.

Check: 6^2+8^2 = 36+64 = 100, and 10^2=100. They match.
```


> **Why does finding a missing leg work differently from finding the hypotenuse?** The formula never changes, only which letter is unknown. When the hypotenuse is missing, you add the two legs' squares. When a leg is missing, you're solving the exact same equation for a different letter, using the same "same thing to both sides" idea from Unit 5 of the algebra book: subtract the known leg's square from the hypotenuse's square instead of adding.

Every example so far has landed on a whole number, 5, 8, 12, but that's the exception among right triangles, not the rule.


*Demonstration 3: legs 1 and 1*

```
a=1, b=1. Find c.

a^2 + b^2 = c^2
1^2 + 1^2 = c^2
1 + 1 = c^2
2 = c^2

What number, squared, gives 2? No whole number does: 1^2=1 and
2^2=4, and 2 sits in between. c is the number whose square is 2,
written c = sqrt(2). The digits 1.414... are a display. They do
not finish. The name is the rule: the number that squares to 2.

The legs 3-4-5, 6-8-10, and 5-12-13 used earlier in this unit are
a special, convenient family. Most right triangles look like
this one instead.
```


**Try It Yourself:** A right triangle has legs 5 and 12. Find the hypotenuse. *Hint: 5^2+12^2=c^2. What's 25+144? What number squared gives that?* Answer: 25+144=169. 13^2=169. The hypotenuse is 13.


### Practice: Unit 5


1. Legs 6 and 8. Find the hypotenuse.

2. Hypotenuse 13, one leg 5. Find the other leg.

3. Legs 9 and 12. Find the hypotenuse.

4. Legs 2 and 2. Find the hypotenuse. It won't be a whole number; leave it as a square root.

5. Explain, using the squares picture, what "a squared plus b squared" actually represents.

---


*Unit 6*

## Circles


> **Big Question:** What do radius, diameter, and `π` actually mean, and how are they connected?


*[Diagram: Radius reaches from the center to the edge. Diameter crosses the whole circle. -- see the PDF version for the actual image]*

The **radius** is the distance from the center of a circle to its edge. The **diameter** is the distance all the way across, through the center, which is always exactly twice the radius: `diameter = 2 * radius`, since crossing the whole circle means going out to the edge and continuing the same distance again on the other side.

The **circumference** is the distance all the way around the outside, the circle's perimeter. On a flat circle, that distance divided by the diameter is the same ratio for every size. The name of that ratio is `π`. Writing 3.14 is a rounded stand-in for display. The leftover is still part of the ratio. This book uses 3.14 when a problem asks for a decimal, and says so.


> **Why is that ratio always the same number, no matter the circle's size?** Measure the distance around any flat circle, divide by the distance across it, and you always get the same number, about 3.14159... forever without repeating. That number gets its own symbol, `π` (pi), because writing out its digits every time would be impossible. Bigger circles have bigger circumferences AND bigger diameters, growing together at that same fixed ratio. This is the same kind of fact as the 180° triangle rule from Unit 2: true because the circle is flat. A circle traced on a curved surface, like a circle of constant latitude near the North Pole, doesn't keep this same ratio.


*Demonstration 1: circumference, radius 10, using π ≈ 3.14*

```
diameter = 2 * radius = 2 * 10 = 20

circumference = pi * diameter = 3.14 * 20 = 62.8
```


*Demonstration 2: area of a circle, radius 10*

```
Area = pi * radius^2 = 3.14 * 10^2 = 3.14 * 100 = 314
```


> **Why does area use radius squared, but circumference just uses radius (or diameter) alone?** Circumference is a length, a distance around a 1-dimensional edge, so it scales directly with radius. Area is a measure of flat space, spreading in two directions at once, so it scales with radius multiplied by itself, the same reason a rectangle's area needed two lengths multiplied together back in Unit 4.


**Try It Yourself:** Find the circumference and area of a circle with radius 4, using π ≈ 3.14. *Hint: circumference = pi * diameter. area = pi * radius^2.* Answer: diameter=8, circumference=3.14*8=25.12. Area=3.14*16=50.24.


### Practice: Unit 6


1. A circle has radius 5. Find its diameter.

2. A circle has radius 10. Find its circumference, using π ≈ 3.14.

3. A circle has radius 10. Find its area, using π ≈ 3.14.

4. Explain, in your own words, why doubling a circle's radius more than doubles its area.

---


*Unit 7*

## Volume of a Box


> **Big Question:** Why does multiplying length times width times height give you the amount of space inside a box?

**Volume** is how much space a solid shape takes up, measured by counting how many unit cubes (cubes 1 unit on every side) fit inside it. A rectangular box (formally, a rectangular prism) has three measurements: length, width, and height.


*[Diagram: A box has three measurements: length, width, and height. -- see the PDF version for the actual image]*


> **Why multiply all three together?** Think of it in two steps, building on what you already know. Unit 4 showed that length times width gives the area of one flat layer, the base of the box, in square units, how many unit squares cover the bottom. Stack that same layer up, one unit cube thick at a time, for as many layers as the height calls for. Multiplying by the height is just repeating that base layer's count, the same repeated-counting idea behind every multiplication in this book so far.


*Demonstration 1: volume of a box, 5 by 4 by 3*

```
Base layer area = length * width = 5 * 4 = 20 unit squares

Stack 3 layers that tall: 20 * 3 = 60

Volume = length * width * height = 5 * 4 * 3 = 60 cubic units
```


**Try It Yourself:** Find the volume of a box 6 by 2 by 4. *Hint: multiply all three measurements together, in any order.* Answer: 6*2*4 = 48 cubic units.


### Practice: Unit 7


1. Volume of a box 7 by 3 by 2.

2. Volume of a cube with every side equal to 4. (Hint: a cube is a box where all three measurements match.)

3. A box has volume 60, length 5, and width 4. Find its height. (Hint: set up 5*4*x=60 and solve, like the algebra book.)

4. Explain, in your own words, why volume needs three measurements multiplied together while area only needs two.

---


*Closing*

## You Can See The Reason Now, Not Just The Formula

Every formula in this book came from a picture first. The Pythagorean theorem came from three real squares, built on the sides of a real triangle, with their areas actually adding up. A triangle's area came from cutting a rectangle in half. A box's volume came from stacking flat layers you already knew how to count. None of it needed to be memorized as a bare fact, because you built each one from something you could see.

Every unit also leaned on the algebra book constantly: solving for a missing side, substituting numbers into a formula, setting up an equation when something was unknown. Shape and unknown numbers were never two separate subjects. Geometry is what algebra looks like once you give it something to measure.

That's arithmetic, algebra, and geometry, three books, each one built entirely on the one before it, and every rule in all three earned the right to be believed instead of asked to be memorized on faith.


---


*Answer Key*

## Check Your Work


### Unit 1


**1.** Right

**2.** Obtuse

**3.** Acute

**4.** Obtuse

**5.** 180-65=115 degrees

### Unit 2


**1.** 180-60-60=60 degrees. All three angles equal means all three sides are equal too, so this is an equilateral triangle.

**2.** 180-40-40=100 degrees

**3.** 180-90-30=60 degrees

**4.** Because on a flat surface the three angles always add to exactly 180 degrees, so the third angle is always 180 minus the sum of the other two.

**5.** 270 degrees. It doesn't break the rule because the rule was always specifically about flat triangles; a triangle on a curved surface was never the thing the rule was describing.

### Unit 3


**1.** 2(7)+2(10)=14+20=34

**2.** 6+7+9=22

**3.** 4(5)=20

**4.** 2(4)+2x=24, 8+2x=24, 2x=16, x=8

### Unit 4


**1.** 9*5=45 square units

**2.** (8*5)/2=20 square units

**3.** 7*7=49 square units

**4.** 8x=48, x=6

### Unit 5


**1.** 6^2+8^2=36+64=100. Hypotenuse=10.

**2.** 13^2-5^2=169-25=144. Other leg=12.

**3.** 9^2+12^2=81+144=225. Hypotenuse=15.

**4.** 2^2+2^2=4+4=8. Hypotenuse = square root of 8, which is 2 times the square root of 2, about 2.83.

**5.** The area of the two squares built on the two legs, added together, always equals the area of the square built on the hypotenuse.

### Unit 6


**1.** Diameter = 2(5) = 10

**2.** Diameter=20, circumference=3.14*20=62.8

**3.** Area=3.14*100=314

**4.** Area uses radius squared (radius times itself), so doubling the radius multiplies the area by 2*2=4, not just 2.

### Unit 7


**1.** 7*3*2=42 cubic units

**2.** 4*4*4=64 cubic units

**3.** 5*4*x=60, 20x=60, x=3

**4.** Area measures flat space, spreading in two directions, so it needs two measurements multiplied. Volume measures space that also spreads upward, a third direction, so it needs a third measurement multiplied in.

---

<!-- PART III END -->


<!-- PART IV BEGIN: sources/every-number-is-a-rule-corrected.md, verbatim -->

*Part IV*

*A Workbook, Complete Edition*

# Every Number Is A Rule

### A Full Calculus, Built From Three Moves And One Alphabet, With Nothing Imported

James Pugmire


---


## Before We Start

This book builds one machine and uses it the whole way through. The machine has an alphabet: pairs of fractions, written `(value, rate)`. It has three moves: `isolate`, which builds a pair from a starting number and a starting rate; `mix`, which combines two pairs by a rule fixed once and used everywhere; and `rate`, which reads off how fast one pair is changing compared to another. Addition and subtraction work piece by piece. Division gets derived from `mix`, not added as a fourth move.

Every number that appears in this book, from the first rate to the square root of 2 to the number `e` to an exact turn through a circle, is the *output* of running these three moves over that alphabet, a specific number of steps, checkable by hand. No number in this book is ever asserted to simply exist, ahead of the steps that produce it. When a number needs more steps than fit on a page, what you get instead is the rule itself: a finite procedure that produces the number to any precision you name, with the exact remaining gap stated, not estimated.

This edition adds three things the first edition didn't reach: a rate that has its own rate, built by nesting the machine inside itself with no new rule written; a way to find exactly when and where two moving things meet, using nothing but subtraction and division; and a second, exact construction for turning and rotation, built from whole-number pairs instead of an infinite series. All three come from the same three moves. Nothing new was adjoined to reach them.


### How This Book Works

Every unit has a big question, an explanation with the reason attached, worked examples done slowly, a "Try It Yourself" with a hint, and practice problems using only what's been covered so far. Answers are in the back, organized by unit.

Some rules in this book are forced: once you fix what came before, they can't come out any other way, and the demonstration shows why. Others are picked, because picking them is useful, and a purple box marked **A choice, not a discovery** says so and says what the choice buys. The book never claims more certainty than a rule earns, and it never calls two different constructions the same thing just because they rhyme.


---


*Unit 1*

## The Alphabet And The First Move


> **Big Question:** How do you write down a number and how fast it's changing, at the same time, without losing either one?

Everything in this book is built on one alphabet: pairs of fractions, `(value, rate)`. Nothing else gets adjoined to it, ever, unless a unit says so explicitly and names what the addition buys.

Picture a bathtub. Right now it has 8 gallons in it. The faucet is adding 2 gallons every minute. Two facts, true at the same moment: the amount right now, and how fast that amount is changing. Write both together as a pair: `(8, 2)`.


> **Why write it this way?** A number alone can't say whether it's about to grow, shrink, or sit still. "8 gallons" alone says nothing about the next minute. Keeping the two numbers glued together as one pair means the second fact is never lost.


### The First Move: isolate

The move that produces a pair from a starting value and a starting rate is called `isolate`. Everything else in this book is built by combining outputs of `isolate`.


*Demonstration 1: isolate(8, 2)*

```
isolate(8, 2)  means  "start at 8, with a rate slot of 2"

isolate(8, 2)  outputs  (8, 2)
```


*Demonstration 2: a rate of 0*

```
A puddle has 3 cups of water and nothing is being added or removed.

isolate(3, 0)  outputs  (3, 0)
```


*Demonstration 3: the shortcut*

```
isolate(5)  is short for  isolate(5, 1)  outputs  (5, 1)

Seeding something with rate 1 means: this is the thing everything
else gets compared to, so of course it moves at rate 1 relative
to itself. Unit 2 shows exactly why that's useful.
```


**Try It Yourself:** A plant is 12 centimeters tall and growing 1 centimeter per week. What does `isolate` output for this? *Hint: value first, then rate.* Answer: `isolate(12, 1)` outputs `(12, 1)`.


### Practice: Unit 1


1. A savings account has $40 in it and grows by $3 a week. What does isolate output?

2. A candle is 15 cm tall and isn't lit. What does isolate output?

3. What does `isolate(20, 4)` output, and what does each number mean?

4. A pool has 500 gallons and is draining at 10 gallons a minute. What does isolate output? (A rate can be negative.)

5. What does `isolate(7)` output, without writing the rate out? What rate does the shortcut assume?

---


*Unit 2*

## The Second Move: Reading A Rate


> **Big Question:** Given two outputs of isolate, how do you find out how fast one is changing compared to the other?

Two hoses filling two buckets. Hose A fills at 4 gallons a minute, Hose B at 2. Hose A is filling twice as fast, found by dividing the two rates: `4/2 = 2`. That's the second move, called `rate`. Given two pairs, it divides the second slot of one by the second slot of the other. It never looks at the first slot of either.


*Demonstration 1: rate(A, B)*

```
A = isolate(10, 4)  outputs  (10, 4)
B = isolate(5, 2)   outputs  (5, 2)

rate(A, B)  =  4 / 2  =  2

A is changing twice as fast as B.
```


> **Why does rate ignore the first slot?** "How much faster is A changing than B" is a question about speed, not about where each one started. A car at 60 mph is going twice as fast as a car at 30 mph, whether the fast car started the trip at mile 0 or mile 500. Only the rate slot answers a question about speed.


*Demonstration 2: comparing an output to itself*

```
x = isolate(7)  outputs  (7, 1)

rate(x, x)  =  1 / 1  =  1

Anything compared to itself outputs rate 1 when its rate slot is
not 0, no matter the value. If the rate slot is 0 there is nothing
to land on. That refusal is named in Unit 6, not answered with 1.
The shortcut rate of 1 is useful because seeding something with
rate 1 means this is what everything else gets compared to, and
the comparison can land.
```


**Try It Yourself:** E = isolate(9,6), F = isolate(2,3). What does rate(E,F) output? *Hint: divide the two rate slots.* Answer: rate(E,F) = 6/3 = 2.


### Practice: Unit 2


1. P=isolate(30,8), Q=isolate(10,4). What does rate(P,Q) output?

2. M=isolate(6,9), N=isolate(1,3). What does rate(M,N) output?

3. If rate(A,B) outputs 3, what does that tell you about how A is changing compared to B?

4. What does rate(x,x) output for x=isolate(50,6), without dividing? Explain how you knew.

5. G=isolate(100,12), H=isolate(8,4). What does rate(G,H) output?

6. Explain why rate never uses the first slot of either pair.

---


*Unit 3*

## The Third Move: Mixing Two Readings


> **Big Question:** If two things are both changing, and you combine them by multiplication, how fast does the result change?

Build this one slowly, with a picture, before touching a rule.


### The Growing Rectangle

A rectangle whose width is growing and whose height is *also* growing, at the same time. What happens to its area? Sketch it: the right edge sliding out, the top edge sliding up, both at once. The area gains new space from two directions:

- A thin new strip along the right edge, as wide as the width is growing, as tall as the *current* height
- A thin new strip along the top edge, as tall as the height is growing, as wide as the *current* width

Miss either strip and you've undercounted the growth. Add exactly these two strips to the starting area, and that sum is what the rule below outputs, in full.


*[Diagram: The starting area plus the two strips. That sum is the whole output. (see the PDF for the image)]*


### The Rule

This move is called `mix`. Given two outputs of isolate, `(v1,r1)` and `(v2,r2)`, it's fixed once, here, and used everywhere in this book from here on:


*The mix rule*

```
mix( (v1,r1), (v2,r2) )  outputs  (v1*v2,  r1*v2 + v1*r2)

new value  =  v1 * v2                 (ordinary multiplication)
new rate   =  r1*v2  +  v1*r2         (the two strips, added)
```

`r1*v2` is the first strip: how fast the first number is growing, spread across the second number's current size. `v1*r2` is the second strip, the other way round. This book writes `mix(A,B)` as `A*B` from here on, since it's the only multiplication a pair ever uses.


*Demonstration 1: x = isolate(4), mix(x,x)*

```
x = isolate(4)  outputs  (4, 1)

mix(x,x):
  new value = 4*4 = 16
  new rate  = (1*4) + (4*1) = 8

mix(x,x)  outputs  (16, 8)

rate(mix(x,x), x)  outputs  8
```


*Demonstration 2: x = isolate(3), mix(x,x)*

```
x = isolate(3)  outputs  (3, 1)

mix(x,x):
  new value = 3*3 = 9
  new rate  = (1*3) + (3*1) = 6

mix(x,x)  outputs  (9, 6)

rate(mix(x,x), x)  outputs  6
```

In both demonstrations the rate that comes out, 8 and 6, is exactly double the value fed in, 4 and 3. Not a coincidence: seeded with rate 1, both strips equal the value itself, so together they output double it.


**Try It Yourself:** x = isolate(6). What does mix(x,x) output, and what does rate(mix(x,x),x) output? *Hint: new value = 6*6. new rate = (1*6)+(6*1).* Answer: mix(x,x) outputs (36,12). rate(mix(x,x),x) outputs 12.


### Practice: Unit 3

For each, isolate the value, then find what mix(x,x) and rate(mix(x,x),x) output. Show both strips before adding.


1. x = isolate(7)

2. x = isolate(8)

3. x = isolate(9)

4. x = isolate(5)

5. Predict, without arithmetic, what rate(mix(x,x),x) outputs for x=isolate(12). Then check.

6. A classmate says "why not just multiply the two rate slots instead of adding two strips?" For x=isolate(3), that would output 1*1=1. Compare to the real output from Demonstration 2, 6. What does that tell you?

---


*Unit 4*

## Bigger Powers


> **Big Question:** Unit 3 mixed two outputs of isolate. What if you need to mix three, or ten?

Nothing new. `x*x*x` is `mix(x,x)`, then mixed with `x` again, the same rule from Unit 3, applied twice.


*Demonstration 1: x = isolate(2), x*x*x*

```
x = isolate(2)  outputs  (2, 1)

Step 1: mix(x,x)
  new value = 2*2 = 4
  new rate  = (1*2)+(2*1) = 4
  mix(x,x) outputs (4, 4)

Step 2: mix(mix(x,x), x), using (4,4) and (2,1)
  new value = 4*2 = 8
  new rate  = (4*2)+(4*1) = 12
  outputs (8, 12)

rate(x*x*x, x) outputs 12
```


> **Why does this work?** The mix rule from Unit 3 takes any two pairs, not just two direct outputs of isolate. mix(x,x) is itself a pair, so mixing it with x again uses the identical rule, with nothing new to check.


*Demonstration 2: x = isolate(4), x*x*x*

```
Step 1: mix(x,x) outputs (16, 8)
Step 2: mix((16,8),(4,1)): value=16*4=64, rate=(8*4)+(16*1)=48
outputs (64, 48)

rate(x*x*x, x) outputs 48
```

At `x=2` the rate output was 12, and `3*2*2=12`. At `x=4` it was 48, and `3*4*4=48`. Cubing always outputs a rate of `3` times `x` times `x`, built here from two applications of one rule, not handed down as a formula.


### Any Number Of Mixes, Not Just Three

Mix `x` with itself `n` times, for any whole number n, and a pattern holds every time: the value is `x` to the n, and the rate is `n` times `x` to the `n-1`. Not asserted, checked.


*Demonstration 3: checking the pattern up to the sixth power, x=isolate(2)*

```
power n    value (2^n)    rate output    n * 2^(n-1)
  2            4              4               4
  3            8             12              12
  4           16             32              32
  5           32             80              80
  6           64            192             192

Every row checked by actually running the mix rule n-1 times, not
by trusting the formula. The pattern holds at every power tried,
here and at other starting values.
```


> **Why does the exponent show up as a multiplier?** Each additional mix with x adds one more "copy" of x contributing a strip, and the bookkeeping from Unit 3 stacks: going from x^(n-1) to x^n multiplies the rate output by x and adds one more full copy of the value, which is exactly what turns "n-1 copies" into "n copies" one mix at a time. Unit 17 names what this pattern is called in a full course; this book builds it before naming it.


**Try It Yourself:** x=isolate(3). What does x*x*x output? *Hint: Step 1 fully, before Step 2.* Answer: Step 1: mix(x,x) outputs (9,6). Step 2: value=9*3=27, rate=(6*3)+(9*1)=27. Outputs (27,27). Check: 3*3*3=27.


### Practice: Unit 4


1. x = isolate(5). What does x*x*x output?

2. x = isolate(6). What does x*x*x output?

3. Predict the rate for x=isolate(10) using 3*x*x, then check by doing both steps.

4. Using the pattern from Demonstration 3, predict rate(x^5,x) for x=isolate(3) without running all four mixes. Then check by running them.

---


*Unit 5*

## Why The Starting Rate Doesn't Matter


> **Big Question:** Unit 1's shortcut, isolate(5), used seed rate 1. Would a different seed, even a negative one, change what later steps output?

Test it instead of assuming it.


*Demonstration 1: x = isolate(5, seed), four seeds*

```
seed 1:  x=(5,1)   x*x outputs (25,10)   rate outputs 10
seed 2:  x=(5,2)   x*x outputs (25,20)   rate outputs 10
seed 3:  x=(5,3)   x*x outputs (25,30)   rate outputs 10
seed 10: x=(5,10)  x*x outputs (25,100)  rate outputs 10

The rate slot inside x*x changes every time. rate(x*x,x)'s output
does not move. It's 10, every time.
```


> **Why doesn't the seed matter?** rate divides x*x's rate slot by x's rate slot. Whatever seed you pick lands in both the top and bottom of that division, in matching amounts, and cancels. Doubling the seed doubles both numbers being divided, and a fraction doesn't change when you double its top and bottom together.


*Demonstration 2: a negative seed*

```
x = isolate(5, -3)   outputs  (5, -3)

x*x:
  new value = 5*5 = 25
  new rate  = (-3*5)+(5*-3) = -15-15 = -30

mix(x,x) outputs (25, -30)

rate(x*x, x) outputs  -30 / -3  =  10

Same output, 10, even though every number along the way turned
negative. The two negatives cancel in the division exactly the
way two positive copies of the same seed did above.
```


> **Does this mean a negative seed is just a "positive seed pointed backward"?** Only half of the time. Flipping the seed on one reading is a labeling choice: both ends of rate(x*x, x) flip together, and the answer stays put, as the -30 / -3 above shows. That is not the only minus. Two departures can point opposite ways, 5 against -3. rate of those two is -5/3. Flip both labels and it is still -5/3. The minus there is the relation, not the label. A bank balance does not carry this: owing and forgiving still move a pile from one side to the other. Two cars driving apart, one paying rope out and one with the rope tied to the bumper, do. The rope gets longer. Nothing left the first car and arrived in the second.


**Try It Yourself:** x=isolate(4,5). What does x*x output, and rate(x*x,x)? *Hint: new value=4*4. new rate=(5*4)+(4*5).* Answer: x*x outputs (16,40). rate outputs 40/5=8, same as Unit 3 Demonstration 1's seed-1 output.


### Practice: Unit 5


1. x=isolate(3,2). What does rate(x*x,x) output? Compare to Unit 3 Demonstration 2 (seed 1).

2. x=isolate(7,4). What does rate(x*x,x) output? Compare to Unit 3 Practice Problem 1.

3. x=isolate(6,-1). What does x*x output, and rate(x*x,x)? Compare to the seed-1 output for x=isolate(6) from Unit 3's Try It Yourself.

4. Explain why the seed cancels out, using the word "divide."

---


*Unit 6*

## Chains, And When A Comparison Has Nothing To Land On


> **Big Question:** What if a quantity depends on another quantity, instead of being isolated directly?


### Multiplying By A Plain Number

First, one small piece. A plain number, like 2, is what isolate outputs with rate 0, the same as Unit 1's puddle. So multiplying by a plain number is mix, using Unit 3's rule, against an output with rate 0.


*Demonstration 1: t = isolate(2), mixed with the plain number 2*

```
t = isolate(2)  outputs  (2, 1)
2 as an output of isolate with rate 0: (2, 0)

mix(t, 2): new value=2*2=4, new rate=(1*2)+(2*0)=2
outputs (4, 2)
```

Both slots of t just get multiplied by 2, because the second strip always vanishes: the plain number's own rate is 0.


### The Chain

A machine with two rooms. Room 1 takes t and outputs u = mix(t,2). Room 2 takes u and outputs y = mix(u,u). y doesn't depend on t directly, only through u.


*Demonstration 2: t = isolate(2), through both rooms*

```
t = isolate(2)          outputs (2, 1)
u = mix(t, 2)            outputs (4, 2)
y = mix(u, u)            new value=4*4=16, new rate=(2*4)+(4*2)=16
                         outputs (16, 16)

rate(y, t) outputs 16/1 = 16

Room by room instead:
rate(y, u) outputs 16/2 = 8
rate(u, t) outputs 2/1 = 2
rate(y,u) * rate(u,t) outputs 8*2 = 16

Both paths output the same number.
```


> **Why do both paths agree?** rate(y,u) is a fraction with u's rate slot on the bottom. rate(u,t) is a fraction with u's rate slot on top. Multiplying them, u's rate cancels, the same way (8/2)*(2/1) simplifies before you multiply. Room 2 never has to know t exists; u carries everything Room 2 needs.


### When A Comparison Has Nothing To Land On

Unit 1 showed isolate can output rate 0, like an unlit candle. What happens if you try rate against one of those?


*Demonstration 3: comparing against something that isn't moving*

```
bathtub = isolate(8, 2)     outputs (8, 2)
candle  = isolate(15, 0)    outputs (15, 0)

rate(bathtub, candle)  =  2 / 0  =  theta

The machine refuses on purpose and names the refusal: theta,
isolator r=0. Not a big number, not zero, not a bare arithmetic
error inherited from the host. A refusal this book states and
means.
```


> **Why doesn't this have an output?** "How many times faster is the bathtub filling than the candle is growing" only makes sense if the candle is changing at all. It isn't. There's no rate to compare against, and no rule can manufacture one.


> **Zero apples, ten apples** If you have 0 apples and a friend has 10, your friend does not have "10 times as many" apples as you. Ten times zero is zero, not ten, and "how many times more" is a question that only makes sense when there's a nonzero amount to be a multiple of. Asking for a ratio to nothing isn't a hard question with a very large or very small answer. It's not the right shape of question to ask. rate(bathtub, candle) is the exact same situation: the candle's rate is the "0 apples," and asking how many times faster the bathtub is filling, compared to that, has nothing to be a multiple of. theta is the honest name for that, not a stand-in for "a huge number" or "basically zero."


**Try It Yourself:** Same two-room machine, t=isolate(5). What does y output, rate(y,t) directly, and rate(y,u)*rate(u,t)? *Hint: Room 1 first, u=mix(t,2)=(10,2).* Answer: u outputs (10,2). y outputs (100,40). rate(y,t) outputs 40. rate(y,u)*rate(u,t)=20*2=40.


### Practice: Unit 6

For each, use u=mix(t,2), y=mix(u,u). Find what y, rate(y,t), and rate(y,u)*rate(u,t) output, and confirm they agree.


1. t = isolate(1)

2. t = isolate(3)

3. t = isolate(4)

4. J=isolate(40,5), K=isolate(20,0). What does rate(J,K) output, and why?

5. Explain why Room 2 doesn't need to know t exists.

6. A classmate says "rate(J,K) from problem 4 must be some huge number, since K's rate is basically nothing." Using the zero-apples idea, explain what's wrong with "huge number" as the answer.

---


*Unit 7*

## Running The Machine On A Bigger Expression


> **Big Question:** Units 1 through 6 combined two outputs at a time. What happens when you chain several mixes and adds together in one expression?

Nothing new. Every step is still Unit 3's mix rule or piece-by-piece addition, applied as many times as the expression has operations.


*Demonstration 1: f(x) = x*x + 3*x, at x = isolate(2)*

```
x*x    =  mix((2,1),(2,1))          outputs  (4, 4)
3*x    =  (2,1)+(2,1)+(2,1)         outputs  (6, 3)
sum    =  (4,4) + (6,3)             outputs  (10, 7)

Check by hand: x*x+3x at x=2 is 4+6=10. The rate rule, applied
twice and added once, output 7 with no extra machinery.
```


*Demonstration 2: f(x) = x*x*x + 2*x + 1, at x = isolate(2)*

```
x*x        outputs (4, 4)
x*x*x      =  mix((4,4),(2,1))     outputs  (8, 12)
2*x        outputs  (4, 2)
sum so far =  (8,12)+(4,2)         outputs  (12, 14)
+ 1        =  (12,14)+(1,0)        outputs  (13, 14)

Nothing in this calculation was written to find a rate
specifically. It was written to find a value, one mix and one
add at a time. Carrying the pair through every step made the
rate output come out exact alongside it.
```


> **Why does chaining several operations still output the exact rate?** Because mix and add were fixed in Units 3 and 6 to work on any two pairs, not only direct outputs of isolate. mix(x,x) is itself a pair, so mixing it with x again is the same rule, with no new case to write.


**Try It Yourself:** Run f(x)=x*x-x at x=isolate(3), one step at a time. *Hint: x*x first, then subtract x.* Answer: x*x outputs (9,6). Subtract x=(3,1): outputs (6,5).


### Practice: Unit 7


1. Run f(x)=x*x+x at x=isolate(4), step by step.

2. Run f(x)=x*x*x at x=isolate(1), step by step.

3. Run f(x)=x*x-x at x=isolate(5). Check the value against plain arithmetic: 5*5-5.

4. Explain why mix doesn't need a separate case for "the second multiplication in a chain" versus "the first."

5. Run f(x)=x*x*x-x at x=isolate(3).

---


*Unit 8*

## A Rate That Has Its Own Rate


> **Big Question:** Unit 3's rate slot tells you how fast a value is changing. Can that rate slot itself be changing, and if so, does the machine need a new rule to track it?

Picture a car. Its position has a rate: speed. Its speed, in turn, can have a rate too: speeding up or slowing down. Nothing about the machine built so far stops a pair's rate slot from changing. What stops it is that the machine, so far, only ever wrote a plain number into the rate slot. Add a third number, and ask whether the existing rules already know what to do with it.


### Extending A Pair To A Triple

Write a triple `(value, rate, curve)`, where `curve` means "the rate of the rate," how fast the rate slot itself is changing. Seed `x` the same way as always, except now the seed states all three: `x = (v, 1, 0)`, read as "x's own rate is 1, and that rate isn't itself changing, its curve is 0."


> **Why does x get curve 0?** x is being compared to itself. Its rate relative to itself is always 1 (Unit 2), a constant, and a constant number has no rate of its own, so the rate of that rate is 0. The same reasoning that gave isolate's rate shortcut (Unit 1) gives this one.


### Finding The Rule, Not Guessing It

The value and rate slots of a triple still follow Unit 3's mix rule exactly: `new value = v1*v2`, `new rate = r1*v2 + v1*r2`. The question is what the curve slot has to be. Answer it by asking for the rate of the rate, applying Unit 3's rule a second time, to each of the two strips separately.


*Demonstration 1: deriving the curve rule, strip by strip*

```
new rate  =  r1*v2  +  v1*r2         (Unit 3's two strips)

Find the rate of EACH strip, using the mix rule on each one:

rate of (r1*v2)  =  (rate of r1)*v2 + r1*(rate of v2)
                  =  c1*v2  +  r1*r2          [c1 is r1's own curve]

rate of (v1*r2)  =  (rate of v1)*r2 + v1*(rate of r2)
                  =  r1*r2  +  v1*c2          [c2 is r2's own curve]

Add the two results together, since the new rate was their sum:

new curve  =  c1*v2  +  r1*r2  +  r1*r2  +  v1*c2
           =  c1*v2  +  2*r1*r2  +  v1*c2

No new rule was written. This is Unit 3's rule, used twice.
```


*The extended mix rule*

```
mix( (v1,r1,c1), (v2,r2,c2) )  outputs:

  value  =  v1*v2
  rate   =  r1*v2 + v1*r2
  curve  =  c1*v2 + 2*r1*r2 + v1*c2
```


*Demonstration 2: x = isolate(3,1,0), x*x*x*

```
x = (3, 1, 0)

Step 1: mix(x,x)
  value = 3*3 = 9
  rate  = (1*3)+(3*1) = 6
  curve = (0*3)+2*(1*1)+(3*0) = 2
  outputs (9, 6, 2)

Step 2: mix((9,6,2), (3,1,0))
  value = 9*3 = 27
  rate  = (6*3)+(9*1) = 27
  curve = (2*3)+2*(6*1)+(9*0) = 6+12 = 18
  outputs (27, 27, 18)

x*x*x at x=3 outputs value 27, rate 27, curve 18.
```


> **Does this match anything you'd recognize from a calculus course?** Value 27 is 3 cubed. Rate 27 is 3 times 3 squared, the same power-rule output Unit 4 already found. Curve 18 is 6 times 3, which a course would call the second derivative of x cubed. This book built it without ever writing "second derivative," by asking the same question (does this have a rate?) one layer deeper and reusing Unit 3's rule to answer it.


**Try It Yourself:** x = isolate(2,1,0). Run x*x*x and report all three slots. *Hint: Step 1 (x*x), fully, before Step 2.* Answer: Step 1: (4, 4, 2). Step 2: value=8, rate=(4*2)+(4*1)=12, curve=(2*2)+2*(4*1)+(4*0)=4+8=12. Outputs (8, 12, 12).


### Practice: Unit 8


1. x=isolate(4,1,0). Run x*x and report all three slots.

2. x=isolate(5,1,0). Run x*x*x and report all three slots.

3. Using Demonstration 2's result at x=3 (curve 18) and your answer to Problem 2 at x=5, predict the pattern connecting curve to 6*x. Check it against both.

4. Explain, in your own words, why the curve rule needed a factor of 2 on the middle term, r1*r2, but the rate rule didn't need one on its two strips.

---


*Unit 9*

## When Two Moving Things Meet


> **Big Question:** Given two moving things, each one an output of isolate, can you find out if and when they meet, using nothing but subtraction and division?

Car A starts at position 0, moving at rate 5. Car B starts at position 10, moving at rate -3, toward A. Subtract one reading from the other, piece by piece, exactly the way Unit 6 already subtracts.


*Demonstration 1: the gap between two cars*

```
A = isolate(0, 5)     outputs (0, 5)
B = isolate(10, -3)   outputs (10, -3)

gap = B - A = (10-0, -3-5) = (10, -8)

The gap's value, 10, is how far apart they start. The gap's rate,
-8, says the gap is closing under this naming: B minus A, with B
coming toward A. Flip the naming to A minus B and the rate slot
flips sign. The meeting does not.

This is not the rope. The rope is two cars driving apart, one
paying rope out, one with the rope tied to the bumper. The rope
gets longer. Nothing left the first car and arrived in the second.
The gap here is a distance being used up. The rope is a relation
getting longer. Unit 5 keeps those apart.
```

The gap is itself just another pair, an output of subtraction, nothing new. Ask a new question of it: divide its rate by its own value, instead of comparing it to something else.


*Demonstration 2: when do they meet?*

```
gap = (10, -8)

grow(gap) = gap's rate / gap's value = -8 / 10 = -4/5

This says: for every 1 unit the gap's value currently has left, it's
shrinking at 4/5 of a unit per tick. Time to zero is the reciprocal
of that, with the sign kept: 1 / (4/5) = 5/4 ticks. It is not
10 / (4/5). That would be 12.5, and 12.5 is not the meeting.

Check directly: gap's value + t * gap's rate = 0
                10 + t*(-8) = 0
                t = 10/8 = 5/4

They meet at t = 5/4. Same number both ways.
```


> **Why divide the gap's rate by its own value, instead of comparing it to A or B?** Comparing the gap to A or B would answer "how fast is the gap closing compared to how fast A is moving," a question about two different things. Dividing the gap's rate by its own value answers "how fast is the gap closing compared to how much gap is left," which is exactly the question "when does the gap run out." Both are legitimate rate questions; they just aren't the same question.


**Try It Yourself:** A is isolate(0,2), B is isolate(20,-2). Find the gap and when they meet. *Hint: gap = B - A, then solve gap.value + t*gap.rate = 0.* Answer: gap = (20,-4). t = 20/4 = 5. They meet at t=5.


### Two Dimensions: Closest Approach

On a flat plane, track two coordinates for each mover. The same subtraction gives a gap in each direction, and the same kind of question, now asking when the *total* squared distance is smallest, tells you not just whether two things meet, but how close they come if they don't.


*Demonstration 3: a genuine meeting*

```
A starts at (0,0), moving (1,0). B starts at (10,0), moving (-1,0).

gap in x: (10, -2)     gap in y: (0, 0)

Time of closest approach (found by the same "rate over value" idea,
applied to the combined squared distance): t = 5

Position of the gap at t=5: (10 + 5*(-2), 0) = (0, 0)

Squared distance at closest approach: 0*0 + 0*0 = 0. They meet.
```


*Demonstration 4: a near miss*

```
A starts at (0,0), moving (1,0). B starts at (5,5), moving (-1,0).

gap in x: (5, -2)     gap in y: (5, 0)

Time of closest approach: t = 5/2

Position of the gap at t=5/2: (5 + 5/2*(-2), 5) = (0, 5)

Squared distance at closest approach: 0*0 + 5*5 = 25

They never meet. The closest they get is a distance whose square
is exactly 25, known in advance, with no measurement and no
trial and error.
```


*[Diagram: A moving right, B moving left on a higher line. The dashed segment is the closest the two paths ever come. (see the PDF for the image)]*


> **Why is knowing the squared distance enough, without taking a square root?** "Do they come within 5 units of each other" is answered exactly by comparing 25 to 5*5, both whole numbers, no irrational step required. The square root of 25 happens to be a whole number here, but Unit 11 shows that's the exception, not the rule. Staying with the squared distance keeps the whole question inside fractions, exactly, for free.


**Try It Yourself:** A starts at (0,0) moving (1,1). B starts at (10,5) moving (-1,-1). Do they meet? Find the gap in each direction first. *Hint: gap in x = (10,-2), gap in y = (5,-2). Find t where the total squared gap is smallest, the same way Demonstration 3 and 4 did.* Answer: time of closest approach works out to t=15/4 using the same method; the squared distance at that time is not 0 (check: gap-x and gap-y don't hit 0 at the same t), so they don't meet, but you can find exactly how close they get the same way Demonstration 4 did.


### Practice: Unit 9


1. A is isolate(0,3), B is isolate(30,-7). Find the gap and when they meet.

2. A is isolate(5,1), B is isolate(5,-1). What does the gap look like right away? What does that tell you about t=0?

3. A starts at (0,0) moving (2,0). B starts at (8,6) moving (-2,0). Find the gap in each direction, the time of closest approach, and the squared distance at that time.

4. Explain, in your own words, why "closest approach" is still a well-defined, computable question even when two things never actually meet.

---


*Unit 10*

## How Far The Machine Reaches


> **Big Question:** Which functions can the machine handle exactly, and where does it stop?

Addition and multiplication of Readings are settled: stipulated directly, as in Unit 3. That leaves division, and this time the rule does not need to be picked. It can be derived: division undoes multiplication, so whatever the quotient is, multiplying it by the divisor has to rebuild the dividend.


*Demonstration 1: what the quotient has to be*

```
Call the quotient (q, s). It has to satisfy:

  (v2, r2) * (q, s)  =  (v1, r1)

Apply the mix rule to the left side:

  (v2*q,  r2*q + v2*s)  =  (v1, r1)

Match the first slots:   v2*q = v1            so  q = v1 / v2
Match the second slots:  r2*q + v2*s = r1     so  s = (r1 - r2*q) / v2
                                                  = (r1*v2 - r2*v1) / v2²

This needs v2 to be something other than 0, for the same reason
ordinary division does.
```


> **Why is this rule derived, when the mix rule was stipulated?** Only the mix rule was picked, back in Unit 3. Everything here follows from requiring that division undo it. Once multiplication is fixed, "the quotient times the divisor gives back the dividend" leaves no freedom: the two slots of the quotient are forced by that one requirement, solved directly from the mix rule already in hand.


*Demonstration 2: 1/x at x = (3,1)*

```
Dividend (1,0), divisor (3,1).

q = 1/3
s = (0*3 - 1*1) / 3² = -1/9

Result: (1/3, -1/9).

Check by multiplying back: (3,1) * (1/3,-1/9)
  = (3*1/3,  1*1/3 + 3*(-1/9))  =  (1,  1/3 - 1/3)  =  (1, 0)
```


*Demonstration 3: (x*x + 1) / (x - 1) at x = (3,1)*

```
numerator:    x*x + 1  =  (9,6) + (1,0)  =  (10, 6)
denominator:  x - 1    =  (3,1) - (1,0)  =  (2, 1)

q = 10/2 = 5
s = (6*2 - 10*1) / 2² = 2/4 = 1/2

Result: (5, 1/2).
```

Combine `+`, `-`, `*`, `/` as many times as you like, starting from `x` and constants, and the machine reports an exact value and an exact rate, at every point where the divisor's value isn't 0.


*Demonstration 4: the edge, where the divisor's value is 0*

```
1/x at x = (0,1) means (1,0) divided by (0,1). q = 1/0. No answer.
The machine refuses: theta. Nothing can be adjusted to fix this,
because ordinary division by 0 has no answer either.
```

Outside that reach sit three kinds of question, each different, and the next three units take them one at a time. What number squares to 2 (Unit 11). What function's rate always equals its own value (Unit 12). What function's rate always equals a partner function's value, and vice versa (Unit 13). None of the three needs anything you don't already have.


**Try It Yourself:** Divide (6,4) by (2,0). *Hint: q = v1/v2, then s = (r1*v2 - r2*v1)/v2², with r2 = 0.* Answer: (3, 2). Check: (2,0)*(3,2) = (6, 0*3+2*2) = (6,4).


### Practice: Unit 10


1. Divide (10,5) by (5,0).

2. Find the Reading for `1/x` at `x=(2,1)`.

3. Find the Reading for `x/(x+1)` at `x=(1,1)`.

4. Find the Reading for `1/(x*x)` at `x=(2,1)`.

5. What does the machine do with `1/x` at `x=(0,1)`, and why?

6. For each, say whether the machine reaches it at x=(3,1): (a) x*x*x+2; (b) 1/(x-3); (c) (x+1)/(x-2).

---


*Unit 11*

## A Number That Isn't A Fraction


> **Big Question:** What do you do when the answer to a question is a number that is not a fraction?

A square with sides of length 1 has a diagonal `d` with `d * d = 2` (Geometry book, Unit 5). Is there a fraction whose square is 2?


*Demonstration 1: no fraction squares to 2*

```
Suppose a/b is a fraction in lowest terms with (a/b)² = 2.

1. Then a² = 2*b², so a² is even, so a is even (odd*odd is
   odd). Write a = 2c.
2. Then 4c² = 2*b², so b² = 2*c², so b is even too.

Now a and b are both even, so a/b was not in lowest terms.
Contradiction. No such fraction exists.
```

That proof is finite and it settles the question: no fraction, none at all, squares to exactly 2. It does not say the question has no answer. It says the answer isn't a fraction. Here are two rules that answer it, staying in fractions at every single step.


*Demonstration 2: closing in by halving*

```
Start knowing 1*1=1 is too small and 2*2=4 is too big. Check the
midpoint; if its square is too small, it becomes the new low end;
if too big, it becomes the new high end. Either way the gap halves.
Every number here is an exact fraction, nothing rounded.

step  low     high    gap    midpoint checked
0     1       2       1
1     1       3/2     1/2    3/2 squared = 9/4, too big, new high
2     5/4     3/2     1/4    5/4 squared = 25/16, too small, new low
3     11/8    3/2     1/8    11/8 squared = 121/64, too small, new low
4     11/8    23/16   1/16   23/16 squared = 529/256, too big, new high

Ask for any gap you want, however small, and this rule tells you
exactly how many steps close it, then runs that many steps.
Halving ten times takes the gap under 1/1000.
```


*Demonstration 3: a faster rule, closing in by averaging*

```
Start at x=1. Each step, replace x with the average of x and 2/x.
Still exact fractions, nothing rounded, at every step.

x0 = 1
x1 = (1 + 2/1) / 2             = 3/2
x2 = (3/2 + 2/(3/2)) / 2       = (3/2 + 4/3) / 2     = 17/12
x3 = (17/12 + 2/(17/12)) / 2   = (17/12 + 24/17) / 2 = 577/408
x4 = (577/408 + 2/(577/408)) / 2                     = 665857/470832

Square the last one directly: (665857/470832)^2 = 443365544449/221682772224
2, written over that same bottom, is 443365544448/221682772224

The two numerators differ by exactly 1. The gap between x4 squared
and 2 is 1/221682772224, a named fraction, after only four
steps. Halving needs about forty steps to close a gap that small.
```


> **Why does averaging close the gap so much faster?** Halving always cuts the gap in half, no matter how close you already are. Averaging's gap shrinks roughly by squaring each time: Demonstration 3's gaps were about 1/4, then 1/144, then 1/166464, each one roughly the square of the one before. Both rules stay in exact fractions and both come with a provable bound. They're different rules, is all, and this book keeps both because seeing two different rules reach the same kind of answer is part of the point: nothing about the square root of 2 is tied to one particular construction.

Either rule *is* the square root of 2, in every sense that matters for computing with it. Name a precision, a rule hands you a fraction within it, and a proof that says how good it is. Nothing about either rule ever finishes, and nothing about it needs to. You call it as many times as your problem needs and stop.


> **Isn't a rule less real than a number?** No more than `1/3` is less real than "1 divided by 3, in progress." `1/3` was already a rule: given how many digits you want, it produces them, forever, on demand, one at a time. The square root of 2 works the same way. It never gets a special status where it "finishes existing." It gets a rule, checked, and that's the whole of what it is here.


> **A choice, not a discovery** Nothing forces you to give this rule a name and a symbol, `√2`. Doing so is a choice, made because the rule comes up often enough to be worth a short label. The label doesn't add anything the rule didn't already have.


**Try It Yourself:** Run the halving rule one more step from step 4 above (low 11/8, high 23/16). Which end moves? *Hint: check the midpoint, 45/32, squared.* Answer: midpoint = (11/8+23/16)/2 = 45/32. Squared: 2025/1024. Compare to 2 = 2048/1024: 2025 is less, so 45/32 is too small, and it becomes the new low end. New range: low 45/32, high 23/16, gap 1/32.


### Practice: Unit 11


1. Show that the square of any odd number `2k+1` is odd.

2. In Demonstration 1, where does "in lowest terms" get used?

3. Continue the halving rule two more steps past your answer to Try It Yourself, keeping every number an exact fraction.

4. Roughly how many halving steps would it take to get the gap under 1/100,000? (You don't need the exact count, just show the gap roughly halves each step and estimate.)

5. Run Demonstration 3's averaging rule one more step, from x4=665857/470832. You don't need to simplify the result, just set up the fraction: `(x4 + 2/x4) / 2`.

6. Explain, in your own words, why calling either rule "√2" doesn't change what it is.

---


*Unit 12*

## A Number Defined By How It Changes


> **Big Question:** How would you build a function whose rate always equals its own value?

Money in an account that grows continuously grows faster the more there is. The cleanest version of that pattern: a quantity `E` that starts at 1 and whose rate always equals its own value.


> **A choice, not a discovery** `E(0) = 1` and `rate(E) = E` are a definition. No rectangle picture produces this function; it is picked because the pattern (grows faster the bigger it gets) is useful.


### Building It By Fixing Shortfalls

The machine can't hold `E` directly, so build polynomials that follow the law as closely as you like, and name exactly what's missing at each stage.

- Start with `P0 = 1`. Rate 0. The law wants 1. Shortfall: 1.
- Add a piece with rate 1: `x`. Now `P1 = 1 + x` has rate 1, but the law wants `1+x`. Shortfall: `x`.
- Add a piece with rate `x`: since `x*x` has rate `2x`, half of it does the job. `P2 = 1 + x + x*x/2`. Shortfall: `x*x/2`.


*Demonstration 1: P(n) at x = 1, and the exact shortfall*

```
n    value P(n)     rate of P(n)    shortfall (value minus rate)
0    1              0               1
1    2              1               1
2    5/2            2               1/2
3    8/3            5/2             1/6
4    65/24          8/3             1/24
5    163/60         65/24           1/120
6    1957/720       163/60          1/720

Each rate equals the previous value. The shortfall is exactly
1/n! every time, provably: the next piece added is x^n/n!, and
that's exactly the shortfall this row is carrying.
```


> **Why can no single polynomial satisfy the law exactly?** The rate of a polynomial of degree n has degree n-1, one lower. A polynomial and its own rate can never be equal unless both are 0, and `E(0)=1` rules that out. So no single, finite polynomial is `E`. `E` is the rule: for any n you name, run this construction n steps, and the shortfall left behind is exactly `1/n!`, a fact proven above, not estimated.


### Precision On Demand


*Demonstration 2: naming a precision, getting a proof*

```
Ask: give me E(1) within 1/1000.

For n=6, the next term is 1/7!. Every term after that is at most
1/8 of the one before it (the denominator grows by at least 8 each
step), so the whole remaining tail is at most a shrinking-by-8
series:

  1/7! * (1 + 1/8 + 1/8^2 + ...) = 1/7! * (8/7) = 8/35280 = 1/4410

That's a closed-form fraction, not an estimate. Compare it to
1/1000 directly: 1/4410 < 1/1000 exactly when 1000 < 4410, true.

So P(6), value 1957/720, answers the request: E(1) is within
1/1000 of 1957/720, proven by a finite calculation entirely in
fractions, no further steps needed.
```

Nothing above required infinitely many steps to run. Every check was a finite sum, or a finite comparison. The rule `E` is fully specified by "compute P(n) for any n I ask, and the shortfall is exactly 1/n!." That sentence is the whole content of what `E` is. `E(1)`, the number people write as `e`, is the name for that rule at `x=1`, nothing more added.


**Try It Yourself:** Find the value, rate, and shortfall of `P3 = 1 + x + x*x/2 + x*x*x/6` at `x = 2`. *Hint: the four pieces at x=2 are 1, 2, 2, 4/3. The rate is P2 at 2.* Answer: value = 1+2+2+4/3 = 19/3. Rate = 1+2+2 = 5. Shortfall = 19/3 - 5 = 4/3, which is 2³/3!.


### Practice: Unit 12


1. Find the value, rate, and shortfall of `P4` at `x = 1/2`.

2. Check at `x = 2` that the rate of `P2` equals the value of `P1`.

3. Explain in your own words why the degree of a polynomial's rate stops it from ever satisfying `rate(E)=E`.

4. What is the shortfall of `P7` at `x = 1`?

5. What does the law say the rate of `E` is at `x = 0`?

---


*Unit 13*

## Two Rates That Feed Each Other


> **Big Question:** What if the rate of one quantity is the value of another, and vice versa?


> **A choice, not a discovery** `S(0)=0`, `C(0)=1`, `rate(S)=C`, `rate(C)=-S`. Four lines, picked as a definition. Whether the functions they define match the sine and cosine measured from triangles is a separate claim, checked against measurement, not proven here.


### Building Them By Matching Rates

Same method as Unit 12. The rate of `x` is 1. The rate of `x*x*x/6` is `x*x/2`. Build two series, term by term, so each one's rate lands on the other's value at the previous stage.


*Demonstration 1: truncated S and C at x = 1*

```
S3 = x - x^3/6                    at 1:  value 5/6,      rate 1/2
C2 = 1 - x^2/2                    at 1:  value 1/2,      rate -1
rate of S3 = 1/2, which is the value of C2.

S5 = x - x^3/6 + x^5/120          at 1:  value 101/120,  rate 13/24
C4 = 1 - x^2/2 + x^4/24           at 1:  value 13/24,    rate -5/6
rate of S5 = 13/24, the value of C4.
rate of C4 = -5/6, which is minus the value of S3.
```

Each one is a finite polynomial. Ask for more accuracy, add more terms; the next term is a specific, computable fraction, exactly like Unit 12's shortfall. Nothing here waits on an infinite process to finish. `S` and `C` are the rule "build the next term this way," the same way `E` was a rule in Unit 12.


### What The Rate Laws Alone Can Show

At any point, if `S` has value `s` and `C` has value `c`, then `S` reads `(s, c)` and `C` reads `(c, -s)`, straight from the definition.


*Demonstration 2: the rate of S*S + C*C*

```
Suppose S reads (3/5, 4/5) and C reads (4/5, -3/5).

S*S = (9/25,   24/25)
C*C = (16/25, -24/25)
S*S + C*C = (1, 0)

Do it with letters instead of numbers: S reads (s,c), C reads
(c,-s).
S*S = (s^2,  2sc)
C*C = (c^2, -2sc)
S*S + C*C = (s^2+c^2, 0)

The rate is exactly 0, for every s and c, not just this pair. Pure
algebra: two terms that are exact negatives of each other, added.
```


> **Does rate 0 mean S*S + C*C stays 1 forever?** That would need a separate argument connecting "rate 0 at a point" to "same value at another point," and this book doesn't build that argument, because it isn't needed for anything else here. What Demonstration 2 shows is smaller and fully finite: at whatever point you check, `S*S+C*C` has rate exactly 0. That's a fact about the rate, proven by algebra, not a claim about every point at once. Unit 14 builds a second, completely different construction where a version of this identity holds exactly, everywhere, for a different reason.


**Try It Yourself:** Find S3 and C2 at `x = 2`. Does the rate of S3 equal the value of C2? Answer: S3 at 2 is 2 - 8/6 = 2/3, rate -1. C2 at 2 is 1 - 2 = -1. Yes, both -1.


### Practice: Unit 13


1. Check that C2's rate at x=1 equals minus the value of S1=x at x=1.

2. Let S read (3/5,4/5) and C read (4/5,-3/5). Find the Reading for S*C.

3. Let S read (5/13,12/13) and C read (12/13,-5/13). Find the Reading for S*S+C*C.

4. Redo Demonstration 2 with letters s, c, but for S*C instead of S*S+C*C. What's its rate, in terms of s and c?

5. Why is "S3 approximates the true sine function" a different kind of sentence than "S3's rate at 1 is exactly 1/2"?

---


*Unit 14*

## A Second Way To Turn, Exactly


> **Big Question:** Unit 13 built two rates that feed each other and showed S*S+C*C has rate 0, without ever proving the value itself stays exactly 1. Is there a construction where it does, provably, with no series at all?

Yes, and it's built from nothing but a pair of whole numbers. This is not Unit 13's S and C under a different name. It's a different construction entirely, picked for a different reason, and this unit is careful to keep the two apart.


### A Pair Of Whole Numbers, Turned Into A Pair That Squares To 1

Take two whole numbers, written `(P : Q)`, called a **heading**. Build two fractions from them:


*The heading rule*

```
heading(P, Q)  outputs  (c, s)  where

  c  =  (Q*Q - P*P) / (P*P + Q*Q)
  s  =  2*P*Q / (P*P + Q*Q)
```


*Demonstration 1: heading(1, 2)*

```
P=1, Q=2.  P*P+Q*Q = 1+4 = 5

c = (4-1)/5 = 3/5
s = 2*1*2/5 = 4/5

heading(1,2) outputs (3/5, 4/5)

Check: c*c + s*s = 9/25 + 16/25 = 25/25 = 1

Exactly 1. Not approximately. The 3-4-5 triangle is sitting
inside this computation: 3, 4, and 5 are exactly the numbers that
came out.
```


*Demonstration 2: two more headings, same check*

```
heading(1,3): c=4/5, s=3/5.  c*c+s*s = 16/25+9/25 = 1
heading(2,3): c=5/13, s=12/13.  c*c+s*s = 25/169+144/169 = 1

Every whole-number pair (P,Q) produces a (c,s) with c*c+s*s
exactly 1, checked here on three pairs, provably true for every
pair by the same algebra each time: expand (Q*Q-P*P)^2 and
(2*P*Q)^2, add them, and the sum is always (P*P+Q*Q)^2 exactly,
which divided by (P*P+Q*Q)^2 is 1.
```


> **Why does this hold exactly, with no series and no limit?** Unit 13's S and C are built by adding up infinitely many shrinking pieces, and only a finite number of them are ever actually added, so S*S+C*C landing on exactly 1 would need infinitely many pieces to finish, which never happens. A heading never adds up pieces at all. It's two fractions built directly from P and Q by one formula, and checking c*c+s*s=1 is a single finite algebra fact, true the same way for every pair, not approached.


### Combining Two Headings

Two headings combine by a rule that mixes P's and Q's the way Unit 3 mixes values and rates:


*Demonstration 3: combining heading(1,2) and heading(1,1)*

```
Combine rule:  P' = P1*Q2 + P2*Q1,   Q' = Q1*Q2 - P1*P2

(1,2) combined with (1,1):
  P' = 1*1 + 1*2 = 3
  Q' = 2*1 - 1*1 = 1

Combined heading: (3, 1). heading(3,1) outputs:
  c = (1-9)/10 = -4/5,  s = 2*3*1/10 = 3/5

Compare to combining the two (c,s) pairs directly:
  heading(1,2) = (3/5, 4/5).  heading(1,1) = (0, 1).
  c1*c2 - s1*s2 = 3/5*0 - 4/5*1 = -4/5
  s1*c2 + c1*s2 = 4/5*0 + 3/5*1 = 3/5

Both routes output the same pair, (-4/5, 3/5).
```


### A Turn Rate, Built The Same Way As Unit 3's Rate

Seed P the way Unit 1 seeds a value, with its own rate attached, and ask how fast the heading turns.


*Demonstration 4: turn rate, and it adds under combining*

```
turn rate of (P,Q), P moving at rate 1, Q fixed:
  turn = 2*(Q*1 - P*0) / (P*P+Q*Q) = 2*Q / (P*P+Q*Q)

heading(1,2): turn = 2*2/5 = 4/5
heading(1,1): turn = 2*1/2 = 1

Combine the two headings (Demonstration 3 gave (3,1)). Under the
same seeding, the combined turn rate works out to 4/5 + 1 = 9/5,
checked directly from the combined (P,Q)=(3,1) and its own rates,
not assumed.
```


> **Is this the same thing as sine and cosine?** No, and saying so plainly matters more here than almost anywhere else in this book. Unit 13's S and C are built from an infinite series and connect, through calculus most books don't build from scratch, to an actual angle measured in degrees or radians. A heading is built from a pair of whole numbers and never mentions an angle at all. Both produce a pair with c*c+s*s=1. Both compose by matching algebra. That's a shared pattern, not a shared identity, and this book has been careful all the way through not to confuse the two. A heading cannot currently answer "what is the cosine of 30 degrees," because connecting P and Q to a specific angle is a question this construction was never built to answer.


> **A choice, not a discovery** The formula for heading(P,Q) is one specific way to turn a whole-number pair into a pair that squares to 1. It was picked because it matches how a 3-4-5 triangle and its relatives are already built from whole numbers, not because it's the only possible choice.


**Try It Yourself:** Find heading(2,1) and check c*c+s*s. *Hint: P=2, Q=1, so P*P+Q*Q=5.* Answer: c=(1-4)/5=-3/5, s=2*2*1/5=4/5. Check: 9/25+16/25=1.


### Practice: Unit 14


1. Find heading(3,4) and check c*c+s*s.

2. Find heading(1,4) and check c*c+s*s.

3. Combine heading(1,2) with heading(2,1) using the P',Q' rule. Find the resulting (c,s) both ways, directly from the combined (P,Q) and by combining the two (c,s) pairs with the c1c2-s1s2 formula, and check they match.

4. Find the turn rate of heading(1,4) with P moving at rate 1.

5. Explain, in your own words, why "both satisfy c*c+s*s=1" is not a strong enough reason to call a heading and Unit 13's (S,C) the same construction.

---


*Unit 15*

## Precision On Demand


> **Big Question:** Units 11 to 13 kept saying "ask for a precision, the rule hands you a fraction within it." What exactly is that move, in general?

Here it is, stripped down. A **rule**, in this sense, is a finite procedure: you give it a positive fraction (how close you need to be), it gives back a whole number (how many steps to run), and running that many steps produces a fraction, with a proof that the fraction is that close. Every step of every part of that is finite. You never run the procedure forever. You run it once, for the precision you actually asked for, and it stops.


*Demonstration 1: the rule for 1/n, made explicit*

```
Request: get 1/n within 1/500 of 0.

Solve 1/n < 1/500 directly: n > 500. So n = 501 works.
Check directly, no decimal needed: 1/501 < 1/500 exactly when
500 < 501, true.

One division settled it. No infinite process ran.
```


*Demonstration 2: the rule for the sums of halves*

```
1, 3/2, 7/4, 15/8, ...   each term is the last plus the next half.

The gap between the n-th term and 2 is exactly 1/2^n, a fact you
can check by induction: gap(0) = 2-1 = 1 = 1/2^0, and each step
covers exactly half of what's left. Request gap under 1/100:
2^n > 100 first happens at n=7 (2^7=128). Run 7 steps, done.
```


*Demonstration 3: the rule for a hole in a fraction*

```
f(x) = (x*x-1)/(x-1) refuses at x=1 (0/0). But away from 1,
algebra simplifies it: x*x-1 = (x-1)*(x+1), so f(x) = x+1 for
every x other than 1.

Feed the rule x = 1 + 1/n:
f(1+1/n) = (1+1/n) + 1 = 2 + 1/n

Request f within 1/50 of 2: need 1/n < 1/50, so n=51 works.
This is algebra, not a limiting process: f genuinely equals x+1
at every point besides x=1, checked directly.
```


> **Where mathematicians usually say "limit," what's actually there?** A rule, exactly like the three above: give it a tolerance, it gives back a stage, checked by a finite calculation. Historically that whole package got a name, "limit," and got talked about as if something was being approached, a target sitting out there waiting. Nothing needs to sit anywhere. The rule is complete in itself: callable, finite per call, and proven correct per call. That's the entire mathematical content. This book will keep saying "rule, requested precision, proven bound" instead of "approaches," because that phrasing doesn't invite the question "approaches what completed thing?" when there's no completed thing in the account at all.


**Try It Yourself:** For the rule `3/n`, find a stage that gets it within 1/100 of 0. *Hint: solve 3/n < 1/100 directly.* Answer: n > 300, so n=301 works. Check directly, no decimal needed: 3/301 < 1/100 exactly when 3*100 < 301*1, and 300 < 301 is true.


### Practice: Unit 15


1. For `5/n`, find a stage within 1/1000 of 0.

2. For the sums of halves, find the first stage with gap under 1/1000.

3. For `f(x)=(x*x-1)/(x-1)` at `x=1+1/n`, find a stage within 1/20 of 2.

4. Unit 11's halving rule for the square root of 2: after 10 steps the gap is 1/1024. How many more steps, roughly, to get the gap under 1/100,000?

5. Explain, in your own words, why a rule that runs finitely for every request you actually make doesn't need to run forever to be complete.

---


*Unit 16*

## "Algebraic" And "Transcendental" Are Rule Labels


> **Big Question:** The square root of 2 gets called "algebraic." The number e gets called "transcendental." What does that difference actually say?

A number is called **algebraic** if it is a root of some polynomial with whole-number coefficients: something like `x*x - 2` (root: the square root of 2) or `2x + 1` (root: -1/2). A number is called **transcendental** if it is not a root of any such polynomial. Every fraction is algebraic. The square root of 2 is algebraic. It is a theorem that `e` is not the root of any whole-number polynomial. That proof is longer than this book has room for; it is stated here, not derived.


> **What does "algebraic" or "transcendental" actually tell you about a number?** Which rule reaches it, and nothing else. "Algebraic" means: reachable by the rule "find a root of a whole-number polynomial." "Transcendental" means: not reachable by that particular rule. It does not mean harder to compute, less precise, less real, or further away. Unit 11 reached the square root of 2 with a halving rule and an averaging rule. Unit 12 reached e with a shortfall rule. All of these rules are finite per step. All come with a proven precision bound on request. No number here is more "arrived at" than another. The words "algebraic" and "transcendental" sort numbers by which generating rule was used to name the sorting question, the way "even" and "odd" sort whole numbers by which rule (divide by 2 cleanly, or not) answers a specific question. Nobody thinks odd numbers are less real than even ones.


*Demonstration 1: the square root of 2 is a root, directly*

```
The halving rule from Unit 11 never mentions a polynomial. But its
target satisfies x*x = 2, which rearranges to x*x - 2 = 0: exactly
the polynomial x*x-2, evaluated at that x, hits 0. That's what
makes the square root of 2 algebraic: a short polynomial names it.
```


*Demonstration 2: not every number gets named this way*

```
Try the same move on e. Is there a whole-number polynomial
a_n*x^n + ... + a_1*x + a_0 with e as a root? The theorem says
no, for any such polynomial, however long. e still has a rule (Unit
12's shortfall construction). It just isn't the root-of-a-polynomial
rule. That's the entire difference.
```


> **Is this a fact about what numbers ultimately are?** No. "Transcendental" sounds like it's announcing something deep about a number's nature, sitting beyond ordinary numbers in some special realm. It isn't. It's a checkable fact about one specific, narrow question: does a whole-number polynomial hit this number exactly? For e, the answer is no, proven. That's the whole claim. Treating "transcendental" as a kind of thing a number IS, rather than a fact about which rule reaches it, turns a checkable classification into an unchecked story about hidden depths. This book keeps the checkable version only.


**Try It Yourself:** Which polynomial, with whole-number coefficients, has 3/4 as a root? *Hint: start from 4x = 3.* Answer: `4x - 3`. Check: `4*(3/4) - 3 = 0`.


### Practice: Unit 16


1. Find a whole-number polynomial with -2/5 as a root.

2. Find a whole-number polynomial with the square root of 3 as a root.

3. Every fraction p/q is algebraic. Give the general polynomial that proves it.

4. Sine and cosine, built in Unit 13 the same way e was built in Unit 12, are also transcendental (a theorem, not proven here). Does that change anything about how you compute S3 or C2 at a point?

5. Explain, in your own words, the difference between "e is transcendental" and "e is less real than the square root of 2."

---


*Unit 17*

## What This Machine Never Needed


> **Big Question:** Look back across Units 1 to 16. What was actually required to reach every number and every construction in this book?

Fractions, and the three moves from Unit 1 through 3. That's the full list. Here is everything this book built, and what it took.


*Demonstration 1: every construction in this book, and its rule*

```
number/function                             rule                                            per-step arithmetic
------------------------------------------- ----------------------------------------------- ------------------
rate of x*x*x+2x+1                          mix and add on Readings (Unit 7)                fractions, finite
rate of the rate of x^3                     the same mix rule, one layer deeper (Unit 8)    fractions, finite
when two movers meet                        subtract, then divide rate by value (Unit 9)    fractions, finite
1/x, (x+1)/(x-2)                            derived quotient (Unit 10)                      fractions, finite
sqrt(2)                                     halving, or averaging (Unit 11)                 fractions, finite
e = E(1)                                    shortfall construction (Unit 12)                fractions, finite
sin(1), cos(1)                              coupled shortfall construction (Unit 13)        fractions, finite
an exact turn, c*c+s*s=1                    whole-number pair (Unit 14)                     fractions, finite
"a rule gets within any distance you name"  naming a stage for a named tolerance (Unit 15)  fractions, finite

Every row: fractions in, fractions out, a finite number of
arithmetic steps, and (where relevant) a finite proof of how
close the answer is. Nothing on this list required a number that
isn't a fraction to exist ahead of time. Nothing required treating
"all the numbers there could ever be" as a single object to reason
about. Every claim was: run this many steps, get this fraction,
here is the proof it's close enough.
```


> **So what was the limit for, in other treatments of this material?** In most courses, "the real numbers" get declared first, as a completed collection that already contains every possible decimal, and then a limit is defined as a way of picking out one member of that collection using a sequence. That's a choice some mathematicians made, for their own reasons: it lets certain existence theorems get stated cleanly, at the cost of talking about a completed infinite collection before doing any arithmetic with it. This book made a different choice: build the rule first, prove its precision bound, and never declare a completed collection that the rule is reaching into. Every number this book named came with its rule attached, in full, with nothing left over that the rule doesn't already supply.


> **A choice, not a discovery** Declaring a completed set called "the real numbers" is a choice other treatments make. This book doesn't make it, because nothing in this book needed it. That doesn't mean the choice is wrong for other purposes; existence theorems and some parts of later mathematics do lean on it. It means the choice was never a prerequisite for anything built here.


**Try It Yourself:** Which unit in this book used a number that wasn't a fraction, at any single step of any calculation? Answer: none. Every intermediate value in every demonstration in Units 1 through 16 was a fraction. The rules reach past what fractions can exactly represent (sqrt(2), e, sine, cosine) without any step along the way leaving fractions.


### Practice: Unit 17


1. For each, name the unit and the rule that reaches it: (a) the rate of x*x*x at x=5; (b) the square root of 2 within 1/500; (c) e within 1/100; (d) an exact turn with c*c+s*s=1.

2. A friend says "e isn't really a number until you take the limit." Using this unit, write two sentences responding to that.

3. Why does building the rule first, instead of declaring a completed set of numbers first, avoid ever having to say "all the real numbers" as a single object?

---


*Unit 18*

## What This Book Claims, And What It Doesn't


> **Big Question:** What kinds of statements has this book been making, and which kinds can no calculation support?

Statements come in three kinds.

- **Kind 1: checked by calculation or proof.** "At x=3 the rate of x*x is 6." "No fraction squares to 2." "e is transcendental." "heading(1,2) satisfies c*c+s*s=1." Anyone can check these, by running the rule or the argument.
- **Kind 2: claims about the world, through a model.** "A dropped ball falls about 4.9*t*t meters in t seconds, ignoring air." Checked by measurement, and can be wrong.
- **Kind 3: claims about what everything ultimately is.** "Numbers exist whether or not anyone thinks about them." "Transcendental numbers belong to a deeper layer of reality than algebraic ones." "A heading is secretly the real meaning of sine and cosine." No calculation and no measurement can test these.

This book makes claims of kinds 1 and 2 only.


> **Where a kind 3 claim likes to hide inside this material** "Transcendental" is a real, checkable, kind 1 fact about a number: which rule reaches it (Unit 16). The word invites a kind 3 reading anyway, because it sounds like it's describing a deeper category of existence rather than a narrow fact about polynomials. It isn't. Reading it as ontology is exactly the mistake this unit exists to name: a kind 1 fact, dressed in language that suggests a kind 3 claim, smuggled past the reader because the two sentences sound similar. "Not the root of a whole-number polynomial" is checkable. "Belongs to a higher order of number" is not, and this book never says it, whatever "transcendental" sounds like it's implying.


> **Where a kind 3 claim likes to hide inside "the same," too** Unit 14 built headings specifically to avoid a different version of this mistake: two constructions that satisfy the same algebraic identity, c*c+s*s=1, are not thereby the same construction. "They satisfy the same equation" is a kind 1 fact, checkable. "They are the same thing" is a much larger claim that the shared equation alone does not support, and this book never makes it. The same caution applies to "the real numbers" (Unit 17): some treatments present them as a completed totality that existed before anyone started computing. Read as a claim about what fundamentally exists, that is also a kind 3 claim, and this book doesn't make it.


### No Method Is Free Of Assumptions

Every calculation in this book rests on assumptions: that whole-number and fraction arithmetic is consistent, and that checking a finite proof by hand is reliable. No check can show that a method has no assumptions at all, so a book claiming none would be claiming more than it can support. What a book can do is state its assumptions where they appear, which is what the purple boxes were for throughout.


**Try It Yourself:** Which kind is this statement: "e is not the root of any whole-number polynomial"? Answer: kind 1. It is a theorem, a checkable argument, even though this book didn't reproduce it in full.


### Practice: Unit 18

For each statement, say which kind it is, and say what would count as checking it (or say that nothing could).


1. At x=4, the rate of x*x is 8.

2. There is no fraction whose square is 2.

3. A dropped ball falls about 4.9*t*t meters in t seconds, ignoring air.

4. Transcendental numbers are more real than algebraic numbers.

5. e is transcendental.

6. The real numbers exist as a completed totality, prior to any rule that reaches into them.

7. Given a requested precision, the halving rule for the square root of 2 reaches it within that many steps.

8. A heading is what sine and cosine really are, underneath the series.

---


*Closing*

## What You Can Say Now

For every function built from a starting Reading with adding, subtracting, multiplying, and dividing, the machine gives an exact value and an exact rate by finite arithmetic, at every point where no division by a zero value occurs. The mix rule is the whole output, two strips added to a starting area, nothing approximated and nothing set aside. The same rule, applied one layer deeper with no new axiom, gives a rate that has its own rate. The same subtraction already in the book, paired with a single division, tells you exactly when and where two moving things meet, or exactly how close they come if they don't.

When a question's answer isn't a fraction, the answer is a rule: a finite procedure that, given any precision you name, hands back a fraction and a proof of how close it is. The square root of 2, e, sine, and cosine were each built this way, by different but structurally similar constructions, none of them needing anything beyond fraction arithmetic at every single step. A heading, built from nothing but a pair of whole numbers, gives a fifth construction that needs no series at all, and satisfies its own version of the same circular identity exactly, for a completely different reason, never claimed to be the same thing as the series it resembles. "Algebraic" and "transcendental" name which construction reaches a number, not what kind of thing it is. Nothing in this book declared a completed totality of numbers, because nothing in this book needed one, and nothing in this book treated a number as existing ahead of the steps that produced it.

The book claimed nothing about what numbers ultimately are. It said what its three moves produce, where each choice was made, and what each choice buys.


### What This Book Does Not Cover

Integrals, the way a rate turns back into a quantity. The proofs that a rate law has a solution and only one, used in Units 12 and 13 without being proven unique. The proof that S and C from Unit 13 match the sine and cosine measured on triangles. Connecting a heading's (P:Q) to an actual angle in degrees or radians. What happens with more than two dimensions. A longer companion, *How To Build A Novel Calculi*, treats the machine itself, and how to build a different one on a different alphabet.


---


*Answer Key*

## Check Your Work


### Unit 1


**1.** isolate(40,3) outputs (40,3).

**2.** isolate(15,0) outputs (15,0).

**3.** isolate(20,4) outputs (20,4): 20 is the value now, 4 is how fast it's changing.

**4.** isolate(500,-10) outputs (500,-10).

**5.** isolate(7) is short for isolate(7,1), and outputs (7,1). It assumes rate 1.

### Unit 2


**1.** rate(P,Q) outputs 8/4=2.

**2.** rate(M,N) outputs 9/3=3.

**3.** A is changing three times as fast as B.

**4.** rate(x,x) outputs 1, because the rate slot is 6, not 0. Compared to itself it is changing exactly as fast as itself. If the rate slot were 0, Unit 6's refusal, not 1.

**5.** rate(G,H) outputs 12/4=3.

**6.** Because "how fast" is a question about speed, not where each Reading started; only the rate slot answers that.

### Unit 3


**1.** x=7: strips 7 and 7, sum 14. mix(x,x) outputs (49,14). rate outputs 14.

**2.** x=8: strips 8,8, sum 16. Outputs (64,16). rate outputs 16.

**3.** x=9: strips 9,9, sum 18. Outputs (81,18). rate outputs 18.

**4.** x=5: strips 5,5, sum 10. Outputs (25,10). rate outputs 10.

**5.** Prediction: 2*12=24. Check: strips 12,12, sum 24. Outputs (144,24). rate outputs 24.

**6.** Shortcut outputs 1*1=1. Real output is 6. Different: the shortcut throws away information the two strips keep.

### Unit 4


**1.** x=5: Step1 outputs (25,10). Step2: value=125, rate=(10*5)+(25*1)=75. Outputs (125,75).

**2.** x=6: Step1 outputs (36,12). Step2: value=216, rate=(12*6)+(36*1)=108. Outputs (216,108).

**3.** Prediction 3*10*10=300. Step1 outputs (100,20). Step2: value=1000, rate=300. Matches.

**4.** Prediction: 5*3^4=405. Running four mixes from x=isolate(3) confirms rate(x^5,x)=405.

### Unit 5


**1.** x=isolate(3,2): x*x outputs (9,12). rate outputs 12/2=6. Matches Unit 3's seed-1 output.

**2.** x=isolate(7,4): x*x outputs (49,56). rate outputs 56/4=14. Matches Unit 3 Practice Problem 1.

**3.** x=isolate(6,-1): x*x outputs (36,-12). rate outputs -12/-1=12. Matches the seed-1 output of 12 for x=isolate(6).

**4.** Whatever seed you pick multiplies into both top and bottom of the rate division, in matching amounts, so it cancels out.

### Unit 6


**1.** t=1: u outputs (2,2). y outputs (4,8). rate(y,t) outputs 8. rate(y,u)*rate(u,t)=(8/2)*(2/1)=8. Matches.

**2.** t=3: u outputs (6,2). y outputs (36,24). rate(y,t) outputs 24. (24/2)*(2/1)=24. Matches.

**3.** t=4: u outputs (8,2). y outputs (64,32). rate(y,t) outputs 32. (32/2)*(2/1)=32. Matches.

**4.** rate(J,K) is 5/0, theta. K isn't changing, so there's nothing to compare J's rate against, the same way there's no "how many times more" when the amount you're comparing to is zero.

**5.** u already carries everything about t that Room 2 needs; Room 2 never has to reach back and ask t anything directly.

**6.** "Huge number" still treats the question as having a well-shaped answer that's just large. It doesn't. K's rate isn't "basically nothing," it's exactly 0, and a ratio to exactly 0 isn't a big number, it's not a number at all.

### Unit 7


**1.** x*x=(16,8). Add x=(4,1): (20,9).

**2.** x*x=(1,2). x*x*x = (1,2)*(1,1) = (1,3).

**3.** x*x=(25,10). Subtract x=(5,1): (20,9). Plain check: 5*5-5=20, matches.

**4.** The mix rule takes any two Readings and returns a Reading, so its output can always be fed back in as an input to the same rule.

**5.** x*x*x=(27,27). Subtract x=(3,1): (24,26).

### Unit 8


**1.** x=isolate(4,1,0): x*x outputs (16,8,2).

**2.** x=isolate(5,1,0): x*x*x outputs (125,75,30).

**3.** Pattern: curve = 6*x. At x=3, 6*3=18, matches Demonstration 2. At x=5, 6*5=30, matches Problem 2.

**4.** The curve's middle term, r1*r2, comes from two different paths (rate of the first strip, and rate of the second strip) that both produce the same product r1*r2, so they add together. The rate rule's two strips, r1*v2 and v1*r2, are different products from the start, so there's nothing to double.

### Unit 9


**1.** gap = (30,-10). Meet when 30+t*(-10)=0, so t=3.

**2.** gap = (0,-2). The gap's value is already 0 at the start: they begin at the same position.

**3.** gap-x=(8,-4), gap-y=(6,0). Time of closest approach: t=2. Squared distance at that time: 36.

**4.** The same subtract-then-divide method finds the exact time the combined squared distance is smallest, whether or not that smallest value happens to be 0; "closest" is a well-defined minimum either way, not something that only makes sense for an actual meeting.

### Unit 10


**1.** q=2, s=(5*5-0*10)/25=1. Result: (2,1).

**2.** q=1/2, s=(0*2-1*1)/4=-1/4. Reading (1/2,-1/4).

**3.** numerator (1,1), denominator (2,1). q=1/2, s=(1*2-1*1)/4=1/4. Reading (1/2,1/4).

**4.** x*x=(4,4). q=1/4, s=(0*4-1*4)/16=-1/4. Reading (1/4,-1/4).

**5.** The divisor's value is 0, so the machine refuses: theta, the same reason ordinary division by 0 has no answer.

**6.** (a) yes, built from + and *. (b) no, divisor's value is 0 at x=3. (c) yes: numerator (4,1), divisor (1,1), q=4, s=(1*1-1*4)/1=-3, Reading (4,-3).

### Unit 11


**1.** (2k+1)² = 4k²+4k+1 = 2(2k²+2k)+1, one more than even, so odd.

**2.** It supplies the contradiction: the argument shows a and b are both even, but lowest terms means they share no factor of 2.

**3.** Step 6: midpoint of 45/32 and 23/16 is 91/64. Squared: 8281/4096, versus 2=8192/4096, too big, new high. Range (45/32, 91/64), gap 1/64. Step 7: midpoint of 45/32 and 91/64 is 181/128. Squared: 32761/16384, versus 2=32768/16384, too small, new low. Range (181/128, 91/64), gap 1/128.

**4.** The gap halves each step, starting at 1. After k steps the gap is 1/2^k. Need 1/2^k under 1/100,000: 2^17=131,072 clears it, so about 17 steps.

**5.** (665857/470832 + 2/(665857/470832)) / 2. No need to simplify the fraction inside.

**6.** The label is just a short name for the rule. Calling it √2 doesn't add any information either rule didn't already contain; you could run the whole book without ever writing the symbol.

### Unit 12


**1.** Value: 1+1/2+1/8+1/48+1/384=211/128. Rate: P3 at 1/2=1+1/2+1/8+1/48=79/48. Shortfall: 1/384.

**2.** P2 at 2 has rate 1+2=3. P1 at 2 is 1+2=3. Equal.

**3.** A degree-n polynomial's rate has degree n-1, one lower, so a polynomial can never equal its own rate unless both are 0. E(0)=1 rules that out, so only the ongoing construction, not any single polynomial, satisfies the law.

**4.** 1/7! = 1/5040.

**5.** The law says rate(E)=E, and E(0)=1, so the rate at 0 is 1.

### Unit 13


**1.** C2's rate at 1 is -x=-1. S1=x at 1 is 1, minus that is -1. Match.

**2.** S*C = (12/25, 7/25).

**3.** S*S+C*C = (1, 0).

**4.** S*C reads (sc, c*c-s*s). The rate is c²-s².

**5.** "Approximates" compares S3 to something else assumed to exist separately. "S3's rate at 1 is exactly 1/2" is a fact about S3 alone, checked by arithmetic, with nothing else assumed.

### Unit 14


**1.** heading(3,4): c=(16-9)/25=7/25, s=2*3*4/25=24/25. Check: 49/625+576/625=625/625=1.

**2.** heading(1,4): c=(16-1)/17=15/17, s=2*1*4/17=8/17. Check: 225/289+64/289=1.

**3.** Combined P,Q = (1*1+2*2, 2*1-1*2) = (5,0). heading(5,0)=(-1,0). Direct combine: c1c2-s1s2 and s1c2+c1s2 using heading(1,2)=(3/5,4/5) and heading(2,1)=(-3/5,4/5) both give (-1,0). Match.

**4.** turn = 2*4/17 = 8/17.

**5.** Satisfying the same equation only shows both pairs sit somewhere on the same algebraic curve; it says nothing about how each pair was built, and a heading (whole-number pair, no series, no angle) and Unit 13's (S,C) (infinite series, connects to measured angles) are built by genuinely different processes.

### Unit 15


**1.** 5/n < 1/1000 needs n > 5000, so n=5001 works.

**2.** 2^n > 1000 first happens at n=10 (2^10=1024), so stage 10.

**3.** 1/n < 1/20 needs n > 20, so n=21 works.

**4.** From 2^10=1024, need 2^n > 100,000; 2^17=131,072 is the first past it, so about 7 more steps.

**5.** Every actual request names one specific precision, and the rule only ever has to answer that one request in finitely many steps; there's no request that would force it to run forever.

### Unit 16


**1.** 5x + 2, since 5*(-2/5)+2=0.

**2.** x*x - 3.

**3.** qx - p, since q*(p/q) - p = 0.

**4.** No. Computing S3 or C2 at any point is exactly the same finite arithmetic either way; being transcendental doesn't change a single step of it.

**5.** "Transcendental" is a checked, narrow fact: e isn't a root of any whole-number polynomial. "Less real" claims something about existence that no calculation tests; it isn't something the transcendence proof says or implies.

### Unit 17


**1.** (a) Unit 7, mix on Readings. (b) Unit 11, the halving or averaging rule. (c) Unit 12, the shortfall construction. (d) Unit 14, the heading rule on a whole-number pair.

**2.** Answers vary. For example: e is fully specified by the rule in Unit 12, which produces a proven-accurate fraction for any precision requested; nothing about that description waits on a limit being taken first.

**3.** Because every claim only ever refers to one specific rule and one specific requested precision at a time; nothing in the reasoning requires gathering every possible number into one object before starting.

### Unit 18


**1.** Kind 1. Check: (4,1)*(4,1) = (16,8).

**2.** Kind 1. Checked by the proof in Unit 11.

**3.** Kind 2. Checked by dropping balls and timing them; fails once air resistance matters.

**4.** Kind 3. No calculation tests "more real."

**5.** Kind 1. A theorem, a checkable argument.

**6.** Kind 3. No calculation or proof in this book tests a claim about what exists prior to any rule.

**7.** Kind 1. Unit 11 proves the bound directly, by the halving construction.

**8.** Kind 3, as written. "Both satisfy c*c+s*s=1" is kind 1 and checkable; "is what they really are, underneath" claims an identity between two different constructions that no shared equation can establish.

---

<!-- PART IV END -->


<!-- PART V BEGIN: part5.md -->

*Part V*

# What The Machines Taught

### Nine Units From Building On A Chip, In The Book's Moves

Parts I to IV built numbers, letters, shapes and a calculus out of three moves. Part V takes those moves onto a chip with no floating point and 400 KB of memory, where every quantity has to be held as whole numbers. Nine habits came out of that work, each one found by a build that failed first. Every number in the demonstrations below is printed by `docs/teach.py` or `workbook/part5.py`, and `workbook/check_workbook.py` fails if any of them stops matching.

Same shape as before: a big question, the reason, demonstrations, a Try It Yourself, practice, and answers at the back of this part. Part V adds one line to each unit, **On the chip**, naming a sketch in `demos/` where the habit does work.


---


*Unit V1*

## The Carry: A Rate As Whole Pulses


> **Big Question:** A wheel should turn 4/3 of a step every tick, and a motor can only take whole steps. How do you send it whole steps without ever drifting?

Part I, Unit 4 kept the remainder of 17 / 5 instead of throwing it away: "the 2 left over is real." The carry keeps it for the next tick. Each tick adds the rate's top to a running remainder; every time the remainder reaches the bottom, one whole pulse leaves and the bottom is taken off.


*Demonstration 1: 7/3 by hand*

```text
tick 1: emit 2, carry 1, count 2, 3*count + carry = 7 = 7*1
tick 2: emit 2, carry 2, count 4, 3*count + carry = 14 = 7*2
tick 3: emit 3, carry 0, count 7, 3*count + carry = 21 = 7*3
```

The last column is the **books**: bottom × count + carry = top × ticks, on every tick. Nothing is lost, so nothing drifts.


*Demonstration 2: 4/3 for 100,000 ticks, against a float*

```text
first 24 ticks: 112112112112112112112112; after 100000: count 133333, d*count+acc == n*ticks held every tick; FLOAT accumulator wrong on 33333 ticks
```

A float adds 1.333… each tick and rounds where 4/3 can't be written in binary. It was wrong on a third of the ticks.


> **Why does the carry need "while" and not "if"?** At 7/3 one tick can owe three pulses. An `if` sends one and lets the remainder grow without bound. The books still hold (they count the remainder), so add the bound 0 ≤ carry < bottom to the check. Books that hold are not a rule that works.

**On the chip:** LACE's forgetting (`demos/lace`), every pulse train, every line drawn by the carry rule in HIGH NOON's ray walk.

**Try It Yourself:** Run 7/3 for ticks 4, 5 and 6. *Hint: start from carry 0 after tick 3.* Answer: the same three lines again with counts 9, 11, 14.


### Practice: Unit V1

1. Write the first six ticks of 5/4: pulses, carry, count.
2. At 4/3, what are the books after 9 ticks?
3. Why does the pattern 112 repeat every three ticks at 4/3?
4. A float accumulator for 1/3 is checked after one tick and after 300. At which one would you expect it to fail, and why? (Part IV's Unit 11 halving rule is a hint about where errors pile up.)

---


*Unit V2*

## The Mouth: Landing Once


> **Big Question:** A fraction has to become a whole number to light a pixel. Where, and by which rule, should that happen?

Part I's Unit 5 said that two "round down" rules disagree on negatives. Here they are, and the rule this project uses instead.

```text
toward the more negative (//) of -7/2: -4; toward zero of -7/2: -3
mouth of 1/2, 3/2, 5/2, -1/2, -3/2: 0, 2, 2, 0, -2
mouth 5/2, 7/2, -5/2, -7/2, 10/3: [2, 4, -2, -4, 3]
mouth mirror fails: 0 of 54009; floor shift (-x>>1) != -(x>>1) on 3000 of 6001
```

**The mouth:** the nearest whole number; an exact half goes to the even neighbour; and mouth(−x) = −mouth(x). It is used once, at the edge, where a quantity leaves the rules (a pixel, a motor step), never in the middle of a chain.


> **A choice, not a discovery** Half to even is a choice. It is picked because it is the only one of the usual rules that is unbiased over many halves and keeps the mirror: a heading (P : Q) and (−P : −Q) must stay the same heading after landing.

**On the chip:** every sketch here has a `mouth` function. TIDE's turns land inside shears with it, so they run back.

**Try It Yourself:** Land 9/2, 11/2 and −9/2. Answer: 4, 6, −4.


### Practice: Unit V2

1. Land 7/4, 10/4, −10/4.
2. A shift right by one is a division by 2 that lands toward the more negative number. On which of −3, −2, 3 does `x >> 1` disagree with the mouth of x/2?
3. Why land once at the edge and not after every multiply?

---


*Unit V3*

## Which Answer Belongs To Which Cut


> **Big Question:** Two cars, A at 0 moving 5, B at 10 moving −3. You rename the rope, point the road the other way, or seed the rates with −1. Which answers move?

Part IV's Unit 5 showed the seed cancels. The same test can be run on every choice an observer makes. Each choice is a **cut**: a naming, a direction, a seed, a grain.

```text
A-B: rope (-10; 8), rate(rope, A) = 8/5, grow = rope rate / rope value = -4/5
B-A: rope (10; -8), rate(rope, A) = -8/5, grow = rope rate / rope value = -4/5
direction cut flipped: rope (-10; 8), rate(B, A) = -3/5, grow = -4/5
seed -1: rope (10; 8), rate(B, A) = -3/5, grow = 4/5
```

`rate(rope, A)` moves when the ends are renamed. `grow` moves with the seed, because it counts per latch. `rate(B, A)` moves with none of the three.


*Demonstration 2: the same turning, counted at seven grains*

```text
same turning, peaks counted at grain 2^k: k=0: 16, k=12: 16, k=16: 32, k=17: 104, k=18: 62, k=19: 31, k=20: 32
```

At fine grains the count is the turning's: 16. At coarse grains the counting rule counts the stairs of the landed staircase. Read at one grain, 104 would have been reported as a fact about the turning.


> **The rule** No reading is believed until it has been taken at two cuts. A number that moves when you change a cut belongs to the cut as much as to the thing.

**On the chip:** NAGARE reads turning round 4 × 4 loops and says so; a different loop size reads a different turning.

**Try It Yourself:** Scale every place and rate by 3. Which of the three answers move? Answer: none. Each is a ratio of two quantities scaled together. (`practice/p06_two_cuts` asks for the full table, with `when` added.)


### Practice: Unit V3

1. Compute `when` (−value ÷ rate) for the rope named A−B and named B−A. Does the naming move it?
2. Name two cuts that a thermometer imposes on "the temperature of the room."
3. Why is "the swirl" a weaker sentence than "the turning counted round 4 × 4 loops"?

---


*Unit V4*

## Running Back


> **Big Question:** Can a step be undone without storing what came before it?

Keep two readings, now and before. Step with next = 2·now − before + push(now). Solved for the other end, the same line is the step back: before = 2·now − next + push(now). The push can be any rule of where things are now, rounding included, because it appears in both directions unchanged.

```text
32 drops, 2000 out and 2000 back: whole numbers 32 of 32 home exactly; FLOAT 30 of 32 within half a unit
x+x: 128 of 256; x*6: 128 of 256; x*5: 256 of 256; x+37: 256 of 256; x^(x>>3): 256 of 256; x*3//4 (a rounding): 192 of 256
```

The second line counts, for each instruction on 8-bit numbers, how many of the 256 inputs give different outputs. Doubling sends 256 inputs to 128 outputs: two inputs to one output, so a bit is lost and no rule can recover it. Multiplying by 5 loses nothing. **A lost bit is a count of collisions.**


> **Why float fails here** Every float step lands the state itself, and a landing is two-to-one. The whole-number version lands only inside the push, which both directions share.

**On the chip:** TIDE (a whole instruction set with no two-to-one instruction) and MINAMO (a pond that runs 1,240 latches out and exactly back).

**Try It Yourself:** Is x → x + x + 1 one-to-one on 8-bit numbers? Answer: no. 2x + 1 is always odd, so 256 inputs land on 128 outputs.


### Practice: Unit V4

1. Count collisions of x → 3x on 8-bit numbers. Then x → 4x.
2. Why must the push read the step's label of *now*, the same going back?
3. `practice/p04_run_back`: write the step in C and make all 256 places come home.

---


*Unit V5*

## Move A Kept Quantity; Never Set It


> **Big Question:** Heat spreads along a row of places. How do you write the spreading so no heat is made or lost?

Take an amount from one place and give the same amount to its neighbour, in one move. Never write a place's new value from a formula of its neighbours: that line makes or loses amount every step it rounds.

```text
transfer: total 8435, broken on 0 of 2000 steps; assignment (a blur): 8435 -> 4288
three quarters a face, 40 steps: total 8000 (start 8000), places below zero 32 of 64
```

The second line is the warning. Each face moved three quarters of the difference between its two places, so a peak gave away one and a half times what it held. The total stayed exactly 8000 while half the places went below zero. **Conservation is not correctness.** Count the negatives too.

**On the chip:** NAGARE's letters (MOVE, PUSH, DRAG, EXCHANGE, LIFT) are all transfers, so its books are exact every step.

**Try It Yourself:** What share of the difference can a face move before a peak between two empty places goes negative? Answer: the peak gives that share of its height to each side, twice the share in all, so the share must be at most a half. A quarter is safe; three quarters is the failure above.


### Practice: Unit V5

1. Write one transfer step by hand on the row 0, 8, 0 with a quarter of the difference a face.
2. Why does an assignment blur lose total when it rounds down?
3. `practice/p05_transfer`.

---


*Unit V6*

## The Lever: A Value With Its Rate Per Source


> **Big Question:** A total depends on several inputs. Which inputs, if changed, would change it, and by how much?

Part IV gave every reading one rate slot. Give it one rate slot per source instead, and keep which sources ever touched it. Then each source is in one of three states:

- **absent:** never touched the total;
- **still:** touched it, with rate 0 here;
- **moving:** touched it, with a rate.

*Demonstration: total = price × qty + fee × fee + floor × 0, at price 12, qty 3, fee 0, floor 5*

```text
total = 36: price moving, rate 3
total = 36: qty moving, rate 12
total = 36: fee still
total = 36: floor still
total = 36: tax absent
```

Fee is still, not absent: at fee = 0 the rate of fee × fee is 0, but the total moves once fee leaves 0. Floor is still for another reason: it was multiplied by 0. A tool that keeps only "touched or not" would call floor a dependency; a tool that keeps only the rate would call fee irrelevant. The three states keep both.

**On the chip:** CANDLE computes each dot's light once as (value; three rates against the flame's move), then lights the room every frame with four multiplies a dot. `docs/MISSING_MACHINE.md` gives the full argument.

**Try It Yourself:** Add tax as total × tax with tax = 2. Which sources move, and at what rates? Answer: total becomes 72; price moves at 6, qty at 24, tax at 36; fee and floor stay still.


### Practice: Unit V6

1. For y = a × b + b × b at a = 2, b = 3, give the rate per source.
2. Why does "still" not mean "will not change"?
3. Name a computing tool that keeps only the touched set, and one that keeps only the rate.

---


*Unit V7*

## A Heading Turns The Plane Exactly


> **Big Question:** Part IV's Unit 14 turned a pair of fractions exactly with a heading. Can a heading turn every whole-number point of a grid without two points landing on one?

Rounding the turn of each point does not work in general. Three shears do: slide x by y·P/Q, slide y by x·2PQ/(P² + Q²), slide x by y·P/Q again, each slide landed with the mouth. Each slide is undone by sliding back the same amount, so no two points can land together.

```text
(1:2) -> c 3, s 4, d 5; c*c+s*s == d*d: True
(1:2) then (1:2) -> (4:3), unit (-7, 24)/25
(1:2) on 3721 points: rounded turn 0 collisions; three shears 0 collisions
(1:4) on 3721 points: rounded turn 860 collisions; three shears 0 collisions
```

The third line is a trap that was found while writing this unit's practice checker. For (1:2) rounding happens to lose no point, and so does (2:3), (1:7) and (3:4). A test drawn only from that family would have passed a rounded turn. (1:4) shows the difference.

**On the chip:** TIDE's TURN instruction; every heading table in the C3 demos.

**Try It Yourself:** Compose (1:2) with (1:4). Answer: P = 1·4 + 1·2 = 6, Q = 2·4 − 1·1 = 7, so (6:7), with unit (13, 84)/85.


### Practice: Unit V7

1. Find the unit of (2:3) and check c·c + s·s = d·d.
2. Why is each shear undone exactly, whatever rounding is used inside it?
3. Why does a mouth inside the shears keep turn(−p) = −turn(p), where a floor would not?

---


*Unit V8*

## A Reading Fed Back Into Its Own Rule


> **Big Question:** You tune a threshold until it scores well. What does the score describe?

```text
threshold tuned on 200: 21; right on the tuning set 186/200, on the sealed set 179/200
```

The tuned number describes the set it was tuned on. Only a set read once, after the tuning stopped, witnesses the claim. A reading folds many configurations into one number at one cut; an actor that is fed that number moves the configuration along the cheapest path that changes the number (Goodhart, mechanically). The guards: readings never feed rules; draw the reading's cut after the act; show the books beside every reading; read yourself at cuts you did not tune.

**On the chip:** NAGARE's KL = 24 was chosen after looking, and its amendment says so: "This amendment is a tuning, and is named as one."

**Try It Yourself:** `practice/p07_kill_line` gives you 200 tuning readings and 200 sealed ones. Seal your kill line before the read.


### Practice: Unit V8

1. Why is a thousand runs in one context one witness?
2. Write a pass mark for a claim you have not tested yet.
3. Why can't a closure (a books equation) be gamed the way a score can?

---


*Unit V9*

## Witnesses, Load And Drag


> **Big Question:** A claim has passed some tests and needed some fixes. How strongly does it stand?

Count three things. **C**: the distinct witnesses it held in (a second build, exact fractions, desk against chip, a sealed set, a person with a board). **L**: its load, the alterations it needed (a mechanism added, a scope narrowed, an exception). **D**: its drag, the load of what it rests on. The claim propagates at v = C / (C + L + D).

```text
C 4, L 0, D 1: v = 4/5
C 4, L 3, D 1: v = 1/2
C 2, L 3, D 1: v = 1/3; L >= C: reconfigure
```

At L ≥ C, stop patching. Keep the core that needed no patch, and vent the rest as a separate claim at L = 0. Effort already spent is not a term.


> **A choice, not a discovery** The formula is a rule for developing rules, measured on the project's ledgers (27 failures, 5 pivots). It orders what to alter first (the least-witnessed relation). It does not say what to try.

**On the chip:** every README in `demos/` lists what was run, what was not, and tiers its claims; NAGARE logs four amendments.

**Try It Yourself:** A claim has C = 3, L = 1, D = 0. Give v. One more fix arrives. What changes? Answer: v = 3/4; with L = 2, v = 3/5, still C > L. A third fix makes L = C and the claim reconfigures.


### Practice: Unit V9

1. Name four kinds of witness.
2. Why is bringing code into line with what a claim already said not load?
3. Write a kill line for "this sketch runs the same on the desk and on the chip."

---


*Answer Key, Part V*

## Check Your Work


### Unit V1

**1.** 5/4: tick 1 emit 1 carry 1; tick 2 emit 1 carry 2; tick 3 emit 1 carry 3; tick 4 emit 2 carry 0; tick 5 emit 1 carry 1; tick 6 emit 1 carry 2. Counts 1, 2, 3, 5, 6, 7.

**2.** count 12, carry 0: 3 × 12 + 0 = 36 = 4 × 9.

**3.** 4 × 3 = 12 = 3 × 4: after three ticks the carry is back to 0, so the pattern starts again.

**4.** After 300. One step's rounding is a fraction of the last bit; the errors pile up over many steps.

### Unit V2

**1.** 2, 2, −2 (10/4 = 5/2, an exact half, goes to the even 2).

**2.** On −3: −3 >> 1 = −2, the mouth of −3/2 is −2: they agree. On −2: both −1. On 3: 3 >> 1 = 1, the mouth of 3/2 is 2: they disagree. (They also disagree at −1: −1 >> 1 = −1, the mouth of −1/2 is 0.)

**3.** Each landing loses up to half a unit. Landing once loses it once; landing after every multiply piles the losses up, and a product of landed numbers carries them all.

### Unit V3

**1.** A−B: rope (−10; 8), when = 10/8 = 5/4. B−A: rope (10; −8), when = 10/8 = 5/4. Naming does not move it.

**2.** For example: where the sensor sits (place), how long it averages (grain), and its scale.

**3.** "The swirl" writes a reading as a thing. The second sentence names the rule and the cut that made the reading, so someone else can take it again.

### Unit V4

**1.** x → 3x: 256 of 256 (3 is odd). x → 4x: 64 of 256.

**2.** If the push reads a different label going back, it adds a different amount than it subtracted, and the step back is not the inverse.

**3.** Checked by `python3 practice/p04_run_back/check.py`.

### Unit V5

**1.** Differences 8 and 8; each face moves 2: 2, 4, 2. Total 8 before and after.

**2.** Each place is landed down separately, so the pieces lost to rounding leave the total and go nowhere.

**3.** Checked by `python3 practice/p05_transfer/check.py`.

### Unit V6

**1.** y = 2 × 3 + 3 × 3 = 15. Rate per a: b = 3. Rate per b: a + 2b = 8.

**2.** The rate is read here, at this point. Away from it the rate can be non-zero (fee × fee at fee = 0).

**3.** Taint tracking and build systems keep a touched set; sensitivity analysis and gradients keep only the rate.

### Unit V7

**1.** (2:3): c = 9 − 4 = 5, s = 12, d = 13. 25 + 144 = 169.

**2.** Each shear adds to one coordinate an amount that depends only on the other, which the shear does not change; subtracting the same amount, rounded the same way, restores it.

**3.** The mouth is mirror-true (mouth(−x) = −mouth(x)), so each shear of −p is minus the shear of p. A floor is not mirror-true.

### Unit V8

**1.** It sees one kind of failure. Distinct contexts see different failures.

**2.** For example: "at least 170 of 200 sealed readings right."

**3.** A closure is forced by construction: it holds or it doesn't, and no change of configuration can make it read better without being true.

### Unit V9

**1.** Any four of: a second implementation, exact fractions, desk against emulated chip, float beside it, a sealed set, a kill line written first, a mirror test, an ablation, a control twin, a person holding the board.

**2.** Load is an alteration to what the claim says or needs. Fixing code so it does what the claim already said changes neither.

**3.** For example: "any printed line that differs between the desk twin and the emulated chip over 2,000 frames of the ghost's play."

---

<!-- PART V END -->
