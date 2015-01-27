__author__ = 'Hannie'

from math import pi
r = float(input("Enter radius of cylinder in cm: "))
l = float(input("Enter length of cylinder in cm: "))
area = r * r * pi
vol = area * l
print("Volume of cylinder is {0:4.1f} cm^3".format(vol))
