
def build_graph(edges):
    g = {}
    for source, target in edges:
        if source not in g:
            g[source] = []
        if target not in g:
            g[target] = []
        g[source].append(target)
    return g


def get_source_node(graph):
    in_degrees = {node: 0 for node in graph}
    out_degrees = {node: 0 for node in graph}
    for node in graph:
        for adjacent in graph[node]:
            in_degrees[adjacent] += 1
            out_degrees[node] += 1
    for node in graph:
        if out_degrees[node] == in_degrees[node] + 1:
            return node
    return list(graph.keys())[0]  # Any node can be the source


def validArrangement(pairs):
    graph = build_graph(pairs)
    source = get_source_node(graph)
    path = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())
        path.append(node)

    dfs(source)

    path = path[::-1]
    return [[path[i], path[i+1]] for i in range(len(path)-1)]


print(validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]))  # [[11,9],[9,4],[4,5],[5,1]]
print(validArrangement([[1, 3], [3, 2], [2, 1]]))  # [[1,3],[3,2],[2,1]]
print(validArrangement([[1, 2], [1, 3], [2, 1]]))  # [[1,2],[2,1],[1,3]]
