__author__ = 'Hannie'

year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap")
elif year % 4 == 0:
    print("Leap")
elif year % 100 != 0:
    print("Non-Leap")
else:
    print("Non-Leap")
