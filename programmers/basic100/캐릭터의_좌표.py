def solution(keyinput, board):
    rpgBoard = rpg_board(board)

    for direction in keyinput:
        if direction == 'left':
            rpgBoard.moveLeft()
        elif direction == 'right':
            rpgBoard.moveRight()
        elif direction == 'up':
            rpgBoard.moveTop()
        elif direction == 'down':
            rpgBoard.moveBottom()
    return rpgBoard.getLocation()


class rpg_board:
    def __init__(self, board):
        self.x = 0
        self.y = 0
        self.limitLeftX = -(board[0] // 2)
        self.limitRightX = (board[0] // 2)
        self.limitTopY = (board[1] // 2)
        self.limitBottomY = -(board[1] // 2)

    def getLocation(self):
        return [self.x, self.y]

    def moveLeft(self):
        if self.limitLeftX < self.x:
            self.x -= 1

    def moveRight(self):
        if self.limitRightX > self.x:
            self.x += 1

    def moveTop(self):
        if self.limitTopY > self.y:
            self.y += 1

    def moveBottom(self):
        if self.limitBottomY < self.y:
            self.y -= 1

print(solution(["left", "right", "up", "right", "right"], [11, 11]))