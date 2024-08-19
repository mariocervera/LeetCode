
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s


def rotateRight(head, k):
    if not head or not head.next:
        return head
    p, n = head, 1
    while p.next:
        p, n = p.next, n+1
    tail = p
    k %= n
    if not k:
        return head
    p, p1, p2 = head, head, head.next
    for _ in range(k):
        p = p.next
    while p.next:
        p = p.next
        p1 = p2
        p2 = p2.next
    p1.next = None
    tail.next = head
    return p2


l0 = ListNode(1)
print(rotateRight(l0, 1))  # 1

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(rotateRight(l1, 2))  # 4 -> 5 -> 1 -> 2 -> 3

l2 = ListNode(0, ListNode(1, ListNode(2)))
print(rotateRight(l2, 0))  # 0 -> 1 -> 2

l3 = ListNode(0, ListNode(1, ListNode(2)))
print(rotateRight(l3, 4))  # 2 -> 0 -> 1


