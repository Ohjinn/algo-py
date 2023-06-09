def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(1, len(score) // m + 1):
        answer += (score[i * m - 1] * m)
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
