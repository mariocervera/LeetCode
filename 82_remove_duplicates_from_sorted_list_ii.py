
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s


def get_group_data(node):
    value, prev, i = node.val, None, 0
    while node and node.val == value:
        prev = node
        node = node.next
        i += 1
    return prev, i


def deleteDuplicates(head):
    dummy = ListNode(0, head)
    p1, p2 = dummy, head
    while p2:
        group_tail, group_count = get_group_data(p2)
        if group_count == 1:
            p1.next = group_tail
            p1 = p1.next
        p2 = group_tail.next
    p1.next = None
    return dummy.next


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
print(deleteDuplicates(l1))  #  1 -> 2 -> 5

l2 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
print(deleteDuplicates(l2))  #  2 -> 3

l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(3))))
print(deleteDuplicates(l3))  #  1 -> 2

l4 = ListNode(1, ListNode(2, ListNode(2)))
print(deleteDuplicates(l4))  #  1
