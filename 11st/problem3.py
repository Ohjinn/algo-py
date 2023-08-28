# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    cost = 0
    for target in range(0, len(S) - 1):
        if S[target] == S[target + 1]:
            cost += min(C[target], C[target + 1])

    return cost


print(solution('abccbd', [0, 1, 2, 3, 4, 5]))
