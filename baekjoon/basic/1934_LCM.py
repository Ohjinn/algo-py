import math

n = int(input())


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


for _ in range(n):
    num1, num2 = map(int, input().split())
    print(lcm(num1, num2))
