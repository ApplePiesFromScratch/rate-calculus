from fractions import Fraction

class Lever:
    def __init__(self, value, rates=None, touched=None):
        self.value = Fraction(value)
        self.rates = {k: Fraction(v) for k, v in (rates or {}).items()}
        self.touched = set(touched or ()) | set(self.rates)
    def _l(self, o):
        return o if isinstance(o, Lever) else Lever(o)
    def __mul__(self, o):
        o = self._l(o); keys = set(self.rates) | set(o.rates)
        return Lever(self.value * o.value, {k: self.rates.get(k, 0) * o.value + self.value * o.rates.get(k, 0) for k in keys}, self.touched | o.touched)
    __rmul__ = __mul__
    def __add__(self, o):
        o = self._l(o); keys = set(self.rates) | set(o.rates)
        return Lever(self.value + o.value, {k: self.rates.get(k, 0) + o.rates.get(k, 0) for k in keys}, self.touched | o.touched)
    __radd__ = __add__
    def state(self, name):
        if name not in self.touched:
            return "absent"
        return "moving"
    def rate_of(self, name):
        return self.rates.get(name, Fraction(0))

def source(name, value):
    return Lever(value, {name: 1}, {name})
