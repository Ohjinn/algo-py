def solution(array, n):
    answer = 0
    subtracted_num = 100
    for num in array:
        if abs(n - num) <= subtracted_num:
            if abs(n - num) == subtracted_num:
                if num > answer:
                    continue
            subtracted_num = abs(n - num)
            answer = num

    return answer

print(solution([3, 10, 28], 20))