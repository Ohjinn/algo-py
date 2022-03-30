def solution(answers):
    answer = []
    p1, p2, p3 = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n1, n2, n3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == p1[i % 5]:
            n1 += 1
        if answers[i] == p2[i % 8]:
            n2 += 1
        if answers[i] == p3[i % 10]:
            n3 += 1

    k = max(n1, n2, n3)

    if k == n1:
        answer.append(1)
    if k == n2:
        answer.append(2)
    if k == n3:
        answer.append(3)
    return answer


print(solution([1, 3, 2, 4, 2]))
