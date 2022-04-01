from itertools import permutations
import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    p = []
    result = []

    for i in range(1, len(numbers) + 1):
        p.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in p]

    for i in set(result):
        if is_prime(i):
            answer += 1

    return answer


print(solution('17'))
