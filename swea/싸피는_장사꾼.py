#######################################################################################################
# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
# 표준 입력 예제
# a = int(input())                                                  # 정수 1개 입력받는 예제
# b, c = map(float, input().split())                                # 실수 2개 입력받는 예제
# var = input()                                                     # 문자열 1개 입력받는 예제
# A = [int(num) for num in input().split()]                         # 1차원 배열에 정수 입력받는 예제
# B = [[int(num) for num in input().split()] for _ in range(row)]   # 2차원 배열에 정수 입력받는 예제
#######################################################################################################
# 표준 출력 예제
# a = 0
# b = 1.0
# c = 2.0
# var = "ABCDEFG"
# N = 10
# A = [0] * N
# B = [[1] * N for _ in range(N)]
# print(a)                                                          # 정수 1개 출력하는 예제
# print(b, c)                                                       # 실수 2개 출력하는 예제
# print(var)                                                        # 문자열 1개 출력하는 예제
# print(' '.join(str(num) for num in A))                            # 1차원 배열 출력하는 예제
# print('\n'.join(' '.join(str(num) for num in N) for N in B))      # 2차원 배열 출력하는 예제
#######################################################################################################

# import sys

'''
   아래의 stdin 함수는 sample_input.txt 를 read only 형식으로 연 후,
   앞으로 표준 입력(키보드) 대신 sample_input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
   여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 sample_input.txt에 입력을 저장한 후,
   stdin 함수를 이용하면 이후 input 을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 함수를 사용하셔도 좋습니다.
   단, 채점을 위해 코드를 제출하실 때에는 반드시 stdin 함수를 지우거나 주석 처리 하셔야 합니다.
'''
# sys.stdin = open('sample_input.txt', 'r')


'''
  여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
'''


def dfs(storage, customers, time, a_sum, max_value):
    # 끝에 도달했다면
    if len(customers) == time:
        if max_value < a_sum:
            max_value = a_sum
    # 끝이 아니라면
    else:
        # 차가 들어올 차례면서 차고가 빈 경우
        if customers[time][0] == 1 and storage == 0:
            dfs(customers[time][1], customers, time + 1, a_sum, max_value)
        # 차가 들어올 차례지만 차고가 비어있지 않은 경우
        if customers[time][0] == 1 and storage != 0:
            dfs(storage, customers, time + 1, a_sum, max_value)
        # 구매자가 온 경우
        if customers[time][0] == -1:
            # 차고의 차 가격이 구매가와 같은 경우
            if storage == customers[time][1]:
                a_sum += storage
                storage = 0

            # 같지 않은 경우
            dfs(storage, customers, time + 1, a_sum, max_value)


T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################
    #'''
    N = int(input())
    # storage가 0이 아니면 해당 가격의 차가 들어있음
    storage = 0
    # 미래의 차 목록을 저장
    customers = []
    # 최댓값 저장
    a_max = 0

    # 입력을 받기 위한 부분
    for i in range(N):
        a, b = map(int, input().split())
        customers.append([a, b])

    # dfs를 이용한 경우의 수 풀이
    dfs(storage, customers, 0, 0, a_max)
    #'''
    #######################################################################################################

    # 표준출력(화면)으로 답안을 출력합니다.
    print(f'#{test_case} {a_max}')
