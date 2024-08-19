class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    size_left_subtree = inorder.index(preorder[0])
    return TreeNode(
        preorder[0],
        buildTree(preorder[1:size_left_subtree+1], inorder[:size_left_subtree]),
        buildTree(preorder[size_left_subtree+1:], inorder[size_left_subtree+1:])
    )


node = buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
print(node)