N = int(input())

stair = [0 for i in range(301)]
dp = [0 for i in range(301)]


def max_value(a, b):
    return a if a > b else b


for i in range(N):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = max_value(stair[0] + stair[1], stair[1])
dp[2] = max_value(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, N):
    dp[i] = max_value(dp[i - 2] + stair[i], stair[i - 1] + stair[i] + dp[i - 3])

print(dp[N-1])