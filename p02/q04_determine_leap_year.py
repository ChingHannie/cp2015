__author__ = 'Hannie'

year = int(input("Enter year: "))
import calendar
if calendar.isleap(year) == True:
    print("Leap")
else:
    print("Non-Leap")
