def solution(array):
    array.sort()
    mid = len(array) // 2
    return array[mid]

print(solution([1, 2, 7, 10, 11]))