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


# 그나마 빠름
def solution2(n):
    results = deque([1 for _ in range(n + 1)])
    for i in range(2, int(n ** (1 / 2)) + 1):
        if results[i] == 1:
            for j in range(i + i, n + 1, i):
                if results[j] == 1:
                    results[j] = 0
    return results.count(1) - 2


def solution3(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


print(solution2(5))
