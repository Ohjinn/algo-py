import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]

for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]

    bugs = 0
    queue = deque()

    for _ in range(K):
        a, b = map(int, input().split())
        queue.append((a, b))
        ground[b][a] = 1

    print(ground)
    print(queue)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0 or dx >= M or dy < 0 or dx >= N:
                continue

            if ground[dx][dy] == 0:
                continue

            if ground[dx][dy] == 1:
                ground[x][y] = 0

        bugs += 1
    print(bugs)
