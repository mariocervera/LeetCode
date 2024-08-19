class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, targetSum):
    res = []

    if not root:
        return res

    def dfs(node, path, target_sum):
        if not node:
            return
        if not node.left and not node.right and target_sum == 0:
            res.append(path.copy())
            return
        if node.left:
            path.append(node.left.val)
            dfs(node.left, path, target_sum - node.left.val)
            path.pop()
        if node.right:
            path.append(node.right.val)
            dfs(node.right, path, target_sum - node.right.val)
            path.pop()

    dfs(root, [root.val], targetSum-root.val)
    return res


t1 = TreeNode(5,
             TreeNode(4,
                      TreeNode(11,
                               TreeNode(7),
                               TreeNode(2))),
             TreeNode(8,
                      TreeNode(13),
                      TreeNode(4,
                               TreeNode(5),
                               TreeNode(1))))

print(pathSum(t1, 22))  # [[5,4,11,2],[5,8,4,5]]


t2 = TreeNode(1,
              TreeNode(2),
              TreeNode(3))

print(pathSum(t2, 5))  # []
