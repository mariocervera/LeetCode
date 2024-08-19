
def containsNearbyDuplicate(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if i > k:
            window.remove(nums[i-k-1])
        if nums[i] in window:
            return True
        window.add(nums[i])
    return False


print(containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))  # True
print(containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))  # True
print(containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))  # False
print(containsNearbyDuplicate(nums=[1, 0, 1, 1], k=2))  # True