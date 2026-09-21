def ipiece(board):
    for i in range(3, 7):
        board[4][i] = 1
    coords = [[4,3],[4,4],[4,5],[4,6]]
    return coords
