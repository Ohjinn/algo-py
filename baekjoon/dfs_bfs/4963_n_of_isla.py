import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(n, m):
    print('call')
    print(n, m)
    for i in range(8):
        nx = n + dx[i]
        ny = m + dy[i]
        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            continue

        if Map[ny][nx] == 1:
            Map[m][n] = 0
            dfs(nx, ny)
        Map[m][n] = 0


while True:
    w, h = map(int, input().split())
    count = 0
    if w == 0 or h == 0:
        break

    Map = [list(map(int, input().split())) for i in range(h)]
    queue = deque()

    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                queue.append([i, j])

    while queue:
        print(queue)
        print(Map)
        n, m = queue.popleft()
        if Map[m][n] == 1:
            print('isit1?')
            dfs(n, m)

            count += 1

    print(count)


