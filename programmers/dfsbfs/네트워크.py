# from collections import deque
#
# def BFS(n, a, b, ck, computers):
#     queue = deque()
#     queue.append([a, b])
#     while queue:
#         i = queue.popleft()[0]
#         j = queue.popleft()[1]
#         ck[i][j] = 1
#         ck[j][i] = 1
#         for c in range(n):
#
#
# def solution(n, computers):
#     answer = 0
#     ck = [[0] * n for _ in range(n)]
#     for i in range(n):
#         ck[i][i] = 1
#
#     for i in range(n):
#         for j in range(n):
#             if not ck[i][j]:
#                 BFS(n, i, j, ck, computers)
#
#     return answer

from collections import deque


def solution(n, computers):
    def BFS(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] and not visited[a]:
                    q.append(a)

    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

