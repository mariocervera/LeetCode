
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    if not root:
        return []
    res, direction = [], 1
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            current_node = q.popleft()
            level.append(current_node.val)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        res.append(level[::direction])
        direction *= -1
    return res


t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(zigzagLevelOrder(t))  # [[3],[20,9],[15,7]]
