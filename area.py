#-------------------- area of shape-------------------
 
from math import pi,sqrt

# Square
def square(a):
    return a * a

# Rectangle
def rectangle(w, h):
    return w * h

# Triangle
def triangle(base, height):
    return (base * height) / 2

# Triangle
def triangle_heron(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

# Trapezoid
def trapezoid(a, b, height):
    return (a + b) * height / 2

# Circle
def circle(r):
    return pi * (r ** 2)

# Parallelogram
def parallelogram(base, height):
    return base * height
