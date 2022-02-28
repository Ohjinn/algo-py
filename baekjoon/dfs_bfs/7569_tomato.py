import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
basket = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if basket[i][j][k] == 1:
                queue.append([i, j, k])


def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if basket[nz][nx][ny] == 0:
                    basket[nz][nx][ny] = basket[z][x][y] + 1
                    queue.append([nz, nx, ny])

bfs()
print(basket)
check = 1
result = -1

for i in basket:
    for j in i:
        for k in j:
            if k == 0:
                check = 0

            result = max(result, k)



if check == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)