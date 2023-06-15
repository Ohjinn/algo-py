import sys
input = sys.stdin.readline


def format_printer(size, number, times, print_result):
    """
    :param size: print 할 사이즈(초기 입력)
    :param number: print 할 숫자(초기 입력)
    :param times: 현재 반복 횟수(세로 값)
    :param print_result: 출력 할 최종 배열
    """
    temp_print = ''
    for i, value in enumerate(number):
        first, middle, last = 0, size + 1, (2 * size) + 2
        if value == '0':
            if times == first or times == last:
                temp_print = ' ' + '-' * size + ' '
            elif times == middle:
                temp_print = ' ' * (size + 2)
            else:
                temp_print = '|' + ' ' * size + '|'
        elif value == '1':
            if times == first or times == last or times == middle:
                temp_print = ' ' * (size + 2)
            else:
                temp_print = ' ' * (size + 1) + '|'
        elif value == '2':
            if times == first or times == last or times == middle:
                temp_print = ' ' + '-' * size + ' '
            elif first < times < middle:
                temp_print = ' ' * (size + 1) + '|'
            elif middle < times < last:
                temp_print = '|' + ' ' * (size + 1)
        elif value == '3':
            if times == first or times == last or times == middle:
                temp_print = ' ' + '-' * size + ' '
            else:
                temp_print = ' ' * (size + 1) + '|'
        elif value == '4':
            if times == first or times == last:
                temp_print = ' ' * (size + 2)
            elif first < times < middle:
                temp_print = '|' + ' ' * size + '|'
            elif middle < times < last:
                temp_print = ' ' * (size + 1) + '|'
            elif times == middle:
                temp_print = ' ' + '-' * size + ' '
        elif value == '5':
            if times == first or times == last or times == middle:
                temp_print = ' ' + '-' * size + ' '
            elif first < times < middle:
                temp_print = '|' + ' ' * (size + 1)
            elif middle < times < last:
                temp_print = ' ' * (size + 1) + '|'
        elif value == '6':
            if times == first or times == last or times == middle:
                temp_print = ' ' + '-' * size + ' '
            elif first < times < middle:
                temp_print = '|' + ' ' * (size + 1)
            elif middle < times < last:
                temp_print = '|' + ' ' * size + '|'
        elif value == '7':
            if times == first:
                temp_print = ' ' + '-' * size + ' '
            elif times == middle or times == last:
                temp_print = ' ' * (size + 2)
            else:
                temp_print = ' ' * (size + 1) + '|'
        elif value == '8':
            if times == first or times == last or times == middle:
                temp_print = ' ' + '-' * size + ' '
            else:
                temp_print = '|' + ' ' * size + '|'
        elif value == '9':
            if times == first or times == last or times == middle:
                temp_print = ' ' + '-' * size + ' '
            elif first < times < middle:
                temp_print = '|' + ' ' * size + '|'
            elif middle < times < last:
                temp_print = ' ' * (size + 1) + '|'

        # 출력 결과를 배열에 저장
        print_result[times] += temp_print + ' '
        temp_print = ''


s, n = map(str, input().split())
s = int(s)
content = [[] for i in range((2 * s) + 3)]

for i in range((2 * s) + 3):
    format_printer(s, n, i, content)

for i in content:
    for j in i:
        print(j, end='')
    print()