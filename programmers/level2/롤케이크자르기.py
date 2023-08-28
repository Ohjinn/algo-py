def solution(topping):
    answer = 0
    chul_dict = {}
    bro_set = set()

    # if len(set(topping)) % 2 == 1:
    #     return 0

    for i in topping:
        if i in chul_dict:
            chul_dict[i] += 1
        else:
            chul_dict[i] = 1

    for i in topping:
        if chul_dict[i] == 1:
            chul_dict.pop(i)
        else:
            chul_dict[i] -= 1
        bro_set.add(i)

        if len(chul_dict) == len(bro_set):
            answer += 1

    return answer