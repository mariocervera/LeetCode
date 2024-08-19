from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def isCompleteTree(root):
    if not root:
        return True
    q = deque([root])
    prev = None
    while q:
        for i in range(len(q)):
            current_node = q.popleft()
            if current_node != root and current_node is not None and prev is None:
                return False
            if current_node is not None:
                q.append(current_node.left)
                q.append(current_node.right)
            prev = current_node
    return True


t1 = TreeNode(1,
              TreeNode(2,
                       TreeNode(4),
                       TreeNode(5)),
              TreeNode(3,
                       TreeNode(6),
                       None))

print(isCompleteTree(t1))  # True


t2 = TreeNode(1,
              TreeNode(2,
                       TreeNode(4),
                       TreeNode(5)),
              TreeNode(3,
                       None,
                       TreeNode(7)))

print(isCompleteTree(t2))  # False