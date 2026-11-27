"""Flow without Navier-Stokes: a box of places that only trade (after the project's NAGARE and FLOWING work).

No equation is imported and there is no time step: a latch is one round of trades. Each place holds three whole numbers:
  stuff  s    (how much air is there)
  rate   mx, my (carried rate, kept as momentum: stuff times how far it is carried a latch; y counts downward)
  warmth w
Every change is a hand-on between two neighbours (one take, one give), or an entry from outside that is counted:
  PUSH      at each face, the crowding on both sides (their stuff together) pushes them apart: rate taken from one
            side and given to the other. A place feels the difference of its two faces, so even crowding cancels
  DRAG      at each face, neighbours trade rate by how much they differ (along the face's line more than across)
  EXCHANGE  stuff is handed down its own difference to the neighbour, carrying its share of rate and warmth
            (PUSH reads two places apart and cannot see an alternation; this sees it)
  LIFT      a place warmer than the box as a whole is handed upward rate, a cooler one downward; the context is the
            box's own warmth; the ground's hand is counted
  MOVE      at each face, stuff is carried by the rate there, from the upwind side, with its share of rate and warmth
  FEED/VENT a heater puts warmth in at the floor; the cold lid takes a share out; both counted
  WALLS     rate carried into a wall is turned round by the wall; the wall's push is counted
Every trade reads the places as the latch found them, and all trades are handed on together afterwards.
The books, checked every latch:
  stuff  = start
  warmth = start + fed - vented
  momentum (each direction) = start + what the walls and the ground gave
plus the range: every place keeps stuff > 0 and warmth >= 0.
"""
from .whole import mouth


class Box:
    def __init__(self, W=32, H=20, stuff=1000, KP=6, KD=2, KE=1, KL=24, KM=1, VENT_DEN=8):
        self.W, self.H, self.N = W, H, W * H
        self.s = [stuff] * self.N
        self.mx = [0] * self.N
        self.my = [0] * self.N
        self.w = [0] * self.N
        self.KP, self.KD, self.KE, self.KL, self.KM, self.VENT_DEN = KP, KD, KE, KL, KM, VENT_DEN
        self.s0, self.w0, self.mx0, self.my0 = sum(self.s), 0, 0, 0
        self.fed = self.vented = 0
        self.walls_x = self.walls_y = self.ground_y = 0
        self.latches = 0
        self.heater = None          # (x, amount per latch) at the floor, or None
        self.plant = None           # a planted fault, for the checks: "assign" sets the middle place's warmth (halves it)

    def i(self, x, y):
        return y * self.W + x

    def puff(self, x, y, amount, radius=2):
        """Warmth laid in at a spot: an outside entry, counted as fed."""
        for yy in range(max(0, y - radius), min(self.H, y + radius + 1)):
            for xx in range(max(0, x - radius), min(self.W, x + radius + 1)):
                self.w[self.i(xx, yy)] += amount
                self.fed += amount

    def latch(self):
        W, H, N = self.W, self.H, self.N
        s, mx, my, w = self.s, self.mx, self.my, self.w
        ds, dmx, dmy, dw = [0] * N, [0] * N, [0] * N, [0] * N
        faces = [(self.i(x, y), self.i(x + 1, y), 0) for y in range(H) for x in range(W - 1)] + \
                [(self.i(x, y), self.i(x, y + 1), 1) for y in range(H - 1) for x in range(W)]
        for a, b, axis in faces:
            # PUSH: the crowding on both sides of the face pushes them apart, one take and one give
            t = mouth((s[a] + s[b]) * self.KP, 32)
            if axis == 0:
                dmx[a] -= t; dmx[b] += t
            else:
                dmy[a] -= t; dmy[b] += t
            # DRAG: trade rate by the difference; along the line at KD/16, across it at KD/32
            along, across = (mx, my) if axis == 0 else (my, mx)
            da, dc = (dmx, dmy) if axis == 0 else (dmy, dmx)
            t1 = mouth((along[a] - along[b]) * self.KD, 16)
            t2 = mouth((across[a] - across[b]) * self.KD, 32)
            da[a] -= t1; da[b] += t1
            dc[a] -= t2; dc[b] += t2
            # EXCHANGE and MOVE: stuff handed across the face, from the donor side, with its share of rate and warmth
            m_face = (mx[a] + mx[b]) if axis == 0 else (my[a] + my[b])
            f = mouth((s[a] - s[b]) * self.KE, 16) + mouth(m_face * self.KM, 8)
            if f != 0:
                d, r = (a, b) if f > 0 else (b, a)
                f = min(abs(f), s[d] // 8)
                if f > 0:
                    cx, cy, cw = mouth(mx[d] * f, s[d]), mouth(my[d] * f, s[d]), mouth(w[d] * f, s[d])
                    ds[d] -= f; ds[r] += f
                    dmx[d] -= cx; dmx[r] += cx
                    dmy[d] -= cy; dmy[r] += cy
                    dw[d] -= cw; dw[r] += cw
        # LIFT, relative to the box's own warmth: (w*N - total) has total exactly 0; each landing's leftover is the ground's
        tot = sum(w)
        for c in range(N):
            l = mouth((w[c] * N - tot) * self.KL, N * 4096)
            dmy[c] -= l
            self.ground_y -= l
        # WALLS push back: each wall face pushes its place away with the place's own crowding, and rate carried into a
        # wall is turned round by it. Both are the walls' hands, counted.
        for y in range(H):
            for x in (0, W - 1):
                c = self.i(x, y)
                p = mouth(s[c] * self.KP, 16) * (1 if x == 0 else -1)
                dmx[c] += p; self.walls_x += p
                if (x == 0 and mx[c] < 0) or (x == W - 1 and mx[c] > 0):
                    dmx[c] -= 2 * mx[c]; self.walls_x -= 2 * mx[c]
        for x in range(W):
            for y in (0, H - 1):
                c = self.i(x, y)
                p = mouth(s[c] * self.KP, 16) * (1 if y == 0 else -1)
                dmy[c] += p; self.walls_y += p
                if (y == 0 and my[c] < 0) or (y == H - 1 and my[c] > 0):
                    dmy[c] -= 2 * my[c]; self.walls_y -= 2 * my[c]
        # FEED and VENT
        if self.heater:
            hx, amt = self.heater
            c = self.i(hx, H - 1)
            dw[c] += amt; self.fed += amt
        for x in range(W):
            c = self.i(x, 0)
            v = w[c] // self.VENT_DEN
            dw[c] -= v; self.vented += v
        # hand every trade on together
        for c in range(N):
            s[c] += ds[c]; mx[c] += dmx[c]; my[c] += dmy[c]; w[c] += dw[c]
        if self.plant == "assign":
            c = self.i(W // 2, H // 2)
            w[c] = w[c] // 2                       # a set, not a trade (halved in place): the books must open here
        self.latches += 1

    def books(self):
        return (sum(self.s) == self.s0,
                sum(self.w) == self.w0 + self.fed - self.vented,
                sum(self.mx) == self.mx0 + self.walls_x,
                sum(self.my) == self.my0 + self.walls_y + self.ground_y)

    def in_range(self):
        return min(self.s) > 0 and min(self.w) >= 0

    def warm_row(self):
        """A reading: the warmth-weighted row of the warmth above the box's mean (rows count down from the lid), as a
        fraction. The cut: above-mean warmth only, the whole box."""
        from fractions import Fraction
        tot = sum(self.w)
        num = den = 0
        for c in range(self.N):
            ex = self.w[c] * self.N - tot
            if ex > 0:
                num += ex * (c // self.W); den += ex
        return Fraction(num, den) if den else None

    def turning(self, x, y):
        """A reading: the turning round the 2 x 2 loop with top-left (x, y): rate carried round it, counted one way."""
        a, b, c, d = self.i(x, y), self.i(x + 1, y), self.i(x + 1, y + 1), self.i(x, y + 1)
        return (self.mx[a] + self.mx[b]) - (self.mx[c] + self.mx[d]) + (self.my[b] + self.my[c]) - (self.my[a] + self.my[d])
