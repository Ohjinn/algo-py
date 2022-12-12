def solution(num_list, n):
    list_max = len(num_list)
    answer = []
    temp_list = []
    count = 0
    for i in num_list:
        temp_list.append(i)
        count += 1
        if count == n:
            answer.append(temp_list)
            temp_list = []
            count = 0

    return answer


def solution2(num_list, n):
    answer, i = [], 0
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer


print(solution2([1, 2, 3, 4, 5, 6, 7, 8], 2))
