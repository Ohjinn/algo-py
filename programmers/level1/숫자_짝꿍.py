def solution(X, Y):
    answer = ''
    x_dict = {n:0 for n in range(10)}
    y_dict = {n:0 for n in range(10)}

    for x in X:
        x_dict[int(x)] += 1

    for y in Y:
        y_dict[int(y)] += 1

    for i in range(9, -1, -1):
        answer += str(i) * min(x_dict[i], y_dict[i])
        # x = x_dict[str(i)]
        # y = y_dict[str(i)]
        # if x > 0 and y > 0:
        #     for _ in range(min(x, y)):
        #         if answer != '0':
        #             answer += str(i)
    if answer == '':
        answer = '-1'
    elif int(answer) == 0:
        answer = '0'
    return answer



print(solution("100", "203045"))
