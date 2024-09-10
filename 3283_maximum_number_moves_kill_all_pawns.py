from collections import deque
from functools import lru_cache

board_size = 50
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def bfs(source, pawns):
    distances, discovered = {}, set()
    q = deque([source])
    pawns.remove(source)
    steps = 0
    while pawns:
        for _ in range(len(q)):
            current_cell = q.popleft()
            if current_cell in pawns:
                distances[current_cell] = steps
                pawns.remove(current_cell)
            for move in knight_moves:
                new_cell = (current_cell[0] + move[0]), (current_cell[1] + move[1])
                if 0 <= new_cell[0] < board_size and 0 <= new_cell[1] < board_size and new_cell not in discovered:
                    discovered.add(new_cell)
                    q.append(new_cell)
        steps += 1
    return distances


def maxMoves(kx, ky, positions):
    n = len(positions)
    knight = (kx, ky)
    pawns = [(i, j) for [i, j] in positions]
    distances = {knight: bfs(knight, set(pawns) | {knight})}
    for pawn in pawns:
        distances[pawn] = bfs(pawn, set(pawns))

    @lru_cache(maxsize=None)
    def backtrack(mask, source, is_alice_turn):
        if mask == (1 << n) - 1:
            return 0
        res = float("-inf") if is_alice_turn else float("inf")
        for i in range(n):
            if mask & (1 << i) != 0:
                continue
            if is_alice_turn:
                res = max(res, distances[source][pawns[i]] + backtrack(mask | (1 << i), pawns[i], not is_alice_turn))
            else:
                res = min(res, distances[source][pawns[i]] + backtrack(mask | (1 << i), pawns[i], not is_alice_turn))
        return res

    return backtrack(0, knight, True)


print(maxMoves(kx=1, ky=1, positions=[[0, 0]]))  # 4
print(maxMoves(kx=0, ky=2, positions=[[1, 1], [2, 2], [3, 3]]))  # 8
print(maxMoves(kx=0, ky=0, positions=[[1, 2], [2, 4]]))  # 3
print(maxMoves(kx=0, ky=1, positions=[[9, 6], [8, 0], [4, 0]]))  # 12
print(maxMoves(kx=0, ky=6, positions=[[8, 8], [4, 9], [0, 9]]))  # 10
print(maxMoves(kx=30,
               ky=10,
               positions=[[47, 47], [40, 47], [24, 1], [17, 38], [18, 20],
                          [9, 34], [34, 45], [39, 41], [39, 5], [35, 46]]))  # 133
