def solution(n):
    answer = []
    i = 0
    while (i * 2 + 1) <= n:
        answer.append(i * 2 + 1)
        i += 1
    return answer