
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


def get_candidates(c):
    return c if c != "." else tuple("abcdefghijklmnopqrstuvwxyz")


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.is_word = True

    def search(self, word):
        return self.__search_rec(self.root, word)

    def __search_rec(self, node, word):
        if len(word) == 0:
            return node.is_word
        rest_of_word = word[1:]
        candidates = get_candidates(word[0])
        for candidate in candidates:
            if candidate in node.children and self.__search_rec(node.children[candidate], rest_of_word):
                return True
        return False


obj = WordDictionary()
obj.addWord("hello")
obj.addWord("hell")
obj.addWord("heck")

print(obj.search("hello"))  # True
print(obj.search("hell"))   # True
print(obj.search("hel."))   # True
print(obj.search("hel.."))  # True
print("------------")
print(obj.search("hel"))    # False
print(obj.search("a"))      # False
print(obj.search("a.."))    # False
