import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 미로 입력
maze = []
for i in range(N):
    maze.append(list(map(int, input().split())))

# 참가자 위치 입력
for i in range(M):
    x, y = map(int, input().split())
    maze[x - 1][y - 1] = 11

# 출구 입력
x, y = map(int, input().split())
maze[x - 1][y - 1] = -1

# 출구
exit_points = []
move_count = 0
part_count = M


print(maze)
for time in range(K):
    participants = [[i, j] for i in range(N) for j in range(N) if maze[i][j] > 10]
    exit_points = [[i, j] for i in range(N) for j in range(N) if maze[i][j] == -1]
    exit_x, exit_y = exit_points[0][0], exit_points[0][1]

    # 참가자가 남아있지 않으면 break
    if part_count == 0:
        break

    # 1. 사람 이동
    for participant in participants:
        before_x, before_y = participant
        if not ((before_y + 1 < N and 0 < maze[before_y + 1][before_x]) < 9 and (before_y - 1 >= 0 and 0 < maze[before_y - 1][before_x] < 9) and exit_y == participant[1]):
            if exit_y > participant[1]:
                participant[1] += 1
            else:
                participant[1] -= 1

            move_count += 1

            if participant == exit_points:
                maze[participant[1]][participant[0]] = 0
                part_count -= 1
            else:
                maze[participant[1]][participant[0]] = maze[before_y][before_x]
                maze[before_y][before_x] = 0

        elif not ((before_x + 1 < N and 0 < maze[before_y][before_x + 1] < 9) and (before_x - 1 >= 0 and 0 < maze[before_y][before_x - 1] < 9) and exit_x == participant[0]):
            if exit_x > participant[0]:
                participant[0] += 1
            else:
                participant[0] -= 1

            move_count += 1

            if participant == exit_points:
                maze[participant[1]][participant[0]] = 0
                part_count -= 1
            else:
                maze[participant[1]][participant[0]] = maze[before_y][before_x]
                maze[before_y][before_x] = 0

        print(maze)
        # 2. 미로 회전
