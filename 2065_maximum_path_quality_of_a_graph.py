def maximalPathQuality(values, edges, maxTime):
    n = len(values)
    graph = [[] for _ in range(n)]
    for edge in edges:
        x, y, w = edge[0], edge[1], edge[2]
        graph[x].append((y, w))
        graph[y].append((x, w))

    max_quality = float("-inf")

    def dfs(node, time, path_nodes):
        nonlocal max_quality
        if time > maxTime:
            return
        if node == 0:
            quality = sum(values[v] for v in path_nodes)
            max_quality = max(max_quality, quality)
        for adjacent, weight in graph[node]:
            dfs(adjacent, time + weight, path_nodes | {adjacent})

    dfs(0, 0, {0})
    return max_quality


print(maximalPathQuality(values=[0, 32, 10, 43], edges=[[0, 1, 10], [1, 2, 15], [0, 3, 10]], maxTime=49))  # 75
print(maximalPathQuality(values=[5, 10, 15, 20], edges=[[0, 1, 10], [1, 2, 10], [0, 3, 10]], maxTime=30))  # 25
print(maximalPathQuality(values=[1, 2, 3, 4], edges=[[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], maxTime=50))  # 7
