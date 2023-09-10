from collections import deque
import re


# 실수로 앞쪽 기준으로 작성
def solution(dartResult):
    answer = 0

    # flag가 2면 2배, -1이면 뺄셈
    flag = deque([])

    #  숫자를 기준으로 split
    split_words = re.findall(r'\d*\w\W*', dartResult)

    for turn in split_words:
        # 리스트에 있던 스타상, 아차상 곱
        turn_flag = 1
        if len(flag) != 0:
            turn_flag *= int(flag.popleft())

        # SDT를 기준으로 split
        turn_list = re.split(r'([SDT])', turn)

        # 다음 차례의 스타상, 아차상 이전에 미리 계산, 리스트에 추가
        if turn_list[2]:
            if turn_list[2] == '*':
                flag.append(2)
                turn_flag *= 2
            else:
                flag.append(-1)
                turn_flag *= -1

        # 이번 차례 점수 저장
        this_num = int(turn_list[0])

        # 이번 차례 차수 계산
        if turn_list == 'D':
            this_num **= 2
        elif turn_list == 'T':
            this_num **= 3

        answer += turn_flag * this_num
    return answer


print(solution("1S2D*3T"))
