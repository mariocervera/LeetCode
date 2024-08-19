import collections
import math

mod = 10 ** 9 + 7

def n_choose_k(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def threeSumMulti(arr, target):
    multiplicities = collections.defaultdict(int)
    for num in arr:
        multiplicities[num] += 1
    arr = sorted(multiplicities.items())
    res, n = 0, len(arr)
    for num, counter in arr:
        if counter > 2 and num * 3 == target:
            res = (res + n_choose_k(counter, 3)) % mod
    if n > 1:
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i][1] > 1 and arr[i][0] * 2 + arr[j][0] == target:
                    res = (res + n_choose_k(arr[i][1], 2) * arr[j][1]) % mod
                if arr[j][1] > 1 and arr[i][0] + arr[j][0] * 2 == target:
                    res = (res + n_choose_k(arr[j][1], 2) * arr[i][1]) % mod
    if n > 2:
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                tuple_sum = arr[i][0] + arr[j][0] + arr[k][0]
                if tuple_sum == target:
                    res += (arr[i][1] * arr[j][1] * arr[k][1]) % mod
                if tuple_sum <= target:
                    j += 1
                else:
                    k -= 1
    return res


print(threeSumMulti(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8))  # 20
print(threeSumMulti(arr=[1, 1, 2, 2, 2, 2], target=5))  # 12
print(threeSumMulti(arr=[2, 1, 3], target=6))  # 1
