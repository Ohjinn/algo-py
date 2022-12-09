def solution(emergency):
    answer = []
    ordered_priority = sorted(emergency, reverse=True)
    for i in emergency:
        for index, j in enumerate(ordered_priority):
            if i == j:
                answer.append(index + 1)
    return answer

print(solution([3, 76, 24]))