from collections import deque

def shortestPathAllKeys(grid):
    m, n = len(grid), len(grid[0])
    all_keys = [False] * 6
    start_position = None
    for i in range(m):
        for j in range(n):
            cell = grid[i][j]
            if cell.islower():
                all_keys[ord(cell) - ord('a')] = True
            elif cell == "@":
                start_position = (i, j)
    all_keys = tuple(all_keys)
    q = deque([(start_position[0], start_position[1], tuple([False] * 6))])
    visited = {(start_position[0], start_position[1], tuple([False] * 6))}
    level = 0
    while q:
        for _ in range(len(q)):
            current_i, current_j, keys = q.popleft()
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = current_i + d[0], current_j + d[1]
                if not (0 <= new_i < m) or not (0 <= new_j < n) or grid[new_i][new_j] == "#":
                    continue
                if grid[new_i][new_j] in '.@' and (new_i, new_j, keys) not in visited:
                    visited.add((new_i, new_j, keys))
                    q.append((new_i, new_j, keys))
                    continue
                if grid[new_i][new_j].islower():
                    new_keys = list(keys)
                    new_keys[ord(grid[new_i][new_j]) - ord('a')] = True
                    new_keys = tuple(new_keys)
                    if new_keys == all_keys:
                        return level + 1
                    if (new_i, new_j, new_keys) not in visited:
                        visited.add((new_i, new_j, new_keys))
                        q.append((new_i, new_j, new_keys))
                    continue
                if grid[new_i][new_j].isupper() and keys[ord(grid[new_i][new_j].lower()) - ord('a')] and (new_i, new_j, keys) not in visited:
                    visited.add((new_i, new_j, keys))
                    q.append((new_i, new_j, keys))
        level += 1
    return -1



print(shortestPathAllKeys(["@.a..",
                           "###.#",
                           "b.A.B"]))  # 8

print(shortestPathAllKeys(["@..aA",
                           "..B#.",
                           "....b"]))  # 6

print(shortestPathAllKeys(["@Aa"]))  # -1

print(shortestPathAllKeys(["@...a",
                           ".###A",
                           "b.BCc"]))  # 10

print(shortestPathAllKeys(["@abcdeABCDEFf"]))  # -1
