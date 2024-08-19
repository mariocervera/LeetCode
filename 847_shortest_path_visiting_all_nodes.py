from collections import deque


def set_bit(n, i):
    return n | (1 << i)


def shortestPathLength(graph):
    n = len(graph)
    visited = {(0, node) for node in range(n)}
    q = deque(list(visited))
    target = (1 << n) - 1
    steps = 0
    while q:
        for _ in range(len(q)):
            visited_nodes, current_node = q.popleft()
            visited_nodes = set_bit(visited_nodes, current_node)
            if visited_nodes == target:
                return steps
            for adj in graph[current_node]:
                if (visited_nodes, adj) not in visited:
                    visited.add((visited_nodes, adj))
                    q.append((visited_nodes, adj))
        steps += 1
    return steps


print(shortestPathLength([[1, 2, 3], [0], [0], [0]]))  # 4
print(shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))  # 4
