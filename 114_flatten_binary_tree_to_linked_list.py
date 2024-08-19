
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    if not root:
        return None

    def __flatten_rec(node):
        if not node:
            return None, None
        if not node.left and not node.right:
            return node, node
        head_left, tail_left = __flatten_rec(node.left)
        head_right, tail_right = __flatten_rec(node.right)
        node.left = None
        if head_left:
            tail_left.right = head_right
            node.right = head_left
            return node, (tail_right if tail_right else tail_left)
        node.right = head_right
        return node, tail_right

    return __flatten_rec(root)[0]



t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
flatten(t)
print(t)