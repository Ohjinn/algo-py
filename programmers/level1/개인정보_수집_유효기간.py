from datetime import datetime
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    today_datetime = datetime.strptime(today, "%Y.%m.%d")

    # 약관 dict
    for term in terms:

        term = term.split(' ')
        term_dict[term[0]] = int(term[1])

    # 개인정보 정리
    for index, privacy in enumerate(privacies):
        # 날짜와 약관 분리
        privacy = privacy.split(' ')
        # 날짜 연, 월, 일로 분리
        # date = privacy[0].split('.')

        date = datetime.strptime(privacy[0], "%Y.%m.%d")
        new_date = date + relativedelta(months=term_dict[privacy[1]], days=-1)
        if today_datetime > new_date:
            answer.append(index + 1)

        # 해당 날짜에 약관의 날짜 더함
        # for i in range(term_dict[privacy[1]]):
        #     while int(date[1]) < 13:
        #         date[0] += 1
        #         date[1] -= 12

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
