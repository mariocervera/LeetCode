class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def insert_min(root, node_to_insert):
    node = root
    while node.left:
        node = node.left
    node.left = node_to_insert


def search(root, key, parent=None):
    if not root:
        return None, None
    if root.val == key:
        return root, parent
    return search(root.left, key, root) if key < root.val else search(root.right, key, root)


def deleteNode(root, key):
    node_to_delete, parent_node = search(root, key)
    if not node_to_delete:
        return root
    new_subtree_root = None
    if not node_to_delete.left:
        new_subtree_root = node_to_delete.right
    elif not node_to_delete.right:
        new_subtree_root = node_to_delete.left
    else:
        insert_min(node_to_delete.right, node_to_delete.left)
        new_subtree_root = node_to_delete.right
    if not parent_node:
        return new_subtree_root
    if (not new_subtree_root and parent_node.left == node_to_delete) or (new_subtree_root and new_subtree_root.val < parent_node.val):
        parent_node.left = new_subtree_root
    else:
        parent_node.right = new_subtree_root
    return root


t1 = TreeNode(5,
              TreeNode(3,
                       TreeNode(2),
                       TreeNode(4)),
              TreeNode(6,
                       None,
                       TreeNode(7)))
t_res = deleteNode(root=t1, key=3)
print(t_res)


t2 = TreeNode(5,
              TreeNode(2,
                       None,
                       TreeNode(4)),
              TreeNode(6,
                       None,
                       TreeNode(7)))
t_res = deleteNode(root=t2, key=0)
print(t_res)
