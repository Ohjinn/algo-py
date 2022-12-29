import itertools


def solution(dots):
    answer = 0
    two_of_list = list(itertools.combinations(dots, 2))
    for i in range(3):
        if grade(two_of_list[i]) == grade(two_of_list[5 - i]):
            answer = 1
    return answer


def grade(points):
    return (points[0][1] - points[1][1]) / (points[1][0] - points[0][0])


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
