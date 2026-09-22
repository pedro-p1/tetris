def ipiece(board):
    for i in range(3, 7):
        board[3][i] = 1
    coords = [[3,3],[3,4],[3,5],[3,6]]
    return coords
