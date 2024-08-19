
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.is_word = True

    def search(self, word: str) -> bool:
        node = self.__get_node(word)
        return node and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self.__get_node(prefix) is not None

    def __get_node(self, word: str) -> TrieNode:
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return None
            current_node = current_node.children[c]
        return current_node


# Tests

obj = Trie()
obj.insert("apple")
obj.insert("app")
print(obj.search("app"))  # True
print(obj.search("apple"))  # True
print(obj.search("ap"))  # False
print(obj.startsWith("ap"))  # True
print(obj.startsWith("acp"))  # False
