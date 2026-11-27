# Example 02: the growing rectangle. mix, strip by strip.
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # find ratecalc from any folder
from ratecalc import *

clock = isolate(0, 1)
width = isolate(6, 2)     # 6 m wide, growing 2 m a minute
height = isolate(4, 1)    # 4 m tall, growing 1 m a minute

v1, r1 = width
v2, r2 = height
print("width", width, " height", height)
print("area now      v1*v2 =", show(v1 * v2))
print("right strip   r1*v2 =", show(r1 * v2))
print("top strip     v1*r2 =", show(v1 * r2))
area = width * height
print("mix(width, height) =", area)
print("rate(area, clock) =", show(rate(area, clock)), "square metres a minute")
print("rate(area, width) =", show(rate(area, width)), "square metres per metre of width")
print("wrong rule (multiply the rates):", R(v1 * v2, r1 * r2), "loses", show(area.rate - r1 * r2), "of the rate")
