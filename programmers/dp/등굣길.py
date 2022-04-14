def solution(m, n, puddles):
    answer = 0
    dp = [[1] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 0
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

    return answer

solution(4, 3, [[2, 2]])

