__author__ = 'Hannie'


def m_series(i):
    sum = 0
    numerator = i
    denominator = i+1
    for x in range(1, i+1):
        sum += numerator/denominator
        numerator -= 1
        denominator -= 1
    return "{:.4f}".format(sum)

# main
check = input("Run test program? (y/n) ")

if check == 'y':
    print("i \t m(i)")
    x = 1
    for y in range(20):
        print(x, "\t", m_series(x))
        x += 1

elif check == 'n':
    num = int(input("Enter integer: "))
    print(m_series(num))

else:
    print("Invalid input.")
