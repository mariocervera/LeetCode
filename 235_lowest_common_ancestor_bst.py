class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if not root or root.val == p.val or root.val == q.val or \
            (p.val < root.val < q.val) or \
            (p.val > root.val > q.val):
        return root
    if p.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    return lowestCommonAncestor(root.right, p, q)


t = TreeNode(6,
             TreeNode(2,
                      TreeNode(0),
                      TreeNode(4,
                               TreeNode(3),
                               TreeNode(5))),
             TreeNode(8,
                      TreeNode(7),
                      TreeNode(9)))

print(lowestCommonAncestor(t, t.left.right.left, t.left.right.right).val)  # 6
