import sys
input = sys.stdin.readline

n = int(input())

check_string = input().strip()

temp = ''
cnt = 0
for i in check_string:
    if temp != i:
        cnt += 1
    temp = i

print(cnt)