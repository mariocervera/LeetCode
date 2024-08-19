
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delNodes(root, to_delete):
    to_delete = set(to_delete)
    res = []

    def dfs(node, parent_exist):
        if node is None:
            return None
        if node.val in to_delete:
            node.left = dfs(node.left, False)
            node.right = dfs(node.right, False)
            return None
        else:
            if not parent_exist:
                res.append(node)
            node.left = dfs(node.left, True)
            node.right = dfs(node.right, True)
            return node

    dfs(root, False)
    return res


# t = TreeNode(1,
#              TreeNode(2,
#                       TreeNode(4),
#                       TreeNode(5)),
#              TreeNode(3,
#                       TreeNode(6),
#                       TreeNode(7)))
#
# arr = delNodes(t, [3, 5])
# print(arr)


t2 = TreeNode(1,
             TreeNode(2,
                      TreeNode(4),
                      TreeNode(3)),
             None)


arr2 = delNodes(t2, [2, 3])
print(arr2)
