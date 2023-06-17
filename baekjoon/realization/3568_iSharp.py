import sys
input = sys.stdin.readline

variable_list = list(map(str, input().split()))

type = variable_list[0]
for i in range(1, len(variable_list)):
    print(type, end='')
    word = variable_list[i]
    word = word.strip(', ')
    word = word.strip(';')
    word = word.replace('[]', '][')

    for j in range(len(word)-1, 0, -1):
        alphabet = word[j]
        if not alphabet.isalpha():
            print(alphabet, end='')

    print('', end=' ')

    for j in range(0, len(word)):
        if word[j].isalpha():
            print(word[j], end='')

    print(';')