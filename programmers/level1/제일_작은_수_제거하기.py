def solution(arr):
    lowest_num = min(arr)
    for i in arr:
        if i == lowest_num:
            arr.remove(lowest_num)
    if len(arr) == 0:
        return [-1]
    return arr

print(solution([4, 3, 2, 1]))
