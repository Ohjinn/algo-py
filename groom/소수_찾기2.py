import sys
input = sys.stdin.readline


def prime(n):
    check = [True] * (n + 1)

    m = int(n ** .5)
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i + i, n + 1, i):
                check[j] = False

    return [i for i in range(2, n + 1) if check[i]]


n = int(input())
p = prime(n)

a = list(map(int, input().split()))
res = 0

for i in p:
    res += a[i - 1]

print(res)