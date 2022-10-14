import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    number_of_scores = int(input())
    scores = list(map(int, input().split()))

    avg = sum(scores) / number_of_scores

    over_avg = 0
    for check in scores:
        if check >= avg:
            over_avg += 1
    print(over_avg, "/", number_of_scores, sep='')