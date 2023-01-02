from itertools import permutations
# def solution(babbling):
#     answer = 0
#     possible_answers = ['aya', 'ye', 'woo', 'ma']
#
#     for target_word in babbling:
#         print('target_word is ', target_word)
#         replaced_word = target_word
#         for possible_answer in possible_answers:
#             replaced_word = replaced_word.replace(possible_answer, '', 1)
#         print('replaced_word is ', replaced_word)
#         if not replaced_word:
#             answer += 1
#             break
#
#     return answer
#
#

def solution(babbling):
    answer = 0
    possible_answers = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        for possible_answer in possible_answers:
            word = word.replace(possible_answer, ' ', 1)

        if len(word.replace(' ', '')) == 0:
            answer += 1
    return answer


print(solution(['ayaye', 'uuuma', 'ye', 'yemawoo', 'ayaa']))
