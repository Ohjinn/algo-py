def solution(absolutes, signs):
    answer = 0
    for idx in range(len(absolutes)):
        if not signs[idx]:
            answer -= absolutes[idx]
        else:
            answer += absolutes[idx]
    return answer


print(solution([4, 7, 12], [True, False, True]))
