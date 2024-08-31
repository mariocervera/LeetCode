
def lexicographicallySmallestArray(nums, limit):
    n = len(nums)
    sorted_nums = sorted([(nums[i], i) for i in range(n)])
    groups, group_indexes = {}, {}

    for i in range(n):
        num, idx = sorted_nums[i]
        if i > 0 and num - sorted_nums[i-1][0] <= limit:
            groups[current_group].append(num)
            group_indexes[current_group].append(idx)
        else:
            # New group
            groups[num] = [num]
            group_indexes[num] = [idx]
            current_group = num

    for leader, group in groups.items():
        group_indexes[leader].sort()
        for i in range(len(group)):
            nums[group_indexes[leader][i]] = group[i]

    return nums


print(lexicographicallySmallestArray(nums=[1, 5, 3, 9, 8],
                                     limit=2))  # [1,3,5,8,9]

print(lexicographicallySmallestArray(nums=[1, 7, 6, 18, 2, 1],
                                     limit=3))  # [1,6,7,18,1,2]

print(lexicographicallySmallestArray(nums=[1, 7, 28, 19, 10],
                                     limit=3))  # [1,7,28,19,10]

print(lexicographicallySmallestArray(nums=[4, 3, 23, 84, 34, 88, 44, 44, 18, 15],
                                     limit=3))  # [3,4,23,84,34,88,44,44,15,18]
