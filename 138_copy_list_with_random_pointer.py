
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None

    head_clone = Node(head.val)

    p_prev, p = head, head.next
    p_clone = head_clone
    while p:
        new_node = Node(p.val)
        p_clone.next = new_node
        p_clone.random = p_prev
        p_prev = p
        p, p_clone = p.next, p_clone.next
    p_clone.random = p_prev

    p, p_clone = head, head_clone
    while p:
        aux = p.next
        p.next = p_clone
        p, p_clone = aux, p_clone.next

    p_clone = head_clone
    while p_clone:
        p_clone.random = p_clone.random.random.next if p_clone.random.random else None
        p_clone = p_clone.next

    return head_clone


n5 = Node(1)
n4 = Node(10, n5)
n3 = Node(11, n4, n5)
n2 = Node(13, n3)
n1 = Node(7, n2, None)
n2.random = n1
n4.random = n3
n5.random = n1

result = copyRandomList(n1)
print(result)
