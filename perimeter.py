#----------- perimter of shape --------------
from math import pi

# Square
def square(a):
    return 4 * a

# Rectangle
def rectangle(w, h):
    return 2 * (w + h)

# Triangle
def triangle(a, b, c):
    return a + b + c

# Trapezoid
def trapezoid(a, b, c, d):
    return a + b + c + d

# Circle 
def circle(r):
    return 2 * pi * r

# Parallelogram
def parallelogram(base, side):
    return 2 * (base + side)
