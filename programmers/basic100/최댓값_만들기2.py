import itertools


def solution(numbers):
    negative, positive, max = [], [], 0
    for number in numbers:
        if number < 0:
            negative.append(number)
        else:
            positive.append(number)

    nega_combi = itertools.permutations(negative, 2)
    posi_combi = itertools.permutations(positive, 2)

    for i in nega_combi:
        if max < i[0] * i[1]:
            max = i[0] * i[1]
    for i in posi_combi:
        if max < i[0] * i[1]:
            max = i[0] * i[1]
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return max


def solution2(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])