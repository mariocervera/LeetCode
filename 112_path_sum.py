
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False
    targetSum -= root.val
    if not root.left and not root.right and targetSum == 0:
        return True
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)



t = TreeNode(5,
             TreeNode(4,
                      TreeNode(11,
                               TreeNode(7),
                               TreeNode(2))),
             TreeNode(8,
                      TreeNode(13),
                      TreeNode(4,
                               None,
                               TreeNode(1))))


print(hasPathSum(t, 22))  # True
print(hasPathSum(t, 23))  # False

