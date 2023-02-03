def solution(a, b, n):
    answer, remained = 0, 0
    while n >= a:
        remained = n % a
        n = n // a * b
        answer += n
        n += remained

    return answer


print(solution(2, 1, 20))
