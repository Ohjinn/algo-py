def solution(arr):
    answer = []
    temp = -1
    for i in arr:
        if temp == i:
            continue
        else:
            temp = i
            answer.append(temp)
    return answer

print(solution([4,4,4,3,3]))