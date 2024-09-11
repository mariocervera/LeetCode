
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_target_and_dirs_from(root, target):
    directions = []

    def dfs(node):
        if not node:
            return None
        if node.val == target:
            return node
        if node.left:
            directions.append("L")
            target_node = dfs(node.left)
            if target_node:
                return target_node
            directions.pop()
        if node.right:
            directions.append("R")
            target_node = dfs(node.right)
            if target_node:
                return target_node
            directions.pop()

    return dfs(root), directions


def get_common_prefix(arr_1, arr_2):
    res = []
    i, n = 0, min(len(arr_1), len(arr_2))
    while i < n and arr_1[i] == arr_2[i]:
        res.append(arr_1[i])
        i += 1
    return res


def getDirections(root, start_value, dest_value):
    node_start, dirs_to_start = get_target_and_dirs_from(root, start_value)
    node_target_from_start, dirs_to_target_from_start = get_target_and_dirs_from(node_start, dest_value)

    if node_target_from_start:
        return "".join(dirs_to_target_from_start)

    node_target, dirs_to_target = get_target_and_dirs_from(root, dest_value)
    node_start_from_target, dirs_to_start_from_target = get_target_and_dirs_from(node_target, start_value)

    if node_start_from_target:
        return "".join(["U"] * len(dirs_to_start_from_target))

    common_prefix = get_common_prefix(dirs_to_start, dirs_to_target)
    return "".join(["U"] * (len(dirs_to_start) - len(common_prefix)) + dirs_to_target[len(common_prefix):])


t1 = TreeNode(5,
              TreeNode(1,
                       TreeNode(3)),
              TreeNode(2,
                       TreeNode(6),
                       TreeNode(4)))
print(getDirections(root=t1, start_value=3, dest_value=6))  # "UURL"


t2 = TreeNode(2, TreeNode(1))
print(getDirections(root=t2, start_value=2, dest_value=1))  # "L"


t3 = TreeNode(2,
              TreeNode(8,
                       TreeNode(7),
                       TreeNode(5)),
              TreeNode(9,
                       TreeNode(1,
                                None,
                                TreeNode(4)),
                       TreeNode(6,
                                None,
                                TreeNode(3))))
print(getDirections(root=t3, start_value=9, dest_value=3))  # "RR"
