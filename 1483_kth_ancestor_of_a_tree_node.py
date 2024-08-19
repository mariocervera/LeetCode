
class TreeAncestor:
    def __init__(self, n, parent):
        self.dp = [[-1 for _ in range(n)] for _ in range(17)]
        for node in range(n):
            self.dp[0][node] = parent[node]
        for i in range(1, 17):
            for node in range(n):
                node_parent = self.dp[i-1][node]
                if node_parent != -1:
                    self.dp[i][node] = self.dp[i-1][node_parent]

    def getKthAncestor(self, node, k):
        i, ancestor = 0, node
        while k:
            if k & 1:
                ancestor = self.dp[i][ancestor]
                if ancestor == -1:
                    return -1
            k >>= 1
            i += 1
        return ancestor


ta = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(ta.getKthAncestor(3, 1))  # 1
print(ta.getKthAncestor(5, 2))  # 0
print(ta.getKthAncestor(6, 3))  # -1
