from collections import defaultdict

class ListNode:
    def __init__(self, k=None, v=None):
        self.key = k
        self.value = v
        self.freq = 1
        self.next = None
        self.prev = None

# An OrderedDict could be used instead since we only need insertion order (and
# constant-time insertion and deletion).
class DLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.dummy.next = self.dummy.prev = self.dummy

    def insert(self, node):
        node.next = self.dummy.next
        node.prev = self.dummy
        node.next.prev = node
        self.dummy.next = node

    def pop(self, node=None):
        if self.dummy == self.dummy.prev:
            return
        if node is None:
            node = self.dummy.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def is_empty(self):
        return self.dummy == self.dummy.next


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.nodes = {}
        self.frequencies = defaultdict(DLinkedList)
        self.min_freq = 0

    def get(self, key):
        self.__update(key)
        if key not in self.nodes:
            return -1
        return self.nodes[key].value

    def put(self, key, value):
        if key not in self.nodes:
            self.__insert_new_element(key, value)
            return
        self.__update(key)
        self.nodes[key].value = value

    def __update(self, key):
        if key not in self.nodes:
            return
        node = self.nodes[key]
        freq_list = self.frequencies[node.freq]
        freq_list.pop(node)
        if freq_list.is_empty() and self.min_freq == node.freq:
            self.min_freq += 1
        node.freq += 1
        self.frequencies[node.freq].insert(node)

    def __insert_new_element(self, key, value):
        if self.size == self.capacity:
            invalidated_node = self.frequencies[self.min_freq].pop()
            self.nodes.pop(invalidated_node.key)
            self.size -= 1
        new_node = ListNode(key, value)
        self.nodes[key] = new_node
        self.frequencies[1].insert(new_node)
        self.min_freq = 1
        self.size += 1


# Test

cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)
print(cache.get(2))  # -1
print(cache.get(3))  # 3
cache.put(4, 4)
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
