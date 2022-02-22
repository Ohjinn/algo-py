import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)

