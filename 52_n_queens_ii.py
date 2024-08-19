

def totalNQueens(n):
    count = 0
    columns, diagonal_1, diagonal_2 = set(), set(), set()

    def backtrack(row):
        nonlocal count, columns, diagonal_1, diagonal_2
        if row == n:
            count += 1
        for column in range(n):
            d1, d2 = row + column, row - column
            if column in columns or d1 in diagonal_1 or d2 in diagonal_2:
                continue
            columns.add(column)
            diagonal_1.add(d1)
            diagonal_2.add(d2)
            backtrack(row+1)
            columns.remove(column)
            diagonal_1.remove(d1)
            diagonal_2.remove(d2)

    backtrack(0)
    return count



print(totalNQueens(1))  # 1
print(totalNQueens(2))  # 0
print(totalNQueens(3))  # 0
print(totalNQueens(4))  # 2
print(totalNQueens(5))  # 10
print(totalNQueens(6))  # 4
print(totalNQueens(7))  # 40
print(totalNQueens(8))  # 92
print(totalNQueens(9))  # 352
print(totalNQueens(10))  # 724
