def solution(n, arr1, arr2):
    answer = [' ' * n for i in range(n)]
    for i in range(len(arr1)):
        bin_len = n - len(bin(arr1[i] | arr2[i])[2:])
        answer[i] = ' ' * bin_len + bin(arr1[i] | arr2[i])[2:]
        answer[i] = answer[i].replace('1', '#')
        answer[i] = answer[i].replace('0', ' ')
    return answer


print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
