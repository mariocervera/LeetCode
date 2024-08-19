
def initialize(used_numbers, board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                used_numbers |= {f"{board[i][j]}r{i}", f"{board[i][j]}c{j}", f"{board[i][j]}c{i//3}{j//3}"}


def solveSudoku(board):
    used_numbers = set()
    initialize(used_numbers, board)

    def backtrack(row, column):
        if row == 9:
            return True

        next_row, next_column = (row, column+1) if column < 8 else (row+1, 0)

        if board[row][column] != ".":
            return backtrack(next_row, next_column)

        for candidate in range(1, 10):
            candidate_set = {f"{candidate}r{row}", f"{candidate}c{column}", f"{candidate}c{row // 3}{column // 3}"}
            if not (used_numbers & candidate_set):
                used_numbers.update(candidate_set)
                board[row][column] = str(candidate)
                if backtrack(next_row, next_column):
                    return True
                board[row][column] = "."
                used_numbers.difference_update(candidate_set)

        return False

    backtrack(0, 0)



b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

solveSudoku(b)

print(b)  # [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
#           ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
#           ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
#           ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
#           ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
#           ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
#           ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
#           ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
#           ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
