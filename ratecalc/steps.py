"""Stepping without a clock (Part V, Units V4 and V5).

run back:  next = 2*now - before + push(now);  the same line solved the other way is the step back:
           before = 2*now - next + push(now). The push can round: it appears in both directions unchanged.
transfer:  take an amount from one place and give the same amount to the neighbour, in one move. Never set a place's
           new value from a formula of its neighbours.
collisions: a lost bit is a count of collisions, two inputs landing on one output.
"""


def step_forward(before, now, push):
    return now, 2 * now - before + push(now)


def step_back(now, nxt, push):
    return 2 * now - nxt + push(now), now


def collisions(f, bits=8):
    """How many distinct outputs f gives over all inputs of the given width, masked to that width."""
    m = (1 << bits) - 1
    return len({f(x) & m for x in range(1 << bits)})


def transfer_step(row, num, den):
    """Each face moves num/den of the difference between its two places (landed toward the more negative number by //,
    applied as one take and one give, so the total is kept exactly)."""
    row = list(row)
    moves = [((row[i] - row[i + 1]) * num) // den for i in range(len(row) - 1)]
    for i, m in enumerate(moves):
        row[i] -= m
        row[i + 1] += m
    return row


def assign_blur_step(row):
    """The wrong way: set each place from its neighbours (rounded down). Kept to show the total leaking."""
    n = len(row)
    return [(row[max(i - 1, 0)] + 2 * row[i] + row[min(i + 1, n - 1)]) // 4 for i in range(n)]


def run_forward(before, now, push, k):
    """k latches forward. Returns (before, now) after them."""
    for _ in range(k):
        before, now = step_forward(before, now, push)
    return before, now


def run_back(before, now, push, k):
    """k latches back, from the pair (before, now) that run_forward returned. Returns the pair k latches earlier."""
    for _ in range(k):
        before, now = step_back(before, now, push)
    return before, now
