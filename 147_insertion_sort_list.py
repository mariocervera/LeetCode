
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = str(self.val)
        if self.next:
            s += f" -> {self.next}"
        return s


def insertionSortList(head):
    dummy, p1 = ListNode(0), head
    while p1:
        p_next = p1.next
        p2 = dummy
        while p2:
            if not p2.next or p2.next.val >= p1.val:
                p1.next = p2.next
                p2.next = p1
                break
            p2 = p2.next
        p1 = p_next
    return dummy.next


l1 = ListNode(2, ListNode(5, ListNode(1, ListNode(4, ListNode(3)))))
print(insertionSortList(l1))
