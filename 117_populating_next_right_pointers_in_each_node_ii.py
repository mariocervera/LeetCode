
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    p = root
    while p:
        next_level_dummy = p_child = Node()
        while p:
            if p.left:
                p_child.next = p.left
                p_child = p_child.next
            if p.right:
                p_child.next = p.right
                p_child = p_child.next
            p = p.next
        p = next_level_dummy.next
    return root


tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
res = connect(tree)
print(res)
