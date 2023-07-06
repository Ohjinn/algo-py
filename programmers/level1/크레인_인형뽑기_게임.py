def grab(index, board, size):
    for j in range(size):
        if board[j][index] != 0:
            value = board[j][index]
            board[j][index] = 0
            return value


def solution(board, moves):
    answer = 0
    basket = []
    size = len(board)
    for move in moves:
        target = grab(move - 1, board, size)
        if target:
            if basket and basket[-1] == target:
                basket.pop()
                answer += 2
            else:
                basket.append(target)
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
