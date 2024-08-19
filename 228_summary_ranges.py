
def get_range(nums, i, j):
    return str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}"

def summaryRanges(nums):
    if not nums:
        return []

    ranges = []
    i = 0
    for j in range(len(nums)):
        if j+1 == len(nums) or nums[j] < nums[j+1]-1:
            ranges.append(get_range(nums, i, j))
            i = j+1
    return ranges


print(summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
print(summaryRanges([0,2,3,4,6,8,9])) # ["0","2->4","6","8->9"]
