import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s


class WrapperNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


def mergeKLists(lists):
    pq = [WrapperNode(node) for node in lists if node]
    if not pq:
        return None
    heapq.heapify(pq)
    dummy = p = ListNode(0)
    while pq:
        node = heapq.heappop(pq).node
        p.next = node
        p = p.next
        if node.next:
            heapq.heappush(pq, WrapperNode(node.next))
    return dummy.next


l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))

print(mergeKLists([l1, l2, l3]))  # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
