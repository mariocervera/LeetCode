from collections import Counter


def minSetSize(arr):
    freq_sum, res = 0, 1
    for freq in sorted(list(Counter(arr).values()), reverse=True):
        freq_sum += freq
        if freq_sum >= len(arr) // 2:
            return res
        res += 1
    return res


print(minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))  # 2
print(minSetSize([7, 7, 7, 7, 7, 7]))  # 1
print(minSetSize([1, 9]))  # 1
