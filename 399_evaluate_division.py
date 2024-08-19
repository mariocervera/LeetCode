
def dfs(graph, source, destination, visited):
    if source == destination:
        return 1
    for adjacent in graph[source]:
        if adjacent not in visited:
            visited.add(adjacent)
            res = dfs(graph, adjacent, destination, visited)
            if res is not None:
                return res * graph[source][adjacent]


def calcEquation(equations, values, queries):
    graph = {}
    for div in equations:
        graph[div[0]], graph[div[1]] = {}, {}
    for i, div in enumerate(equations):
        graph[div[0]][div[1]] = values[i]
        graph[div[1]][div[0]] = float(1)/values[i]

    res = [-1] * len(queries)
    for i, query in enumerate(queries):
        if query[0] not in graph or query[1] not in graph:
            continue
        if query[1] in graph[query[0]]:
            res[i] = graph[query[0]][query[1]]
            continue

        sol = dfs(graph, query[0], query[1], set())
        if sol:
            res[i] = sol
    return res



# Result: [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
print(calcEquation(equations=[["a", "b"], ["b", "c"]],
                   values=[2.0, 3.0],
                   queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

# Result: [3.75000, 0.40000, 5.00000, 0.20000]
print(calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
                   values=[1.5, 2.5, 5.0],
                   queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))


# Result: [0.50000, 2.00000, -1.00000, -1.00000]
print(calcEquation(equations=[["a", "b"]],
                   values=[0.5],
                   queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))


# Result:
print(calcEquation(equations=[["a", "b"], ["c", "d"]],
                   values=[1.0, 1.0],
                   queries=[["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]))
