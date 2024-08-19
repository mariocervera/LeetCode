
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
def sumNumbers(root):
    res = 0
    number = []

    def dfs(node):
        nonlocal res, number
        if not node:
            return
        number.append(str(node.val))
        if not node.left and not node.right:
            res += int("".join(number))
        else:
            dfs(node.left)
            dfs(node.right)
        number.pop()

    dfs(root)
    return res
'''

'''
def dfs(node, _sum):
    if not node:
        return 0
    new_sum = _sum * 10 + node.val
    if not node.left and not node.right:
        return new_sum
    return dfs(node.left, new_sum) + dfs(node.right, new_sum)
'''

from collections import deque

def sumNumbers(root):
    if not root:
        return 0
    res, q = 0, deque([root])
    while q:
        node = q.popleft()
        if not node.left and not node.right:
            res += node.val
        if node.left:
            node.left.val += node.val * 10
            q.append(node.left)
        if node.right:
            node.right.val += node.val * 10
            q.append(node.right)
    return res


t1 = TreeNode(1,
              TreeNode(2),
              TreeNode(3))

print(sumNumbers(t1))  # 25


t2 = TreeNode(4,
              TreeNode(9,
                       TreeNode(5),
                       TreeNode(1)),
              TreeNode(0))

print(sumNumbers(t2))  # 1026
