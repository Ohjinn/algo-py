import sys
from collections import deque

input = sys.stdin.readline

tests = int(input())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def case(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1))

    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            print(visit[x2][y2] - 1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue

            if visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))


for _ in range(tests):
    size = int(input())
    visit = [[0] * size for i in range(size)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    visit[x1][y1] = 1
    case(x1, y1, x2, y2)