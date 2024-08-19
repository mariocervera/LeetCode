
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s


def reverseBetween(head, left, right):
    if not head.next or left == right:
        return head
    prev = l_node = r_node = after = None
    i = 1
    current_node = head
    while i <= right:
        if i == left-1:
            prev = current_node
        elif i == left:
            l_node = current_node
        elif i == right:
            r_node = current_node
            after = current_node.next
        i += 1
        current_node = current_node.next
    p, p_next = l_node, l_node.next
    p.next = None
    while p != r_node:
        aux = p_next.next
        p_next.next = p
        p = p_next
        p_next = aux
    l_node.next = after
    if prev:
        prev.next = r_node
        return head
    return r_node



l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverseBetween(l1, 2, 4))  # 1 -> 4 -> 3 -> 2 -> 5

l2 = ListNode(5)
print(reverseBetween(l2, 1, 1))  # 5

l3 = ListNode(3, ListNode(5))
print(reverseBetween(l3, 1, 1))  # 3 -> 5
