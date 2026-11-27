# Example 01: a bathtub, a clock and a candle. isolate, rate, theta and when.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

clock = isolate(0, 1)          # counts minutes: everything is compared with it
tub = isolate(8, 2)            # 8 gallons now, 2 gallons a minute in
candle = isolate(15, 0)        # 15 cm, not lit
rim = const(40)                # the tub holds 40 gallons: a plain number

print("tub:", tub)
print("rate(tub, clock):", show(rate(tub, clock)), "gallons a minute")
print("rate(tub, candle):", rate(tub, candle))
room = rim - tub               # the room left in the tub, as a Reading
print("room left:", room)
print("when the room runs out:", show(when(room)), "minutes")
print("check: 32 + 16 * (-2) =", room.value + when(room) * room.rate)
plug = isolate(0, -5)          # pull the plug too: 5 gallons a minute out
both = tub + plug
print("tub with the plug out:", both)
print("when it empties:", show(when(both)), "minutes")
print("landed for a display (the mouth, once):", mouth_of(when(both)), "minutes")
print("when the room runs out now:", when(rim - both))
