def solution(N, stages):
    # 답 계산을 위한 dictionary
    answer = {i:0 for i in range(1, N + 2)}
    # 통과한 플레이어를 계산하기 위한 list
    reached_people = [0 for i in range(1, N + 3)]

    # 스테이지에 도달한 사람 수와 통과한 사람 수 계산
    for i in stages:
        answer[i] += 1
        for j in range(1, i + 1):
            reached_people[j] += 1

    # 실패율 계산
    for stage in answer:
        if answer[stage] != 0:
            answer[stage] /= reached_people[stage]

    # 정렬
    answer.pop(N + 1)
    answer = sorted(answer.items(), key=lambda item: (-item[1], item[0]))
    return [i[0] for i in answer]


def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
