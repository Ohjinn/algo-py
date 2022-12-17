def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return True
    return False


solution([1, 2, 3])