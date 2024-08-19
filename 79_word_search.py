
def exist(board, word):
    m, n = len(board), len(board[0])

    def backtrack(pos_i, pos_j, solution_i, visited):
        if word[solution_i] != board[pos_i][pos_j]:
            return False
        if solution_i == len(word) - 1:
            return True
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_i, new_j = pos_i + d[0], pos_j + d[1]
            if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                visited.add((new_i, new_j))
                if backtrack(new_i, new_j, solution_i + 1, visited):
                    return True
                visited.remove((new_i, new_j))
        return False

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0, {(i, j)}):
                return True
    return False


print(exist(board=[["a"]], word="a"))  # True

print(exist(board=[["a", "a"]], word="aaa"))  # False


print(exist(board=[["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], word="ABCCED"))  # True

print(exist(board=[["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], word="SEE"))  # True

print(exist(board=[["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], word="ABCB"))  # False