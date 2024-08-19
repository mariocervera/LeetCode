from sortedcontainers import SortedSet

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n+1)]
    for source, destination, weight in times:
        graph[source].append((destination, weight))
    discovered = SortedSet([(0, k)])
    distances = [float("inf")] * (n+1)
    distances[k] = 0
    in_tree = [False] * (n + 1)

    while discovered:
        current_node = min(discovered)

        discovered.remove(current_node)
        in_tree[current_node[1]] = True

        for adj_node, adj_weight in graph[current_node[1]]:
            if not in_tree[adj_node]:
                updated_distance = distances[current_node[1]] + adj_weight
                if updated_distance < distances[adj_node]:
                    if (distances[adj_node], adj_node) in discovered:
                        discovered.remove((distances[adj_node], adj_node))
                    distances[adj_node] = updated_distance
                    discovered.add((updated_distance, adj_node))

    max_distance = float("-inf")
    for i in range(1, n+1):
        if distances[i] == float("inf"):
            return -1
        max_distance = max(max_distance, distances[i])
    return max_distance




print(networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))  # 2
print(networkDelayTime(times=[[1, 2, 1]], n=2, k=1))  # 1
print(networkDelayTime(times=[[1, 2, 1]], n=2, k=2))  # -1
