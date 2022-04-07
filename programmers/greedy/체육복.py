def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    print(reserve_set)
    print(lost_set)

    for reserve_person in reserve_set:
        if reserve_person - 1 in lost_set:
            lost_set.remove(reserve_person - 1)
        elif reserve_person + 1 in lost_set:
            lost_set.remove(reserve_person + 1)

    return n - len(lost_set)

print(solution(9, [5, 6, 8, 1, 2], [2, 3, 1, 4, 8, 9]))

