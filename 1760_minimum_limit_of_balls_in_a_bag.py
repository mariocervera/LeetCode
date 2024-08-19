
def is_penalty_possible(nums, target, max_ops):
    ops = 0
    for num in nums:
        x = num // target
        if num % target == 0:
            x -= 1
        ops += x
        if ops > max_ops:
            return False
    return True


def minimumSize(nums, maxOperations):
    low, high = 1, max(nums)
    while low < high:
        penalty = low + (high - low) // 2
        if is_penalty_possible(nums, penalty, maxOperations):
            high = penalty
        else:
            low = penalty+1
    return low


print(minimumSize(nums=[9], maxOperations=2))  # 3
print(minimumSize(nums=[2, 4, 8, 2], maxOperations=4))  # 2
print(minimumSize(nums=[7, 17], maxOperations=2))  # 7
