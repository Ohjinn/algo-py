def solution(n, lost, reserve):
    answer = n - len(lost)

    for reserved in reserve:
        if reserved - 1 in lost:
            answer += 1
            reserve.remove(reserved - 1)
        elif reserved + 1 in lost:
            answer += 1
            reserve.remove(reserved + 1)

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
