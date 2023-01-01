def solution(score):
    avg = [(x[0] + x[1]) / 2 for x in score]
    sorted_avg = sorted(avg, reverse=True)
    return [sorted_avg.index(x) + 1 for x in avg]


print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
