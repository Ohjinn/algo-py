def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** (1 / 2)) + 1):
            if j * j == i:
                count += 1
            elif i % j == 0:
                count += 2
        if count > limit:
            answer += power
        else:
            answer += count
    return answer


print(solution(5, 3, 2))
