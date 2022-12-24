def solution(polynomial):
    x = 0
    n = 0
    split_poly = polynomial.split()
    for i in split_poly:
        if i == '+':
            continue
        if i[-1] == 'x':
            if len(i) == 1:
                x += 1
            else:
                x += int(i[0:-1])
        else:
            n += int(i)

    if x == 1:
        x = 'x'
    elif x != 0:
        x = str(x) + 'x'
    else:
        x = ''
    if n and x:
        n = ' + ' + str(n)
    elif n:
        n = n
    else:
        n = ''
    return x + str(n)


print(solution("22"))
