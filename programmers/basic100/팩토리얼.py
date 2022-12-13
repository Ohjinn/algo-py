def solution(n):
    counted_number = 1
    factorial_number = 1
    while factorial_number * counted_number <= n:
        factorial_number *= counted_number
        counted_number += 1

    return counted_number - 1


def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i - 1)


print(solution(3628800))
