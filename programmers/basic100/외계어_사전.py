def solution(spell, dic):
    answer = 2
    for dic_word in dic:
        replaced = dic_word
        flag = True
        for alphabet in spell:
            if alphabet not in replaced:
                flag = False
            replaced = replaced.replace(alphabet, '', 1)
        if len(replaced) == 0 and flag:
            return 1
    return answer


print(solution(["s", "o", "m", "d"]	, ["moos", "dzx", "smm", "sunmmo", "som"]))