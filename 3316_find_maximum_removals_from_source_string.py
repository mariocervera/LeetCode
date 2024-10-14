from functools import lru_cache


def maxRemovals(source, pattern, targetIndices):
    m, n = len(source), len(pattern)

    @lru_cache(maxsize=None)
    def backtrack(i, j, k):
        while i < m and j < n and (k == len(targetIndices) or i < targetIndices[k]):
            j += int(source[i] == pattern[j])
            i += 1

        if j == n:
            return len(targetIndices) - k
        if i == m:
            return float("-inf")

        return max(backtrack(i, j, k+1), 1 + backtrack(i+1, j, k+1))

    return backtrack(0, 0, 0)


print(maxRemovals(source="abbaa", pattern="aba", targetIndices=[0, 1, 2]))  # 1
print(maxRemovals(source="bcda", pattern="d", targetIndices=[0, 3]))  # 2
print(maxRemovals(source="dda", pattern="dda", targetIndices=[0, 1, 2]))  # 0
print(maxRemovals(source="yeyeykyded", pattern="yeyyd", targetIndices=[0, 2, 3, 4]))  # 2
