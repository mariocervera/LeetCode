
class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]


def minValidStrings(words, target):
    n = len(target)
    trie = Trie()
    for w in words:
        trie.insert(w)
    dp = [float("inf")] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        if dp[i] == float("inf") and target[i-1] not in trie.root.children:
            return -1
        current_node = trie.root
        j = i
        while j <= n and target[j-1] in current_node.children:
            current_node = current_node.children[target[j-1]]
            dp[j] = min(dp[j], dp[i-1] + 1)
            j += 1
    return dp[n]


print(minValidStrings(words=["abc", "aaaaa", "bcdef"], target="aabcdabc"))  # 3
print(minValidStrings(words=["abababab", "ab"], target="ababaababa"))  # 2
print(minValidStrings(words=["abcdef"], target="xyz"))  # -1
