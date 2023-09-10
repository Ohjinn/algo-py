def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        num_of_factor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                num_of_factor += 1
        if num_of_factor % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

print(solution(13, 17))