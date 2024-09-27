
def circularArrayLoop(nums):
    n = len(nums)

    def next_index(idx, step):
        return (idx + step) % n if step > 0 or idx + step >= 0 else n + (idx + step)

    def breaks_cycle_condition(i1, i2):
        return nums[i1] * nums[i2] < 0 or nums[i1] == 0 or nums[i2] == 0

    def normalize_input():
        for idx in range(n):
            nums[idx] = nums[idx] % n if nums[idx] > 0 else -(-nums[idx] % n)

    normalize_input()
    for i in range(n):
        slow, fast = i, i
        while True:
            next_fast = next_index(fast, nums[fast])
            next_next_fast = next_index(next_fast, nums[next_fast])
            if breaks_cycle_condition(fast, next_fast) or breaks_cycle_condition(next_fast, next_next_fast):
                break
            slow = next_index(slow, nums[slow])
            fast = next_next_fast
            if slow == fast:
                return True
        slow = i
        while True:
            nums[slow] = 0
            next_slow = next_index(slow, nums[slow])
            if breaks_cycle_condition(slow, next_slow):
                break
            slow = next_slow
    return False


print(circularArrayLoop([2, -1, 1, 2, 2]))  # True
print(circularArrayLoop([-1, -2, -3, -4, -5, 6]))  # False
print(circularArrayLoop([1, -1, 5, 1, 4]))  # True
print(circularArrayLoop([1, 1, 2]))  # True
print(circularArrayLoop([2, -1, 1, -2, -2]))  # False
