def solution(numlist, n):
    answer = []
    for i in numlist:
        answer.append((i, abs(n - i)))

    answer = sorted(answer, key=lambda x: (x[1], -x[0]))
    return [x[0] for x in answer]


def solution2(numlist, n):
    return sorted(numlist, key=lambda x: [abs(x-n), -x])


print(solution([10000,20,36,47,40,6,10,7000], 30))
