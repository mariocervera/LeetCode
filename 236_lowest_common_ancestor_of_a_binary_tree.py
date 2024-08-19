
class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


def lowestCommonAncestor(root, p, q):
    def dfs(node):
        if node in (None, p, q):
            return node
        left = dfs(node.left)
        right = dfs(node.right)
        return node if left and right else left or right
    return dfs(root)


node_4 = TreeNode(4)

node_5 = TreeNode(5,
                      TreeNode(6),
                      TreeNode(2,
                               TreeNode(7),
                               node_4))

node_1 = TreeNode(1,
                      TreeNode(0),
                      TreeNode(8))


t = TreeNode(3, node_5, node_1)

print(lowestCommonAncestor(t, node_5, node_1).val)  # 3
print(lowestCommonAncestor(t, node_5, node_4).val)  # 5
