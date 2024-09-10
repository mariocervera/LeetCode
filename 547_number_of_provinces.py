
def findCircleNum(isConnected):
    n = len(isConnected)
    discovered = [False] * n

    def dfs(source):
        discovered[source] = True
        for adj in range(n):
            if isConnected[source][adj] and not discovered[adj]:
                dfs(adj)

    components = 0
    for node in range(n):
        if not discovered[node]:
            components += 1
            dfs(node)
    return components


print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
