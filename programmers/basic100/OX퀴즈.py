def solution(quiz):
    answer = []
    for formula in quiz:
        values = formula.split()
        if values[1] == '+':
            if int(values[0]) + int(values[2]) == int(values[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif values[1] == '-':
            if int(values[0]) - int(values[2]) == int(values[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
