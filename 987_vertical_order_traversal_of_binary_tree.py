
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_column_counts(source_node):
    columns_to_left, columns_to_right = 1, -1

    def dfs(node, node_column):
        nonlocal columns_to_left, columns_to_right
        if not node:
            return
        columns_to_left = min(columns_to_left, node_column)
        columns_to_right = max(columns_to_right, node_column)
        dfs(node.left, node_column - 1)
        dfs(node.right, node_column + 1)

    dfs(source_node, 0)
    return columns_to_left * -1, columns_to_right


def get_columns(source_node, columns_to_left, columns_to_right):
    columns = [[] for _ in range(columns_to_left + columns_to_right + 1)]

    def dfs(node, row, column):
        if not node:
            return
        columns[column].append((row, node.val))
        dfs(node.left, row + 1, column - 1)
        dfs(node.right, row + 1, column + 1)

    dfs(source_node, 0, columns_to_left)
    sorted_columns = [sorted(column) for column in columns]
    return [[value for _, value in sorted_column] for sorted_column in sorted_columns]



def verticalTraversal(root):
    columns_to_left, columns_to_right = get_column_counts(root)
    return get_columns(root, columns_to_left, columns_to_right)


t1 = TreeNode(3,
             TreeNode(9),
             TreeNode(20,
                      TreeNode(15),
                      TreeNode(7)))

print(verticalTraversal(t1))  # [[9],[3,15],[20],[7]]



t2 = TreeNode(1,
             TreeNode(2,
                      TreeNode(4),
                      TreeNode(5)),
             TreeNode(3,
                      TreeNode(6),
                      TreeNode(7)))

print(verticalTraversal(t2))  # [[4],[2],[1,5,6],[3],[7]]
