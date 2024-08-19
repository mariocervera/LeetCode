
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def subtreeWithAllDeepest(root):
    max_depth = float("-inf")
    max_depth_node_counter = 0
    max_depth_node = None

    def dfs_depth(node, current_depth):
        nonlocal max_depth, max_depth_node_counter, max_depth_node
        if not node:
            return
        if current_depth > max_depth:
            max_depth = current_depth
            max_depth_node_counter = 1
            max_depth_node = node
        elif current_depth == max_depth:
            max_depth_node_counter += 1
        dfs_depth(node.left, current_depth + 1)
        dfs_depth(node.right, current_depth + 1)

    dfs_depth(root, 0)

    if max_depth_node_counter == 1:
        return max_depth_node

    def lowest_common_ancestor(node, current_depth):
        if not node or current_depth == max_depth:
            return node
        node_left = lowest_common_ancestor(node.left, current_depth + 1)
        node_right = lowest_common_ancestor(node.right, current_depth + 1)
        if node_left and node_right:
            return node
        return node_left or node_right

    return lowest_common_ancestor(root, 0)


t = TreeNode(3,
             TreeNode(5,
                      TreeNode(6,
                               TreeNode(1)),
                      TreeNode(2,
                               TreeNode(7),
                               TreeNode(4))),
             TreeNode(1,
                      TreeNode(0),
                      TreeNode(8)))

ans = subtreeWithAllDeepest(t)
print(ans)


t2 = TreeNode(1)
ans = subtreeWithAllDeepest(t2)
print(ans)