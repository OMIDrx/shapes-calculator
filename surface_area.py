#---------------- surface area ------------

from math import pi,sqrt

# Cube
def cube(a):
    return 6 * (a ** 2)

# Rectangular Prism
def prism(w, h, l):
    return 2 * (w*h + h*l + w*l)

# Sphere
def sphere(r):
    return 4 * pi * (r ** 2)

# Cylinder
def cylinder(r, h):
    return 2 * pi * r * (h + r)

# Cone
def cone(r, h):
    s = sqrt(h**2 + r**2)
    return pi * r * (r + s)

# Pyramid
def pyramid(base_area, base_perimeter, slant_height):
    return base_area + (base_perimeter * slant_height) / 2
