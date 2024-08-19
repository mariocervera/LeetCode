
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None
    nodes = [None] * 101
    q = deque([node])
    nodes[node.val] = Node(node.val)
    while q:
        current_node = q.popleft()
        for neighbor in current_node.neighbors:
            if not nodes[neighbor.val]:
                nodes[neighbor.val] = Node(neighbor.val)
                q.append(neighbor)
            nodes[current_node.val].neighbors.append(nodes[neighbor.val])
    return nodes[node.val]


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.append(n2)
n1.neighbors.append(n3)
n2.neighbors.append(n4)

cloned_graph = cloneGraph(n1)

print(1)
