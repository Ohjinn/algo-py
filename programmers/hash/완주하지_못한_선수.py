import sys

input = sys.stdin.readline

participant = list(input().split())
completion = list(input().split())

participant.sort()
completion.sort()
answer = ''

for i in range(len(completion)):
    if participant[i] != completion[i]:
        answer = participant[i]
        break
if answer == '':
    answer = participant[-1]

print(answer)