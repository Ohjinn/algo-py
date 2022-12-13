def solution(box, n):
    x, y, z = box[0], box[1], box[2]
    return (x // n) * (y // n) * (z // n)
