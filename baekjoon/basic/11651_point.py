import sys
input = sys.stdin.readline #입력시간 줄이기 위함

n = int(input())

array = []

for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

array = sorted(array)

for y, x in array:
    print(x, y)

# 진짜 너무 양아치 파이썬이다.