
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start + 1, end

    while left <= right:
        # pivot보다 작은 데이터를 찾을때까지
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 큰 데이터를 찾을때까지
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 교차하는경우
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 교차하지 않는 경우
        else:
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def solution(unsorted):
    quick_sort(unsorted, 0, len(unsorted) - 1)
    print(unsorted)


solution([4, 1, 2, 7, 9, 5, 6, 8, 3, 9])


# 출처 이코테 인듯