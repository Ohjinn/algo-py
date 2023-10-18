from collections import deque


def solution(board):
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    R = ()
    queue = deque()
    visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    y_max, x_max = len(board), len(board[0])
    for i in range(len(board)):
        print(board[i])

    for i in range(y_max):
        board[i] = list(board[i])
        for j in range(x_max):
            if board[i][j] == 'R':
                R = (j, i)
            if board[i][j] == 'G':
                G = (j, i)
    queue.append(R)

    while queue:
        r_location = queue.popleft()
        print(r_location)
        for move in moves:
            x, y = r_location[0], r_location[1]

            while True:
                x += move[0]
                y += move[1]

                if x_max <= x or x < 0 or y_max <= y or y < 0:
                    break
                if board[y][x] == 'D':
                    break
            x -= move[0]
            y -= move[1]
            print(x, y)
            if (x, y) != r_location and (not visited[y][x] or visited[y][x] > visited[r_location[1]][r_location[0]] + 1):
                queue.append((x, y))
                visited[y][x] = visited[r_location[1]][r_location[0]] + 1
        print(queue)
        print(visited)

    return visited[G[1]][G[0]] if visited[G[1]][G[0]] else -1

# print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# print(solution([".D.R", "....", ".G..", "...D"]))
# print(solution(["DRD", "D.D", "DGD"]))
# print(solution(["R...", "....", ".DDD", ".DGD"]))
print(solution(["..R", "...", "...", "..D", "DG."]))