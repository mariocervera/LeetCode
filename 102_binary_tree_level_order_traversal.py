from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []
    levels = []
    q = deque([root])
    while q:
        new_level = []
        for _ in range(len(q)):
            current_node = q.popleft()
            new_level.append(current_node.val)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        levels.append(new_level)
    return levels


t = TreeNode(3, TreeNode(9, right=TreeNode(11)), TreeNode(20, TreeNode(15), TreeNode(7))) # [[3], [9, 20], [11, 15, 7]]
print(levelOrder(t))
