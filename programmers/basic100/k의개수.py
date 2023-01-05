def solution(i, j, k):
    answer = 0
    for count in range(i, j + 1):
        answer += str(count).count(str(k))
    return answer

print(solution(1, 13, 1))