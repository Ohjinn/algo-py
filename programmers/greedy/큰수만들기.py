# def solution(number, k):
#     answer = ''
#     biggest = list(map(int, number[k:].split()))
#     print(biggest)
#     for i in range(k - 1, -1, -1):
#         if biggest[0] < number[i]:
#             biggest.insert(0, number[i])
#             mini = 9
#             idx = 0
#             for k, j in enumerate(biggest):
#                 if mini < j:
#                     mini = j
#                     idx = k
#             del biggest[idx]
#     print(biggest)
#     return answer

def solution(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])


print(solution("1924", 0))

