import sys

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

dp = [[0, 0] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [1, 2]
dp[4] = [2, 3]

for i in range(5, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for i in nums:
    print(dp[i][0], end=' ')
    print(dp[i][1])

