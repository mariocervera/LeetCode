
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s


def mergeNodes(head):
    p1 = p2 = head
    while p2.next:
        _sum = 0
        p2 = p2.next
        while p2.val != 0:
            _sum += p2.val
            p2 = p2.next
        p1.next.val = _sum
        p1.next.next = p2.next
        p1 = p2
    return head.next



l1 = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
print(mergeNodes(l1))  # 4 -> 11


l2 = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
print(mergeNodes(l2))  # 1 -> 3 -> 4
