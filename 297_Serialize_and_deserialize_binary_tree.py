
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Codec:
    def serialize(self, root):
        traversal = []
        def pre_order(node):
            if not node:
                traversal.append("N")
                return
            traversal.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)
        pre_order(root)
        return ",".join(traversal)

    def deserialize(self, data):
        tree_arr = data.split(",")
        def deserialize_tree(i):
            if tree_arr[i] == "N":
                return None, i+1
            node = TreeNode(tree_arr[i])
            node.left, i_right = deserialize_tree(i+1)
            node.right, i_next_node = deserialize_tree(i_right)
            return node, i_next_node
        tree, _ = deserialize_tree(0)
        return tree


c = Codec()
t = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized_tree = c.serialize(t)  # 1,2,N,N,3,4,N,N,5,N,N
deserialized_tree = c.deserialize(serialized_tree)
print(deserialized_tree)
