import heapq as hq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    arr = []
    # for row in jobs:
    #     hq.heappush(arr, [row[0], row[1]])

    while i < len(jobs):
        for row in jobs:
            if start < row[0] <= now:
               hq.heappush(arr, [row[1], row[0]])
        if len(arr) > 0:
            current = hq.heappop(arr)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))

