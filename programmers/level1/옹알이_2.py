def solution(babbling):
    answer = 0
    possible_answers = ['aya', 'ye', 'woo', 'ma']
    for babble in babbling:
        for possible_answer in possible_answers:
            if possible_answer * 2 not in babble:
                babble = babble.replace(possible_answer, ' ')

        if len(babble.replace(' ', '')) == 0:
            answer += 1
    return answer


solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
