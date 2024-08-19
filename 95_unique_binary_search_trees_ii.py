
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def generateTrees(n):

    def generate_trees(nodes):
        if not nodes:
            return [None]
        trees = []
        for i in range(len(nodes)):
            left_subtrees = generate_trees(nodes[:i])
            right_subtrees = generate_trees(nodes[i+1:])
            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    trees.append(TreeNode(nodes[i], left_subtree, right_subtree))
        return trees

    return generate_trees(list(range(1, n+1)))


res = generateTrees(3)
print(res)
