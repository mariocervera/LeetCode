
def countPairs(n, edges):
    graph = {node: [] for node in range(n)}
    for node_1, node_2 in edges:
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    component_sizes = []
    node_components = [None] * n
    discovered_nodes = set()

    def dfs(node):
        node_components[node] = len(component_sizes) - 1
        discovered_nodes.add(node)
        component_sizes[-1] += 1
        for adjacent in graph[node]:
            if adjacent not in discovered_nodes:
                dfs(adjacent)

    for node in range(n):
        if node not in discovered_nodes:
            component_sizes.append(0)
            dfs(node)

    res = 0
    for node in range(n):
        res += (n - component_sizes[node_components[node]])
    return res // 2


#print(countPairs(n=3, edges=[[0, 1], [0, 2], [1, 2]]))  # 0
print(countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))  # 14
