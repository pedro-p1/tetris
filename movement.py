def gravity(board,coords):
    for i in range(4):
        board[coords[i][0]][coords[i][1]] = 0
    for i in range(4):
        coords[i][0] += 1
    for i in range(4):
        board[coords[i][0]][coords[i][1]] = 1