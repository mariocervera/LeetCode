
def makeConnected(n, connections):
    graph = [[] for _ in range(n)]
    for source, target in connections:
        graph[source].append(target)
        graph[target].append(source)

    discovered = set()

    def dfs(node):
        if node is None:
            return
        for adj in graph[node]:
            if adj not in discovered:
                discovered.add(adj)
                dfs(adj)

    components = 0
    for computer in range(n):
        if computer not in discovered:
            components += 1
            discovered.add(computer)
            dfs(computer)

    return components-1 if len(connections) >= n-1 else -1


print(makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))  # 1
print(makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))  # 2
print(makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]))  # -1
