from itertools import permutations


def dfs(k, dungeons, visited, cnt, answer):
    print(visited)
    for i in range(len(dungeons)):
        if visited[i] != 1 and dungeons[i][0] <= k:
            visited[i] = 1
            answer = dfs(k - dungeons[i][1], dungeons, visited, cnt + 1, answer)
            visited[i] = 0

    answer = max(answer, cnt)
    return answer


# dfs 이용
def solution(k, dungeons):
    visited = [0 for i in range(len(dungeons))]

    answer = dfs(k, dungeons, visited, 0, 0)
    return answer


# permutation 이용
def solution_with_permutation(k, dungeons):
    answer = -1
    n = len(dungeons)

    for permutation in list(permutations(range(0, n), n)):
        cnt = 0
        temp_k = k
        for i in permutation:
            if temp_k >= dungeons[i][0]:
                temp_k -= dungeons[i][1]
                cnt += 1
        answer = max(answer, cnt)
    return answer


# print(solution(80, [[80, 20], [50, 40], [30, 10]]))
print(solution_with_permutation(80, [[80, 20], [50, 40], [30, 10]]))
