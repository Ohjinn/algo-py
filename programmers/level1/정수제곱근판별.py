def solution(n):
    square_root = n ** (1 / 2)
    if square_root - int(square_root) == 0:
        return (int(square_root) + 1) ** 2
    else:
        return -1


print(solution(121))
