from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    q = deque([root])
    res = []
    while q:
        _sum = 0
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            _sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(_sum / n)
    return res


t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))  # [3.00000,14.50000,11.00000]
print(averageOfLevels(t))
