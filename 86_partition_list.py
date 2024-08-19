
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s


def partition(head, x):
    if not head or not head.next:
        return head
    dummy_1 = p1 = ListNode(0)
    dummy_2 = p2 = ListNode(0)
    p = head
    while p:
        if p.val < x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next
        p = p.next
    p1.next = dummy_2.next
    p2.next = None
    return dummy_1.next


l0 = ListNode(1, ListNode(4, ListNode(3, ListNode(0, ListNode(2, ListNode(5, ListNode(2)))))))
print(partition(l0, 3))  # 1 -> 0 -> 2 -> 2 -> 4 -> 3 -> 5

l1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print(partition(l1, 3))  # 1 -> 2 -> 2 -> 4 -> 3 -> 5

l2 = ListNode(2, ListNode(1))
print(partition(l2, 2))  # 1 -> 2
