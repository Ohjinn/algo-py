from itertools import combinations


def solution(numbers):
    answer = []
    combination = list(combinations(numbers, 2))

    for two_numbers in combination:
        if sum(two_numbers) not in answer:
            answer.append(sum(two_numbers))

    return sorted(answer)


print(solution([2,1,3,4,1]))
