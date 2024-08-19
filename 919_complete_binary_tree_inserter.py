from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class CBTInserter:
    def __init__(self, root):
        self.arr = [None]
        q = deque([root])
        while q:
            self.arr.append(q.popleft())
            if self.arr[-1].left:
                q.append(self.arr[-1].left)
            if self.arr[-1].right:
                q.append(self.arr[-1].right)

    def insert(self, val):
        new_node = TreeNode(val)
        self.arr.append(new_node)
        new_node_index = len(self.arr)-1
        parent = self.arr[new_node_index // 2]
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
        return parent.val

    def get_root(self):
        return self.arr[1]


t = TreeNode(1)

obj = CBTInserter(t)
print(obj.insert(2))  # 1
print(obj.insert(3))  # 1
print(obj.insert(4))  # 2
print(obj.insert(5))  # 2
print(obj.insert(6))  # 3
r = obj.get_root()
print(r)
