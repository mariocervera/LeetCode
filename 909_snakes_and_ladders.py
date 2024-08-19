
from collections import deque

def to_1D_forward_array(board):
    res, n = [-1], len(board)
    for i in range(n):
        if i % 2 == 0:
            res.extend(board[n-i-1])
        else:
            res.extend(board[n-i-1][::-1])
    return res

def get_adjacent_cells(board, cell, target):
    regular_cell_added = False
    adjacents = []
    for x in range(min(target, cell + 6), cell, -1):
        if board[x] != -1:
            adjacents.append(board[x])
        elif not regular_cell_added:
            adjacents.append(x)
            regular_cell_added = True
    return adjacents

def snakesAndLadders(board):
    board = to_1D_forward_array(board)
    target = len(board) - 1
    visited = [False] * len(board)
    q = deque([1])
    moves = -1
    while q:
        moves += 1
        for _ in range(len(q)):
            cell = q.popleft()
            visited[cell] = True
            adjacent_cells = get_adjacent_cells(board, cell, target)
            for adjacent in adjacent_cells:
                if adjacent == target:
                    return moves + 1
                if not visited[adjacent]:
                    q.append(adjacent)
    return -1


print(snakesAndLadders(
    [[-1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1],
     [-1, 35, -1, -1, 13, -1],
     [-1, -1, -1, -1, -1, -1],
     [-1, 15, -1, -1, -1, -1]]))  # 4


print(snakesAndLadders([[-1,-1],[-1,3]]))  # 1


