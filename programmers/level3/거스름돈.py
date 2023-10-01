def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for price in range(m, n + 1):
            dp[price] += dp[price - m]

    return dp[-1] % 10000000007


print(solution(5, [1, 2, 5]))
