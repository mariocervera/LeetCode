
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):

    counter = 0

    def in_order(node):
        nonlocal counter
        if not node:
            return None
        ans = in_order(node.left)
        if ans is not None:
            return ans
        counter += 1
        if counter == k:
            return node.val
        ans = in_order(node.right)
        if ans is not None:
            return ans

    return in_order(root)



t = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(kthSmallest(t, 3)) # 3
print(kthSmallest(t, 4)) # 4