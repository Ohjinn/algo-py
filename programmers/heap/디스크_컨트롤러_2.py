import heapq


# 다시 풀어도 못풀겠다.
def solution(jobs):
    answer, i, now = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # i가 전체 job의 갯수가 될 때 까지
        for job in jobs:
            # 요청 타이밍이 이전 작업의 시작 시간보다 후, 현재시간보다 작거나 같으면 최소 힙에 넣을 수 있다.
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        # 힙이 비어있지 않다면
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        # 비어있다면 시간 ++
        else:
            now += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))


# max_heap prac
def max_heap(jobs):
    answer = 0
    pr_heap = []
    for job in jobs:
        heapq.heappush(pr_heap, (-job, job))

    while pr_heap:
        print(heapq.heappop(pr_heap)[1])


# print(max_heap([1, 8, 7, 3, 6, 2]))
