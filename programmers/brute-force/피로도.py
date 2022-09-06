def dfs(k, dungeons, visited, cnt, answer):
    for i in range(len(dungeons)):
        if visited[i] != 1 and dungeons[i][0] <= k:
            visited[i] = 1
            answer = dfs(k - dungeons[i][1], dungeons, visited, cnt + 1, answer)
            visited[i] = 0

    answer = max(answer, cnt)
    return answer


def solution(k, dungeons):
    visited = [0 for i in range(len(dungeons))]

    answer = dfs(k, dungeons, visited, 0, 0)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
