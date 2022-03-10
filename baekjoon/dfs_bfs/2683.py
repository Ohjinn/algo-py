from collections import deque
import sys

input = sys.stdin.readline

m, n, k = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

square = [[0] * n for i in range(m)]
printList = []


def bfs(x, y):
    square[y][x] = 1
    global count
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if square[ny][nx] == 0:
                square[ny][nx] = 1
                queue.append((nx, ny))
                count += 1


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            square[i][j] = 1

for i in range(m):
    for j in range(n):
        if square[i][j] == 0:
            count = 1
            bfs(j, i)
            printList.append(count)

print(len(printList))
printList.sort()
for i in printList:
    print(i, end=' ')






