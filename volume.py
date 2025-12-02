#-------------- volume ------------------
from math import pi,sqrt
# Cube
def cube(a):
    return a ** 3

# Rectangular Prism
def rectangular_prism(w, h, l):
    return w * h * l

# Sphere
def sphere(r):
    return (4/3) * pi * (r ** 3)

# Cylinder
def cylinder(r, h):
    return pi * (r ** 2) * h

# Cone
def cone(r, h):
    return (1/3) * pi * (r ** 2) * h

# Square / Rectangl
def pyramid(base_area, height):
    return (base_area * height) / 3
