__author__ = 'Hannie'

import calendar
a = 1
while a != 0:
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    print("{0} {1} has {2} days. ".format(calendar.month_name[month], year, calendar.monthrange(year, month)[a]))
    break
