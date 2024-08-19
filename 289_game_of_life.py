



def gameOfLife(board):
    def get_number_of_live_neighbours(i, j):
        live_cells = 0
        for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            new_i, new_j = i + d[0], j + d[1]
            if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] in (1, 3):
                live_cells += 1
        return live_cells

    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            live_neighbours = get_number_of_live_neighbours(i, j)
            if board[i][j] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                    board[i][j] = 3
            elif board[i][j] == 0 and live_neighbours == 3:
                board[i][j] = 2

    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 1
            elif board[i][j] == 3:
                board[i][j] = 0





# Test 1
_board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
gameOfLife(_board)
print(_board)  # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Test 2
_board = [[1, 1], [1, 0]]
gameOfLife(_board)
print(_board)  # [[1,1],[1,1]]
