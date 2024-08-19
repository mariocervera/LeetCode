from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    if not root:
        return None
    q = deque([root])
    res = []
    while q:
        for _ in range(len(q)):
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        res.append(current_node.val)
    return res

t = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3, right=TreeNode(4)))
print(rightSideView(t))  # [1, 3, 4]
