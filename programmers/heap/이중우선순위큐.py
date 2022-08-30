import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    # 최대, 최소 힙 두개를 이용, 큰 수를 뽑을 때는 최대힙에서 뽑으면 log n 의 속도로 정렬된 최댓값을 뽑을 수 있다.
    # 이를 최소힙 리스트에서 remove 해준다.

    for operation in operations:
        op_list = operation.split()
        if op_list[0] == 'I':
            heapq.heappush(min_heap, int(op_list[1]))
            heapq.heappush(max_heap, (-int(op_list[1]), int(op_list[1])))
        elif len(min_heap) == 0:
            continue
        elif op_list[0] == 'D' and op_list[1] == '1':
            max_value = heapq.heappop(max_heap)[1]
            min_heap.remove(max_value)
        elif op_list[0] == 'D' and op_list[1] == '-1':
            min_value = heapq.heappop(min_heap)
            max_heap.remove((-int(min_value), min_value))
    if min_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    return [0, 0]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))
