def solution(common):
    if common[len(common) - 1] - common[len(common) - 2] == common[len(common) - 2] - common[len(common) - 3]:
        return common[len(common) - 1] + (common[len(common) - 1] - common[len(common) - 2])
    else:
        return common[len(common) - 1] * (common[len(common) - 2] // common[len(common) - 1])

print(solution([1, 2, 3, 4]))