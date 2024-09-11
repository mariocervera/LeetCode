from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_swaps_to_make_sorted(arr):
    res, n = 0, len(arr)
    visited = [False] * n
    indexes_in_sorted_arr = {num: i for i, num in enumerate(sorted(arr))}
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            original_index = i
            steps = 1
            index = indexes_in_sorted_arr[arr[i]]
            while index != original_index:
                visited[index] = True
                index = indexes_in_sorted_arr[arr[index]]
                steps += 1
            res += (steps - 1)
    return res



def minimumOperations(root):
    q = deque([root])
    swaps = 0
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        swaps += min_swaps_to_make_sorted(level)
    return swaps


t1 = TreeNode(1,
              TreeNode(4,
                       TreeNode(7),
                       TreeNode(6)),
              TreeNode(3,
                       TreeNode(8,
                                TreeNode(9)),
                       TreeNode(5,
                                TreeNode(10))))

print(minimumOperations(t1))  # 3


t2 = TreeNode(1,
              TreeNode(3,
                       TreeNode(7),
                       TreeNode(6)),
              TreeNode(2,
                       TreeNode(5),
                       TreeNode(4)))

print(minimumOperations(t2))  # 3


t3 = TreeNode(1,
              TreeNode(2,
                       TreeNode(4),
                       TreeNode(5)),
              TreeNode(3,
                       TreeNode(6)))

print(minimumOperations(t3))  # 0
