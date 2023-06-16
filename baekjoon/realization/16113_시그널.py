import sys
input = sys.stdin.readline


def identify_number(whole_digit, current_index, last_index):
    check_1 = True
    for i in range(2):
        for j in range(5):
            if i == 0 and whole_digit[j][current_index] == '.':
                check_1 = False
            if current_index + 1 < last_index and i == 1 and whole_digit[j][current_index + 1] == '#':
                check_1 = False
    if check_1:
        return '1'

    num = ['' for i in range(10)]
    num[0] = "######...######"
    num[2] = "#.####.#.####.#"
    num[3] = "#.#.##.#.######"
    num[4] = "###....#..#####"
    num[5] = "###.##.#.##.###"
    num[6] = "######.#.##.###"
    num[7] = "#....#....#####"
    num[8] = "######.#.######"
    num[9] = "###.##.#.######"

    target_number = ''
    for i in range(current_index, current_index + 3):
        for j in range(5):
            target_number += whole_digit[j][i]

    for i in range(len(num)):
        if target_number == num[i]:
            return str(i)


def check_exist(whole_digit, current_index, last_index):
    for j in range(5):
        if whole_digit[j][current_index] == '#':
            return True
    return False


def flow(whole_digit, array_element_length):
    result_number = ''

    i = 0
    while i < array_element_length:
        if check_exist(whole_digit, i, array_element_length):
            number = identify_number(whole_digit, i, array_element_length)
            if number != '1':
                i += 2
            result_number += number
        i += 1
    return result_number


total_length = input()
a = input()
chunk_length = len(a) // 5
a = [a[i:i + chunk_length] for i in range(0, len(a) - 1, chunk_length)]
print(flow(a, chunk_length))
