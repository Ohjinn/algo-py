def dfs(s, words, answer, idx):
    global count
    print(answer, idx)
    print('조건', len(s) - 1)
    if idx == len(s) - 1:
        if answer > count:
            count = answer
        return
    for sub_idx in range(2, 11):
        if s[idx:idx + sub_idx] in words:
            print(s[idx:idx+sub_idx])
            idx += (sub_idx - 1)
            dfs(s, words, answer + 1, idx)


def solution(s, word_dict):
    words = dict.fromkeys(word_dict)
    global count
    count = 0

    dfs(s, words, 0, 0)
    return count

print(solution("centerminus", ["cent", "center", "term", "terminus", "rm", "min", "minus", "us"]))
print()
print(solution("aaaababab", ["aaa", "aaaa", "ab", "bab", "aababa"]))

# 이거 그럼 aaa ab ab ab 이렇게 해도 네가지 아니야??