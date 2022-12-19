def solution(my_string):
    queue = my_string.split()
    answer = int(queue.pop(0))
    for i in range(0, len(queue), 2):
        if queue[i] == '+':
            answer += int(queue[i + 1])
        else:
            answer -= int(queue[i + 1])

    return answer


print(solution("3 + 4 - 1 + 0 - 3"))
