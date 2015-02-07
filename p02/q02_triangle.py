__author__ = 'Hannie'

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
sides = side1 + side2 + side3
if side1 + side2 < side3 or side2 + side3 < side1 or side1 + side3 < side2:
    print("Invalid triangle!")
else:
    print(sides)
