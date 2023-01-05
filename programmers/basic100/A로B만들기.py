def solution(before, after):
    before_dict, after_dict = {}, {}
    for before_word in before:
        if before_word in before_dict:
            before_dict[before_word] += 1
        else:
            before_dict[before_word] = 0
    for after_word in after:
        if after_word in after_dict:
            after_dict[after_word] += 1
        else:
            after_dict[after_word] = 0
    return 1 if before_dict == after_dict else 0


def solution2(before, after):
    before = sorted(before)
    after = sorted(after)
    return 1 if before == after else 0

solution("olleh", "hello")
