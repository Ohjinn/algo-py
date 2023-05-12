from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    p = list(truck_weights) # 트럭 무게
    x = [0] * bridge_length # 다리
    s=0
    while (x):
        time += 1
        s-=x.pop(0) # s: 다리 위의 총 트럭 무게
        if p:
            if ( s + p[0] ) <= weight:
                s+=p[0] # 여유되면 트럭 추가
                x.append(p.pop(0)) # 다리에 트럭 추가
            else:
                x.append(0) # 여유 없으면 무게 0 추가

    return time


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     waiting_list = deque(truck_weights)  # 기다리는 트럭
#     now_bridge = deque([0 for _ in range(bridge_length)])  # 다리 위 공간
#     weight_on_bridge = 0  # 다리 위 무게
#
#     while waiting_list:
#         answer += 1
#         target = waiting_list.popleft()
#
#         # 만약 다음 대기열과 큐 안의 무게가 제한을 넘으면 차가 나오길 기다림
#         while target + weight_on_bridge > weight:
#             now_bridge.appendleft(0)
#             weight_on_bridge -= now_bridge.pop()
#             answer += 1
#
#         # 현재 다리 위의 무게에 더하고 다리 위 큐에 집어넣음
#         weight_on_bridge += target
#         now_bridge.appendleft(target)
#
#         # 가장 오른쪽 유닛을 빼서 현재 다리 무게에서 뺌
#         leaving_car = now_bridge.pop()
#         weight_on_bridge -= leaving_car
#
#     return answer

print(solution(2, 10, [7, 4, 5, 6]))
