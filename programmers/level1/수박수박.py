def solution(n):
    answer = ''
    answer = (n // 2 + 1) * '수박'

    return answer[:n]


print(solution(3))
