def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == ')' and not stack:
            return False
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

    # stack 이 비어있지 않으면 올바르지 않은 괄호
    if stack:
        answer = False
    return answer


print(solution("(())()"))
