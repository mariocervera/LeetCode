
class LRUCacheNode:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt


class LRUCache:
    def __init__(self, capacity):
        self.ht = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key):
        if key not in self.ht:
            return -1
        node_to_return = self.ht[key]
        self.__move_to_front(node_to_return)
        return node_to_return.value

    def put(self, key, value):
        if key not in self.ht:
            new_node = LRUCacheNode(key, value)
            self.ht[key] = new_node
            if not self.capacity:
                self.__evict_lru()
            else:
                self.capacity -= 1
        self.ht[key].value = value
        self.__move_to_front(self.ht[key])

    def __move_to_front(self, node):
        if self.head == node:
            return
        if not self.head:
            self.head = self.tail = node
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.tail == node:
            self.tail = self.tail.next
        node.prev = self.head
        node.next = None
        self.head.next = node
        self.head = node

    def __evict_lru(self):
        self.ht.pop(self.tail.key)
        new_tail = self.tail.next
        if new_tail:
            new_tail.prev = None
        self.tail = new_tail
        if not self.tail:
            self.head = None


lru_cache = LRUCache(1)
print(lru_cache.get(6))
print(lru_cache.get(8))
lru_cache.put(12, 1)
print(lru_cache.get(2))
lru_cache.put(15, 11)
lru_cache.put(5, 2)
lru_cache.put(1, 15)
lru_cache.put(4, 2)
print(lru_cache.get(5))
lru_cache.put(15, 15)


# lru_cache = LRUCache(2)
# lru_cache.put(1, 1)  # {1=1}
# lru_cache.put(2, 2)  # {1=1, 2=2}
# print(lru_cache.get(1))         # 1
# lru_cache.put(3, 3)  # {1=1, 3=3}
# print(lru_cache.get(2))         # -1
# lru_cache.put(4, 4)  # {4=4, 3=3}
# print(lru_cache.get(1))         # -1
# print(lru_cache.get(3))         # 3
# print(lru_cache.get(4))         # 4

# lru_cache = LRUCache(1)
# lru_cache.put(2, 1)
# print(lru_cache.get(2))  # 1
# lru_cache.put(3, 2)
# print(lru_cache.get(2))  # -1
# print(lru_cache.get(3))  # 2


# lru_cache = LRUCache(2)
# lru_cache.put(2, 1)
# lru_cache.put(2, 2)
# print(lru_cache.get(2))  # 2
# lru_cache.put(1, 1)
# lru_cache.put(4, 1)
# print(lru_cache.get(2))  # -1