import sys
input = sys.stdin.readline

n, m = map(int, input().split())
routes = []
visited = [0] * (n + 1)

def dfs():
    if len(routes) == m:
        print(' '.join(map(str, routes)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            routes.append(i)
            dfs()
            routes.pop()
            visited[i] = False

dfs()