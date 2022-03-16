import sys

input = sys.stdin.readline


def solution(clothes):
    dict = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]].append(cloth[0])
        else:
            dict[cloth[1]] = [cloth[0]]

    for value in dict.values():
        answer *= (len(value) + 1)

    return answer - 1