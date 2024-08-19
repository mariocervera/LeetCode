from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findFrequentTreeSum(root):
    frequencies = Counter()

    def post_order(node):
        if node is None:
            return 0
        subtree_sum = post_order(node.left) + post_order(node.right) + node.val
        frequencies[subtree_sum] += 1
        return subtree_sum

    post_order(root)
    max_freq = max(frequencies.values())
    return [s for s in frequencies if frequencies[s] == max_freq]


t1 = TreeNode(5,
              TreeNode(2),
              TreeNode(-3))

print(findFrequentTreeSum(t1))  # [2,-3,4]


t2 = TreeNode(5,
              TreeNode(2),
              TreeNode(-5))

print(findFrequentTreeSum(t2))  # [2]
