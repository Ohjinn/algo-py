def solution(want, number, discount):
    answer = 0
    count_dict = dict(zip(want, number))
    for i, value in enumerate(discount):
        if sum(count_dict.values()) == 0:
            answer += 1
            for j in count_dict.values():
                if j != 0:
                    answer -= 1
        if i >= 10:
            if discount[i - 10] in count_dict:
                count_dict[discount[i - 10]] += 1
            if value in count_dict:
                count_dict[value] -= 1
        else:
            if value in count_dict:
                count_dict[value] -= 1

    return answer


from collections import Counter


def solution2(want, number, discount):
    best_day = 0
    want_number = dict(zip(want, number))
    # 언제 가입하면 좋을 지 확인
    for i in range(len(discount) - 10 + 1):
        # 동일할 경우 증가
        if want_number == Counter(discount[i:i + 10]):
            best_day += 1
    return best_day