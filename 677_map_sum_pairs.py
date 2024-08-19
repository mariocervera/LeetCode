
class TrieNode:
    def __init__(self):
        self.value = 0
        self.sum = 0
        self.children = {}

class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, val):
        self.__put(self.root, key, val, 0)

    def __put(self, node, key, val, i):
        if i == len(key):
            diff = val - node.value
            node.value = val
            node.sum += diff
            return diff
        if key[i] not in node.children:
            node.children[key[i]] = TrieNode()
        diff_put = self.__put(node.children[key[i]], key, val, i + 1)
        node.sum += diff_put
        return diff_put

    def sum(self, prefix):
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return 0
            current_node = current_node.children[c]
        return current_node.sum

m = MapSum()
m.insert("apple", 3)
print(m.sum("apple"))  # 3
m.insert("app", 2)
print(m.sum("ap"))  # 5


# m = MapSum()
# m.insert("apple", 3)
# print(m.sum("ap"))  # 3
# m.insert("app", 2)
# print(m.sum("ap"))  # 5


# m = MapSum()
# m.insert("apple", 3)
# print(m.sum("ap"))  # 3
# m.insert("app", 2)
# m.insert("apple", 2)
# print(m.sum("ap"))  # 4



