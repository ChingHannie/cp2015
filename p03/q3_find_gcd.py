__author__ = 'Hannie'


def gcd(m, n):
    if m > n:
        x = m
    else:
        x = n
    for each in range(x):
        x -= 1
        if m % x == 0 and n % x == 0:
            return x

# main
print(gcd(24, 16))
print(gcd(255, 25))
