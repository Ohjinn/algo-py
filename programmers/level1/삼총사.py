from itertools import combinations


def solution(number):
    answer = 0
    # permutations(array, n) => 원소의 종류가 같아도 순서가 다르면 다른 배열, 순열
    # combinations(array, n) => 원소의 종류가 같으면 순서가 달라도 같은 배열, 조합
    combinate = combinations(number, 3)

    for i in combinate:
        if sum(i) == 0:
            answer += 1
    return answer


print(solution([-2, 3, 0, 2, -5]))
