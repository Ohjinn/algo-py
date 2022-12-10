import math
from functools import reduce


def solution(balls, share):
    answer = custom_factorial(balls) / (custom_factorial(balls - share) * custom_factorial(share))

    return answer


def solution2(balls, share):
    answer = math.factorial(balls) / (math.factorial(balls - share) * math.factorial(share))


# 런타임
def solution3(balls, share):
    answer = custom_factorial_with_reduce(balls) / (custom_factorial_with_reduce(balls - share) * custom_factorial_with_reduce(share))


def custom_factorial_with_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def custom_factorial(n):
    if n > 1:
        return n * custom_factorial(n - 1)
    else:
        return 1

