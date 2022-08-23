def solution(nums):
    answer = 0
    heap = []
    # 중복제거
    for i in nums:
        if i not in heap:
            heap.append(i)

    # 최대 갯수 입력
    answer = len(nums) / 2
    print(answer)
    print(len(heap))
    if answer > len(heap):
        answer = len(heap)

    return answer