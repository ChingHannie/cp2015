__author__ = 'Hannie'


def display_pattern(n):
    list = []
    for each in range(1, n+1):
        list.append(str(each))
        print(' '.join(list[::-1]).rjust(2*n - 1))

# main
display_pattern(int(input("Enter integer: ")))
