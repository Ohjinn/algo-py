import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

global number
number = 0


def dfs(graph, visited, current):
    global number
    number += 1
    visited[current] = number
    for i in graph[current]:
        if visited[i] == 0:
            dfs(graph, visited, i)


n, m, r = map(int, input().split())

visited = [0 for i in range(n + 1)]
graph = [[] for i in range(n + 1)]

for _ in range(m):
    x, y, = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n):
    graph[i].sort()

dfs(graph, visited, r)

for i in range(1, n + 1):
    print(visited[i])