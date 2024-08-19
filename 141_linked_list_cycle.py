
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

tail = ListNode(-4)
l = ListNode(3, ListNode(2, ListNode(0, tail)))
tail.next = l.next

print(hasCycle(l)) # True

l = ListNode(3, ListNode(2, ListNode(0)))
print(hasCycle(l)) # false