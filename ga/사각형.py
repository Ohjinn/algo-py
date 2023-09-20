def square_sum(n):
    if n > 1:
        return n * n + square_sum(n - 1)
    else:
        return 1


def solution(n):
    answer = 0
    if n > 3:
        answer = square_sum(n - 1) + square_sum(n - 2) + square_sum(n - 3)
    else:
        answer = square_sum(n - 1) + square_sum(n - 2)
    return answer

print(solution(5))