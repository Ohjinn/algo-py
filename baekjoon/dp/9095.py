import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

add = [0, 1, 2, 4]

for i in range(4, 12):
    add.append(sum(add[i-3:i]))


for i in arr:
    print(add[i])