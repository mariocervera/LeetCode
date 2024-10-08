
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {'-> ' + str(self.next) if self.next else ''}"


def mergeTwoLists(list1, list2):
    dummy = p = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            p.next = list1
            list1 = list1.next
        else:
            p.next = list2
            list2 = list2.next
        p = p.next
    p.next = list1 if list1 else list2
    return dummy.next


l1 = ListNode(1, ListNode(3, ListNode(4)))
l2 = ListNode(2, ListNode(5))
merged = mergeTwoLists(l1, l2)
print(merged)
