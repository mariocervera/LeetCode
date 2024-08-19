
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def recoverTree(root):
    prev_node, node_a, node_b = None, None, None

    def in_order_traversal(node):
        nonlocal prev_node, node_a, node_b
        if not node:
            return
        in_order_traversal(node.left)
        if prev_node is not None and prev_node.val > node.val:
            if node_a is None:
                node_a = prev_node
                node_b = node
            else:
                node_b = node
        prev_node = node
        in_order_traversal(node.right)

    in_order_traversal(root)
    node_a.val, node_b.val = node_b.val, node_a.val



t = TreeNode(3,
             TreeNode(1),
             TreeNode(4,
                      TreeNode(2)))
recoverTree(t)
print(t)
