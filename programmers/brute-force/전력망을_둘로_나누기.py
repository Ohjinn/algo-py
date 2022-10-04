from collections import deque


def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    visited[start] = True
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if not visited[i]:
                result += 1
                queue.append(i)
                visited[i] = True
    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)

    # print(graph)
    for start, unvisited in wires:
        visited = [False] * (n + 1)
        visited[unvisited] = True
        result = bfs(start, visited, graph)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n-result))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [9, 7]]))
