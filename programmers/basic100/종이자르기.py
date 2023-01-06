def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        return answer
    if M > N:
        answer += N - 1
        answer = answer + (M - 1) * (answer + 1)
    else:
        answer += M - 1
        answer = answer + (N - 1) * (answer + 1)
    return answer

print(solution(2, 2))