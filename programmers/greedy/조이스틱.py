def solution(name):
    answer = 0
    answer += len(name) - 1
    initial_word = ''
    cursor = 0
    for i in range(len(name)):
        initial_word += 'A'

    # for i, alpha in enumerate(name):
    print(initial_word[1])
    return answer

print(solution('JEROEN'))