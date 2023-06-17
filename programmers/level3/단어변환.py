from collections import deque


def solution(begin, target, words):

    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        x, count = queue.popleft()

        if x == target:
            return count

        for i in range(0, len(words)):
            diff,  word = 0, words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                queue.append([word, count + 1])
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
