# 00. Setup, and how to read these guides

This guide assumes nothing. If you have never opened a terminal, start at step 1. If you have Python 3 and a terminal open in this folder, skip to step 5.

## What you get from this repo

- **A way of working with quantities that change**, built from one alphabet and three moves (the book *Every Number Is A Rule*, by James Pugmire).
- **A small library, `ratecalc`**, that runs those moves exactly (Python, standard library only), and a C version in `core_c/`.
- **Guides** (this folder), one idea each, in order, with every number checked by a program.
- **Examples** (`examples/`) in several fields: money, motion, populations, fluids, evolution, code, pictures, a chip.
- **Lessons** (`lessons/`): practice tasks you write yourself, each graded by a checker that has been shown to catch planted wrong answers.

## Step 1. Get Python 3

You need Python 3.8 or newer. Nothing else gets installed: the library uses only Python's standard library.

- **Windows:** go to python.org, download the Python 3 installer, run it, and tick **"Add python.exe to PATH"** on the first screen before you click Install.
- **macOS:** open the Terminal app (Applications → Utilities → Terminal) and type `python3 --version`. If macOS offers to install developer tools, accept. Or install from python.org.
- **Linux:** Python 3 is almost always installed. Check with `python3 --version`; if it is missing, install the `python3` package with your system's package manager.

## Step 2. Open a terminal

- **Windows:** press the Windows key, type `cmd` (or `PowerShell`), press Enter.
- **macOS:** Terminal app.
- **Linux:** your terminal program.

## Step 3. Check Python

Type this and press Enter:

```text
python3 --version
```

You should see something like `Python 3.11.4`. On Windows the command may be `python` or `py` instead of `python3`; use whichever one prints a version, everywhere below.

## Step 4. Get this repo and go into its folder

Either download the zip and unzip it, or clone it with git. Then move the terminal into the folder:

```text
cd path/to/rate-calculus
```

Replace `path/to/` with where you put it. You are in the right place when `ls` (macOS, Linux) or `dir` (Windows) lists `README.md`, `ratecalc`, `guide` and `examples`.

## Step 5. Run every check once

```text
python3 tools/check_all.py
```

The last line should read `check_all: N passed, 0 failed`. Here is what that command did:

1. It ran every claim in every guide (the ```` ```check ```` blocks, explained below) and every example, comparing each printed line with the line written in its README.
2. It broke the library on purpose, one rule at a time (the **planted faults**), and confirmed that some check turned red each time. A check that stays green while the rule under it is broken is not checking anything.
3. It checked the writing for the words this project refuses (guide 01).
4. It ran the library's own tests.
5. It built and tested the C version, if a C compiler is installed. With no compiler it prints `SKIPPED`, which is not a pass.

If anything fails, the failing line is printed with its file and line number. Do not edit a checker to make it pass: fix the claim or the code.

## Step 6. Try the library by hand

Start Python from this folder:

```text
python3
```

Then type, one line at a time:

```text
>>> from ratecalc import *
>>> x = isolate(4)
>>> x * x
(16, 8)
>>> rate(x * x, x)
Fraction(8, 1)
```

`Fraction(8, 1)` is Python's way of writing the exact fraction 8/1. Type `exit()` to leave.

## How each guide is laid out

Every guide has the same parts, in this order:

1. **The question** it answers.
2. **The rule**, with the reason attached, and whether the rule is *forced* (it cannot come out any other way) or *chosen* (picked because it is useful; the guide says what the choice buys).
3. **Steps**, numbered, slow. Do them on paper first.
4. **Checked claims**: a ```` ```check ```` block. Each line is either a name being set (`x = isolate(4)`), a one-line `def`, a statement written after `do ` (run, not judged), or a claim that must be true. `tools/check_docs.py` runs every line. If a guide says a number, a program has computed it.
5. **Try it yourself**, with a hint and the answer.
6. **Mistakes people make** at this step.
7. **Where it goes next.**

Here is a checked block. You can run it yourself by pasting the lines after `from ratecalc import *`:

```check
x = isolate(4)
x * x == R(16, 8)
rate(x * x, x) == 8
```

## How to read the notation

| You see | It means |
|---|---|
| `(8, 2)` | a **Reading**: value 8, rate 2 |
| `R(8, 2)` | the same Reading, written in Python |
| `isolate(8, 2)` | the move that builds the Reading (8, 2) |
| `isolate(5)` | short for `isolate(5, 1)` |
| `F(1, 3)` or `F('1/3')` | the exact fraction 1/3 |
| `A * B` | `mix(A, B)`, the only multiplication a Reading uses |
| `rate(A, B)` | A's rate slot divided by B's rate slot |
| `theta` | the named refusal when B's rate is 0 |

## Order of the guides

Read them in number order the first time. Each one uses only what came before it.

| # | Guide | Book unit |
|---|---|---|
| 01 | House rules: no independent variable, kinds of claim, refused words | Unit 15; project rules |
| 02 | The alphabet and `isolate` | Unit 1 |
| 03 | Reading a rate, and `theta` | Units 2, 6 |
| 04 | `mix` | Unit 3 |
| 05 | Adding, subtracting, plain numbers | Units 6, 7 |
| 06 | Powers and whole expressions | Units 4, 7 |
| 07 | The seed cancels; two cuts | Unit 5; Part V, Unit V3 |
| 08 | Chains (rooms) | Unit 6 |
| 09 | Division and the machine's reach | Unit 8 |
| 10 | A rate that has its own rate | consolidated edition, Unit 8 |
| 11 | When two moving things meet | consolidated edition, Unit 9 |
| 12 | Numbers that are not fractions are rules | Units 9, 12, 13, 14 |
| 13 | Rate laws: E, S and C | Units 10, 11 |
| 14 | Headings: turning exactly | consolidated edition, Unit 14; Part V, Unit V7 |
| 15 | Whole numbers: the mouth and the carry | Part V, Units V1, V2 |
| 16 | Stepping a changing system with no clock | Part V, Units V4, V5 |
| 17 | The lever: a rate per source | Part V, Unit V6 |
| 18 | Computers and code as alphabets and mixing rules | project |
| 19 | Designing your own alphabet and mixing rule | project; closing note of the book |
| 20 | Checking your work | Part V, Units V8, V9; project |
| 21 | Claims, tiers and reports | Unit 15; project |
| 22 | The modelling recipe: any problem, step by step | project |
| 23 | Mistakes and presumptions | project |
| 24 | Glossary | all |
| 25 | Questions people ask | all |
| 26 | The useful pattern, run as rules | James Pugmire's text; project |
| 27 | Evolutionary modelling | James Pugmire's text; Part V, Unit V9 |
| 28 | Fluid dynamics without Navier–Stokes | project (NAGARE, FLOWING) |
| 29 | A bridge to standard courses | math-of-logic's bridge sheet |
