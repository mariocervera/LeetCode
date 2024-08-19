
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    min_diff = float("inf")
    prev_node = None

    def get_min_difference_rec(node):
        nonlocal min_diff, prev_node
        if not node:
            return
        get_min_difference_rec(node.left)
        if prev_node:
            min_diff = min(min_diff, abs(prev_node.val - node.val))
        prev_node = node
        get_min_difference_rec(node.right)

    get_min_difference_rec(root)
    return min_diff

t = TreeNode(8, TreeNode(3, TreeNode(0)), TreeNode(11))
print(getMinimumDifference(t))