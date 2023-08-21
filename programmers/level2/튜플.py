def solution(s):
    answer = []
    by_list = []

    s = s.replace('},{', ' ')
    s = s.replace('{{', '')
    s = s.replace('}}', '')
    s = s.split(' ')

    for i in s:
        by_list.append(i.split(','))

    for i in sorted(by_list, key=len):
        for j in i:
            if j not in answer:
                answer.append(int(j))
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
