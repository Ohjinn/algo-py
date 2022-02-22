N = int(input())
M = int(input())

graph = [[0] * N for i in range(N)]
visit = [0 for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

cnt = 0

def dfs(x):
    visit[x] = 1
    for i in range(N):
        if graph[x][i] == 1 and visit[i] == 0:
            dfs(i)

dfs(0)
for i in range(1, N):
    if visit[i] == 1:
        cnt += 1
print(cnt)