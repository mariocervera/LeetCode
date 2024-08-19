class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative in-order traversal (checking each node with the previous value).
def isValidBST(root):
    prev_value = None
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev_value is not None and root.val <= prev_value:
            return False
        prev_value = root.val
        root = root.right
    return True


t = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(isValidBST(t))  # False

t = TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(3), TreeNode(10)))
print(isValidBST(t))  # False

t = TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(6), TreeNode(10)))
print(isValidBST(t))  # True
