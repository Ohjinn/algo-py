def solution(dots):
    dots.sort()

    x = abs(dots[0][0] - dots[2][0])
    y = abs(dots[0][1] - dots[1][1])

    return x * y
# 아.

solution([[-1, -1], [1, 1], [1, -1], [-1, 1]])
