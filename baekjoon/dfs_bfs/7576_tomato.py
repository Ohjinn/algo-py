import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
basket = [list(map(int, input().split())) for i in range(N)]
queue = deque()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if basket[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            near_x, near_y = x + dx[i], y + dy[i]
            if 0 <= near_x < N and 0 <= near_y < M:  # 배열 범위를 넘어가지 않고
                if basket[near_x][near_y] == 0:  # 탐색중인 칸의 값이 0이면
                    queue.append([near_x, near_y])  # 탐색 대상 큐에 넣는다.
                    basket[near_x][near_y] = basket[x][y] + 1  # 이전 칸 + 1로 익은 일자를 구한다


bfs()

check = 1
result = -1
for i in basket:
    for j in i:
        if j == 0:
            check = 0
        result = max(result, j)

if check == 0:
    result = -1
elif result == 1:
    result = 0
else:
    result -= 1

print(result)
