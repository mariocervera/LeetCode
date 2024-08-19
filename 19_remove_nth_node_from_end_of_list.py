

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s



def removeNthFromEnd(head, n):
    if n == 1 and not head.next:
        return None
    i, p1 = 0, head
    while i <= n and p1:
        p1 = p1.next
        i += 1
    if i == n and not p1:
        return head.next
    p2 = head
    while p1:
        p1, p2 = p1.next, p2.next
    p2.next = p2.next.next
    return head



l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(removeNthFromEnd(l1, 2))  # 1 -> 2 -> 3 -> 5

l2 = ListNode(1)
print(removeNthFromEnd(l2, 1))  # None

l3 = ListNode(1, ListNode(2))
print(removeNthFromEnd(l3, 1))  # 1

l4 = ListNode(1, ListNode(2, ListNode(3)))
print(removeNthFromEnd(l4, 3))  # 2 -> 3

l5 = ListNode(1, ListNode(2, ListNode(3)))
print(removeNthFromEnd(l5, 2))  # 1 -> 3
