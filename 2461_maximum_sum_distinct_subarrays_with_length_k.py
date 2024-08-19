from collections import defaultdict

def add_number(num, window_nums, dupes):
    if num not in window_nums:
        window_nums.add(num)
    else:
        dupes[num] += 1


def remove_number(num, window_nums, dupes):
    if num in dupes:
        dupes[num] -= 1
        if dupes[num] == 0:
            dupes.pop(num)
    else:
        window_nums.remove(num)



def maximumSubarraySum(nums, k):
    window_nums, dupes = set(), defaultdict(int)
    i, j, n = 0, 0, len(nums)
    current_sum = 0
    while j < k:
        current_sum += nums[j]
        add_number(nums[j], window_nums, dupes)
        j += 1
    j -= 1
    max_sum = current_sum if len(dupes) == 0 else 0
    while True:
        i, j = i+1, j+1
        if j == n:
            break
        current_sum -= nums[i-1]
        remove_number(nums[i-1], window_nums, dupes)
        current_sum += nums[j]
        add_number(nums[j], window_nums, dupes)
        if len(dupes) == 0:
            max_sum = max(max_sum, current_sum)
    return max_sum


print(maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))  # 15
print(maximumSubarraySum([4, 4, 4], 3))  # 0
