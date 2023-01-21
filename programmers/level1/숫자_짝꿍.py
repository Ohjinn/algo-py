def solution(X, Y):
    result_arr = []
    for i in X:
        if i in Y:
            Y = Y.replace(i, '', 1)
            result_arr.append(i)
    result_arr.sort(reverse = True)
    answer = ''.join(result_arr)

    if len(answer) != 0 and int(answer) != 0:
        return answer
    elif int(answer) == 0:
        return '0'
    else:
        return '-1'


print(solution("100", "2345"))
