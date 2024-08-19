class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + (f" -> {self.next}" if self.next else "")


def merge_lists(head1, head2):
    dummy = p = ListNode(0)
    p1, p2 = head1, head2
    while p1 and p2:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next
    p.next = p1 if p1 else p2
    return dummy.next


def sortList(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head2 = slow.next
    slow.next = None

    head = sortList(head)
    head2 = sortList(head2)

    return merge_lists(head, head2)


unordered_list = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(5)))))
print(sortList(unordered_list))  # 1 -> 2 -> 3 -> 4 -> 5
