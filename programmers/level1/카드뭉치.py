def solution(cards1, cards2, goal):
    answer = ''
    a, b = 0, 0
    for i in range(len(goal)):
        if a < len(cards1) and goal[i] == cards1[a] and a <= len(goal):
            a += 1
        elif b < len(cards2) and goal[i] == cards2[b] and b <= len(goal):
            b += 1
        else:
            return 'NO'
    return 'YES'


print(solution(["i", "water", "drink"],	["want", "to"],	["i", "want", "to", "drink", "water"]))
