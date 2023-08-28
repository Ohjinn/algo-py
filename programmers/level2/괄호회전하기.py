def solution(s):
    count=0
    for strt_idx in range(len(s)):
        target=s[strt_idx:]+s[:strt_idx]
        while True:
            length = len(target)
            target = target.replace("()","")
            target = target.replace("{}","")
            target = target.replace("[]","")
            if len(target) == 0:
                count += 1
                break
            if length == len(target):
                break
    return count