# 이항계수는 경우의 수를 계산할 때 쓰는 것으로 nCk를 의미
# nCk -> factorial(n) // (factorial(k)*factorial(n-k))
import sys


def factorial_recursion(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# or math의 factorial을 이용할 수도 있다.


n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))
