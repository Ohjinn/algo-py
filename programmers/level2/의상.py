def solution(clothes):
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