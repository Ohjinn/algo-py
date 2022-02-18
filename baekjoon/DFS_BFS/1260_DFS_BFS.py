import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())


def bfs(edges, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for e in edges[now]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True