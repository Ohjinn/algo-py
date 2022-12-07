def solution(n):
    answer = [i * 2 for i in range((int)(n / 2) + 1)]
    return sum(answer)


print(solution(10))
