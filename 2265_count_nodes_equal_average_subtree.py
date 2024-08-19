

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def averageOfSubtree(root):
    res = 0

    def dfs(node):
        nonlocal res
        if not node:
            return 0, 0
        counter_left, sum_left = dfs(node.left)
        counter_right, sum_right = dfs(node.right)
        counter_this, sum_this = counter_left + counter_right + 1, sum_left + sum_right + node.val
        avg = sum_this // counter_this
        if avg == node.val:
            res += 1
        return counter_this, sum_this

    dfs(root)
    return res



t = TreeNode(4,
             TreeNode(8,
                      TreeNode(0),
                      TreeNode(1)),
             TreeNode(5,
                      None,
                      TreeNode(6)))

print(averageOfSubtree(t))  # 5
