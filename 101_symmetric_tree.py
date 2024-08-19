
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_two_pointers(regular_node, symmetric_node):
    if not regular_node and not symmetric_node:
        return True

    if not regular_node or not symmetric_node or \
            not in_order_two_pointers(regular_node.left, symmetric_node.right) or \
            regular_node.val != symmetric_node.val or \
            not in_order_two_pointers(regular_node.right, symmetric_node.left):
        return False

    return True

def isSymmetric(root):
    return in_order_two_pointers(root.left, root.right)


t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(isSymmetric(t))  # True

t = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(isSymmetric(t))  # False

t = TreeNode(1, TreeNode(2, TreeNode(2), None), TreeNode(2, TreeNode(2)))
print(isSymmetric(t))  # False
