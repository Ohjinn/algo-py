def solution(array):
    answer = ''.join(map(str, array))
    return answer.count('7')


print(solution([7, 77, 17]))
