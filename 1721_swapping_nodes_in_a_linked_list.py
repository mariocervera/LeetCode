
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = str(self.val)
        if self.next:
            s += f" -> {self.next}"
        return s


def swapNodes(head, k):
    p1, p2 = head, head
    for _ in range(k-1):
        p1 = p1.next
    kth_node_start = p1
    while p1.next:
        p1, p2 = p1.next, p2.next
    kth_node_end = p2
    kth_node_start.val, kth_node_end.val = kth_node_end.val, kth_node_start.val
    return head


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(swapNodes(l1, 2))  # 1 -> 4 -> 3 -> 2 -> 5

l2 = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8,ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
print(swapNodes(l2, 5))  # 7 -> 9 -> 6 -> 6 -> 8 -> 7 -> 3 -> 0 -> 9 -> 5

l3 = ListNode(1)
print(swapNodes(l3, 1))  # 1

l4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(swapNodes(l4, 3))  # 1 -> 2 -> 3 -> 4 -> 5
