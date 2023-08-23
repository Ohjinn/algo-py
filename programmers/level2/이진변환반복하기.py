def solution(s):
    answer = []
    count, times = 0, 0
    while s != '1':
        result = binary_convert(s, count, times)
        s, count, times = result[0], result[1], result[2]
    return [times, count]


def binary_convert(num, count, times):
    count += num.count('0')
    num = num.replace('0', '')
    num = format(len(num), 'b')
    return [num, count, times + 1]

print(solution("110010101001"))