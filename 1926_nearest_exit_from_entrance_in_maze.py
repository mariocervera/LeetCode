from collections import deque


def nearestExit(maze, entrance):
    m, n = len(maze), len(maze[0])

    def is_border_cell(i, j):
        return [i, j] != entrance and (i == 0 or i == m-1 or j == 0 or j == n-1)

    steps = 0
    start_position = (entrance[0], entrance[1])
    q = deque([start_position])
    while q:
        for _ in range(len(q)):
            current_cell = q.popleft()
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = current_cell[0] + d[0], current_cell[1] + d[1]
                if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] == ".":
                    if is_border_cell(new_i, new_j):
                        return steps + 1
                    maze[new_i][new_j] = "+"
                    q.append((new_i, new_j))
        steps += 1
    return -1


print(nearestExit(maze=[["+", "+", ".", "+"],
                        [".", ".", ".", "+"],
                        ["+", "+", "+", "."]],
                  entrance=[1, 2]))  # 1


print(nearestExit(maze=[["+", "+", "+"],
                        [".", ".", "."],
                        ["+", "+", "+"]],
                  entrance=[1, 0]))  # 2


print(nearestExit(maze=[[".", "+"]],
                  entrance=[0, 0]))  # -1
