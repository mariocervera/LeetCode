from collections import Counter

def can_create_sequence(counters, num, k):
    for i in range(num, num + k):
        if i not in counters or counters[i] == 0:
            return False
        counters[i] -= 1
    return True

def isPossibleDivide(nums, k) -> bool:
    nums.sort()
    counters = Counter(nums)
    for num in nums:
        if counters[num] > 0 and not can_create_sequence(counters, num, k):
            return False
    return True



print(isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))  # True
print(isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3))  # True
print(isPossibleDivide(nums=[1, 2, 3, 4], k=3))  # False
