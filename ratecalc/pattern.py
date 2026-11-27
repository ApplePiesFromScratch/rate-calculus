"""The useful pattern, run as rules (James Pugmire's text; the mechanical reading follows the project's PATTERN map).

A field holds the available gradient: a whole number of units. Patterns draw on it. Each pattern carries
  L      its loaded history: what its propagation has laid down so far (taken from the field)
  C      its support: how well the available gradients carry it
  cells  where it sits (drag is found from shared cells, never declared)
The six clauses, as rules a latch runs:
  UP1 loaded history     a served pattern takes `take` units from the field into its L
  UP2 demand set by history  its next due mark moves forward by (C + L + D) / C
  UP3 simplest propagates fastest  the pattern with the earliest due mark is served next (ties: lighter L, then order),
                         so propagation goes at C / (C + L + D)
  UP4 drag               D = the loaded history of other patterns met in shared cells (computed each latch from contact)
  UP5 reconfigure past the boundary  a pattern whose L passes THETA keeps KAPPA/16 of L, vents the rest to the field,
                         and starts again at the front
  UP6 vent simplicity    after each service a pattern gives vent_num/vent_den of its L back to the field
  theta (refusal)        a pattern served when the field cannot cover its take lays nothing: a named refusal, counted
The books, every latch: field + sum of every L = G0 - drained (the context's own losses, counted).
The front (the earliest due mark) never moves back.
This file claims the readings these rules print (kinds 1 and 2). It does not claim the rules are how anything
ultimately is.
"""
from fractions import Fraction


class Pattern:
    def __init__(self, name, C, cells, take, vent_num, vent_den):
        self.name, self.C, self.cells, self.take = name, C, set(cells), take
        self.vent_num, self.vent_den = vent_num, vent_den
        self.L, self.due, self.served, self.refused, self.reconfigs, self.vented = 0, Fraction(0), 0, 0, 0, 0


class Flux:
    def __init__(self, field, THETA=60, KAPPA=4):
        self.field, self.G0, self.THETA, self.KAPPA = field, field, THETA, KAPPA
        self.p, self.drained, self.latches, self.front = [], 0, 0, Fraction(0)
        self.front_moved_back = False

    def add(self, *a, **k):
        self.p.append(Pattern(*a, **k))
        return self.p[-1]

    def drag(self, P):
        return sum(len(P.cells & Q.cells) * Q.L for Q in self.p if Q is not P)

    def drain(self, amount):
        """The context changes: the field loses units to outside (counted, so the books still close)."""
        amount = min(amount, self.field)
        self.field -= amount
        self.drained += amount

    def latch(self):
        P = min(self.p, key=lambda q: (q.due, q.L, self.p.index(q)))          # UP3
        front = P.due
        if front < self.front:
            self.front_moved_back = True
        self.front = front
        D = self.drag(P)                                                        # UP4
        if self.field >= P.take:                                                # UP1
            self.field -= P.take; P.L += P.take; P.served += 1
        else:
            P.refused += 1                                                      # theta: nothing to land on
        P.due += Fraction(P.C + P.L + D, P.C)                                   # UP2
        v = P.L * P.vent_num // P.vent_den                                      # UP6
        P.L -= v; self.field += v; P.vented += v
        if P.L > self.THETA:                                                    # UP5
            kept = P.L * self.KAPPA // 16
            self.field += P.L - kept; P.L = kept; P.reconfigs += 1
            P.due = front
        self.latches += 1

    def books(self):
        return self.field + sum(q.L for q in self.p) == self.G0 - self.drained
