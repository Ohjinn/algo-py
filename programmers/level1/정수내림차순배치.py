def solution(n):
    num_list = [i for i in str(n)]
    num_list.sort(reverse=True)
    return int(''.join(num_list))

print(solution(118372))
