import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for i in range(n + 1)]
arr = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    arr[i] = int(input())

if n < 4:
    if n == 1:
        print(arr[1])
        exit()
    elif n == 2:
        print(arr[1] + arr[2])
        exit()
    elif n == 3:
        print(max(arr[1] + arr[3], arr[2] + arr[3], dp[2]))
        exit()

dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[2] + arr[3], arr[1] + arr[3], dp[2])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])

print(dp)