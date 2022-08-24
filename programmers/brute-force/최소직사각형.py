def solution(sizes):
    answer = 0
    final_w = final_h = 0
    for i in sizes:
        w = max(i[0], i[1])
        h = min(i[0], i[1])
        final_w = max(final_w, w)
        final_h = max(final_h, h)
    return final_h * final_w


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))