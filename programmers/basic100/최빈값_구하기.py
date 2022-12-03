# def solution(array):
#     # check = [0 for i in range(len(array))]
#     if len(array) == 1:
#         return 1
#     numbers = {}
#     for value in array:
#         value_count = numbers.get(value, 0)
#         numbers[value] = value_count + 1
#
#     numbers = dict(sorted(numbers.items(), key=lambda item: item[1], reverse=True))
#     max_value, count = 0, 0
#     print(numbers)
#     for key, value in numbers.items():
#         if max_value == value:
#             return -1
#         elif count >= 1:
#             return max_value
#         max_value = key
#         count += 1
from collections import Counter

def solution(array):
    cnt = Counter(array)
    ordered = cnt.most_common()
    maximum, maximum_count = ordered[0][0], ordered[0][1]
    count = 0
    for num in ordered:
        if count == 0:
            count += 1
            continue
        if num[1] == maximum_count:
            return -1
    return maximum


print(solution([1, 2, 2, 5, 5, 5, 4]))
