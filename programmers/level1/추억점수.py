def solution(name, yearning, photo):
    answer = []
    name_yearning_dict = dict(zip(name, yearning))
    for names in photo:
        sum_of_list = 0
        for name in names:
            sum_of_list += name_yearning_dict.get(name, 0)
        answer.append(sum_of_list)
    return answer

