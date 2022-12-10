def solution(rsp):
    answer = ''
    kind_of_rsp = {'2': '0', '0': '5', '5': '2'}
    for i in rsp:
        answer += kind_of_rsp[i]
    return answer