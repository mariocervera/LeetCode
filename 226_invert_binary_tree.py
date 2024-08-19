
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root:
        return None
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.right = left
    root.left = right
    return root


t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted_t = invertTree(t)
print(inverted_t)