

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"{self.val}"
        if self.next:
            s += f" -> {self.next}"
        return s



def reverseKGroup(head, k):
    p1, p2 = head, head.next
    tail_of_prev_group, tail_of_group, head_of_group = None, head, None
    node_to_return = None
    while True:
        p, i = p1, 0
        while p:
            p = p.next
            i += 1
        if i < k:
            tail_of_prev_group.next = p1
            return node_to_return
        i = 0
        p1.next = None
        while p2 and i < k-1:
            aux = p2.next
            p2.next = p1
            p1, p2 = p2, aux
            i += 1
        if not node_to_return:
            node_to_return = p1
        head_of_group = p1
        if tail_of_prev_group:
            tail_of_prev_group.next = head_of_group
        tail_of_prev_group = tail_of_group
        tail_of_group = p2
        if not p2:
            break
        p1 = p2
        p2 = p2.next
    return node_to_return


#l0 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
# l0 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
# print(reverseKGroup(l0, 3))


l0 = ListNode(1, ListNode(2, ListNode(3)))
print(reverseKGroup(l0, 1))  # 1 -> 2 -> 3

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
print(reverseKGroup(l1, 2))  # 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 7

l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
print(reverseKGroup(l2, 3))  # 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7

l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(reverseKGroup(l3, 3))  # 3 -> 2 -> 1 -> 6 -> 5 -> 4

l4 = ListNode(1, ListNode(2, ListNode(3)))
print(reverseKGroup(l4, 3))  # 3 -> 2 -> 1

l5 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverseKGroup(l5, 3))  # 3 -> 2 -> 1 -> 4 -> 5