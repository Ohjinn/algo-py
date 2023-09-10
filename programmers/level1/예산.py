def solution(d, budget):
    sum, answer = 0, 0
    d.sort()
    for i in d:
        sum += i
        if sum <= budget:
            answer += 1
    return answer


print(solution([1, 3, 2, 5, 4], 9))
