from collections import deque

n, m, k = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
attack_history = []
attacker = ()
target = ()

list_test = [1, 2, 3, 4, 5]
list_test2 = [1, 2]


def select_attacker():
    global map_arr, attack_history, attacker, n, m

    same_min = []
    min_value = 5001
    for i in range(n):
        for j in range(m):
            if map_arr[i][j] == min_value:
                same_min.append((j, i))
            elif map_arr[i][j] and map_arr[i][j] < min_value:
                min_value = map_arr[i][j]
                same_min = [(j, i)]

    if len(same_min) > 1:
        for value in same_min:
            if value in attack_history:
                for history in reversed(attack_history):
                    if history in same_min:
                        attacker = history
                        break
        else:
            same_xy_sum = [i + j for i, j in same_min]

            check_same = list(filter(lambda x: same_xy_sum[x] == max(same_xy_sum), range(len(same_xy_sum))))
            if len(check_same) > 1:
                y_sum = [j for i, j in same_min]
                max_y_index = y_sum.index(max(y_sum))
                attacker = same_min[max_y_index]
            else:
                attacker = same_min[same_xy_sum.index(max(same_xy_sum))]
    else:
        attacker = same_min[0]


def select_target():
    global map_arr, attack_history, target, n, m

    same_max = []
    max_value = -1
    for i in range(n):
        for j in range(m):
            if map_arr[i][j] == max_value:
                same_max.append((j, i))
            elif map_arr[i][j] and map_arr[i][j] > max_value:
                max_value = map_arr[i][j]
                same_max = [(j, i)]
    if len(same_max) > 1:
        for value in same_max:
            if value in attack_history:
                for history in reversed(attack_history):
                    if history in same_max:
                        target = history
                        break
        else:
            same_xy_sum = [i + j for i, j in same_max]

            check_same = list(filter(lambda x: same_xy_sum[x] == min(same_xy_sum), range(len(same_xy_sum))))
            if len(check_same) > 1:
                y_sum = [j for i, j in same_max]
                max_y_index = y_sum.index(min(y_sum))
                target = same_max[max_y_index]
            else:
                target = same_max[same_xy_sum.index(min(same_xy_sum))]
    else:
        target = same_max[0]


def laser_attack():
    global map_arr, attack_history, attacker, target, n, m, visited
    traverse_x, traverse_y = [1, 0, -1, 0], [0, 1, 0, -1]

    routes = []
    route_queue = deque([attacker])
    visited[attacker[1]][attacker[0]] = 1
    while route_queue:
        route = route_queue.popleft()
        route_x, route_y = route[0], route[1]

        routes.append([route_x, route_y])
        print('visited', visited)

        if (route_x, route_y) == target:
            print('break signal', visited)
            break

        for i in range(4):
            new_route_x, new_route_y = route_x + traverse_x[i], route_y + traverse_y[i]

            if new_route_x < 0:
                new_route_x = new_route_x + m
            elif new_route_x >= m:
                new_route_x = 0

            if new_route_y < 0:
                new_route_y = new_route_y + n
            elif new_route_y >= n:
                new_route_y = 0

            print('new_route', new_route_x, new_route_y)

            if not visited[new_route_y][new_route_x] and map_arr[new_route_y][new_route_x]:
                route_queue.append([new_route_x, new_route_y])
                print(visited[route_y][route_x], route_x, route_y)
                visited[new_route_y][new_route_x] = visited[route_y][route_x] + 1
                print('after', visited)


select_attacker()
select_target()
print('from', attacker)
print('to', target)
print()
laser_attack()
print(visited)


