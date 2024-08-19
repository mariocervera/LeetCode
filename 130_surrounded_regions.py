def traverse_region(board, i, j, m, n):
    if not (0 <= i < m) or not (0 <= j < n) or board[i][j] == "1" or board[i][j] == "X":
        return
    board[i][j] = "#"
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_i = i + d[0]
        new_j = j + d[1]
        traverse_region(board, new_i, new_j, m, n)


def solve(board):
    m = len(board)
    n = len(board[0])

    for i in (0, m - 1):
        for j in range(n):
            if board[i][j] == "O":
                traverse_region(board, i, j, m, n)

    for j in (0, n - 1):
        for i in range(m):
            if board[i][j] == "O":
                traverse_region(board, i, j, m, n)

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "#":
                board[i][j] = "O"


matrix = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
solve(matrix)
print(matrix)  # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]



