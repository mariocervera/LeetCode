
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_tree_string(node):
    if not node:
        return "."
    return str(node.val) + get_tree_string(node.left) + get_tree_string(node.right)

def isSameTree(p, q):
    return get_tree_string(p) == get_tree_string(q)



t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(3))

print(isSameTree(t1, t2)) # True


t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2))


print(isSameTree(t1, t2)) # False


t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(4))

print(isSameTree(t1, t2)) # False
