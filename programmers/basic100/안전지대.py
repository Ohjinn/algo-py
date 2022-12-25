def solution(board):
    answer = 0
    x, y = [1, 1, 1, 0, -1, -1, -1, 0], [1, 0, -1, -1, -1, 0, 1, 1]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                answer += 1
                for k in range(len(x)):
                    if 0 <= i + x[k] < len(board) and 0 <= i + y[k] < len(board) and board[i + x[k]][i + y[k]] == 0:
                        board[i + x[k]][i + y[k]] = 1
                        answer += 1

    return len(board) * len(board) - answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))