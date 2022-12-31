import math
def solution(a, b):
    gcd_of_two = math.gcd(a, b)
    b /= gcd_of_two

    while b % 2 == 0:
        b /= 2
    while b % 5 == 0:
        b /= 5

    return 1 if b == 1 else 2