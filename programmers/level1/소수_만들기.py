from itertools import combinations


def solution(nums):
    combination = combinations(nums, 3)
    answer = len(list(combination))

    for i in combination:
        for j in range(2, sum(i) + 1):
            if sum(i) % j != 0:
                answer -= 1
                break
    return answer


print(solution([1, 2, 3, 4]))
