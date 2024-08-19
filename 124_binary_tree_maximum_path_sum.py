
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def maxPathSum(root):
#     max_sum = float("-inf")
#
#     def dfs(node):
#         nonlocal max_sum
#         if not node:
#             return float("-inf")
#         best_left = dfs(node.left)
#         best_right = dfs(node.right)
#         max_sum = max(max_sum, node.val, best_left, best_right, best_left + node.val, best_right + node.val, best_left + best_right + node.val)
#
#         return max(best_left + node.val, best_right + node.val, node.val)
#
#     dfs(root)
#     return max_sum


def maxPathSum(root):
    max_sum = float("-inf")
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        best_left = max(dfs(node.left), 0)
        best_right = max(dfs(node.right), 0)
        current_max = node.val + best_left + best_right
        max_sum = max(max_sum, current_max)
        return node.val + max(best_left, best_right)
    dfs(root)
    return max_sum


t0 = TreeNode(-3)
print(maxPathSum(t0))  # -3


t1 = TreeNode(1,
              TreeNode(2),
              TreeNode(3))

print(maxPathSum(t1))  # 6


t2 = TreeNode(-10,
              TreeNode(9),
              TreeNode(20,
                       TreeNode(15),
                       TreeNode(7)))

print(maxPathSum(t2))  # 42
