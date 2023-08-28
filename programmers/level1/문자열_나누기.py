def solution(s):
    counter = 0

    index = 0
    while index < len(s):
        if index == len(s) - 1:
            counter += 1

        target_word = s[index]
        target_counter = 1
        other_counter = 0
        index += 1
        while index < len(s):
            if target_word == s[index]:
                target_counter += 1
            else:
                other_counter += 1
            index += 1

            if target_counter == other_counter:
                counter += 1
                break

            if index == len(s):
                counter += 1

    return max(1, counter)


print(solution("baaa"))