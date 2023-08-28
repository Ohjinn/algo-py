def solution(keymap, targets):
    answer = []
    avail_count = {}
    for key_list in keymap:
        for index, avail in enumerate(key_list):
            if avail not in avail_count:
                avail_count[avail] = index + 1
            else:
                if avail_count[avail] > index:
                    avail_count[avail] = index + 1

    for target in targets:
        counter = 0
        for word in target:
            if word not in avail_count:
                answer.append(-1)
                break
            else:
                counter += avail_count[word]
        else:
            answer.append(counter)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))