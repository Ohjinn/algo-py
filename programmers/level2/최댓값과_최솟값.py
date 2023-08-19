import sys
def solution(s):
    answer = ''
    min_int = sys.maxsize
    max_int = -sys.maxsize - 1
    for temp_int in s.split():
        i = int(temp_int)
        if max_int < i:
            max_int = i
        if min_int > i:
            min_int = i
    answer = str(min_int) + ' ' + str(max_int)
    return answer