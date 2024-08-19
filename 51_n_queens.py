
def get_board_from(n, solution):
    board = []
    for i in range(n):
        row = ["."] * n
        row[solution[i]] = "Q"
        board.append("".join(row))
    return board

def solveNQueens(n):
    taken_columns, taken_diag_1, taken_diag_2 = set(), set(), set()
    solutions = []

    def backtrack(row, solution):
        nonlocal solutions
        if row == n:
            solutions.append(solution.copy())
            return
        for column in range(n):
            new_diag_1, new_diag_2 = row + column, row - column
            if column not in taken_columns and new_diag_1 not in taken_diag_1 and new_diag_2 not in taken_diag_2:
                taken_columns.add(column)
                taken_diag_1.add(new_diag_1)
                taken_diag_2.add(new_diag_2)
                solution.append(column)
                backtrack(row+1, solution)
                solution.pop()
                taken_columns.remove(column)
                taken_diag_1.remove(new_diag_1)
                taken_diag_2.remove(new_diag_2)

    backtrack(0, [])

    boards = []
    for sol in solutions:
        boards.append(get_board_from(n, sol))
    return boards


print(solveNQueens(4))  # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solveNQueens(1))  # [["Q"]]
