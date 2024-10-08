def get_one_row_grid(graph, degrees, n):
    row = [None] * n
    for i in range(n):
        if degrees[i] == 1:
            row[0 if row[0] is None else -1] = i
    for i in range(1, n - 1):
        for adj in graph[row[i - 1]]:
            if degrees[adj] == 2 and (i == 1 or row[i - 2] != adj):
                row[i] = adj
    return [row]


def get_two_rows_grid(graph, degrees, n):
    seen = set()
    rows, columns = 2, n // 2
    grid = [[None for _ in range(columns)] for _ in range(rows)]
    grid[0][0] = degrees.index(2)
    degree_2 = []
    for i in range(grid[0][0] + 1, n):
        if degrees[i] == 2:
            if i in graph[grid[0][0]] and grid[1][0] is None:
                grid[1][0] = i
            else:
                degree_2.append(i)
    for col in range(1, columns - 1):
        for adj in graph[grid[0][col - 1]]:
            if adj not in seen and (degrees[adj] == 3 and (col == 1 or (grid[0][col - 2] != adj and grid[1][col - 1] != adj))):
                grid[0][col] = adj
                seen.add(adj)
        for adj in graph[grid[1][col - 1]]:
            if adj not in seen and (degrees[adj] == 3 and adj in graph[grid[0][col]]):
                grid[1][col] = adj
                seen.add(adj)
    grid[0][-1] = degree_2[0] if degree_2[0] in graph[grid[0][-2]] else degree_2[1]
    grid[1][-1] = degree_2[0] if degree_2[0] in graph[grid[1][-2]] else degree_2[1]
    return grid


def get_general_grid(graph, degrees, n):
    seen = set()
    grid = [[]]
    source = degrees.index(2)
    seen.add(source)
    grid[0].append(source)
    j, found_degree_2 = 1, False
    while not found_degree_2:
        for adj in graph[grid[0][j - 1]]:
            if 2 <= degrees[adj] <= 3 and adj not in seen:
                grid[0].append(adj)
                seen.add(adj)
                if degrees[adj] == 2:
                    found_degree_2 = True
                break
        j += 1
    rows, columns = n // len(grid[0]), len(grid[0])
    for row in range(1, rows):
        grid.append([])
        for column in range(columns):
            for adj in graph[grid[row - 1][column]]:
                if adj not in seen and (((column == 0 or column == columns - 1) and (degrees[adj] == 2 if row == rows - 1 else degrees[adj] == 3)) or\
                                        (1 <= column < columns - 1 and (degrees[adj] == 3 if row == rows - 1 else degrees[adj] == 4))):
                    grid[row].append(adj)
                    seen.add(adj)
    return grid


def constructGridLayout(n, edges):
    graph = [[] for _ in range(n)]
    degrees = [0 for _ in range(n)]
    for s, t in edges:
        graph[s].append(t)
        graph[t].append(s)
        degrees[s] += 1
        degrees[t] += 1
    if degrees.count(1) > 0:
        return get_one_row_grid(graph, degrees, n)
    elif degrees.count(4) == 0:
        return get_two_rows_grid(graph, degrees, n)
    return get_general_grid(graph, degrees, n)


print(constructGridLayout(n=4,
                          edges=[[0, 1], [0, 2], [1, 3], [2, 3]]))  # [[3,1], [2,0]]

print(constructGridLayout(n=5,
                          edges=[[0, 1], [1, 3], [2, 3], [2, 4]]))  # [[4,2,3,1,0]]

print(constructGridLayout(n=9,
                          edges=[[0, 1], [0, 4], [0, 5], [1, 7], [2, 3], [2, 4],
                                 [2, 5], [3, 6], [4, 6], [4, 7], [6, 8], [7, 8]]))  # [[8,6,3], [7,4,2], [1,0,5]]

print(constructGridLayout(n=6,
                          edges=[[0, 1], [0, 2], [0, 4], [1, 3], [2, 5], [3, 4], [4, 5]]))  # [[1, 0, 2], [3, 4, 5]]

print(constructGridLayout(n=8,
                          edges=[[0, 1], [0, 3], [0, 4], [1, 5], [1, 6],
                                 [2, 3], [2, 4], [3, 6], [5, 7],  [6, 7]]))  # [[2, 3, 6, 7], [4, 0, 1, 5]]
