# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    count = 0
    while 'B' in S and 'A' in S and 'N' in S and S.count('B') >= 1 and S.count('N') >= 2 and S.count('A') >= 3:
        S = S.replace('B', '', 1)
        S = S.replace('N', '', 2)
        S = S.replace('A', '', 3)
        count += 1
    return count

print(solution('NAANAAXNABABYNNBZ'))