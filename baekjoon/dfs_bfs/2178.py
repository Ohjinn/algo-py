from collections import deque

X, Y = map(int, input().split())
graph = []

for _ in range(X):
    graph.append(list(map(int, input())))


def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[X - 1][Y - 1]

print(bfs(0, 0))