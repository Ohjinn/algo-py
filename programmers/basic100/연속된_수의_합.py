def solution(num, total):
    answer = []
    for i in range(-total - 100, total + 100):
        if len(answer) == num:
            answer.pop(0)
            answer.append(i)
        else:
            answer.append(i)

        if sum(answer) == total:
            return answer


print(solution(3, 0))
