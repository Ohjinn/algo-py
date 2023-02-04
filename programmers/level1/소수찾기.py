from collections import deque


# 시간초과
def solution(n):
    results = deque([i for i in range(2, n + 1)])
    for i in range(2, int(n ** (1 / 2)) + 1):
        if i in results:
            for j in range(i + i, n + 1, i):
                if j in results:
                    print(j)
                    results.remove(j)
    return len(results)


def solution2(n):
    results = deque([1 for _ in range(n + 1)])
    for i in range(2, int(n ** (1 / 2)) + 1):
        if i in results:
            for j in range(i + i, n + 1, i):
                if j in results:
                    print(j)
                    results.remove(j)
    return len(results)



print(solution2(10))
