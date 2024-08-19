from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isEvenOddTree(root):
    q = deque([root])
    level = 0
    while q:
        last_node = None
        for _ in range(len(q)):
            current_node = q.popleft()
            if level % 2 == 0 and (current_node.val % 2 == 0 or (last_node is not None and last_node.val >= current_node.val)):
                return False
            if level % 2 != 0 and (current_node.val % 2 != 0 or (last_node is not None and last_node.val <= current_node.val)):
                return False
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            last_node = current_node
        level += 1
    return True


t1 = TreeNode(1,
             TreeNode(10,
                      TreeNode(3,
                               TreeNode(12),
                               TreeNode(8)),
                      None),
             TreeNode(4,
                      TreeNode(7,
                               TreeNode(6),
                               None),
                      TreeNode(9,
                               None,
                               TreeNode(2))))

print(isEvenOddTree(t1))  # True

print("----------------------------------------------")

t2 = TreeNode(5,
              TreeNode(4,
                       TreeNode(3),
                       TreeNode(3)),
              TreeNode(2,
                       TreeNode(7),
                       None))

print(isEvenOddTree(t2))  # False

print("----------------------------------------------")

t3 = TreeNode(5,
              TreeNode(9,
                       TreeNode(3),
                       TreeNode(5)),
              TreeNode(1,
                       TreeNode(7),
                       None))

print(isEvenOddTree(t3))  # False
