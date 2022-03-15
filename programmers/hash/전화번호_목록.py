import sys

input = sys.stdin.readline
answer = True
phone_book = list(input().split())

sorted_book = sorted(phone_book)

# 시간초과
# for i in range(len(sorted_book)):
#     for j in range(i + 1, len(sorted_book)):
#         if sorted_book[j].startswith(sorted_book[i]):
#             answer = False
#             break

# 접두사라면 정렬했을 때 앞뒤에 위치한다.
for i in range(len(sorted_book)):
    if sorted_book[i + 1].startswith(sorted_book[i]):
        answer = False
        break

print(answer)
