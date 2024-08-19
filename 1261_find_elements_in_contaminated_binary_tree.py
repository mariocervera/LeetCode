
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root=None):
        self.root = root
        self.root.val = 0
        self.__dfs(root)

    def __dfs(self, node):
        if not node:
            return
        if node.left:
            node.left.val = node.val * 2 + 1
        self.__dfs(node.left)
        if node.right:
            node.right.val = node.val * 2 + 2
        self.__dfs(node.right)

    def find(self, target):
        if target == 0:
            return True
        current_node = self.root
        for bit in bin(target+1)[3:]:
            if bit == '0':
                if not current_node.left:
                    return False
                current_node = current_node.left
            else:
                if not current_node.right:
                    return False
                current_node = current_node.right
            if current_node.val == target:
                return True
        return False


t = TreeNode(-1,
             TreeNode(-1,
                      TreeNode(-1),
                      TreeNode(-1)),
             TreeNode(-1))


fe = FindElements(t)
print(fe.find(1))  # True
print(fe.find(3))  # True
print(fe.find(5))  # False