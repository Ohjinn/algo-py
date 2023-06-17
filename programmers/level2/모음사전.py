from itertools import product


def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    tmp = []
    for i in range(1, 6):
        for j in product(words, repeat = i):
            # print(j)
            tmp.append(''.join(j))
    tmp.sort()
    print(tmp)
    return tmp.index(word) + 1


print(solution("AAAAE"))
