"""L09 reference: the six clauses of the useful pattern as rules (guide 26)."""
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
