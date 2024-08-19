from collections import defaultdict

def totalFruit(fruits):
    window = defaultdict(int)
    i, n = 0, len(fruits)
    res = 0
    for j in range(n):
        window[fruits[j]] += 1
        while len(window) > 2:
            window[fruits[i]] -= 1
            if window[fruits[i]] == 0:
                window.pop(fruits[i])
            i += 1
        res = max(res, j-i+1)
    return res


print(totalFruit([1, 2, 1]))  # 3
print(totalFruit([0, 1, 2, 2]))  # 3
print(totalFruit([1, 2, 3, 2, 2]))  # 4
print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # 5
