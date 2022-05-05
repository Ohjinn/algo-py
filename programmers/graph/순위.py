# 접근방식이 잘못됐다.
# def solution(n, results):
#     answer = 0
#
#     graph = [[0] * (n + 1) for _ in range(n + 1)]
#     ranking = []
#
#     for result in results:
#
#         graph[result[0]][result[1]] = 1
#         graph[result[1]][result[0]] = -1
#
#     for i in range(1, n + 1):
#         ck = 0
#         rank_sum = 0
#         for j in range(1, n + 1):
#             if graph[i][j] != 0:
#                 ck += 1
#                 rank_sum += graph[i][j]
#         if ck == n - 1:
#
#     return answer

def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        matrix[win - 1][lose - 1] = True
        matrix[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[j][i] == None:
                    continue

                if matrix[j][i] == matrix[i][k]:
                    matrix[j][k] = matrix[j][i]
                    matrix[k][j] = not matrix[j][i]

    answer = 0
    for i in range(n):
        if None in matrix[i][:i] + matrix[i][i + 1:]:
            continue
        answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

