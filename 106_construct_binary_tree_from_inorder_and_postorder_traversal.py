
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = postorder[-1]
    left_subtree_size = inorder.index(root)
    return TreeNode(
        root,
        buildTree(inorder[:left_subtree_size], postorder[:left_subtree_size]),
        buildTree(inorder[left_subtree_size+1:], postorder[left_subtree_size:len(postorder)-1]),
    )


t = buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print(t)
