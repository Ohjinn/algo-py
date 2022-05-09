def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]].append(cloth[0])
        else:
            dict[cloth[1]] = [cloth[0]]

    for value in dict.values():
        answer *= len(value)

    return answer - 1


def solution2(clothes):
    answer = 1
    cloth_dict = {}

    for _, cloth in clothes:
        if cloth not in cloth_dict:
            cloth_dict[cloth] = 2
        else:
            cloth_dict[cloth] += 1

    for num in cloth_dict.values():
        answer *= num

    return answer - 1


print(solution2([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

