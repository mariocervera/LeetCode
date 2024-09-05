def closest_target(words, target, start):
    res, n = float("inf"), len(words)
    for i in range(n):
        if words[i] == target:
            dist = abs(i - start)
            res = min(res, dist, n - dist)
    return res if res != float("inf") else -1


print(closest_target(words=["hello", "i", "am", "leetcode", "hello"], target="hello", start=2))  # 2
print(closest_target(words=["a", "b", "leetcode"], target="leetcode", start=0))  # 1
print(closest_target(words=["i", "eat", "leetcode"], target="ate", start=0))  # -1
