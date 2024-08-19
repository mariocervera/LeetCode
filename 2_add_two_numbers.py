class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = str(self.val)
        p = self
        while p.next:
            s += f" -> {p.next.val}"
            p = p.next
        return s


def addTwoNumbers(l1, l2):
    dummy = p = ListNode()
    carry = 0
    while l1 and l2:
        _sum = l1.val + l2.val + carry
        p.next = ListNode((_sum % 10))
        carry = _sum // 10
        l1, l2, p = l1.next, l2.next, p.next
    l1 = l1 if l1 else l2
    while l1:
        _sum = l1.val + carry
        p.next = ListNode((_sum % 10))
        carry = _sum // 10
        l1, p = l1.next, p.next
    if carry:
        p.next = ListNode(1)
    return dummy.next


L1 = ListNode(2, ListNode(4, ListNode(3)))
L2 = ListNode(5, ListNode(6, ListNode(4)))
print(addTwoNumbers(L1,L2))

L1 = ListNode(2, ListNode(4, ListNode(3)))
L2 = ListNode(5, ListNode(6))
print(addTwoNumbers(L1,L2))

L1 = ListNode(6)
L2 = ListNode(5)
print(addTwoNumbers(L1,L2))