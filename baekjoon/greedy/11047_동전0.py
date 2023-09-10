import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
result = 0
for i in range(n):
    coins.append(int(input()))


for i in range(n - 1, -1, -1):
    while coins[i] <= k:
        k -= coins[i]
        result += 1

    if k == 0:
        break

print(result)