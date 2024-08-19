
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(node):
    height = 0
    while node.left:
        node = node.left
        height += 1
    return height


def count_nodes_full_bt(height):
    return 2 ** (height + 1) - 1


def count_nodes_complete_bt(node, height):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    p, h = node.left, 1
    while p.right:
        p = p.right
        h += 1
    if h == height:
        return 1 + count_nodes_full_bt(height-1) + count_nodes_complete_bt(node.right, height-1)
    return 1 + count_nodes_complete_bt(node.left, height-1) + count_nodes_full_bt(height-2)


def countNodes(root):
    if not root:
        return 0
    height = get_height(root)
    return count_nodes_complete_bt(root, height)



t1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))
print(countNodes(t1))  # 6

t2 = TreeNode(1)
print(countNodes(t2))  # 1

print(countNodes(None))  # 0
