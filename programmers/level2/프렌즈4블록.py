def solution(m, n, board):
    answer = 0
    list_board = [[] for i in range(n)]
    for i in range(m):
        for j in range(n):
            list_board[j].append(board[i][j])

    for i in range(m):
        list_board[i] = list_board[i][::-1]

    deleted = True
    while deleted == True:
        deleted = False
        deleted_set = set()
        for i in range(n - 1):
            for j in range(m - 1):
                try:
                    if list_board[i][j] == list_board[i][j + 1] and list_board[i][j] == list_board[i + 1][j] and \
                            list_board[i][j] == list_board[i + 1][j + 1]:
                        deleted_set.update({(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)})
                        deleted = True
                except IndexError:
                    continue

        target_list = sorted(deleted_set, reverse=True)
        for target in target_list:
            list_board[target[0]].pop(target[1])
            # print(list_board[target[0]][target[1]])
            answer += 1

    return answer