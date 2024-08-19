
class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self, board, words):
        self.root = TrieNode()
        self.__build_trie(board, words)

    def __build_trie(self, board, words):
        m, n = len(board), len(board[0])
        chars = set()
        for word in words:
            chars |= set(word)

        def backtrack(parent_node, i, j, visited, depth):
            position = (i, j)
            if depth >= 10 or not (0 <= i < m) or not (0 <= j < n) or position in visited or board[i][j] not in chars:
                return
            visited.add(position)
            if board[i][j] not in parent_node.children:
                parent_node.children[board[i][j]] = TrieNode()
            child_node = parent_node.children[board[i][j]]
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i + d[0], j + d[1]
                backtrack(child_node, new_i, new_j, visited, depth+1)
            visited.remove(position)

        for row in range(m):
            for column in range(n):
                backtrack(self.root, row, column, set(), 0)


    def search(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True


def findWords(board, words):
    t = Trie(board, words)
    return [word for word in words if t.search(word)]


print(findWords(board=[["o", "a", "a", "n"],
                       ["e", "t", "a", "e"],
                       ["i", "h", "k", "r"],
                       ["i", "f", "l", "v"]],
                words=["oath", "pea", "eat", "rain"]))  # ["eat","oath"]

print(findWords(board=[["a", "b"],
                       ["c", "d"]],
                words=["abcb"]))  # []

print(findWords(board=[["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                       ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]],
                words=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))

