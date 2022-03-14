import sys

input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split()))
arr.sort()

sum = 0
wait = 0

for i in range(n):
    wait += arr[i]
    sum += wait

print(sum)
