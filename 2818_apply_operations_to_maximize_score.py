
mod = 10**9 + 7


def fast_pow(x, n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * x) % mod
        x = (x * x) % mod
        n //= 2
    return res


def maximumScore(nums, k):
    n = len(nums)
    upper = max(nums) + 1

    prime = [True] * upper
    prime[0] = prime[1] = False
    factors = [0] * upper
    for i in range(2, upper):
        if prime[i]:
            for j in range(i, upper, i):
                factors[j] += 1
                prime[j] = False

    next_greater = [n] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and factors[nums[i]] >= factors[nums[stack[-1]]]:
            stack.pop()
        next_greater[i] = stack[-1] if stack else n
        stack.append(i)

    prev_greater_or_equal = [-1] * n
    stack = []
    for i in range(n):
        while stack and factors[nums[i]] > factors[nums[stack[-1]]]:
            stack.pop()
        prev_greater_or_equal[i] = stack[-1] if stack else -1
        stack.append(i)

    score = 1
    tuples = [(nums[i], i) for i in range(n)]
    tuples.sort(reverse=True)
    for num, index in tuples:
        number_of_ranges_for_num = (index - prev_greater_or_equal[index]) * (next_greater[index] - index)
        operations = min(number_of_ranges_for_num, k)
        score = (score * (fast_pow(num, operations))) % mod
        k -= operations
        if k == 0:
            return score

    return score



print(maximumScore(nums=[1,7,11,1,5], k=14))  # 823751938
print(maximumScore(nums=[3289,2832,14858,22011], k=6))  # 256720975
print(maximumScore(nums=[8, 3, 9, 3, 8], k=2))  # 81
print(maximumScore(nums=[19, 12, 14, 6, 10, 18], k=3))  # 4788
