def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(int(total / 2)-1, 2, -1):
        if total % i == 0:
            if ((i * 2) + int((total/i) - 2) * 2) == brown:
                answer.append(i)
                answer.append(int(total/i))
                break
    return answer


print(solution(8, 1))

