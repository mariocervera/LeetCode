
class ListNode:
    def __init__(self, val, previous_node=None, next_node=None):
        self.value = val
        self.count = 1
        self.previous = previous_node
        self.next = next_node

    def __str__(self):
        return f"(value: \"{self.value}\", count: {self.count})"


class AllOne:

    def __init__(self):
        self.ht = {}
        self.min_node = None
        self.max_node = None

    def inc(self, key):
        if key not in self.ht:
            new_node = ListNode(key)
            self.ht[key] = new_node
            if self.min_node:
                new_node.next = self.min_node
                self.min_node.previous = new_node
            self.min_node = new_node
            if not self.max_node:
                self.max_node = new_node
        else:
            node = self.ht[key]
            if self.max_node == node:
                node.count += 1
                return
            p = node
            while p and p.count == node.count:
                p = p.next
            node.count += 1
            if p and p.previous == node:
                return
            if node.previous:
                node.previous.next = node.next
                node.next.previous = node.previous
            else:
                self.min_node = self.min_node.next
                self.min_node.previous = None
            if not p:
                self.max_node.next = node
                node.previous = self.max_node
                self.max_node = node
                node.next = None
            else:
                p.previous.next = node
                node.previous = p.previous
                node.next = p
                p.previous = node


    def dec(self, key):
        node = self.ht[key]
        if node.count == 1:
            self.__delete_node(key)
            return
        if self.min_node == node:
            node.count -= 1
            return
        p = node
        while p and p.count == node.count:
            p = p.previous
        node.count -= 1
        if p and p.next == node:
            return
        if node.next:
            node.previous.next = node.next
            node.next.previous = node.previous
        else:
            self.max_node = self.max_node.previous
            self.max_node.next = None
        if not p:
            self.min_node.previous = node
            node.next = self.min_node
            self.min_node = node
            node.previous = None
        else:
            p.next.previous = node
            node.next = p.next
            node.previous = p
            p.next = node


    def __delete_node(self, key):
        node = self.ht[key]
        self.ht.pop(key)
        if self.max_node == self.min_node == node:
            self.min_node = None
            self.max_node = None
            return
        if self.min_node == node:
            self.min_node = self.min_node.next
            self.min_node.previous = None
            return
        if self.max_node == node:
            self.max_node = self.max_node.previous
            self.max_node.next = None
            return
        node.previous.next = node.next
        node.next.previous = node.previous


    def getMaxKey(self):
        return self.max_node.value if self.max_node else ""

    def getMinKey(self):
        return self.min_node.value if self.min_node else ""


obj = AllOne()
obj.inc("hello")
obj.inc("hello")
obj.inc("world")
obj.inc("world")
obj.inc("hello")
obj.dec("world")
print(obj.getMaxKey())  # Hello  (3)
print(obj.getMinKey())  # World  (1)
obj.inc("world")
obj.inc("world")
obj.inc("leet")                                           # leet (1), hello (3), world (3)
print(obj.getMaxKey())  # Either hello or world
print(obj.getMinKey())  # leet
obj.inc("leet")
obj.inc("leet")                                            # leet (3), hello (3), world (3)
print(obj.getMinKey())   # Either hello, world or leet




# obj = AllOne()
# obj.inc("bye")
# obj.inc("talk")
# obj.inc("hello")
# obj.inc("bye")
# obj.inc("talk")
# obj.inc("hello")  # hello (2) <--> talk (2) <--> bye (2)
# obj.dec("talk")   # talk <--> hello (2) <--> bye (2)
# obj.dec("hello")   # talk <--> hello <--> bye (2)
# obj.dec("hello")   # talk <--> bye (2)
# print(obj)


# obj = AllOne()
# obj.inc("bye")
# obj.inc("talk")
# obj.inc("hello")
# obj.inc("bye")      # hello <--> talk <--> bye (2)
# obj.inc("talk")     # hello <--> talk (2) <--> bye (2)
# obj.inc("talk")     # hello <--> bye (2) <--> talk (3)
# obj.inc("hello")    # hello (2) <--> bye (2) <--> talk (3)
# obj.inc("hello")    # bye (2) <--> hello (3) <--> talk (3)
# obj.inc("bye")      # bye (3) <--> hello (3) <--> talk (3)
# obj.inc("bye")      # hello (3) <--> talk (3) <--> bye (4)
# print(obj)