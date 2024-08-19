
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_depth(node, node_depth):
    if not node:
        return -1
    left_depth = dfs_depth(node.left, node_depth + 1)
    right_depth = dfs_depth(node.right, node_depth + 1)
    return max(left_depth, right_depth) + 1


def lca(node, node_depth, tree_depth):
    if not node or node_depth == tree_depth:
        return node
    left = lca(node.left, node_depth + 1, tree_depth)
    right = lca(node.right, node_depth + 1, tree_depth)
    return node if left and right else left or right


def lcaDeepestLeaves(root):
    tree_depth = dfs_depth(root, 0)
    return lca(root, 0, tree_depth)




t = TreeNode(3,
             TreeNode(5,
                      TreeNode(6),
                      TreeNode(2,
                               TreeNode(7),
                               TreeNode(4))),
             TreeNode(1,
                      TreeNode(0),
                      TreeNode(8)))

lca = lcaDeepestLeaves(t)
print(lca.val)  # 2
