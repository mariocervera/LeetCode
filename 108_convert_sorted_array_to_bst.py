class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    def get_bst(i,j):
        if i > j:
            return
        if i == j:
            return TreeNode(nums[i])
        mid = (i+j)//2
        return TreeNode(nums[mid], get_bst(i, mid-1), get_bst(mid+1, j))
    return get_bst(0,len(nums)-1)


root = sortedArrayToBST([1,2,3,4,5,6,7])
print(root)
