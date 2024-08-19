
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = str(self.val)
        if self.next:
            s += f" -> {self.next}"
        return s


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def get_middle_nodes(head):
    if not head or not head.next:
        return head
    prev_slow, slow, fast = None, head, head
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    return prev_slow, slow

def sortedListToBST(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    prev_middle, middle = get_middle_nodes(head)
    prev_middle.next = None
    return TreeNode(middle.val,
                    sortedListToBST(head),
                    sortedListToBST(middle.next))



l0 = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
res = sortedListToBST(l0)
print(res)

#l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
#prev, mid = get_middle_nodes(l1)
#print(prev, mid)

#l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#prev, mid = get_middle_nodes(l2)
#print(prev, mid)
