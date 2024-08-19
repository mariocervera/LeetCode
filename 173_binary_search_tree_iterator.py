
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.push_left_branches(root)

    def next(self) -> int:
        next_node = self.stack.pop()
        self.push_left_branches(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def push_left_branches(self, node):
        while node:
            self.stack.append(node)
            node = node.left


t = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))

it = BSTIterator(t)
print(it.hasNext())  # True
print(it.next())  # 3
print(it.next())  # 7
print(it.next())  # 9
print(it.next())  # 15
print(it.next())  # 20
print(it.hasNext())  # False
