def solution(n, m, section):
    answer = 0
    i = 0
    # 1이면 어차피 다 칠해야 됨
    if m == 1:
        answer = len(section)
    else:
        while i < len(section):
            target = section[i]
            while i + 1 < len(section) and section[i + 1] < target + m:
                i += 1
            i += 1
            answer += 1
    return answer