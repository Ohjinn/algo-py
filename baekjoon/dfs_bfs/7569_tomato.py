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
            near_x = x + dx[i]
            near_y = y + dy[i]
            near_z = z + dz[i]

            if 0 <= near_x < N and 0 <= near_y < M and 0 <= near_z < H:
                if basket[near_z][near_x][near_y] == 0:
                    basket[near_z][near_x][near_y] = basket[z][x][y] + 1
                    queue.append([near_z, near_x, near_y])

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
    result = -1
elif result == 1:
    result = 0
else:
    result -= 1

print(result)