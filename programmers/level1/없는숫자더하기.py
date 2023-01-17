def solution(numbers):
    zero_to_nine = set([i for i in range(10)])
    for number in numbers:
        zero_to_nine.remove(number)

    return sum(zero_to_nine)


def solution2(numbers):
    return sum(set(range(10)) - set(numbers))


print(solution2([1, 2, 3, 4, 6, 7, 8, 0]))
