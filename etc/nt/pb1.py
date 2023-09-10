def solution(s, N):
    answer = 0
    dupl = set()

    if len(s) < N:
        return -1

    for i in range(len(s)):
        dupl = set()
        for j in range(N):
            print(len(dupl))
            if len(dupl) == N:
                print('check', s[i:i + N])
                if answer < s[i:i+N]:
                    answer = s[i:i+N]
            elif (i + j) >= len(s) or s[i + j] in dupl:
                break
            elif int(s[i + j]) > N:
                break
            else:
                dupl.add(s[i + j])
                print('i = ', i, 'j = ', j, 'dupl = ', dupl)


    return answer

print(solution("1451232125", 2))