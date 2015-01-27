__author__ = 'Hannie'

num = int(input("Enter an integer between 0 and 1000: "))
if 0 < num < 1000:
    digit1 = num // 10 // 10
    digit2 = num // 10 % 10
    digit3 = num % 10
    sum = digit1 + digit2 + digit3
    print("The sum of digits in the integer is ", sum)
else:
    print("Invalid integer entered. Try again. ")
