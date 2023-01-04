def solution(chicken):
    answer = 0
    while chicken > 1:
        chicken /= 10
        answer += chicken
    return int(answer)

print(solution(1081))
